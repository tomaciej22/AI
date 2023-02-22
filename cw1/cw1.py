import csv
import numpy as np
import pandas as pd

#zad3 wyswietlenie csv
# with open('dane\Churn_Modelling.csv', 'r') as file:
#     reader = csv.reader(file)
#     headers = next(reader)
#     print(f"{' | '.join(headers)}")
#     for row in reader:
#         print(f"{' | '.join(row)}")

#zad3a jakie mamy klasy
# ostatnia_kolumna = 'Exited'
#
# with open('dane\Churn_Modelling.csv', 'r') as file:
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
# with open('dane\Churn_Modelling.csv', 'r') as file:
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
# customer_id_kolumna = 'CustomerId'
# with open('dane\Churn_Modelling.csv', 'r') as file:
#     odczyt = csv.DictReader(file)
#
#     min_value = float('inf')
#     max_value = float('-inf')
#
#     for row in odczyt:
#         value = int(row[customer_id_kolumna])
#         if value < min_value:
#             min_value = value
#         if value > max_value:
#             max_value = value
#
#     print(f"Najmniejsza wartość: {min_value}")
#     print(f"Największa wartość: {max_value}")

#zad3d
# df = pd.read_csv('dane\Churn_Modelling.csv')
# print('Liczba różnych wartości dla każdego atrybutu:')
# print(df.nunique())

#zad3e
# df = pd.read_csv('dane\Churn_Modelling.csv')
# print('Lista wszystkich różnych wartości dla każdego atrybutu:')
# for kolumny in df.columns:
#     print(kolumny)
#     print(df[kolumny].unique())

#zad3f
# df = pd.read_csv('dane\Churn_Modelling.csv')
# print('Odchylenie standardowe dla poszczególnych atrybutów:')
# for kolumny in df.columns:
#     if df[kolumny].dtype == 'float64':
#         print(f'Cały plik CSV: {df[kolumny].std()}')
#         print(f'Klasy decyzyjne: {df.groupby("Exited")[kolumny].std()}\n')

#zad4a
# kolumna = 'Exited'
# df = pd.read_csv('dane\Churn_Modelling.csv')
# liczba_wierszy = df.shape[0]
# liczba_brakujacych_wierszy = int(liczba_wierszy * 0.1)
# losowe_brakujace_wiersze = np.random.choice(liczba_wierszy, size=liczba_brakujacych_wierszy, replace=False)
# df.loc[losowe_brakujace_wiersze, kolumna] = np.nan
#
# if df[kolumna].dtype == 'float64':
#     atrybut_numeryczny = df[kolumna].mean()
#     df[kolumna].fillna(atrybut_numeryczny, inplace=True)
# else:
#     atrybut_symboliczny = df[kolumna].mode()[0]
#     df[kolumna].fillna(atrybut_symboliczny, inplace=True)
#
# print(df.head(10))

#zad5a
# def znormalizowane_wartosci_atrybutu(sciezka_pliku, indeks_atrybutow, poczatek_przedzialu, koniec_przedzialu):
#     data = []
#     with open(sciezka_pliku, 'r') as file:
#         reader = csv.reader(file)
#         header = next(reader)
#         data.append(header)
#         min_val = float('inf')
#         max_val = float('-inf')
#         for row in reader:
#             wartosc_atrybutow = float(row[indeks_atrybutow])
#             if wartosc_atrybutow < min_val:
#                 min_val = wartosc_atrybutow
#             if wartosc_atrybutow > max_val:
#                 max_val = wartosc_atrybutow
#             data.append(row)
#
#     dane_znormalizowane = []
#     dane_znormalizowane.append(header)
#     for row in data[1:]:
#         wartosc_atrybutow = float(row[indeks_atrybutow])
#         wartosc_znormalizowana = ((wartosc_atrybutow - min_val) * (koniec_przedzialu - poczatek_przedzialu) / (max_val - min_val)) + poczatek_przedzialu
#         row[indeks_atrybutow] = wartosc_znormalizowana
#         dane_znormalizowane.append(row)
#
#     with open('znormalizowane_dane.csv', 'w', newline='') as file:
#         zapis = csv.writer(file)
#         zapis.writerows(dane_znormalizowane)
#
#     print(f"Atrybut  {header[indeks_atrybutow]} znormalizowany do przedziału ({poczatek_przedzialu}, {koniec_przedzialu})")
#
# znormalizowane_wartosci_atrybutu('dane\Churn_Modelling.csv', 1, -1, 1) # <-1,1>

#zad5c
