# Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

# list

seasons_to_months = [ 
    "Winter",   # January
    "Winter",   # Febrary
    "Spring",   # March
    "Spring",   # April
    "Spring",   # May
    "Summer",   # June
    "Summer",   # July
    "Summer",   # August
    "Autumn",   # September
    "Autumn",   # October
    "Autumn",   # November
    "Winter"    # December
]

index = int(input("[list] Enter the month number >>> ")) - 1

print(f"{index + 1} month in {seasons_to_months[index]}" )

# dict 
# также будет выводится название месяца

seasons_dict = {

    "1" : {
       "month" : "January",
        "season" : "Winter"
    },

    "2" : {
        "month" : "Febrary",
        "season" : "Winter"
    },

    "3" : {
        "month" : "March",
        "season" : "Spring"
    },

    "4" : {
        "month" : "April",
        "season" : "Spring"
    },

    "5" : {
        "month" : "May",
        "season" : "Spring"
    },

    "6" : {
        "month" : "June",
        "season" : "Summer"
    },

    "7" : {
        "month" : "July",
        "season" : "Summer"
    },

    "8" : {
        "month" : "August",
        "season" : "Summer"
    },

    "9" : {
        "month" : "September",
        "season" : "Autumn"
    },

    "10" : {
        "month" : "October",
        "season" : "Autumn"
    },

    "11" : {
        "month" : "November",
        "season" : "Autumn"
    },

    "12" : {
        "month" : "December",
        "season" : "Winter"
    }

}

index = input("[dict] Enter the month number >>> ")

print(f"{index} month is {seasons_dict[index]['month']} and it is {seasons_dict[index]['season']}")







