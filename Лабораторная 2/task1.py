money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months=0

while money_capital>=0:
    budget_na_mesyac = money_capital + salary
    if spend > budget_na_mesyac:
        break
    months += 1
    spend = spend * ( 1 + increase)
    money_capital = money_capital - spend + salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
