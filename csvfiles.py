import csv
with open('C:\Users\vinit\Desktop\Calculator1\Calculator1\data\Unit Test Addition.csv', mode='r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['Value 1'])

import csv
with open('C:\Users\vinit\Desktop\Calculator1\Calculator1\data\Unit Test Subtraction.csv', mode='r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['Value 1'])

import csv
with open('C:\Users\vinit\Desktop\Calculator1\Calculator1\data\Unit Test Multiplication.csv', mode='r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['Value 1'])

import csv
with open('C:\Users\vinit\Desktop\Calculator1\Calculator1\data\Unit Test Division.csv', mode='r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['Value 1'])

import csv
with open('C:\Users\vinit\Desktop\Calculator1\Calculator1\data\Unit Test Square.csv', mode='r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['Value 1'])

import csv
with open('C:\Users\vinit\Desktop\Calculator1\Calculator1\data\Unit Test Square Root.csv', mode='r') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['Value 1'])