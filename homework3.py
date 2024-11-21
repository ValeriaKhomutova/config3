import json
import sys

# Функция для преобразования значений
def convert_value(value):
    if isinstance(value, str):
        return f"'{value}'"  # строковые значения заключаются в одинарные кавычки
    elif isinstance(value, bool):
        return str(value).lower()  # логические значения (True/False) в нижнем регистре
    elif isinstance(value, int):
        return str(value)  # числовые значения остаются без изменений
    elif isinstance(value, float):
        return float(value)
    elif isinstance(value, list):
        return f"<< {', '.join(convert_value(v) for v in value)} >>"  # массивы в формате <<...>>
    elif isinstance(value, dict):
        return convert_dict(value)  # вложенные словари
    return str(value)

# Функция для обработки словаря
def convert_dict(data):
    output = "dict(\n"
    for key, value in data.items():
        output += f"    {key} = {convert_value(value)},\n"
    output += ")"
    return output

# Основная функция для чтения и записи
def main(input_file, output_file):
    # Чтение входного JSON
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Преобразование в конфигурационный язык
    config_data =  convert_dict(data)

    # Запись результата в выходной файл
    with open(output_file, 'w') as f:
        f.write(config_data)

# Запуск программы
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
