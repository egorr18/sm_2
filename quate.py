import random

# Словник міст та відомих людей
city_dict = {
    "Київ": ["Тарас Шевченко", "Леся Українка", "Богдан Ступка"],
    "Львів": ["Іван Франко", "Соломія Крушельницька", "Андрій Садовий"],
    "Харків": ["Сергій Жадан", "Олександр Довженко"],
    "Одеса": ["Ісаак Бабель", "Кіра Муратова", "Жанна Бадоєва"],
    "Дніпро": ["Олег Блохін", "Лілія Подкопаєва"]
}

# Пошук по місту
def search_by_city(city_name):
    return city_dict.get(city_name, "Місто не знайдено.")

# Сортування по довжині імен в кожному місті
def sort_people_by_name_length(city_name):
    if city_name in city_dict:
        return sorted(city_dict[city_name], key=len)
    return "Місто не знайдено."

# Вивід N випадкових постатей з усієї мапи
def get_random_figures(n):
    all_people = []
    for people in city_dict.values():
        all_people.extend(people)
    return random.sample(all_people, min(n, len(all_people)))

# Меню користувача
def main():
    while True:
        print("\nМеню:")
        print("1. Пошук відомих людей за містом")
        print("2. Сортувати людей по довжині імен у місті")
        print("3. Показати N випадкових постатей з усієї України")
        print("4. Вийти")

        choice = input("Оберіть опцію (1-4): ")

        if choice == "1":
            city = input("Введіть назву міста: ")
            result = search_by_city(city)
            print(result)

        elif choice == "2":
            city = input("Введіть назву міста: ")
            result = sort_people_by_name_length(city)
            print(result)

        elif choice == "3":
            try:
                n = int(input("Скільки випадкових постатей показати? "))
                result = get_random_figures(n)
                print(result)
            except ValueError:
                print("Будь ласка, введіть число.")

        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main()