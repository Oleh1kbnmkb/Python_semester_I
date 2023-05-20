from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from films import films



film_choice = InlineKeyboardMarkup()
for film in films:
    button = InlineKeyboardButton(text=film, callback_data=film)
    film_choice.add(button)




    #     [InlineKeyboardButton(text="Джон Уік 4 (16+)", callback_data="Джон Уік 4")],
    #     [InlineKeyboardButton(text="Підземелля і дракони", callback_data="Підземелля і дракони")],
    #     [InlineKeyboardButton(text="Екзорцист Ватикану", callback_data="Екзорцист Ватикану")],
    #     [InlineKeyboardButton(text="Чорна мітка", callback_data="Чорна мітка")],
    #     [InlineKeyboardButton(text="Банк Дейва", callback_data="Банк Дейва")]
    # ]

