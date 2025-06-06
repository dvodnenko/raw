import json


def read_data() -> dict:
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_field(data_dict: dict, field: str):
    value = data_dict.get(field)

    return value


def rewrite_data(new_data: dict) -> None:
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

    return None
