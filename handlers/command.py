from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyboard.inline import start_kb
from keyboard.reply import keyboard
import requests

command_router = Router()

get = "https://currate.ru/api/?get=rates&pairs=EURRUB,EURUSD,EURGBP,EURJPY,EURKZT,EURAED,EURBYN,USDRUB,USDGBP,USDJPY,USDKZT,USDKGS,USDAED,USDUAH,USDTHB,USDBYN,GBPRUB,GBPJPY,GBPAUD,JPYRUB,GBPBYN,RUBAMD,RUBBGN,RUBMYR,MDLEUR,MDLRUB,MDLUSD,ETHRUB,ETHEUR,ETHGBP,ETHJPY,RSDRUB,RSDEUR,RSDUSD,LKRRUB,LKRUSD,LKREUR,MMKRUB,MMKUSD,MMKEUR,RUBKZT,RUBAED,BYNRUB,CNYRUB,CNYUSD,CNYEUR,BTCRUB,BTCUSD,BTCEUR,BTCGBP,BTCJPY,BTCBCH,BTCXRP,BCHUSD,BCHRUB,BCHGBP,BCHEUR,BCHJPY,BCHXRP,XRPUSD,XRPRUB,XRPGBP,XRPEUR,XRPJPY,GELUSD,GELRUB,THBEUR,THBRUB,BTGUSD,ETHUSD,ZECUSD,USDVND,USDMYR,RUBAUD,THBCNY,JPYAMD,JPYAZN,IDRUSD,EURTRY,USDAMD,USDILS,RUBNZD,RUBTRY,RUBSGD,RUBUAH,CADRUB,CHFRUB,USDAUD,USDCAD,EURAMD,EURBGN,USDBGN,&key=1877cdc72be0b4a9fd54325f6b052979"


@command_router.message(Command("usd"))
async def get_money(m: Message):
    response = requests.get(get)
    # response.text
    await m.answer(text=str(response.text))




deals = []
@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hi there, I am ValutaObmenshikBot , Я могу : 1 - Калькулятор для перевода валют по курсу в реальном времени.Введите команду __menu__ для начала работы____", reply_markup=start_kb )

@command_router.message(Command("about"))
async def about(message:Message) -> None:
    await message.answer("This bot can convert currency at the current exchange rate")

@command_router.message(Command("help"))
async def help(message:Message) -> None:
    await message.answer("""
/help - helps to know more commands 
/about - helps to know functions of the bot 
/start - starts the bot
/menu - this is a menu""")

@command_router.message(F.text.lower() == "menu")
async def menu(message:Message) -> None:
    await message.answer("Доступные функции : 1- Калькулятор валюты 2 - Простотр актуального курса 3 - Где купить или продать валюту", reply_markup = keyboard)


@command_router.message(F.text.lower() == "привет")
async def hi(message:Message) -> None:
    await message.answer("Hi! How are u?")

@command_router.message(F.text.lower() =="пока")
async def bye(message:Message) -> None:
    await message.answer("Bye!")

@command_router.message(F.text =="Калькулятор валюты")
async def t1(message:Message) -> None:
    await message.answer("TEXT1")

@command_router.message(F.text =="Простотр актуального курса")
async def t2(message:Message) -> None:
    await message.answer("трёхбуквенный код")

@command_router.message(F.text =="Где купить или продать валюту")
async def t3(message:Message) -> None:
    await message.answer("TEXT3")

@command_router.message(F.text.contains("❤️"))
async def heart_of_iron(message:Message) -> None:
    await message.answer("Thanks for a heart")

@command_router.message(F.sticker)
async def stickers(message:Message) -> None:
    await message.answer("Good job")

@command_router.message(F.photo)
async def photo(message:Message) -> None:
    await message.answer("Da best photo i've ever seen")

@command_router.message(Command("deal_create"))
async def deal_create(message:Message):
    a = message.text
    a = a.replace("/deal_create", "")
    a = a.replace(" ", "")
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