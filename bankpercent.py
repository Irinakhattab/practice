#Создаю словарь распределением процентных ставок
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

#Ввожу сумму вклада
money = int(input("Введите сумму:"))

#выделяю процентные ставки банков в список
procent = list(per_cent.values())

#записываю доход в каждом банке в переменные и округляю
bankTKB = int(procent[0]/100*money)
bankCKB = int(procent[1]/100*money)
bankVTB = int(procent[2]/100*money)
bankSBER = int(procent[3]/100*money)

# создаю список с возможными доходами
deposit = [bankTKB, bankCKB, bankVTB, bankSBER]

# вывожу в консоль список возможных доходов
print("Возможный доход:", deposit )

#сортирую список доходов
deposit.sort()

#вывожу максимальный доход
print("Максимальная сумма, которую вы можете заработать - ", deposit[-1])
