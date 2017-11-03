#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

DATE_FORMAT = '%m-%d-%Y'
FILE_NAME = 'GasPrices.txt'


def average_price(gas_prices_dict):
    average_price_per_year=dict()

    for date_value in gas_prices_dict:
        if date_value.year in average_price_per_year:
            average_price_per_year[date_value.year].append(float(gas_prices_dict[date_value]))
        else:
            average_price_per_year[date_value.year] =[float(gas_prices_dict[date_value])]

    for year in average_price_per_year:
        values=average_price_per_year[year]
        print("The average price in {Year} is ${cost:.3f}/gallon".format(Year=year, cost=sum(values)/len(values)))


def average_price_month(gas_prices_dict):
    average_price_per_month=dict()
    for date_value in gas_prices_dict:
        month_year = date_value.strftime('%m-%Y')
        print(month_year)
        if month_year in average_price_per_month:
            average_price_per_month[month_year].append(float(gas_prices_dict[date_value]))
        else:
            average_price_per_month[month_year]=[float(gas_prices_dict[date_value])]
    for month in average_price_per_month:
        values=average_price_per_month[month]
        print("The average price in {Month} is ${cost:.3f}/gallon".format(Month=month, cost=sum(values)/len(values)))


def read_file(file_name):
    price_dictionary = dict()
    with open(file_name, 'r') as file_object:
        file_contents = file_object.readlines()
        for line in file_contents:
            date, price = line.strip('\n').split(":")
            price_dictionary[datetime.strptime(date, DATE_FORMAT)] = price
    return price_dictionary


def high_low_price(gas_prices_dict):
    price_per_year=dict()
    for date_value in gas_prices_dict:
        if date_value.year in price_per_year:
            price_per_year[date_value.year].append(float(gas_prices_dict[date_value]))
        else:
            price_per_year[date_value.year] =[float(gas_prices_dict[date_value])]
    for year in price_per_year:
        values=price_per_year[year]
        print("In {Year},the highest gas price is {highest} and the lowest gas price is {lowest}".format(Year=year, highest=max(price_per_year[year]),lowest=min(price_per_year[year])))


def get_value(x):
    return x[1]


def sort_value(gas_prices_dict,descending,file_name):

    sorted_values=sorted(gas_prices_dict.items(), key=get_value,reverse=descending)
    with open(file_name,'w') as file_object:
        file_object.write("Date\tPrice($/gallon)\n")
        for date_value, rate in sorted_values:
            file_object.write("{date_value}\t{cost}\n".format(date_value=date_value.strftime('%d-%m-%y'),cost=rate))
if __name__ == '__main__':
    gas_prices = read_file(FILE_NAME)
    average_price(gas_prices)
    average_price_month(gas_prices)
    high_low_price(gas_prices)
    sort_value(gas_prices, descending=False,file_name='lowest_highest.txt')
    sort_value(gas_prices, descending=True,file_name='highest_lowest.txt')
