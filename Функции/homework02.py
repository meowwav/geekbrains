# Реализовать функцию, принимающую несколько параметров,          
# описывающих данные пользователя:                                
# имя, фамилия, год рождения, город проживания, email, телефон.   
# Функция должна принимать параметры как именовонные аргументы.   
# Реализовать вывод данных о пользователе одной строкой.          


# default для быстрой проверки работы функции
def user_info(name="Name", 
              surname="Surname", 
              year_of_birth="1980", 
              city="City", 
              email="email@example.com", 
              phone_number="123 456 78 90"):
    # Преобразуем поток данных в форматированную строку
    return f"{name} {surname}, {year_of_birth} year of birth, living in {city}.\nEmail: {email} \nPhone number: {phone_number}"

name = input("Enter the name >>> ")
surname = input("Enter the surname >>> ")
year_of_birth = input("Enter the year of birth >>> ")
city = input("Enter the city of residence >>> ")
email = input("Enter the email-adress >>> ")
phone_number = input("Enter the phone number >>> ")

print(user_info(name=name, 
                surname=surname, 
                year_of_birth=year_of_birth, 
                city= city, email=email, 
                phone_number=phone_number))