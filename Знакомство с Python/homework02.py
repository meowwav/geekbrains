# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Enter time in seconds >>> "))
hours = 0
minutes = 0
seconds = 0

if time >= 3600:
    hours = time // 3600
    time -= 3600 * hours

if time >= 60:
    minutes = time // 60
    time -= 60 * minutes

seconds = time

if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds) 

print(f"{hours}:{minutes}:{seconds}")

