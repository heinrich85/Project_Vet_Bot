from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_animals_keyboard(animals: list):
    builder = InlineKeyboardBuilder()

    for index, animal in enumerate(animals):
        builder.button(text=animal, callback_data=f"animal_{index}")

    builder.adjust(4)
    return builder.as_markup()


def build_animal_actions_keyboard(index: str|int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Додати до вилікуваних", callback_data=f"cured_animal_{index}")
    builder.button(text="Видалити зі списку", callback_data=f"remove_animal_{index}")
    return builder.as_markup()