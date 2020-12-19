## Простые выражения

```python
>>> 5 + 2     # => 7
>>> 5 - 2     # => 3
>>> 5 / 2     # => 2.5
>>> 5 * 2     # => 10

>>> 5 // 2    # => 2
>>> 5 %  2    # => 1
>>> 3 ** 2    # => 4
```


### Выражения могут быть составными

```python
>>> (5 + 3) / 2 + 4  # =>
```



### Выражения могут быть составными

```python
>>> (5 + 3) / 2 + 4  # => 8
```



## Вывод на экран

```python
>>> print("Привет!")
Hello, World!
```



## Пользовательский ввод

```python
>>> input()
Привет!
'Привет!'
```




### Переменные

```python
a = 10
a         # => 10
b = 15
b         # => 15

a + b     # => 25
```



### Комментарии

```python
# Это комментарий, его программа не исполняет
y = 10
x = 2 + y
```



### Пример. Ввод и вывод данных

```python
print("Введи свое имя:")
name = input()
greeting = "Привет, " + name + "!"
print(greeting)
```



### Условия

```python
x = int(input())
if x > 0:
  print(x)
else:
  print(-x)
print('end of if')
```



### Вложенные условные конструкции

![image](https://upload.wikimedia.org/wikipedia/commons/c/c9/2D_Cartesian_Coordinates.PNG)


```python
x = int(input())
y = int(input())
if x > 0:
  if y > 0:               # x > 0, y > 0
    print("Первая четверть")
  else:                   # x > 0, y < 0
    print("Четвертая четверть")
else:
  if y > 0:               # x < 0, y > 0
    print("Вторая четверть")
  else:                   # x < 0, y < 0
    print("Третья четверть")
```



### Операторы сравнения

```python
print(10 < 10) # False
print(10 > 9)  # True
print(10 <= 10) # True
print(10 >= 10) # True
print(10 == 10) # True
print(10 != 10) # True
```



### Логические операторы

```python
print(10 % 2 == 0 and 10 % 5 == 0) # True
print(9 % 3 == 0 or 9 % 2 == 0) # True
print(not (1 > 0)) # False
print(10 % 2 == 0 and 10 % 5 == 0 and not (1 > 0)) # False
```



### Каскадные условные конструкции

```python
x = int(input())
y = int(input())
if x > 0 and y > 0:
  print("Первая четверть")
elif x > 0 and y < 0:
  print("Четвертая четверть")
elif y > 0:
  print("Вторая четверть")
else:
  print("Третья четверть")
```



### Спасибо
