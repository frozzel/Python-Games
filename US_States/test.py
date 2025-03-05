with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    # print(data)
    
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    # print(temperatures)
    
import pandas
import statistics

data = pandas.read_csv("weather_data.csv")
# print(data["day"])

data_dict = data.to_dict()
# print(data_dict)

data_list = data["temp"].to_list()
# print(data_list)

average_temp = statistics.mean(data_list)
# print(average_temp)

easy = data["temp"].mean()
# print(easy)

max = data["temp"].max()
# print(max)

test = data.day
# print(test)

monday = data[data.day == "Monday"]
# print(monday)

highest_temp = data[data.temp == data.temp.max()]
# print(highest_temp)

monday_temp = int(monday.temp)
# print(monday_temp)

fahrenheit = (9/5) * monday_temp + 32
# print(fahrenheit)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

