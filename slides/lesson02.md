## Действительные числа

```python
>>> a = float(4.5)
>>> a - 2     # => 2.5
>>> a / 2     # => 2.25
>>> a * 2     # => 9.0
>>> a // 2    # => 2.0
```



## Библиотека math

```python [1|2|3|4|5]
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




### Практическая задача

Дано положительное действительное число X. Выведите его первую цифру после десятичной точки. (4. **9** 234523)



#### Решение
``` python
import math

a = float(input())

print(int(a * 10) % 10)

```


