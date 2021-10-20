## Словари

```python
regions = {}
regions['Brest']     = 1
regions['Vitebsk']   = 2
regions['Gomel']     = 3
regions['Grodno']    = 4
regions['Minsk']      = 5
regions['Mogilev']   = 6
regions['Minsk (c)'] = 7
```



```python
>>> regions['Minsk (c)']  # => 7
```



```python
regions = {'Brest': 1, 'Vitebsk': 2, 'Gomel': 3,
           'Grodno': 4, 'Minsk': 5, 'Mogilev': 6,
           'Minsk (c)': 7}
```



## Итерирование

```python
>>> for key in {'a': 1, 'b': 2, 'c': 3}:
>>>  print(key)
a
b
c
```



```python
>>> for key, value in {'a': 1, 'b': 2, 'c': 3}.items():
>>>   print(key, value)
a 1
b 2
c 3
```



## Проверить наличие в словаре

```python
>>> {'a': 1}['b']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'b'
```



```python
>>> data = {'a': 1}
>>> for e in ['a', 'b']:
>>>   if 'b' in data:
>>>     print(data['b'])
>>>   else:
>>>     print('miss')
1
miss
```



## Обновление данных в словаре
```python
>>> data = {'a': 1}
>>> data['b'] = 2
>>> print(data['b'])
2
```



```python
>>> data = {'a': 1}
>>> data['a'] = 2
>>> print(data['a'])
2
```



```python
>>> data = {'a': 1}
>>> del data['a']
>>> print(data)
{}
```
