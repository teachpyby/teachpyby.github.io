## Функции

```python
def max(a, b):
  if a > b:
    return a
  else:
    return b

res = max(4, 10)
print(res) # 10
print(max(max(4, 10), 1)) # 10

```



## Функции с переменным числом аргументов

```python
def max(*a):
  res = a[0]
  for val in a[1:]:
    if val > res:
      res = val
  return res

print(max(1, 2, 3, 4, 5))  # 5

```



## Локальные и глобальные переменные

```python
a = 1
def f():
  print(a) # ???

f()
print(a) # ???
```



```python
a = 1
def f():
  a = 2
  print(a) # ???

f()
print(a)  # ???
```



```python
a = 1
def f():
  a += 1
  print(a) # ???

f()
print(a)  # ???
```


```python
a = 1
def f():
  global a
  a += 1
  print(a) # ???

f()
print(a)  # ???
```



## Пример

```python
def isRainbowColor(color):
  colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet']
  if (color in colors):
    result = True

  return result

print(isRainbowColor('green')) # ???
print(isRainbowColor('brown')) # ???
```



## Рекурсия

```python
def short_story():
  print("У попа была собака, он ее любил.")
  print("Она съела кусок мяса, он ее убил,")
  print("В землю закопал и надпись написал:")
  short_story()

short_story()
```


```python
def short_story(counter):
  if counter == 0:
    return
  print("У попа была собака, он ее любил.")
  print("Она съела кусок мяса, он ее убил,")
  print("В землю закопал и надпись написал:")
  short_story(counter - 1)

short_story(5)
```



## факториал

```
5! = 5 * 4 * 3 * 2 * 1 = 120
0! = 1
```

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```
