## 
Селекторы CSS



## Группировка селекторов
```css
h2 {
	color: red;
}
h3 {
	color: red;
}
p {
	color: red;
}
```
```css
h2, h3, p {
	color: red;
}
```



## Вложенность тегов
```css
div p {
	color: red;
}
```



## Селектор по ID

Формат: #ID_NAME

```html
<p id="test">
	Абзац с атрибутом id в значении "test".
</p>
```
```css
#test {
	color: green;
}
```



## Вложенность тегов и ID
```css
#test p {
	color: red;
}
```



## Селектор по классам

Формат: .CLASS_NAME
```html
<h2 class="test">
	Заголовок h2 с классом test.
</h2>
```
```css
.test {
	color: red;
}
```



## Особенности работы с селектором по классам
Абзацы с классом test
```css
p.test {
	color: red;
}
```

Элементы с классом test внутри абзацев 
```css
p .test {
	color: red;
}
```