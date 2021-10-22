## Действительные числа

```python
>>> a = float(4.5)
>>> a - 2     # => 2.5
>>> a / 2     # => 2.25
>>> a * 2     # => 9.0
>>> a // 2    # => 2.0
```



## Библиотека math

```python [1|2|3|4|5|6]
>>> import math
>>> math.ceil(4.8) # 5
>>> math.ceil(4.2) # ?
>>> math.ceil(-1.5) # ?
>>> math.floor(4.8) # 4
>>> math.floor(-4.1) # ?
```




### Некоторые функции

```python [1|2|3|4|5|6|7-12]
round(x)
round(x, n)
floor(x)
ceil(x)
abs(x)
sqrt(x)
# Тригонометрия
sin(x)
cos(x)
tan(x)
degrees(x)
radians(x)
```
[Подробное описание функций из math](https://pyprog.pro/python/st_lib/math.html)




### Практическая задача №2

За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? Программа получает на вход числа n и m.


#### Решение
``` python
import math

n = int(input())
m = int(input())

print(math.ceil(m / n))
```




### Практическая задача №2

Условие
Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на a метров, а за ночь спускаясь на b метров. На какой день улитка доползет до вершины шеста?

Программа получает на вход натуральные числа h, a, b.

Программа должна вывести одно натуральное число. Гарантируется, что a>b.


#### Решение
``` python
import math

h = int(input())
a = int(input())
b = int(input())

h0 = h - a
d = 0
if h0 <= 0:
    h0 = 0

d = math.ceil(h0 / (a-b))

print(d + 1)
```



## Цикл for
```python
for name in 'uberkek', 'Monolith986', 'Staivon',
  '@Vikusssa', 'KloyJokes', 'TheDiamondX', 'Cвета', 'Матвей':
    print(name, ', ты сделал домашку?', sep='')
```

```python
pupils = ['uberkek', 'Monolith986', 'Staivon',
  '@Vikusssa', 'KloyJokes', 'TheDiamondX', 'Cвета', 'Матвей']
for pupil in pupils:
  print(pupil, ', ты сделал домашку?', sep='')

```



## range

```python
banana0_price = int(input())
for i in 1, 2, 3, 4:
  print(f'стоимость банана {i} - {banana0_price * i}')
```


```python
banana0_price = int(input())
banana_total = int(input())
for i in range(banana_total):  # то же самое: for i in 0, 1, 2, 3, ..., banana_total:
  print(f'стоимость банана {i} - {banana0_price * i}')
```



## Цикл while

```python [0|5-7]
banana0_price = int(input())
banana_total = int(input())
i = 0
while i <= banana_total:
  print(f'стоимость банана {i} - {banana0_price * i}')
  i += 1
```



## Инструкция `break`

Мама сказала купить `N` бананов и дала `K` денег. . Первый банан стоит `M` рублей. Второй банан стоит `M * 2` рублей и так далее.
После каждого купленного банана перед мамой надо отчитываться. В конце нужно вывести сколько бананов было куплено


```python [0|1-2|3|4|7|12]
banana_total = int(input('Сколько мама сказала купить бананов: '))
available_money = int(input('Сколько мама дала денег: '))
banana0_price = int(input('Стоимость первого банана: '))
bananas_count = 0
for i in range(1, banana_total):
  banana_i_price = banana0_price * i
  if available_money - banana_i_price > 0:
    available_money = available_money - banana_i_price
    bananas_count += 1
    print(f'Мам, я купил банан за {banana_i_price}, у меня осталось {available_money} денег')
  else:
    break
print(f'Я купил {bananas_count} бананов')

```



## Лесенка

По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
Например:
Ввод:
4
Вывод:
1
12
123
1234



## Потерянная карточка

Условие
Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.

