# HERMES AI: доступ к репозиторию и прямой push в main

Инструкция для VPS с агентом HERMES AI и публичным репозиторием
`Valeron001/arbuzSVG`.

Цель: агент может менять код в репозитории и напрямую пушить в `main`.
GitHub Pages обновляется автоматически после каждого push.

## Что используется

- SSH deploy key с правом записи, привязанный только к `Valeron001/arbuzSVG`.
- Прямой push в `main`, без PR.
- GitHub Pages как автодеплой.
- Отдельный пользователь на VPS, без root.

PAT и GitHub App не нужны.

## 1. Пользователь на VPS

Не работать под root.

```bash
sudo adduser hermes
sudo -iu hermes
```

Если HERMES AI уже работает под отдельным сервисным пользователем, использовать
его. Главное, чтобы у этого пользователя был свой `HOME` и доступ к `~/.ssh`.

## 2. SSH deploy key

```bash
install -d -m 700 ~/.ssh
ssh-keygen -t ed25519 -C "hermes@vps" -f ~/.ssh/arbuz_deploy -N ""
chmod 600 ~/.ssh/arbuz_deploy
chmod 644 ~/.ssh/arbuz_deploy.pub
cat ~/.ssh/arbuz_deploy.pub
```

Ключ создаётся без пароля, чтобы агент мог работать автоматически.

## 3. Добавить ключ в GitHub

В репозитории:

**Settings → Deploy keys → Add deploy key**

- вставить содержимое `arbuz_deploy.pub`;
- включить **Allow write access**;
- сохранить.

Deploy key действует только на этот репозиторий. Это нужное ограничение.

## 4. Минимальная защита main

**Settings → Branches → Add branch protection rule**

Для ветки `main`:

- включить **Do not allow force pushes**;
- включить **Do not allow deletions**;
- **не** включать **Require a pull request before merging**, иначе прямой push
  перестанет работать.

## 5. SSH-конфиг

Файл `~/.ssh/config`:

```sshconfig
Host github-arbuz
  HostName github.com
  User git
  IdentityFile ~/.ssh/arbuz_deploy
  IdentitiesOnly yes
```

Если исходящий SSH на порт 22 заблокирован, использовать fallback GitHub
SSH over 443:

```sshconfig
Host github-arbuz
  HostName ssh.github.com
  Port 443
  User git
  IdentityFile ~/.ssh/arbuz_deploy
  IdentitiesOnly yes
```

## 6. Клонирование репозитория

```bash
git clone git@github-arbuz:Valeron001/arbuzSVG.git ~/landing
cd ~/landing
git config user.name "Hermes AI"
git config user.email "hermes@vps.local"
```

Проверка:

```bash
ssh -T git@github-arbuz
git remote -v
git fetch origin
```

SSH должен успешно аутентифицироваться. GitHub не даёт shell-доступ — это
нормально.

## 7. Рабочий цикл агента

```bash
cd ~/landing
git pull --ff-only

# правки

# проверки
# git diff
# Chrome headless
# печать PDF: 13 страниц
# нет горизонтального скролла
# проверка ссылок, телефонов, email

git add -A
git commit -m "Краткое описание изменений"
git push origin main
```

После push GitHub Pages обновится автоматически.

## 8. Проверка деплоя

```bash
curl -L "https://valeron001.github.io/arbuzSVG/?v=$(git rev-parse --short HEAD)"
```

Проверить, что в HTML есть новое изменение. Кэш GitHub Pages может держаться
до 10 минут. В браузере использовать `Ctrl+F5`.

## 9. Проверки перед push

- `git diff` просмотрен.
- Нет ошибок в консоли Chrome.
- Печать PDF: 13 страниц A4.
- Нет горизонтального скролла на мобильной ширине.
- Нет лишних внешних запросов, кроме разрешённых.
- Ссылки, телефоны и email корректны.
- В репозиторий не попали секреты, токены и приватные ключи.

## 10. Откат

```bash
git log --oneline -5
git revert <bad-commit>
git push origin main
```

Перед крупными правками:

```bash
git tag backup-$(date +%Y%m%d-%H%M)
git push origin --tags
```

## 11. Интеграция с HERMES AI

Убедиться, что агент работает под пользователем `hermes` и видит ключ.

Проверка от имени агента:

```bash
whoami
echo $HOME
ssh -T git@github-arbuz
cd ~/landing && git status
```

Если HERMES AI запущен как systemd-сервис:

- указать `User=hermes`;
- передать `HOME=/home/hermes`;
- проверить, что сервис видит `~/.ssh/arbuz_deploy`.

Если HERMES AI запущен в контейнере:

- смонтировать `~/.ssh` пользователя `hermes`;
- либо использовать SSH-agent;
- не давать контейнеру доступ к Docker socket и production-секретам.

## 12. Безопасность

- HERMES AI запускать без sudo.
- Ключ хранить только в `~/.ssh/arbuz_deploy`, права `600`.
- Репозиторий публичный: не коммитить токены, пароли и приватные ключи.
- При утечке ключа удалить deploy key в GitHub и сгенерировать новый.
- Не давать агенту доступ к чужим репозиториям и production-секретам.
- Прямой push в `main` идёт без ревью: перед push обязательно смотреть
  `git diff`.
- После крупных изменений проверять сайт и при необходимости делать
  `git revert`.

## 13. Критерии готовности

- `ssh -T git@github-arbuz` успешно аутентифицируется.
- `git push origin main` проходит без пароля.
- GitHub Pages собирается и отдаёт новый HTML.
- HERMES AI проходит цикл: правка → проверка → commit → push.
