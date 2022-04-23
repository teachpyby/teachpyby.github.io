## Практика CSS. Часть 3

Работа с фоном



## background-color

Что это?



## background-color

Заливка фона элемента одним цветом

```css
div {
	background-color: orange;
}
```



## background-image

Что это?



## background-image

Задает фоновое изображение


*Если изображение маленькое - оно будет повторяться как по горизонтали, так и по вертикали*


```css
div {
	background-image: url("путь к изображению");
}
```



## background-repeat

Что это?



## background-repeat

| Значение  | Будет повторяться |
| --------- | -------- |
| no-repeat | Не будет |
| repeat-x  | По оси X |
| repeat-y  | По оси Y |
| repeat    | По всем осям (по умолчанию) |



## background-position

Что это?



## background-position

Сдвиг фонового изображения по зарезервированным словами

```css
div {
	background-position: right bottom;
}
```

Продолжение →



## background-position

| Значение по горизонтали | Положение |
| --------- | -------- |
| left      | Слева (по умолчанию) |
| right     | Справа |
| center    | По центру |

Продолжение →



## background-position

| Значение по вертикали | Положение |
| --------- | -------- |
| top       | Сверху (по умолчанию) |
| bottom    | Снизу |
| center    | По центру |

Продолжение →



## background-position

Сдвиг фонового изображения по значениям

Первое значение: сдвиг по оси X

Второе значение: сдвиг по оси Y

```css
div {
	background-position: 100px 30px;
}
```



## background-attachment

Что это?



## background-attachment

Задаёт, будет ли прокручиваться фон вместе с текстом или оставаться на месте 

| Значение | Описание |
| -------- | -------- |
| scroll   | Будет прокручиваться (по умолчанию) |
| fixed    | Будет оставаться на месте |



## background

Что это?



## background

Это свойство-сокращение в котором в любом порядке можно писать значения всех вышеуказанных свойств

```css
div {
	background-color: green;
	background-image: url("image.png");
	background-repeat: repeat-x;
	background-position: left bottom;
}
```

```css
div {
	background: green url("image.png") repeat-x left bottom;
}
```