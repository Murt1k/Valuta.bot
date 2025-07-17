from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyboard.inline import start_kb
from keyboard.reply import keyboard , Calculator , keyboard_start , Kursik , Nach_Calculator
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
import os

import requests
load_dotenv()

class CurrencyStates(StatesGroup):
    waiting_for_currency_code = State()
    waiting_for_amount = State()
    waiting_for_target_currency = State()
    waiting_for_operation = State()
    waiting_for_value = State()


KURSA = {"AED":0.04694,"AFN":0.882935,"ALL":1.077203,"AMD":4.907809,"ANG":0.022872,"AOA":11.719052,"ARS":16.121687,"AUD":0.019795,"AWG":0.023004,"AZN":0.021572,"BAM":0.021575,"BBD":0.025805,"BDT":1.551534,"BGN":0.021567,"BHD":0.004819,"BIF":38.086213,"BMD":0.01278,"BND":0.016443,"BOB":0.088316,"BRL":0.071177,"BSD":0.012781,"BTC":1.08125e-7,"BTN":1.099839,"BWP":0.172661,"BYN":0.041826,"BYR":250.483577,"BZD":0.025673,"CAD":0.017597,"CDF":36.88243,"CHF":0.010284,"CLF":0.000322,"CLP":12.359574,"CNY":0.091746,"CNH":0.091833,"COP":51.298014,"CRC":6.448877,"CUC":0.01278,"CUP":0.338664,"CVE":1.216352,"CZK":0.271948,"DJF":2.27598,"DKK":0.082373,"DOP":0.768872,"DZD":1.663713,"EGP":0.631583,"ERN":0.191697,"ETB":1.773808,"EUR":0.011038,"FJD":0.028934,"FKP":0.009519,"GBP":0.009542,"GEL":0.03463,"GGP":0.009519,"GHS":0.133236,"GIP":0.009519,"GMD":0.913779,"GNF":110.90737,"GTQ":0.098067,"GYD":2.672887,"HKD":0.100307,"HNL":0.334487,"HRK":0.083152,"HTG":1.678061,"HUF":4.405317,"IDR":208.945477,"ILS":0.042922,"IMP":0.009519,"INR":1.100082,"IQD":16.743108,"IRR":538.347999,"ISK":1.56514,"JEP":0.009519,"JMD":2.048929,"JOD":0.009061,"JPY":1.900742,"KES":1.651218,"KGS":1.117589,"KHR":51.229189,"KMF":5.409038,"KPW":11.501402,"KRW":17.815767,"KWD":0.003907,"KYD":0.010651,"KZT":6.825815,"LAK":275.616128,"LBP":1145.162121,"LKR":3.851753,"LRD":2.562563,"LSL":0.228848,"LTL":0.037735,"LVL":0.00773,"LYD":0.069507,"MAD":0.115833,"MDL":0.217272,"MGA":57.141947,"MKD":0.679079,"MMK":26.824428,"MNT":45.831682,"MOP":0.10333,"MRU":0.508416,"MUR":0.584048,"MVR":0.196859,"MWK":22.161905,"MXN":0.240472,"MYR":0.054269,"MZN":0.817388,"NAD":0.228848,"NGN":19.543214,"NIO":0.470369,"NOK":0.132093,"NPR":1.759725,"NZD":0.021625,"OMR":0.004914,"PAB":0.012781,"PEN":0.045339,"PGK":0.0537,"PHP":0.731846,"PKR":3.641224,"PLN":0.046966,"PYG":98.92752,"QAR":0.0466,"RON":0.056004,"RSD":1.292917,"RUB":1,"RWF":18.367054,"SAR":0.047935,"SBD":0.106145,"SCR":0.187651,"SDG":7.674243,"SEK":0.124919,"SGD":0.016447,"SHP":0.010043,"SLE":0.289464,"SLL":267.985529,"SOS":7.3038,"SRD":0.47443,"STD":264.515527,"SVC":0.111834,"SYP":166.160673,"SZL":0.228809,"THB":0.415739,"TJS":0.122185,"TMT":0.044857,"TND":0.037644,"TOP":0.029931,"TRY":0.514799,"TTD":0.086761,"TWD":0.376173,"TZS":33.355213,"UAH":0.535071,"UGX":45.790381,"USD":0.01278,"UYU":0.517031,"UZS":163.316452,"VES":1.494787,"VND":334.318897,"VUV":1.528919,"WST":0.035274,"XAF":7.236035,"XAG":0.000338,"XAU":3.842963e-6,"XCD":0.034538,"XDR":0.008969,"XOF":7.235972,"XPF":1.315577,"YER":3.084397,"ZAR":0.228996,"ZMK":115.033327,"ZMW":0.298749,"ZWL":4.115082}


key = os.getenv ("Curs")
getEUR = os.getenv ("get1")
getUSD = os.getenv ("get2")
getCNY = os.getenv ("get3")
getJPY = os.getenv ("get4")
getAED = os.getenv ("get5")
getBYN = os.getenv ("get6")
getKurs = os.getenv ('get7')
KursRUB = os.getenv('KursRUB')
command_router = Router()


deals = []

@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет пользователь, меня зовут - ValutaObmenshikBot", reply_markup=keyboard_start )


@command_router.message(F.text =="🔙CANCEL🔙")
async def command_start_handler(message: Message) -> None:
    await message.answer("🔙Возврат к началу🔙", reply_markup=keyboard_start)

@command_router.message(F.text =="📄о боте📄")
async def about(message:Message) -> None:
    await message.answer(f"Этот бот показывает актуальный курс валют по отношению к RUB\nА также бот может переводить валюту по актальному курсу в виде калькулятора")

@command_router.message(F.text =="🆘помощь🆘")
async def help(message:Message) -> None:
    await message.answer("""
🆘помощь🆘 - helps to know more commands 
📄о боте📄 - helps to know functions of the bot 
📋меню📋 - this is a menu
""")

@command_router.message(F.text.lower() == "📋меню📋")
async def menu(message:Message) -> None:
    await message.answer("Доступные функции :\n 1 - 💱Калькулятор валют💱\n 2 - 🔎Простотр актуального курса🔎\n 3 - ‼️Где купить или продать валюту‼️", reply_markup=keyboard)


@command_router.message(F.text.lower() == "⚖️просмотр актуального курса⚖️")
async def Kurs(message:Message) -> None:
    await message.answer("Самые популярные валюты :\n 1 - 🇷🇺РУБ и ЕВРО🇪🇺 |\n 2 - 🇷🇺РУБ и ДОЛЛАР🇺🇸 |\n 3 - 🇷🇺РУБ и ЮАНЬ🇨🇳 |\n 4 - 🇷🇺РУБ и ЙЕНА🇯🇵 |\n 5 - 🇷🇺РУБ и ДИРХАМЫ🇦🇪  |\n 6 - 🇷🇺РУБ и БелРУБ🇧🇾 |\n MORE - любая валюта  ", reply_markup=Kursik)

@command_router.message(F.text.lower() == "‼️где купить или продать валюту‼️")
async def Prosmotr(message:Message) -> None:
    await message.answer("⚙️Функция в разработке⚙️")





@command_router.message(F.text == "MORE")
async def cmd_more(message: Message, state: FSMContext):
    await message.answer(
        "Введите трехбуквенный код валюты, курс которой вы хотите узнать\n"
        "Пример: USD\n"
    )
    await state.set_state(CurrencyStates.waiting_for_currency_code)

@command_router.message(CurrencyStates.waiting_for_currency_code)
async def process_currency_code(message: Message, state: FSMContext):
    currency_code = message.text.upper().strip()
    
    if len(currency_code) == 3 and currency_code.isalpha():
        if currency_code in KURSA:
            rate = KURSA[currency_code]
            await message.answer(
                f"Курс {currency_code}:\n"
                f"🇷🇺 RUB = {rate:.2f} {currency_code}🇺🇳\n"
                f"🇺🇳{currency_code} = {1/rate:.2f} RUB🇷🇺"
            )
        else:
            try:
                response = requests.get(KursRUB)
                t = response.json()
                if currency_code in t['rates']:
                    rate = t['rates'][currency_code]
                    rub_per_curr = 1 / rate
                    await message.answer(
                        f"Курс {currency_code} (актуальный):\n"
                        f"🇷🇺RUB = {rate:.2f} {currency_code}🇺🇳\n"
                        f"🇺🇳{currency_code} = {rub_per_curr:.2f} RUB🇷🇺"
                    )
                else:
                    await message.answer("Валюта не найдена. Попробуйте другой код.")
                    return
            except:
                await message.answer("Ошибка получения курса. Попробуйте позже.")
                return
        
    await state.clear()






@command_router.message(F.text.lower() == "💱калькулятор валют💱")
async def calculator_menu(message: Message, state: FSMContext):
    await message.answer(
        "Выберите операцию:\n1. Конвертировать RUB в другую валюту 🇷🇺->🇺🇳\n2. Конвертировать валюту в RUB 🇺🇳->🇷🇺",
        reply_markup=Nach_Calculator
    )
    await state.set_state(CurrencyStates.waiting_for_operation)

@command_router.message(CurrencyStates.waiting_for_operation)
async def process_calc_operation(message: Message, state: FSMContext):
    operation = message.text
    
    if operation in ['1', '2']:
        await state.update_data(operation=operation)
        if operation == '1':
            await message.answer("Введите сумму в RUB для конвертации:")
        elif operation == '2':
            await message.answer("Введите код валюты (например: USD):")     
        await state.set_state(CurrencyStates.waiting_for_value)
    else:
        await message.answer("Пожалуйста, введите 1 или 2")

@command_router.message(CurrencyStates.waiting_for_value)
async def process_calc_values(message: Message, state: FSMContext):
    data = await state.get_data()
    operation = data['operation']
    user_input = message.text.upper()
    
    try:
        if operation == '1':
            amount = float(user_input)
            await state.update_data(amount=amount)
            await message.answer("Введите код целевой валюты \n(например: USD):")
            await state.set_state(CurrencyStates.waiting_for_target_currency)
            
        elif operation == '2':
            if len(user_input) == 3 and user_input.isalpha():
                await state.update_data(currency=user_input)
                await message.answer("Введите сумму в валюте для конвертации в RUB:")
                await state.set_state(CurrencyStates.waiting_for_amount)
            else:
                await message.answer("Пожалуйста, введите корректный код валюты (3 буквы)")
                
    except ValueError:
        await message.answer("Пожалуйста, введите числовое значение")

@command_router.message(CurrencyStates.waiting_for_amount)
async def process_amount(message: Message, state: FSMContext):
    try:
        amount = float(message.text)
        data = await state.get_data()
        currency = data['currency']
        
        if currency in KURSA:
            rate = KURSA[currency]
            result = amount / rate
            await message.answer(f"{amount} {currency} = {result:.2f} RUB")
        else:
            await message.answer("Валюта не найдена. Пожалуйста, введите корректный код валюты.")
        
        await state.clear()
    except ValueError:
        await message.answer("Пожалуйста, введите числовое значение")

@command_router.message(CurrencyStates.waiting_for_target_currency)
async def process_target_currency(message: Message, state: FSMContext):
    currency = message.text.upper()
    data = await state.get_data()
    amount = data['amount']
    
    if len(currency) == 3 and currency.isalpha():
        if currency in KURSA:
            rate = KURSA[currency]
            result = amount * rate
            await message.answer(f"{amount} RUB = {result:.2f} {currency}")
        else:
            await message.answer("Валюта не найдена. Пожалуйста, введите корректный код валюты.")
    else:
        await message.answer("Пожалуйста, введите корректный код валюты (3 буквы)")
    
    await state.clear()






@command_router.message(F.text == "коды валют")
async def command_list_currencies_handler(message: Message) -> None:
    await message.answer(""" 
- <code>AED</code> – Дирхам ОАЭ  
- <code>AFN</code> – Афгани  
- <code>AMD</code> – Армянский драм  
- <code>ANG</code> – Нидерландский гульден  
- <code>AOA</code> – Ангольская кванза  
- <code>ARS</code> – Аргентинское песо  
- <code>AUD</code> – Австралийский доллар  
- <code>BHD</code> – Бахрейнский динар    
- <code>BRL</code> – Бразильский реал  
- <code>BTC</code> – Биткоин (криптовалюта)  
- <code>BYN</code> – Белорусский рубль  
- <code>CAD</code> – Канадский доллар  
- <code>CHF</code> – Швейцарский франк  
- <code>CLP</code> – Чилийское песо  
- <code>CNY</code> – Китайский юань  
- <code>COP</code> – Колумбийское песо  
- <code>CZK</code> – Чешская крона  
- <code>DJF</code> – Джибутийский франк  
- <code>DKK</code> – Датская крона  
- <code>DOP</code> – Доминиканское песо  
- <code>DZD</code> – Алжирский динар  
- <code>EGP</code> – Египетский фунт  
- <code>EUR</code> – Евро  
- <code>GBP</code> – Фунт стерлингов  
- <code>GEL</code> – Грузинский лари  
- <code>GNF</code> – Гвинейский франк  
- <code>HKD</code> – Гонконгский доллар  
- <code>HNL</code> – Гондурасская лемпира  
- <code>HTG</code> – Гаитянский гурд  
- <code>HUF</code> – Венгерский форинт  
- <code>IDR</code> – Индонезийская рупия  
- <code>ILS</code> – Израильский шекель  
- <code>INR</code> – Индийская рупия  
- <code>IQD</code> – Иракский динар  
- <code>IRR</code> – Иранский риал  
- <code>ISK</code> – Исландская крона  
- <code>JPY</code> – Японская иена  
- <code>KGS</code> – Киргизский сом  
- <code>KMF</code> – Коморский франк  
- <code>KPW</code> – Северокорейская вона  
- <code>KRW</code> – Южнокорейская вона  
- <code>KWD</code> – Кувейтский динар  
- <code>KZT</code> – Казахстанский тенге  
- <code>LBP</code> – Ливанский фунт  
- <code>LRD</code> – Либерийский доллар  
- <code>LYD</code> – Ливийский динар  
- <code>MAD</code> – Марокканский дирхам  
- <code>MDL</code> – Молдавский лей  
- <code>MGA</code> – Малагасийский ариари  
- <code>MKD</code> – Македонский денар  
- <code>MMK</code> – Мьянманский кьят  
- <code>MNT</code> – Монгольский тугрик  
- <code>MVR</code> – Мальдивская руфия  
- <code>MWK</code> – Малавийская квача  
- <code>MXN</code> – Мексиканское песо  
- <code>MYR</code> – Малайзийский ринггит  
- <code>NGN</code> – Нигерийская найра  
- <code>NOK</code> – Норвежская крона  
- <code>NPR</code> – Непальская рупия  
- <code>OMR</code> – Оманский риал  
- <code>PHP</code> – Филиппинское песо  
- <code>PKR</code> – Пакистанская рупия  
- <code>PLN</code> – Польский злотый  
- <code>PYG</code> – Парагвайский гуарани  
- <code>QAR</code> – Катарский риал  
- <code>RON</code> – Румынский лей  
- <code>RSD</code> – Сербский динар  
- <code>RUB</code> – Российский рубль  
- <code>SAR</code> – Саудовский риял  
- <code>SBD</code> – Доллар Соломоновых островов  
- <code>SCR</code> – Сейшельская рупия  
- <code>SDG</code> – Суданский фунт  
- <code>SEK</code> – Шведская крона  
- <code>SGD</code> – Сингапурский доллар  
- <code>SYP</code> – Сирийский фунт  
- <code>TJS</code> – Таджикский сомони  
- <code>TMT</code> – Туркменский манат  
- <code>TND</code> – Тунисский динар   
- <code>TRY</code> – Турецкая лира   
- <code>TWD</code> – Новый тайваньский доллар  
- <code>UAH</code> – Украинская гривна  
- <code>USD</code> – Доллар США  
- <code>UYU</code> – Уругвайское песо  
- <code>UZS</code> – Узбекский сум   
- <code>VND</code> – Вьетнамский донг  
- <code>XAG</code> – Серебро (тройская унция)  
- <code>XAU</code> – Золото (тройская унция)  
""", parse_mode="HTML")






@command_router.message(F.text=="EUR")
async def get_moneyC(message: Message):
    response = requests.get(KursRUB)
    t = response.json()
    eur_rate = t['rates']['EUR']
    rub_per_eur = 1 / eur_rate
    message_text = f" 🇷🇺Рубль равен {eur_rate:.2f}🇪🇺|\n🇪🇺Евро равно {rub_per_eur:.2f}🇷🇺|"
    await message.answer(text = message_text)
    await state.clear()

@command_router.message(F.text=="USD")
async def get_moneyC(message: Message):
    response = requests.get(KursRUB)
    t = response.json()
    usd_rate = t['rates']['USD']
    rub_per_usd = 1 / usd_rate
    message_text = f" 🇷🇺Рубль равен {usd_rate:.2f}🇺🇸|\n🇺🇸Доллар равен {rub_per_usd:.2f}🇷🇺|"
    await message.answer(text = message_text) 
    await state.clear()  

@command_router.message(F.text=="CNY")
async def get_moneyC(message: Message):
    response = requests.get(KursRUB)
    t = response.json()
    cny_rate = t['rates']['CNY']
    rub_per_cny = 1 / cny_rate
    message_text = f" 🇷🇺Рубль равен {cny_rate:.2f}🇨🇳|\n🇨🇳Юань равен {rub_per_cny:.2f}🇷🇺|"
    await message.answer(text = message_text)
    await state.clear()

@command_router.message(F.text=="JPY")
async def get_moneyC(message: Message):
    response = requests.get(KursRUB)
    t = response.json()
    jpy_rate = t['rates']['JPY']
    rub_per_jpy = 1 / jpy_rate
    message_text = f" 🇷🇺Рубль равен {jpy_rate:.2f}🇯🇵|\n🇯🇵Йена равна {rub_per_jpy:.2f}🇷🇺|"
    await message.answer(text = message_text)
    await state.clear()

@command_router.message(F.text=="AED")
async def get_moneyC(message: Message):
    response = requests.get(KursRUB)
    t = response.json()
    aed_rate = t['rates']['AED']
    rub_per_aed = 1 / aed_rate
    message_text = f" 🇷🇺Рубль равен {aed_rate:.2f}🇦🇪|\n🇦🇪Дирхамма равна {rub_per_aed:.2f}🇷🇺|"
    await message.answer(text = message_text)
    await state.clear()

@command_router.message(F.text=="BYN")
async def get_moneyC(message: Message):
    response = requests.get(KursRUB)
    t = response.json()
    byn_rate = t['rates']['BYN']
    rub_per_byn = 1 / byn_rate
    message_text = f" 🇷🇺Рубль равен {byn_rate:.2f}🇧🇾|\n🇧🇾Белорусский Рубль равен {rub_per_byn:.2f}🇷🇺|"
    await message.answer(text = message_text)
    await state.clear()


@command_router.message(Command("deal_create"))
async def deal_create(message:Message):
    a = message.text
    a = a.replace("/deal_create", "")
    a = a.replace(" dfdfd", "")
    await message.answer("What time will i remind it to you?")
    print(a)

@command_router.message(Command("style"))
async def send_styles(message:Message):
    text = (
        "<b>bold</b> -- <strong>bold</strong>\n"
        "<i>italic</i> -- <em>italic</em>\n"
        "<u>underline</u> -- <ins>underline</ins>\n"
        "<s>strikethrough</s> -- <strike>strikethrough</strike> --  <del>strikethrough</del>\n"
        "<span class=\"tg-spoiler\">spoiler</span> -- <tg-spoiler>spoiler</tg-spoiler>\n"
        "<b>bold   <i>italic bold   <s>italic bold strikethrough "
        "<span class=\"tg-spoiler\">italic bold strikethrough spoiler</span>"
        "</s> <u>underline italic bold</u></i> bold</b>\n"
        "<a href=\"http://www.example.com/\">inline URL</a>\n"
        "<code>inline fixed-width code</code>\n"
        "<pre>pre-formatted fixed-width code block</pre>\n"
        "<pre><code class=\"language-python\">pre-formatted fixed-width code block written in the Python programming "
        "language</code></pre>"
    )
    await message.answer(text = text, parse_mode="HTML")


