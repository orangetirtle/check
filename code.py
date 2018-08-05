#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Xenia
#
# Created:     04.08.2018
# Copyright:   (c) Xenia 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, json, csv

country_codes = {'Россия': [460, 461, 462, 463, 464, 465, 466, 467, 468, 469], 'Китай': [690, 691, 692, 693], 'Книжные издания': [978]}
base = {}
price = {}

def open_base():
    global base
    with open("base.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        for i in reader:
            base[i[0]] = i[1]

def open_price():
    global price
    with open("price.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        for i in reader:
            price[i[0]] = i[1]

def cost(card):
    try:
        return int(price[card[0:14].strip('\n')].split()[0])
    except:
        return 0

def what_is_it(code):
    global country_codes
    card = ""

    card += code + '\n'

    country = code[0:3:1]
    flag_country = 0
    for i in country_codes:
        if int(country) in country_codes[i]:
            card += "Страна-изготовитель: " + i + '.\n'
            flag_country = 1
            break

    if not flag_country:
        card += "Неизвестная страна-изготовитель.\n"

    summ1 = 0
    summ2 = 0
    for i in range(1, len(code), 2):
        summ1 += int(code[i])
        summ2 += int(code[i-1])

    summ1 *= 3
    summ1 += summ2
    summ1 %= 10
    summ1 = 10 - summ1

    if summ1 == int(code[len(code)-1]):
        card += 'Товар прошёл проверку на подлинность.\n'
    else:
        card += 'Товар произведён незаконно!\n'

    flag_base = 0
    for i in base:
        if i == code:
            card += 'Наименование товара: ' + base[i] + '.\n'
            card += 'Стоимость товара: ' + price[i] + '.\n'
            flag_base = 1
            break

    if flag_base == 0:
        card += 'К сожалению, этого товара нет в нашей базе данных. Но мы исправимся!\n'
        errors = open('errors.txt', 'a')
        errors.write(code)
        errors.close()

    check = open('check.txt', 'a')
    check.write(card[14::])
    check.write('---------------------------------------------\n')
    check.close()

    return card


file = open('text.txt', 'w')
file.close()
file = open('text.txt', 'r')
check = open('check.txt', 'w')
check.close()
errors = open('errors.txt', 'w')
errors.close()
begin_size = os.path.getsize('text.txt')
all_sum = 0
open_base()
open_price()
flag = 1

while flag:
    now_size = os.path.getsize("text.txt")

    while begin_size < now_size:


        line = file.readline().strip('\n')
        begin_size += len(line) + 2

        if len(line) == 0:
            flag = 0
            break

        all_sum += cost(what_is_it(line))

file.close()

check = open('check.txt', 'a')
check.write('---------------------------------------------\n')
check.write("Общая сумма: " + str(all_sum) + '.\n')
check.write("Кассир: Колесникова Ксения\n")
check.close()

