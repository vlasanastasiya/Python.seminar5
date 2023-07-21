
# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_func(path):
    path_1, file_name_1 = path.rsplit("/", 1) 
    nam, extention_1 = file_name_1.split(".", 1)
    return path_1, nam, f".{extention_1}"

a = 'C:/Users/selec/OneDrive/Рабочий стол/файл.txt'
path_dir, name_file, extension = split_func(a)
print(path_dir, "- Путь")
print()
print(name_file, "- Имя файла")
print()
print(extension, "- Расширение")


# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь 
# с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная 
# на процент премии

names = ["Антон", "Bася", "Ирина"]
salaries = [55000, 70000, 40000]
bonuses = ["10.25", "5.15%", "20.10%"]

def generate_dict(name, salary, bonus):
    return {name_1: salary_1 * (1 + float(bonus_1.strip('%')) / 100) for name_1, salary_1, bonus_1 in zip(name, salary, bonus)}

generate = generate_dict(names, salaries, bonuses)
print(generate)

# 4. Создайте функцию генератор чисел Фибоначчи

def fibbonachi_func(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
for i in fibbonachi_func(20):
    print(i)