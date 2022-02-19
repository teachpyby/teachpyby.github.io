## CSS

```html
<p style="font-size: 25px;">Hello World!</p>
```



## Наследование стилей (пример 1)
```html
<div style="border: solid 1px;">
    Блок с рамкой шириной 1 пиксель

    <p>Параграф без рамки</p>
</div>
```



## Наследование стилей (пример 2)
```html
<div style="font-size: 20px;">
    Размер шрифта — 20 пикселей

    <p>Вложенный параграф - также 20 пикселей</p>
</div>
```



## Тег style
```html
<style>
    div {
        font-size: 20px;
    }
</style>

<div>
    Размер шрифта — 20 пикселей

    <p>Вложенный параграф - также 20 пикселей</p>
</div>
```



### Единицы измерения
 * Чёткие величины:
    - пиксели **px** - зависит от реальных размеров пикселя
 * Относительные:
    - **em** - текущего шрифта
    - **%** - текущего контекста
    - **rem** - стандартного размера шрифта html
    - **vw** - % ширины окна
    - **vh** - % высоты окна
    - **vmin** - min(vw, vh)
    - **vmax** - max(vw, vh)



### Классы
```html
<p class="paragraph">Hello world!</p>
```
```css
.paragraph {
    background-color: yellow;
}
```



### Селекторы
```html
<p id='red'>Hello world!</p>
```
```css
#red {
  color: red;
}
```



### Дополнительная информация + Домашка
 - [Интерактивный курс "CSS для начинающих" (!!! ДОМАШКА)](https://ru.code-basics.com/languages/css)
 - CSS. Уровень 1
   - [Основы CSS](https://webref.ru/course/css-basics)
   - [Текст в CSS](https://webref.ru/course/css-text)
   - [Блочная модель в CSS](https://webref.ru/course/box-model)
   - [Позиционирование в CSS](https://webref.ru/course/positioning)
   - [Продвинутый CSS](https://webref.ru/course/css-advanced)



### Дополнительная информация + Домашка
 - CSS. Уровень 2
   - [Блочная модель](https://webref.ru/course/block-model)
   - [Блочные и строчные элементы](https://webref.ru/course/block-inline)
   - [float в теории и на практике](https://webref.ru/course/float)
   - [Позиционирование элементов](https://webref.ru/course/position)



### Интересное
 - [Почему блочная верстка лучше табличной?](https://artjoker.ua/ru/blog/pochemy-blochnaya-verstka-saita-luchshe-tablichnoy/)
 - [Журанал "Код"](https://t.me/thecodemedia)