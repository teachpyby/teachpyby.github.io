## Связанные списки



### Односвязный список

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

a.next.value
```


### Задача 1

Считать N строк в список, вывести все элементы списка через пробел.

Пример ввода:
```python
4 # Количество строк
2
3
4
5
```

Вывод:
```python
2 3 4 5
```


### Задача 2

Найти середину списка длины N. Если N чётное - вывести элементы `N/2-1` и `N/2+1 через пробел`

Пример ввода:
```python
5 # Количество строк
1
2
3
4
5
```

Вывод:
```python
3
```



### Задача 3

Определить если в списке длины N цикл.
![loop](./img/loop.gif)


Пример

```python
def has_loop(node):
  # ...

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = b

print(has_loop(a)) # True
```

Note:
Развернуть список в обратном порядке
17. Let's say there are two lists of varying lengths that merge at a certain point; how do we know where the merging point is?
https://www.interviewbit.com/linked-list-interview-questions/#find-length-longest-palindrome-list-linked-list-using-o1-extra-space
