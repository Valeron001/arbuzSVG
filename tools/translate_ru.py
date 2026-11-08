import os
import re
from bs4 import BeautifulSoup

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'index-en.html')
OUT = os.path.join(BASE, 'index.html')

D = {
# --- head / chrome ---
"ARBUZ · Sovetskaya Gavan — Income-producing asset at 40.9% of build cost": "АРБУЗ · Советская Гавань — доходный актив за 40,9% от себестоимости строительства",
"Skip to content": "Перейти к содержанию",
"ARBUZ": "АРБУЗ",
"SOVETSKAYA GAVAN": "СОВЕТСКАЯ ГАВАНЬ",
"Asset": "Актив",
"Economics": "Экономика",
"Location": "Локация",
"Upside": "Потенциал",
"Process": "Процесс",
"Deck": "Презентация",
"Request data room": "Запросить data room",
"Public auction · Far Eastern District · 127-FZ": "Публичные торги · Дальневосточный федеральный округ · 127-ФЗ",
"A ready-made income-producing asset at": "Готовый доходный актив за",
"of its 2015 build cost.": "от себестоимости строительства 2015 года.",
"Shopping centre “Arbuz” and a capital warehouse with 1.58 ha of freehold land, on the red line in the logistics hub of Sovetskaya Gavan, Khabarovsk Krai.": "ТЦ «Арбуз» и капитальный склад с 1,58 га земли в собственности на красной линии в логистическом хабе Советской Гавани, Хабаровский край.",
"Lot composition": "Состав лота",
"Shopping centre “Arbuz”, 4 floors": "ТЦ «Арбуз», 4 этажа",
"Capital warehouse, 1 floor": "Капитальный склад, 1 этаж",
"Freehold land, 3 parcels": "Земля в собственности, 3 участка",
"Auction threshold price": "Пороговая цена аукциона",
"Application deadline": "Срок подачи заявок",
"25 November 2026": "25 ноября 2026",
"Request the data room": "Запросить data room",
"Presentation (PDF)": "Презентация (PDF)",
"Total built area": "Общая площадь зданий",
"Price per sqm": "Цена за кв.м",
"NOI per year, base case": "NOI в год, базовый сценарий",
"Cap rate, base case": "Ставка капитализации, база",
"Payback range": "Диапазон окупаемости",
"Price per sqm is calculated on total built area, not leasable area (GLA). See the Asset section. Price in USD: ≈ USD 4.50 M at 81.7947 USD/RUB, Bank of Russia, 06.11.2026.": "Цена за кв.м рассчитана по общей площади зданий, а не по арендопригодной (GLA). См. раздел «Актив». Цена в USD: ≈ 4,50 млн долл. США по курсу 81,7947 USD/RUB, Банк России, 06.11.2026.",
"11,520 sqm": "11 520 кв.м",
"1,500 sqm": "1 500 кв.м",
"15,812 sqm · 1.58 ha": "15 812 кв.м · 1,58 га",
"13,020 sqm": "13 020 кв.м",
"RUB 368,376,909": "368 376 909 руб.",
"RUB 28,293": "28 293 руб.",
"RUB 23.1 M": "23,1 млн ₽",
"RUB 27.5 M": "27,5 млн ₽",
"13–16 yrs": "13–16 лет",
"15.96 yrs": "15,96 лет",
"13.4 yrs": "13,4 года",
"13 yrs": "13 лет",
"RUB 70,800,000 / yr": "70 800 000 руб. / год",
"RUB 23,080,800 / yr": "23 080 800 руб. / год",
"RUB 75,600,000 / yr": "75 600 000 руб. / год",
"RUB 27,492,000 / yr": "27 492 000 руб. / год",
"RUB 453 gross · RUB 148 NOI": "453 руб. брутто · 148 руб. NOI",
"RUB 288,510,000": "288 510 000 руб.",
"RUB 343,650,000": "343 650 000 руб.",
"RUB 256,453,333": "256 453 333 руб.",
"RUB 305,466,667": "305 466 667 руб.",
"RUB 230,808,000": "230 808 000 руб.",
"RUB 274,920,000": "274 920 000 руб.",
"RUB 192,340,000": "192 340 000 руб.",
"RUB 229,100,000": "229 100 000 руб.",
"15,812 sqm": "15 812 кв.м",
"1,499.9 sqm": "1 499,9 кв.м",
"ARBUZ · SOVETSKAYA GAVAN": "АРБУЗ · СОВЕТСКАЯ ГАВАНЬ",
"A": "А",
"MTS": "МТС",
"Telegram": "Telegram",
"WhatsApp": "WhatsApp",
"Email": "Email",

# --- facade ---
"Schematic elevation of the Arbuz shopping centre": "Схематический фасад ТЦ «Арбуз»",
"Four-storey mall block with a green cornice, a double-height glazed anchor entrance, four levels of windows, a public frontage band and parking.": "Четырёхэтажный блок ТЦ с зелёным карнизом, двухсветным остеклённым входом якорного арендатора, четырьмя уровнями окон, полосой общественного фронта и парковкой.",
"SAMBURI": "САМБЕРИ",
"LEVEL 4": "УРОВЕНЬ 4",
"LEVEL 3": "УРОВЕНЬ 3",
"LEVEL 2": "УРОВЕНЬ 2",
"LEVEL 1": "УРОВЕНЬ 1",
"PUBLIC FRONTAGE / PARKING": "ОБЩЕСТВЕННЫЙ ФРОНТ / ПАРКОВКА",
"Schematic elevation — illustrative, not an architectural drawing.": "Схематический фасад — иллюстративно, не архитектурный чертёж.",

# --- map ---
"Schematic regional map of Sovetskaya Gavan": "Схематическая региональная карта Советской Гавани",
"Sovetskaya Gavan as the eastern terminus of the Baikal-Amur Mainline, with the Vanino deep-water port 10 km away and the Northern Sea Route running north.": "Советская Гавань как восточная конечная станция Байкало-Амурской магистрали, в 10 км от глубоководного порта Ванино, с Северным морским путём на север.",
"BAIKAL–AMUR MAINLINE": "БАЙКАЛО-АМУРСКАЯ МАГИСТРАЛЬ",
"NORTHERN SEA ROUTE": "СЕВЕРНЫЙ МОРСКОЙ ПУТЬ",
"SOVETSKAYA GAVAN": "СОВЕТСКАЯ ГАВАНЬ",
"TERMINUS OF THE BAM": "КОНЕЧНАЯ СТАНЦИЯ БАМ",
"VANINO DEEP-WATER PORT": "ГЛУБОКОВОДНЫЙ ПОРТ ВАНИНО",
"10 km": "10 км",
"ONLY LARGE SHOPPING CENTRE": "ЕДИНСТВЕННЫЙ КРУПНЫЙ ТЦ",
"Serving the two districts": "Обслуживает два района",
"56,433 people · 4.5% vacancy": "56 433 человека · 4,5% вакантных площадей",
"BAM": "БАМ",
"Port link": "Порт",
"Northern Sea Route": "СМП",
"N": "С",
"Schematic regional diagram, not a cartographic map. Population: Sovetskaya Gavan city 23,232 + Vaninsky District 33,201 (2025).": "Схематическая региональная диаграмма, не картографическая карта. Население: город Советская Гавань 23 232 + Ванинский район 33 201 (2025).",
"Eastern terminus": "Восточная конечная станция",
"To Vanino deep-water port": "До глубоководного порта Ванино",
"Catchment population": "Население зоны охвата",

# --- summary ---
"Executive summary": "Резюме",
"Why this asset, why now": "Почему этот актив и почему сейчас",
"Four reasons a sceptical buyer can underwrite, each with the figure that supports it.": "Четыре причины, которые может обосновать скептичный покупатель, каждая — с подтверждающей цифрой.",
"Inflation hedge": "Инфляционный хедж",
"Hard walls and freehold land revalue with inflation; fixed deposit rates do not.": "Капитальные стены и земля в собственности индексируются с инфляцией; фиксированные ставки по вкладам — нет.",
"1.58 ha freehold · 3 parcels": "1,58 га в собственности · 3 участка",
"No systemic exposure": "Нет системных рисков",
"Rent flows in locally from an operating asset — no freeze risk, no deposit limits.": "Арендный поток формируется на месте в действующем активе — нет риска заморозки и лимитов по вкладам.",
"95.5% occupied · 4.5% vacancy": "95,5% занято · 4,5% вакантных площадей",
"Monopoly position": "Монопольное положение",
"The only large shopping centre serving the two districts, in the centre of the city.": "Единственный крупный ТЦ, обслуживающий два района, в центре города.",
"56,433 catchment population": "56 433 жителя зоны охвата",
"Basis discount": "Дисконт к оценке",
"Priced 30.4% below the 2025 independent appraisal — a measurable entry discount.": "Цена на 30,4% ниже независимой оценки 2025 года — измеримый дисконт на входе.",
"RUB 160,594,091 saving": "Экономия 160 594 091 руб.",

# --- economics ---
"Financial passport": "Финансовый паспорт",
"The numbers, before the story.": "Сначала цифры, потом история.",
"Two operating scenarios, the margin gap that creates the upside, and a five-year path with stated assumptions. All figures are taken from the investment memorandum and the 2025 independent appraisal.": "Два операционных сценария, разрыв в марже, создающий потенциал, и пятилетняя траектория с явными допущениями. Все цифры взяты из инвестиционного меморандума и независимой оценки 2025 года.",
"Base case": "Базовый сценарий",
"As currently operated": "Текущая эксплуатация",
"Current": "Текущий",
"Gross revenue": "Выручка",
"NOI": "NOI",
"NOI margin": "Маржа NOI",
"Cap rate": "Ставка капитализации",
"Gross yield": "Валовая доходность",
"Payback": "Окупаемость",
"Rent per sqm / month": "Аренда за кв.м / мес",
"Optimisation case": "Сценарий оптимизации",
"After repricing and filling the 4.5% vacancy": "После пересмотра аренды и заполнения 4,5% вакансии",
"Memo case": "Из меморандума",
"Revenue uplift": "Рост выручки",
"NOI uplift": "Рост NOI",
"Where the upside actually comes from": "Откуда на самом деле берётся потенциал",
"A 33% NOI margin is far below the": "Маржа NOI 33% значительно ниже",
"55–65% district-mall norm": "55–65% — нормы для районного ТЦ",
". The memorandum’s optimisation case captures only": ". Сценарий оптимизации меморандума даёт лишь",
"+6.8% of revenue": "+6,8% выручки",
", so the asset is": ", поэтому актив",
"unmanaged, not weak": "не слабый, а неуправляемый",
". At current operating costs, a 55% margin requires": ". При текущих операционных расходах для маржи 55% нужна выручка",
"RUB 106,042,667 of revenue — +49.8%": "106 042 667 руб. — +49,8%",
"Quick check: filling the 4.5% vacancy alone takes NOI to RUB 26,416,926 and the cap rate to 7.17%.": "Быстрая проверка: только заполнение 4,5% вакансии увеличивает NOI до 26 416 926 руб., а ставку капитализации — до 7,17%.",
"NOI target": "Целевой NOI",
"per year, memo case": "в год, сценарий меморандума",
"Cap target": "Целевая ставка",
"memo case": "сценарий меморандума",
"GRM": "GRM",
"Five-year operating path": "Пятилетняя операционная траектория",
"Revenue +10% p.a.; NOI shown with operating costs held flat and with costs inflating at 5% p.a. Cap-rate line on the secondary axis.": "Выручка +10% в год; NOI при неизменных операционных расходах и при инфляции расходов 5% в год. Линия ставки капитализации — на второй оси.",
"Five-year revenue, NOI and cap-rate chart": "График выручки, NOI и ставки капитализации за пять лет",
"Revenue rises from 77.9 to 114.0 million roubles. NOI with flat operating costs rises from 30.2 to 66.3 million. NOI with costs inflating 5 percent rises from 27.8 to 53.1 million. Cap rate reaches 18.0 percent in the flat-cost case and 14.4 percent in the inflating-cost case.": "Выручка растёт с 77,9 до 114,0 млн руб. NOI при неизменных расходах растёт с 30,2 до 66,3 млн. NOI при инфляции расходов 5% растёт с 27,8 до 53,1 млн. Ставка капитализации достигает 18,0% в сценарии с неизменными расходами и 14,4% — при инфляции расходов.",
"RUB million": "млн руб.",
"Y1": "1-й",
"Y2": "2-й",
"Y3": "3-й",
"Y4": "4-й",
"Y5": "5-й",
"Revenue": "Выручка",
"NOI · opex flat": "NOI · OPEX без роста",
"NOI · opex +5% p.a.": "NOI · OPEX +5% в год",
"Cap · opex flat": "Cap · OPEX без роста",
"Cap · opex +5%": "Cap · OPEX +5%",
"Indexation of 10% p.a. reaches a market margin by year 4–5 if operating costs are held flat. With costs inflating at 5% p.a. the target margin is not reached within five years — cost discipline, not rent, drives the return. Price denominator: RUB 368,376,909. Values in RUB million.": "Индексация 10% в год выводит на рыночную маржу к 4–5 году, если операционные расходы не растут. При инфляции расходов 5% в год целевая маржа не достигается за пять лет — доходность определяет дисциплина расходов, а не аренда. Знаменатель цены: 368 376 909 руб. Значения — млн руб.",
"Cap-rate screen: the price you are paying vs. the price a screen implies": "Скрининг по ставке капитализации: цена, которую вы платите, и цена, которую подразумевает скрининг",
"Implied value at base NOI of RUB 23.08 M and at optimised NOI of RUB 27.49 M.": "Подразумеваемая стоимость при базовом NOI 23,08 млн руб. и оптимизированном NOI 27,49 млн руб.",
"Implied value at base NOI 23.08 M": "Стоимость при базовом NOI 23,08 млн",
"At optimised NOI 27.49 M": "При оптимизированном NOI",
"Rent, gross": "Аренда, брутто",
"RUB 453 / sqm / month": "453 руб. / кв.м / мес",
"RUB 148 / sqm / month NOI": "148 руб. / кв.м / мес NOI",
"Land-inclusive effective price": "Эффективная цена с землёй",
"RUB 12,777 / sqm": "12 777 руб. / кв.м",
"Built area plus 1.58 ha land": "Здания плюс 1,58 га земли",
"Operating expenses": "Операционные расходы",
"RUB 47.7 M / yr": "47,7 млн ₽ / год",
"67.4% of gross revenue": "67,4% выручки",

# --- discount ---
"The discount": "Дисконт",
"Two benchmarks. Two separate discounts.": "Два ориентира. Два отдельных дисконта.",
"The auction price sits below both the 2015 construction cost and the 2025 independent appraisal. The two figures are measured against different benchmarks and are not additive.": "Цена аукциона ниже и себестоимости строительства 2015 года, и независимой оценки 2025 года. Эти два показателя измеряются от разных ориентиров и не суммируются.",
"From build cost and appraisal to the auction price": "От себестоимости и оценки к цене аукциона",
"RUB million. The 2015 construction cost is shown as a benchmark with a hatched fill.": "млн руб. Себестоимость 2015 года показана как ориентир со штриховкой.",
"Discount waterfall": "Водопад дисконта",
"2015 construction cost 900 million roubles. 2025 independent appraisal 528.97 million. Auction price 368.38 million. The auction price is 40.9 percent of the 2015 build cost and 30.4 percent below the 2025 appraisal.": "Себестоимость строительства 2015 года — 900 млн руб. Независимая оценка 2025 года — 528,97 млн. Цена аукциона — 368,38 млн. Цена аукциона составляет 40,9% от себестоимости 2015 года и на 30,4% ниже оценки 2025 года.",
"2015 BUILD COST": "СЕБЕСТОИМОСТЬ 2015",
"BENCHMARK · RUB 900 M": "ОРИЕНТИР · 900 МЛН ₽",
"2025 APPRAISAL": "ОЦЕНКА 2025",
"INDEPENDENT · RUB 528.97 M": "НЕЗАВИСИМАЯ · 528,97 МЛН ₽",
"AUCTION PRICE": "ЦЕНА АУКЦИОНА",
"THRESHOLD · RUB 368.38 M": "ПОРОГ · 368,38 МЛН ₽",
"40.9% of 2015 build cost": "40,9% от себестоимости 2015",
"30.4% below 2025 appraisal": "30,4% ниже оценки 2025",
"Saving vs appraisal": "Экономия к оценке",
"RUB 160.59 M": "160,59 млн ₽",
"30.4% below": "30,4% ниже",
"Price vs build cost": "Цена к себестоимости",
"RUB 531.62 M": "531,62 млн ₽",
"59.1% below": "59,1% ниже",
"Build-cost multiple": "Кратность к себестоимости",
"2.44×": "2,44×",
"cheaper than building": "дешевле строительства",
"total built area": "общая площадь зданий",
"Per-sqm comparison": "Сравнение за кв.м",
"Location / category": "Локация / категория",
"RUB per sqm": "руб. за кв.м",
"vs. this asset": "к данному активу",
"Vladivostok, primary market": "Владивосток, первичный рынок",
"6.7× higher": "в 6,7 раза выше",
"Khabarovsk, prime offices": "Хабаровск, прайм-офисы",
"4.4× higher": "в 4,4 раза выше",
"Khabarovsk, commercial": "Хабаровск, коммерческая недвижимость",
"3.9–4.2× higher": "в 3,9–4,2 раза выше",
"Sovetskaya Gavan, this asset": "Советская Гавань, данный актив",
"Comparison based on total built area of the subject asset.": "Сравнение по общей площади зданий данного актива.",
"The 2015 construction cost is a benchmark for what this asset would cost to build today at 2015 prices; the 2025 appraisal is an independent market opinion. The 40.9% and 30.4% figures are measured against different benchmarks and are not additive.": "Себестоимость строительства 2015 года — ориентир для того, сколько стоило бы построить этот актив сегодня по ценам 2015 года; оценка 2025 года — независимое рыночное мнение. Показатели 40,9% и 30,4% измеряются от разных ориентиров и не суммируются.",

# --- asset ---
"The asset, floor by floor": "Актив, этаж за этажом",
"A 4-floor mall, a capital warehouse and 1.58 ha of land.": "4-этажный ТЦ, капитальный склад и 1,58 га земли.",
"Every level has a defined role in the tenant mix. The plans below are schematic zoning diagrams, not measured drawings; the areas are per the investment memorandum.": "У каждого уровня своя роль в составе арендаторов. Планы ниже — схематические зонирования, а не обмерные чертежи; площади — по инвестиционному меморандуму.",
"Schematic floor plan, level 1": "Схематический план 1 этажа",
"Ground floor with a 1,900 sqm Samburi supermarket anchor, a gallery of about 2,900 sqm, telecom salons, OZON, jewellery, pharmacy and food court.": "Первый этаж с якорным супермаркетом «Самбери» 1 900 кв.м, галереей около 2 900 кв.м, салонами связи, OZON, ювелирным магазином, аптекой и фуд-кортом.",
"GALLERY": "ГАЛЕРЕЯ",
"~2 900 sqm": "~2 900 кв.м",
"FOOD": "ФУД-",
"COURT": "КОРТ",
"telecom": "связь",
"marketplace": "маркетплейс",
"ZOLOTAYA": "ЗОЛОТАЯ",
"RUS": "РУСЬ",
"jewellery": "ювелирный",
"PHARMACY": "АПТЕКА",
"services": "услуги",
"SERVICES": "УСЛУГИ",
"WC · ATM · customer desk": "WC · банкомат · стойка",
"1 900 sqm · anchor supermarket": "1 900 кв.м · якорный супермаркет",
"GROCERY · PRODUCE": "ПРОДУКТЫ · ОВОЩИ",
"CHECKOUTS": "КАССЫ",
"VERTICAL CORE": "ВЕРТИКАЛЬНОЕ ЯДРО",
"ENTRANCE": "ВХОД",
"0 — 30 m": "0 — 30 м",
"Schematic zoning diagram, not to scale. Areas per the investment memorandum.": "Схематическая диаграмма зонирования, не в масштабе. Площади — по инвестиционному меморандуму.",
"Level 1 · 11,520 sqm total building": "Уровень 1 · 11 520 кв.м общей площади",
"Supermarket & services": "Супермаркет и услуги",
"The ground floor carries the anchor and the daily-needs traffic. A regional supermarket, telecom salons, a marketplace pickup point, jewellery, a pharmacy and a food court create repeat visits rather than a single-purpose shopping trip.": "Первый этаж несёт якорного арендатора и трафик повседневного спроса. Региональный супермаркет, салоны связи, пункт выдачи маркетплейса, ювелирный магазин, аптека и фуд-корт создают повторные визиты, а не поездку за одной покупкой.",
"Gallery area": "Площадь галереи",
"~2,900 sqm": "~2 900 кв.м",
"Anchor tenant": "Якорный арендатор",
"Samburi · 1,900 sqm": "Самбери · 1 900 кв.м",
"Telecom salons": "Салоны связи",
"MTS · MegaFon · Tele2": "МТС · МегаФон · Теле2",
"OZON, “Zolotaya Rus” jewellery, pharmacy, food court": "OZON, ювелирный «Золотая Русь», аптека, фуд-корт",
"Schematic floor plan, level 2": "Схематический план 2 этажа",
"Second floor with an open gallery loop, fashion retail, a cinema or family entertainment unit, jewellery and home goods, escalators and goods lifts.": "Второй этаж с открытой галереей, модной торговлей, кинотеатром или семейным развлекательным блоком, ювелирными изделиями и товарами для дома, эскалаторами и грузовыми лифтами.",
"OPEN SPACE": "ОТКРЫТОЕ ПРОСТРАНСТВО",
"Gallery loop": "Галерея",
"OPEN GALLERY LOOP": "ОТКРЫТАЯ ГАЛЕРЕЯ",
"RETAIL CELLS": "ТОРГОВЫЕ ЯЧЕЙКИ",
"CINEMA / FAMILY": "КИНОТЕАТР / СЕМЕЙНЫЙ",
"ENTERTAINMENT": "ДОСУГ",
"Anchor footfall driver": "Якорный трафик",
"on the upper level": "на верхнем уровне",
"JEWELLERY": "ЮВЕЛИРНЫЕ",
"& HOME": "И ДОМ",
"FASHION": "МОДА",
"RETAIL": "ТОРГОВЛЯ",
"ESCALATORS": "ЭСКАЛАТОРЫ",
"GOODS LIFTS": "ГРУЗОВЫЕ ЛИФТЫ",
"Level 2 · open-plan retail": "Уровень 2 · открытая планировка",
"Fashion retail & entertainment": "Мода и развлечения",
"An open gallery loop gives every unit a shopfront on the main circulation route. The entertainment unit adds evening and weekend trips, while jewellery and home goods broaden the offer beyond fashion.": "Открытая галерея даёт каждой ячейке витрину на главном маршруте. Развлекательный блок добавляет вечерние и выходные визиты, а ювелирные изделия и товары для дома расширяют предложение за пределы моды.",
"Fashion retail around an": "Торговля вокруг",
"open gallery loop": "открытой галереи",
"Cinema / family entertainment unit": "Кинотеатр / семейный развлекательный блок",
"Jewellery and home-goods group": "Ювелирные изделия и товары для дома",
"Escalators and goods lifts": "Эскалаторы и грузовые лифты",
"Schematic plans for levels 3 and 4": "Схематические планы 3 и 4 этажей",
"Level 3 has retail and a cafe, including KARI at 557.2 sqm. Level 4 has 1,899 sqm of offices, a banquet hall, Kafe Manna with a kitchen and an open terrace.": "На 3 уровне — торговля и кафе, включая KARI 557,2 кв.м. На 4 уровне — офисы 1 899 кв.м, банкетный зал, «Kafe Manna» с кухней и открытой террасой.",
"LEVEL 3 · RETAIL & CAFÉ": "УРОВЕНЬ 3 · ТОРГОВЛЯ И КАФЕ",
"LEVEL 4 · OFFICES & BANQUET": "УРОВЕНЬ 4 · ОФИСЫ И БАНКЕТНЫЙ ЗАЛ",
"KARI": "KARI",
"557.2 sqm": "557,2 кв.м",
"CAFÉ": "КАФЕ",
"food & beverage": "еда и напитки",
"open plan": "открытая планировка",
"CORE": "ЯДРО",
"OFFICES": "ОФИСЫ",
"1,899 sqm": "1 899 кв.м",
"BANQUET": "БАНКЕТНЫЙ",
"HALL": "ЗАЛ",
"KAFE MANNA": "KAFE MANNA",
"kitchen · dining": "кухня · зал",
"OPEN": "ОТКРЫТАЯ",
"TERRACE": "ТЕРРАСА",
"outdoor dining": "на улице",
"Levels 3–4": "Уровни 3–4",
"Retail, offices & banquet": "Торговля, офисы и банкетный зал",
"The upper floors combine destination retail with office and event space. The fourth-floor banquet hall and Kafe Manna with its open terrace monetise the building beyond shopping.": "Верхние этажи объединяют целевую торговлю с офисным и событийным пространством. Банкетный зал на 4 этаже и «Kafe Manna» с открытой террасой монетизируют здание за пределами торговли.",
"Level 3 — retail and café,": "Уровень 3 — торговля и кафе,",
"KARI 557.2 sqm": "KARI 557,2 кв.м",
"Level 4 — offices": "Уровень 4 — офисы",
"Banquet hall, “Kafe Manna” with kitchen": "Банкетный зал, «Kafe Manna» с кухней",
"Open terrace for the café": "Открытая терраса кафе",
"Capital warehouse": "Капитальный склад",
"One storey on a 4,500 sqm plot, 6 m clear height, heated, ventilated, sprinklered and multi-purpose. Use it as a regional distribution hub for the two districts, or lease it to a federal logistics operator or marketplace such as Ozon or Wildberries.": "Один этаж на участке 4 500 кв.м, высота в свету 6 м, отопление, вентиляция, спринклеры, многофункциональное использование. Подойдёт как региональный распределительный хаб для двух районов или для сдачи федеральному логистическому оператору или маркетплейсу (Ozon, Wildberries).",
"6 m clear height": "6 м высота в свету",
"Heated · ventilated · sprinklered": "Отопление · вентиляция · спринклеры",
"4,500 sqm warehouse plot": "Участок склада 4 500 кв.м",
"Land — 1.58 ha freehold on the red line": "Земля — 1,58 га в собственности на красной линии",
"Three parcels in freehold: 8,503 / 4,500 / 2,809 sqm. The 2,809 sqm parcel is street frontage; the 4,500 sqm parcel carries the warehouse. The mall and front parking occupy the largest parcel.": "Три участка в собственности: 8 503 / 4 500 / 2 809 кв.м. Участок 2 809 кв.м — фронт улицы; на участке 4 500 кв.м расположен склад. ТЦ и фронтальная парковка занимают крупнейший участок.",
"Area check:": "Проверка площади:",
"8,503 + 4,500 + 2,809 = 15,812 sqm = 1.58 ha.": "8 503 + 4 500 + 2 809 = 15 812 кв.м = 1,58 га.",
"Documented leasable areas total ~5,356 sqm (floor 1 ~2,900; floor 3 557.2; floor 4 1,899; floor 2 not stated); the remainder is common areas. On GLA of ~5,400–7,000 sqm the effective price is RUB 52,000–68,000 / sqm. Anchor tenant Samburi is ~33% of GLA.": "Документированные арендопригодные площади — ~5 356 кв.м (1 этаж ~2 900; 3 этаж 557,2; 4 этаж 1 899; 2 этаж не указан); остальное — общие зоны. При GLA ~5 400–7 000 кв.м эффективная цена — 52 000–68 000 руб. / кв.м. Якорный арендатор «Самбери» — ~33% GLA.",

# --- location ---
"Location & regional tailwinds": "Локация и региональные драйверы",
"The eastern terminus of the BAM, 10 km from a deep-water port.": "Восточная конечная станция БАМ, 10 км до глубоководного порта.",
"Sovetskaya Gavan is a working logistics point, not a seasonal market. The city is the eastern terminus of the Baikal–Amur Mainline and an operating point on the Northern Sea Route.": "Советская Гавань — рабочий логистический пункт, а не сезонный рынок. Город является восточной конечной станцией Байкало-Амурской магистрали и опорным пунктом Северного морского пути.",
"Detailed regional diagram": "Детальная региональная диаграмма",
"Baikal-Amur Mainline terminating at Sovetskaya Gavan, gold link to Vanino deep-water port 10 km away, dashed Northern Sea Route running north, and a callout for the 56,433-person catchment.": "Байкало-Амурская магистраль с конечной станцией в Советской Гавани, золотая линия к глубоководному порту Ванино в 10 км, пунктир Северного морского пути на север и выноска о зоне охвата 56 433 человека.",
"Schematic regional diagram. The coastline is abstract; no external basemap is used. Population: Sovetskaya Gavan city 23,232 + Vaninsky District 33,201 (2025).": "Схематическая региональная диаграмма. Береговая линия абстрактна; внешняя картографическая подложка не используется. Население: город Советская Гавань 23 232 + Ванинский район 33 201 (2025).",
"Only large shopping centre serving the two districts —": "Единственный крупный ТЦ, обслуживающий два района, —",
"56,433 catchment": "56 433 жителя зоны охвата",
"Eastern terminus of the": "Восточная конечная станция",
"Baikal–Amur Mainline": "Байкало-Амурской магистрали",
"Freight infrastructure linking to Komsomolsk-on-Amur and the rest of Russia.": "Грузовая инфраструктура, связывающая с Комсомольском-на-Амуре и остальной Россией.",
"A modern CHP plant serving the transport hub.": "Современная ТЭЦ, обеспечивающая транспортный узел.",
"Port and logistics zone with new coal and container terminals, ship-repair centres and fish-processing.": "Портовая и логистическая зона с новыми угольными и контейнерными терминалами, судоремонтными центрами и рыбопереработкой.",
"Planned": "Планируется",
"Polymetal has returned to pre-feasibility work on the Pacific Hydro-Metallurgical Complex (TGMK) in Sovetskaya Gavan after the project was paused in 2022. In June 2026 the company, the Khabarovsk regional government and Rosvodokanal signed a three-party agreement covering modern wastewater treatment (3,500 m³/day, first phase targeted 2031). Planned capacity 250–300 kt of third-party gold concentrate per year, previously estimated at RUB 60 bn.": "«Полиметалл» вернулся к предпроектной проработке Тихоокеанского гидрометаллургического комбината (ТГМК) в Советской Гавани после паузы 2022 года. В июне 2026 года компания, правительство Хабаровского края и «Росводоканал» подписали трёхстороннее соглашение о современных очистных сооружениях (3 500 м³/сут, первый этап — к 2031 году). Плановая мощность — 250–300 тыс. тонн стороннего золотого концентрата в год; ранее проект оценивался в 60 млрд руб.",
"Sovetsko-Gavansky District total population: 35,915. The wider catchment used in this memorandum is 56,433.": "Общая численность населения Советско-Гаванского района — 35 915. Более широкая зона охвата, используемая в меморандуме, — 56 433.",

# --- engineering ---
"Engineering & autonomy": "Инженерия и автономность",
"100% engineering autonomy. No capex for 15 years.": "100% инженерная автономность. Без CAPEX 15 лет.",
"Own 10 kV line, own substation, own heating point and a 300 kW diesel generator on automatic start. The building is designed to keep trading when the grid does not.": "Собственная линия 10 кВ, собственная подстанция, собственный тепловой пункт и дизель-генератор 300 кВт с автозапуском. Здание рассчитано на продолжение торговли при отключении сети.",
"Engineering one-line diagram": "Однолинейная инженерная схема",
"Own 10 kV line to own substation and switchboard, feeding ventilation with heat recovery, a metered heating point and four lifts plus escalators. A 300 kW diesel generator provides backup on automatic start. Seismic rating 9 on a rock foundation.": "Собственная линия 10 кВ к собственной подстанции и распределительному щиту, питание вентиляции с рекуперацией тепла, теплового пункта с учётом и четырёх лифтов с эскалаторами. Дизель-генератор 300 кВт — резерв с автозапуском. Сейсмичность 9 баллов, скальное основание.",
"SEISMIC 9 · DALGIPROTRANS": "СЕЙСМИКА 9 · ДАЛЬГИПРОТРАНС",
"ROCK FOUNDATION": "СКАЛЬНОЕ ОСНОВАНИЕ",
"OWN 10 kV LINE": "СОБСТВЕННАЯ ЛИНИЯ 10 кВ",
"OWN SUBSTATION": "СОБСТВЕННАЯ ПОДСТАНЦИЯ",
"10 kV transformer": "трансформатор 10 кВ",
"SWITCHBOARD": "РАСПРЕДЕЛИТЕЛЬНЫЙ ЩИТ",
"VENTILATION + HEAT RECOVERY": "ВЕНТИЛЯЦИЯ + РЕКУПЕРАЦИЯ ТЕПЛА",
"Multi-zone · heat recovery": "Многозонная · рекуперация тепла",
"HEATING POINT · METERED": "ТЕПЛОВОЙ ПУНКТ · УЧЁТ",
"Own heating point": "Собственный тепловой пункт",
"4 LIFTS + ESCALATORS": "4 ЛИФТА + ЭСКАЛАТОРЫ",
"Plus goods lifts": "Плюс грузовые лифты",
"HEAT RECOVERY": "РЕКУПЕРАЦИЯ ТЕПЛА",
"300 kW DIESEL · AUTOMATIC START": "ДИЗЕЛЬ 300 кВт · АВТОЗАПУСК",
"Backup supply — not primary": "Резервное питание — не основное",
"RESERVE": "РЕЗЕРВ",
"LOAD": "НАГРУЗКА",
"BUS": "ЩИТ",
"Seismic 9": "Сейсмика 9",
"Dalgiprotrans project, rock foundation": "Проект «Дальгипротранс», скальное основание",
"Own 10 kV line": "Собственная ЛЭП 10 кВ",
"Dedicated line and own substation": "Выделенная линия и своя подстанция",
"300 kW diesel": "Дизель 300 кВт",
"Automatic start, backup supply": "Автозапуск, резервное питание",
"4 lifts": "4 лифта",
"Escalators, goods lifts, tufoblok walls": "Эскалаторы, грузовые лифты, туфоблок",
"Heat recovery": "Рекуперация тепла",
"Multi-zone ventilation": "Многозонная вентиляция",
"Own heating point": "Свой тепловой пункт",
"With metering": "С учётом",
"No capex": "Без CAPEX",
"Next 15 years": "Ближайшие 15 лет",
"One owner": "Один собственник",
"No tenant capital required": "Капитал арендаторов не требуется",
"100% engineering autonomy — no capital expenditure for 15 years.": "100% инженерная автономность — без капитальных вложений 15 лет.",
"Dalgiprotrans · seismic 9 · rock foundation": "Дальгипротранс · сейсмика 9 · скальное основание",

# --- land ---
"Land & warehouse": "Земля и склад",
"Three freehold parcels. One obvious development story.": "Три участка в собственности. Очевидная история развития.",
"The land bank is not a residual. It is a separate, monetisable asset on the red line, with street frontage and a warehouse plot already in use.": "Земельный банк — не остаток. Это отдельный монетизируемый актив на красной линии с фронтом улицы и уже используемым участком склада.",
"Schematic site and parcel plan": "Схематический план участков",
"Three freehold parcels of 8,503, 4,500 and 2,809 square metres, totalling 15,812 square metres or 1.58 hectares. The mall and front parking occupy the largest parcel; the warehouse plot carries a 1,500 square metre warehouse; the smallest parcel is street frontage on the red line.": "Три участка в собственности — 8 503, 4 500 и 2 809 кв.м, всего 15 812 кв.м или 1,58 га. ТЦ и фронтальная парковка занимают крупнейший участок; на участке склада расположен склад 1 500 кв.м; наименьший участок — фронт улицы на красной линии.",
"PARCEL A": "УЧАСТОК A",
"8,503 sqm": "8 503 кв.м",
"MALL ZONE + FRONT PARKING": "ЗОНА ТЦ + ФРОНТАЛЬНАЯ ПАРКОВКА",
"PARCEL B": "УЧАСТОК B",
"4,500 sqm": "4 500 кв.м",
"WAREHOUSE PLOT": "ЗОНА СКЛАДА",
"PARCEL C": "УЧАСТОК C",
"2,809 sqm": "2 809 кв.м",
"STREET FRONTAGE": "ФРОНТ УЛИЦЫ",
"MALL FOOTPRINT": "ПЯТНО ТЦ",
"11,520 sqm · 4 floors": "11 520 кв.м · 4 этажа",
"WAREHOUSE": "СКЛАД",
"1,500 sqm": "1 500 кв.м",
"STREET": "ФРОНТ",
"FRONTAGE": "УЛИЦЫ",
"RED LINE (КРАСНАЯ ЛИНИЯ)": "КРАСНАЯ ЛИНИЯ",
"0 — 50 m": "0 — 50 м",
"Schematic parcel diagram. Parcel areas per the memorandum: 8,503 + 4,500 + 2,809 = 15,812 sqm (1.58 ha).": "Схематическая диаграмма участков. Площади по меморандуму: 8 503 + 4 500 + 2 809 = 15 812 кв.м (1,58 га).",
"Monetisation": "Монетизация",
"What the land can carry": "Что можно разместить на земле",
"Each option is owner-side and does not require capital from the existing tenant base. The 2,809 sqm street-frontage parcel is the most obvious development play; the warehouse plot can be leased or sold separately.": "Каждый вариант — действие собственника, не требующее капитала от действующих арендаторов. Участок 2 809 кв.м с фронтом улицы — наиболее очевидный сценарий развития; участок склада можно сдать или продать отдельно.",
"Build-materials store": "Стройматериалы",
"Car dealership": "Автосалон",
"Car wash": "Автомойка",
"Drive-thru QSR or fuel station": "Drive-thru QSR или АЗС",
"Paid parking": "Платная парковка",
"Bus terminal": "Автовокзал",
"Sell parcels to developers": "Продажа участков застройщикам",
"Schematic warehouse block": "Схематический блок склада",
"One-storey capital warehouse of 1,499.9 square metres on a 4,500 square metre plot, with 6 metre clear height, three loading docks, and heating, ventilation and sprinklers.": "Одноэтажный капитальный склад 1 499,9 кв.м на участке 4 500 кв.м, высота в свету 6 м, три погрузочных ворот, отопление, вентиляция и спринклеры.",
"CAPITAL WAREHOUSE": "КАПИТАЛЬНЫЙ СКЛАД",
"1,499.9 sqm · one storey · 4,500 sqm plot": "1 499,9 кв.м · 1 этаж · участок 4 500 кв.м",
"LOADING DOCKS × 3": "ПОГРУЗОЧНЫЕ ВОРОТА × 3",
"6 m CLEAR HEIGHT": "6 м ВЫСОТА В СВЕТУ",
"HEATED · VENTILATED · SPRINKLERED · MULTI-PURPOSE": "ОТОПЛЕНИЕ · ВЕНТИЛЯЦИЯ · СПРИНКЛЕРЫ · МНОГОФУНКЦИОНАЛЬНЫЙ",
"Schematic axonometric diagram, not to scale.": "Схематическая аксонометрическая диаграмма, не в масштабе.",

# --- upside ---
"Upside levers": "Точки роста",
"Five owner-side actions. One outcome.": "Пять действий собственника. Один результат.",
"All five levers require no capital from the tenant base. The memorandum’s optimisation case assumes only +6.8% revenue; the gap between that and a 55% margin is where the asset’s value is created.": "Все пять рычагов не требуют капитала от арендаторов. Сценарий оптимизации меморандума предполагает лишь +6,8% выручки; разрыв между этим и маржой 55% — там, где создаётся стоимость актива.",
"Asset capitalisation reserve": "Резерв капитализации актива",
"Professional management and merchandising — a reserve for capitalising the asset, not a promise of new tenants.": "Профессиональное управление и мерчендайзинг — резерв капитализации актива, а не обещание новых арендаторов.",
"Lease optimisation": "Оптимизация аренды",
"Operating costs have never been benchmarked. Bringing them to market is the first source of margin.": "Операционные расходы никогда не бенчмаркились. Приведение их к рынку — первый источник маржи.",
"Rent indexation": "Индексация аренды",
"Leases have not been indexed.": "Ставки аренды длительное время не индексировались.",
"15–20% revenue uplift available": "потенциал роста выручки 15–20%",
"— an estimate, not a guarantee.": "— оценка, а не гарантия.",
"OPEX reduction": "Снижение OPEX",
"67.4% of revenue": "67,4% выручки",
"goes to operating costs. The district-mall norm is a 55–65% NOI margin.": "уходит на операционные расходы. Норма для районного ТЦ — маржа NOI 55–65%.",
"Warehouse development + land monetisation": "Развитие склада + монетизация земли",
"Lease the 1,500 sqm warehouse; monetise the 2,809 sqm street-frontage parcel.": "Сдать склад 1 500 кв.м; монетизировать участок 2 809 кв.м с фронтом улицы.",
"Five levers": "Пять рычагов",
"One outcome": "Один результат",
"NOI · RUB per year": "NOI · руб. в год",
"23.1 → 27.5 M": "23,1 → 27,5 млн",
"CAP 6.27% → 7.46%": "CAP 6,27% → 7,46%",
"The memo case captures +19.1% NOI. A 55–65% margin remains the larger prize.": "Сценарий меморандума даёт +19,1% NOI. Маржа 55–65% остаётся более крупным призом.",
"Honest note.": "Честная оговорка.",
"All five levers are owner-side actions and require no capital from the tenant base. The memo’s optimisation case assumes only +6.8% revenue. The gap between that and a 55% margin is where the asset’s value is created.": "Все пять рычагов — действия собственника, не требующие капитала от арендаторов. Сценарий оптимизации меморандума предполагает лишь +6,8% выручки. Разрыв между этим и маржой 55% — там, где создаётся стоимость актива.",

# --- process ---
"Process, legal, tax": "Процесс, юридика, налоги",
"The trust section.": "Раздел доверия.",
"A public auction under 127-FZ, a clean title mechanism and a tax treatment that matters to a buyer without input VAT deduction.": "Публичные торги по 127-ФЗ, чистый титульный механизм и налоговая трактовка, важная для покупателя без права на вычет входного НДС.",
"Legal cleanliness guaranteed": "Юридическая чистота гарантирована",
"Under Federal Law No. 127-FZ on insolvency, the seller’s tax debts, pledges, attachments and encumbrances are extinguished on purchase and the price is protected from challenge.": "По Федеральному закону № 127-ФЗ о несостоятельности налоговые долги продавца, залоги, аресты и обременения прекращаются при покупке, а цена защищена от оспаривания.",
"Purchase procedure": "Процедура покупки",
"Public auction, open bidding, at the threshold price. The process is transparent and the price is the auction threshold.": "Публичные торги, открытые торги, по пороговой цене. Процесс прозрачен, цена — пороговая цена аукциона.",
"Applications are accepted until": "Заявки принимаются до",
". Missing the date is the only way to lose the asset.": ". Пропустить дату — единственный способ потерять актив.",
"Tax note — precisely": "Налоговая оговорка — точно",
"Sale of a bankrupt debtor’s property is not subject to VAT (Clause 15, Sub-clause 2, Article 146 of the Russian Tax Code). For a buyer with no right to deduct input VAT this is worth": "Реализация имущества банкрота не облагается НДС (пп. 15 п. 2 ст. 146 НК РФ). Для покупателя без права на вычет входного НДС это стоит",
"16.7% of the price": "16,7% цены",
"(RUB 368,376,909 vs. RUB 442,052,291 with VAT).": "(368 376 909 руб. против 442 052 291 руб. с НДС).",
"Free-port (SPV) and Advanced Development Territory (TOR) preferences —": "Преференции Свободного порта (СПВ) и Территории опережающего развития (ТОР) —",
"zero property tax for 5 years, zero land tax for 5 years, reduced social contributions from 30% to 7.6%": "ноль налога на имущество на 5 лет, ноль земельного налога на 5 лет, снижение социальных взносов с 30% до 7,6%",
"— require registration of the asset under a dedicated project, resident status, and a tax opinion. They are a regime for a resident, not an automatic entitlement of the buyer.": "— требуют регистрации актива под отдельным проектом, статуса резидента и налогового заключения. Это режим для резидента, а не автоматическое право покупателя.",
"Source: investment memorandum; Russian Tax Code, Article 146, Clause 15, Sub-clause 2.": "Источник: инвестиционный меморандум; НК РФ, ст. 146, п. 2, пп. 15.",

# --- deck ---
"The presentation": "Презентация",
"15-slide investor deck.": "Инвесторская презентация на 15 слайдов.",
"The original Russian-language presentation that accompanies the memorandum. View it here or open the PDF directly.": "Оригинальная русскоязычная презентация к меморандуму. Смотрите здесь или откройте PDF.",
"Open PDF": "Открыть PDF",
"Download": "Скачать",
"Memorandum (PDF)": "Меморандум (PDF)",
"Original Russian-language investor deck · 15 slides · reproduced whole, without cropping": "Оригинальная русскоязычная презентация · 15 слайдов · показана целиком, без кадрирования",
"Open full PDF →": "Открыть полный PDF →",
"Slide rasters are shown as complete slides. No photograph has been cropped out of a slide for use elsewhere on this page.": "Слайды показаны целиком. Ни одна фотография не вырезана из слайда для использования на этой странице.",

# --- contact ---
"Contact · data room": "Контакт · data room",
"Request the data room.": "Запросить data room.",
"Rent roll, operating accounts, cadastral and engineering documentation and the 2025 appraisal report are available under NDA.": "Арендная ведомость, операционные счета, кадастровая и инженерная документация и отчёт об оценке 2025 года доступны под NDA.",
"Owner / Company / Broker": "Владелец / компания / брокер",
"Role, e.g. Head of Asset Management": "Должность, например руководитель управления активами",
"Sample: Owner / Company / Broker · Head of Asset Management": "Пример: владелец / компания / брокер · руководитель управления активами",
"NDA and financial model on request": "NDA и финансовая модель по запросу",
"Presentation:": "Презентация:",
"PDF deck": "PDF-презентация",
"Memorandum": "Меморандум",
"Telegram handle": "Telegram",
"WhatsApp number": "WhatsApp",
"Email address": "Email",
"e.g. @your_handle": "например, @your_handle",
"e.g. +7 900 000-00-00": "например, +7 900 000-00-00",
"e.g. name@example.com": "например, name@example.com",
"Address": "Адрес",
"Sovetskaya Gavan, Khabarovsk Krai, Russian Far East": "Советская Гавань, Хабаровский край, Дальний Восток России",
"Asset location": "Местоположение актива",
"This page summarises an investment memorandum prepared for a public auction. Figures are taken from the memorandum and the 2025 independent appraisal; forward-looking statements are projections. This is not a public offer.": "Эта страница резюмирует инвестиционный меморандум, подготовленный к публичным торгам. Цифры взяты из меморандума и независимой оценки 2025 года; прогнозные заявления являются оценками. Это не публичная оферта.",
}

ATTR = {
"Language / Язык": "Язык / Language",
"Primary": "Основная навигация",
"ARBUZ, Sovetskaya Gavan — back to top": "АРБУЗ, Советская Гавань — наверх",
"Key metrics": "Ключевые показатели",
"Choose a slide": "Выберите слайд",
"Previous slide": "Предыдущий слайд",
"Next slide": "Следующий слайд",
"Presentation viewer. Use left and right arrow keys to change slides.": "Просмотр презентации. Используйте стрелки влево и вправо для переключения слайдов.",
"Arbuz investor presentation, slide 1 of 15": "Инвесторская презентация «Арбуз», слайд 1 из 15",
"Investor landing page for the Arbuz shopping centre and capital warehouse with 1.58 ha of freehold land in Sovetskaya Gavan, Khabarovsk Krai. Public auction, 127-FZ.": "Инвесторская страница ТЦ «Арбуз» и капитального склада с 1,58 га земли в собственности в Советской Гавани, Хабаровский край. Публичные торги, 127-ФЗ.",
}

DATE_RE = re.compile(r"\b\d{2}\.\d{2}\.\d{4}\b")

def localize_num(s):
    dates = DATE_RE.findall(s)
    for d in dates:
        s = s.replace(d, d.replace(".", "§"))
    s = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", " ", s)
    s = re.sub(r"(?<!\d)(\d+)\.(\d{1,4})(?!\d)", r"\1,\2", s)
    s = s.replace("§", ".")
    return s

def translate_text(t):
    if t in D:
        return D[t]
    return t

soup = BeautifulSoup(open(SRC, encoding="utf-8").read(), "html.parser")

missing = []
for node in soup.find_all(string=True):
    if node.find_parent(["script", "style"]):
        continue
    if node.parent is None or node.parent.name == "[document]":
        continue
    raw = str(node)
    t = raw.strip()
    if not t:
        continue
    if t in D:
        ru = D[t]
    else:
        ru = t
        if re.search(r"[A-Za-z]{2,}", t):
            if not t.startswith("{{") and t not in {"NOI", "GRM", "BAM", "PDF", "NDA", "OPEX", "CAP", "SPV", "TOR", "USD", "RUB", "KARI", "OZON", "MTS", "MEGAFON", "TELE2", "ARBUZ", "SAMBURI", "RU", "EN", "Telegram", "WhatsApp", "Email"}:
                missing.append(t)
    ru = localize_num(ru)
    if ru != t:
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        node.replace_with(lead + ru + trail)
    elif localize_num(t) != t:
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        node.replace_with(lead + localize_num(t) + trail)

for tag in soup.find_all(True):
    for attr in ("aria-label", "alt", "title", "content"):
        if tag.has_attr(attr):
            v = tag[attr]
            m = re.fullmatch(r"Slide (\d+)", v)
            if attr == "aria-label" and m:
                tag[attr] = "Слайд " + m.group(1)
            elif v in ATTR:
                tag[attr] = ATTR[v]
            elif attr == "content" and "Investor landing page" in v:
                tag[attr] = ATTR["Investor landing page for the Arbuz shopping centre and capital warehouse with 1.58 ha of freehold land in Sovetskaya Gavan, Khabarovsk Krai. Public auction, 127-FZ."]

sw = soup.select_one('.lang-switch')
if sw:
    sw['aria-label'] = 'Язык / Language'
    links = sw.find_all('a')
    if len(links) >= 2:
        links[0]['href'] = 'index.html'
        links[0]['class'] = [c for c in links[0].get('class', []) if c != 'is-active'] + ['is-active']
        links[1]['href'] = 'index-en.html'
        links[1]['class'] = [c for c in links[1].get('class', []) if c != 'is-active']
        if not links[1]['class']:
            del links[1]['class']

html = str(soup)
html = html.replace('<lineargradient', '<linearGradient').replace('</lineargradient>', '</linearGradient>')
html = html.replace('<radialgradient', '<radialGradient').replace('</radialgradient>', '</radialGradient>')
html = html.replace('<textpath', '<textPath').replace('</textpath>', '</textPath>')
html = html.replace('<clippath', '<clipPath').replace('</clippath>', '</clipPath>')
html = html.replace('<foreignobject', '<foreignObject').replace('</foreignobject>', '</foreignObject>')
for a, b in [
    ('viewbox=', 'viewBox='),
    ('preserveaspectratio=', 'preserveAspectRatio='),
    ('gradientunits=', 'gradientUnits='),
    ('gradienttransform=', 'gradientTransform='),
    ('patternunits=', 'patternUnits='),
    ('patterntransform=', 'patternTransform='),
    ('markerwidth=', 'markerWidth='),
    ('markerheight=', 'markerHeight='),
    ('markerunits=', 'markerUnits='),
    ('refx=', 'refX='),
    ('refy=', 'refY='),
    ('textlength=', 'textLength='),
    ('startoffset=', 'startOffset='),
    ('spreadmethod=', 'spreadMethod='),
    ('clippathunits=', 'clipPathUnits='),
    ('maskunits=', 'maskUnits='),
    ('filterunits=', 'filterUnits='),
    ('primitiveunits=', 'primitiveUnits='),
]:
    html = html.replace(a, b)
html = html.replace('<html lang="en">', '<html lang="ru">')
html = html.replace(
    '<div class="lang-switch" aria-label="Language / Язык">\n      <a href="index.html" hreflang="ru" lang="ru">RU</a>\n      <span class="sep" aria-hidden="true">/</span>\n      <a href="index-en.html" hreflang="en" lang="en" class="is-active">EN</a>\n    </div>',
    '<div class="lang-switch" aria-label="Язык / Language">\n      <a href="index.html" hreflang="ru" lang="ru" class="is-active">RU</a>\n      <span class="sep" aria-hidden="true">/</span>\n      <a href="index-en.html" hreflang="en" lang="en">EN</a>\n    </div>'
)
html = html.replace(
    "deckImg.alt = 'Arbuz investor presentation, slide ' + current + ' of ' + total;",
    "deckImg.alt = 'Инвесторская презентация «Арбуз», слайд ' + current + ' из ' + total;"
)
html = html.replace(
    'alt="Arbuz investor presentation, slide 1 of 15"',
    'alt="Инвесторская презентация «Арбуз», слайд 1 из 15"'
)
if not html.startswith("<!DOCTYPE html>"):
    html = "<!DOCTYPE html>\n" + html
open(OUT, "w", encoding="utf-8").write(html)
print("written", len(html))
print("missing", len(missing))
for m in missing:
    print("MISS\t" + m)
