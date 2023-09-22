import sys

print("WheAthHeR PrOGrAmmeE \n")

class Forecast:
    def __init__(self):
        self.state = 'Austin'
        self.hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                      12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.temperatures = [67, 67, 68, 69, 71, 73, 75, 76, 79, 81,
                             81, 80, 82, 81, 81, 80, 78, 75, 72, 70, 67, 65, 66, 66]
        self.humidity = [60, 65, 65, 70, 70, 70, 70, 75, 75, 75,
                         75, 80, 80, 85, 85, 85, 85, 80, 80, 80, 80, 80, 80, 80]
        self.rainfall = [0, 0, 0, 0.1, 0.1, 0.05, 0.1, 0.15,
                         0.2, 0.3, 0.3, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.days = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']

    def fn_name(self):
        return "All Report"

    def daily_high(self):
        return max(self.temperatures)

    def daily_low(self):
        return min(self.temperatures)

    def one_liner(self):
        print("\n\t Temperature at 2PM : ", self.temperatures[13], "F", "\n\t Humidity at 11PM",
              self.humidity[22], "%", "\n\t Rainfall at 9AM :", self.rainfall[8], "\n")

    def data_a_day(self):
        c = len(self.hours) - 1

        for i in range(c):
            print(
                f"\t Hour: {self.hours[i]}, Temperature: {self.temperatures[i]}, , humidity: {self.humidity[i]}, Rainfall: {self.rainfall[i]}")

    def weekly_data(self):
        w = len(self.days)
        r = sum(self.rainfall) + 8.2

        for i in range(w):
            print("\t", self.days[i], ":", "\tHigh", get.daily_high(
            ), ",", "Low", get.daily_low(), ",", "Rain :", r, "%.")
            
my_dict = [
    {'name': 'All Functions'},
    {'name': '24HRS Data'},
    {'name': 'Weekly Data & One Liner'},
    {'name': 'Min Max'},
    {'name': 'One Liner'},
]

t = my_dict
max_len = len(my_dict) - 1
print("\n Select a number value from 1 -", max_len)
for i in range(max_len):
    print(i, ":", t[i]["name"])

u_input = sys.stdin.readline()
print("\n Please Enter a number from 1 -", max_len, u_input)
sw = int(u_input)

if(sw == 0):
    get = Forecast()
    print(get.fn_name())
    get.data_a_day()
    get.one_liner()
    get.weekly_data()
elif(sw == 1):
    get = Forecast()
    get.fn_name()
    get.data_a_day()
elif(sw == 2):
    get = Forecast()
    print(get.fn_name())
    get.one_liner()
    get.weekly_data()
elif(sw == 3):
    get = Forecast()
    print("low",get.daily_low())
    print("high", get.daily_high())

elif(sw < 0 or sw > max_len) :
    exit
