from classes.create_tables import TablesCreator
from classes.fill_db import FillDB
from classes.db_manager import DBManager


def main():
    """Код выполняющий программу программы"""
    employers = ['skyeng', 'FIT SERVICE', 'Альфа-Банк', 'ООО Газпром ЦПС', 'Answeroom', 'ПАО Ростелеком',
                 'SberTech', 'Тинькофф', 'ООО ВсеИнструменты.ру', 'Яндекс Крауд']
    print(f"""Программа загружает информацию по вакансиям из списка работодателей {', '.join(employers)}""")
    user_emp = input("Введите название для таблицы с работодателями: ")
    tables_creator = TablesCreator
    tables_creator.create_employers(user_emp)
    user_vac = input("Введите название для таблицы с вакансиями: ")
    tables_creator.create_vacancies(user_vac, user_emp)
    print('Загрузка данных...')
    fill_db = FillDB(employers)
    fill_db.fill_db_employers(user_emp)
    try:
        fill_db.fill_db_vacancies(user_vac)
    except TypeError:
        print("Данные не получены")
    db_manager = DBManager

    # Цикл для получения информации из БД
    while True:
        print()
        print('Для вывода информации выберите пункт в меню:\n'
              '1 - список компаний и кол-во вакансий у каждой компании\n'
              '2 - список всех вакансий с указанием названия компании и вакансии, зарплаты, ссылки на вакансию\n'
              '3 - средняя зп по вакансиям\n'
              '4 - список вакансий у которых зп выше средней\n'
              '5 - список вакансий, в названии которых содержатся слова\n'
              '0 - Завершение работы')
        user_input = input('Выберите пункт:')
        print()
        if user_input == '1':
            data = db_manager.get_companies_and_vacancies_count(user_emp, user_vac)
            for d in data:
                print(d)
        elif user_input == '2':
            all_info = db_manager.get_all_vacancies(user_emp, user_vac)
            for info in all_info:
                print(info)
        elif user_input == '3':
            salary = db_manager.get_avg_salary(user_vac)
            print(salary)
        elif user_input == '4':
            top_salary = db_manager.get_vacancies_with_higher_salary(user_vac)
            for top in top_salary:
                print(top)
        elif user_input == '5':
            user_word = input('Введите слова для поиска вакансии:')
            vacancies = db_manager.get_vacancies_with_keyword(user_vac, user_word)
            if vacancies == []:
                print('Результат не найден')
                continue
            for vac in vacancies:
                print(vac)
        elif user_input == '0':
            print('Завершение работы...')
            exit()
        else:
            print('Неверный ввод')


if __name__ == "__main__":
    main()
