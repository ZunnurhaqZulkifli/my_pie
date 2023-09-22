# TEXTBOOK
# max_count = len(names) This method is used to count items of in an array

# Solution #1 Using Simple Arrays
# names = ["Zunnurhaq", "Amani", "Arif"]
# employment = ['Admin', 'Cleaner', 'Technician']
# rates_per_hours = ['10', '20', '50']

# total_count = len(names)

# for i in range(total_count):
#     print("My name is,", names[i], "My Job is,", employment[i], "My rate per hour is :", rates_per_hours[i])
#     print("\n")

# Solution #2 Using Dictionaries, More Or less complicated
# my_dict = [
#     {"name": "Cik Rahmah", "age": 37, "city": "Selangor"},
#     {"name": "Shiette", "age": 44, "city": "Kota Bharu"},
#     {"name": "Salman", "age": 54, "city": "Turki"}
# ]

# b = my_dict

# total_count = len(my_dict)

# for i in range(total_count) :
#     print("My Name is", b[i]["name"], "My Age is :",b[i]["age"], "I love",b[i]["city"], "It Is My city")

# Solution #3 - Select On Demand

# From Here
import sys

my_dict = [
    {'name' : 'Zunnruhaq', 'age' : '24', 'job' : 'Tukang Masak Untuk Kucing'},
    {'name' : 'Arif Osman', 'age' : '27', 'job' : 'Tukang Angkat Baldi'},
    {'name' : 'Nana', 'age' : '94', 'job' : 'Tukang Cuci Kasut Kucing'},
    {'name' : 'Jono', 'age' : '55', 'job' : 'Tukang Cuci Baju Rosmah'},
    {'name' : 'Mika', 'age' : '64', 'job' : 'Tukang Habiskan Duit'},
    {'name' : 'Daniel', 'age' : '28', 'job' : 'Tukang Takde Kerja'}
]

t = my_dict
max_len = len(my_dict) - 1

print("\n Select a number value from 0 -", max_len)

for i in range(max_len) :
    print(i,":", t[i]["name"])

u_input = sys.stdin.readline()
print("\n Please Enter a number from 0-2 :", u_input)
input = int(u_input)

if(input <= max_len) :
    print("\n Hi There!, Nama Saya", t[input]["name"],",", "My Umur is :", t[input]["age"], ",", "Kerja Saya Adalah", t[input]["job"], ".")
elif(input < 0) :
    print("The Number", u_input, "is invalid!")


# // functions python

# import sys

# def start() :
#     print("Hello There!,", "How Can I Help You?")

#     ui = sys.stdin.readline()
#     print("\n Please Enter Your Name :", ui)

# def input(ui) :
#     print(ui)

class Forecast:
    def __init__(self, state, hour):
        self.state = state
        self.hour = hour

        def display_info(self):
            print(f"State : {self.state}, Hour: {self.hour}")

        forecast1 = Forecast("AUSTIN", "00:00")

        forecast1.display_info()


# one_day_of_hourly_temperatures = [67,67,68,69,71,73,75,76,79,81,81,80,82,81,81,80,78,75,72,70,67,65,66,66]
# one_day_of_hourly_humidity = [60,65,65,70,70,70,70,75,75,75,75,80,80,85,85,85,85,80,80,80,80,80,80,80]
# one_day_of_hourly_rainfall = [0,0,0,0.1,0.1,0.05,0.1,0.15,0.2,0.3,0.3,0.5,0,0,0,0,0,0,0,0,0,0,0,0]

# count = len(one_day_of_hourly_temperatures)

# class Forecast() :

# test = Forecast("Austin,TX")
# test.display_daily_forecast()
# test.display_weekly_forecast()

# test = Forecast("Austin,TX")
# print("High:", test.get_daily_high())
# print("Low:", test.get_daily_low())
# print("Chance of Rain:", test.get_daily_chance_of_rain(),'%')
