import csv
import numpy as np

#zad3 wyswietlenie csv
# with open('Churn_Modelling.csv', 'r') as file:
#     reader = csv.reader(file)
#     headers = next(reader)
#     print(f"{' | '.join(headers)}")
#     for row in reader:
#         print(f"{' | '.join(row)}")

#zad3a jakie mamy klasy
# ostatnia_kolumna = 'Exited'
#
# with open('Churn_Modelling.csv', 'r') as file:
#     odczyt = csv.DictReader(file)
#
#     nazwy_klas = set(row[ostatnia_kolumna] for row in odczyt)
#
#     print(f"Ile klas w kolumnie: {len(nazwy_klas)}")
#     print(f"Nazwy klas: {', '.join(nazwy_klas)}")

#zad3b ile razy wystepuje 0 i 1 w kolumnie Exited
# ostatnia_kolumna = 'Exited'
#
# licznik_zero = 0
# licznik_jeden = 0
#
# with open('Churn_Modelling.csv', 'r') as file:
#     odczyt = csv.DictReader(file)
#
#     for row in odczyt:
#         if row[ostatnia_kolumna] == '0':
#             licznik_zero += 1
#         elif row[ostatnia_kolumna] == '1':
#             licznik_jeden += 1
#
# print(f"Ile razy 0: {licznik_zero}")
# print(f"Ile razy 1: {licznik_jeden}")

#zad3c min i max wartosc w atrybucie
customer_id_kolumna = 'CustomerId'
with open('Churn_Modelling.csv', 'r') as file:
    reader = csv.DictReader(file)

    min_value = float('inf')
    max_value = float('-inf')

    for row in reader:
        value = int(row[customer_id_kolumna])
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    print(f"Najmniejsza wartość: {min_value}")
    print(f"Największa wartość: {max_value}")