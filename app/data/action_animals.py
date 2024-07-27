import json

from app.data import list_files, open_files


def remove_animal(anim_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(anim_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тваринку {animal} успішно видалено."
    return msg


def cured_animal(prod_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(prod_index)

    cured_animals = open_files.get_cured_animals()
    cured_animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    with open(list_files.CURED_ANIMALS, "w", encoding="utf-8") as file:
        json.dump(cured_animals, file)

    msg = f"Тваринку {animal} додано до списку вилікуваних."
    return msg


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        msg = f"тваринка {animal} вже є у списку."
        return msg

    animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тваринку {animal} успішно додано."
    return msg
