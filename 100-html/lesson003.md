## HTML

```html
<h1>Hello world</h1>
<p>Пример HTML разметки</p>
```



## Теги
```html
<h1>Заголовок первого уровня</h1>
<h6>Заголовок шестого уровня</h6>
<p>Первый параграф</p>
<p>Второй параграф</p>
<a href="google.com">Ссылка на Google.com</a>
<p>
    <img src="https://logosarchive.com/wp-content/uploads/2021/08/Minecraft-icon.png" alt="Minecraft logo"
        width="100" />
</p>
```



### Вложенность тегов
```html
<ul>
    <li>Первый элемент списка</li>
    <li>Второй элемент списка</li>
</ul>
```

### Атрибуты тегов
```html
<p>Стандартный вывод текста</p>
<p align="center">Вывод текста по центру</p>
<p align="right">Вывод текста справа</p>
```



### Параграфы <p>
```html
<p>Первый параграф</p>
<p>Второй параграф</p>
```

### Начертание текста
```html
<p><b>"Жирное"</b> начертание.</p>
<p>Выделения <strong>важного</strong> текста.</p>
<p><em>Логическое</em> выделение.</p>
<p><i>Курсивное</i> выделение.</p>
```



### Заголовки
```html
<h1>Заголовок первого уровня</h1>
<h2>Заголовок второго уровня</h2>
<h3>Заголовок третьего уровня</h3>
<h4>Заголовок четвёртого уровня</h4>
<h5>Заголовок пятого уровня</h5>
<h6>Заголовок шестого уровня</h6>
```



### Списки
```html
<p>Маркированный список</p>
<ul>
    <li>Первый элемент</li>
    <li>Второй элемент</li>
    <li>Нумерованный список
        <ol>
            <li>Первый элемент</li>
            <li>Второй элемент</li>
        </ol>
    </li>
</ul>
```



### Таблицы
```html
<table>
    <thead>
        <!-- Блок с заголовками -->
        <tr>
            <!-- Строка -->
            <th>Ячейка 1</th>
            <th>Ячейка 2</th>
        </tr>
    </thead>
    <tbody>
        <!-- Тело таблицы -->
        <tr>
            <!-- Вторая строка -->
            <td>Ячейка 2</td>
            <td>Ячейка 3</td>
        </tr>
    </tbody>
</table>
```


### Таблицы. Объединение ячеек
```html
<table>
    <thead>
        <tr>
            <th>Заголовок 1</th>
            <th>Заголовок 2</th>
            <th>Заголовок 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ячейка 1</td>
            <td colspan="2">Объединённая ячейка 2-3</td>
        </tr>
    </tbody>
</table>
```



### Специальные символы
``` html
<p>
    &lsquo;&alpha;&lowast;&beta;&asymp;&real;&rsquo;
</p>
<p>
    &lt;p&gt; разметка не будет обработана &lt;/p&gt;
</p>
```

<sub><sub><sub>[Мнемоники в HTML](https://ru.wikipedia.org/wiki/%D0%9C%D0%BD%D0%B5%D0%BC%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8_%D0%B2_HTML)</sub></sub>




### Ссылки
```html
<p>
    <a href="https://google.com/">Абсолютная ссылка</a>
</p>
<p>
    <a href="/catalog/item">Относительная ссылка</a>
</p>
<p>
    <a href="#anchor">Ссылка-якорь</a>
</p>
<div id="anchor">
    <h2>Заголовок</h2>
</div>
```




### Форматированный текст
```html
<p>Вы ушли,</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;как говорится,</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;в
    мир в иной.</p>
<pre>
Вы ушли,
        как говорится,
                в мир в иной.
</pre>
```



### Вставка компьютерного кода в HTML
```html
<code>
    <pre>
// Пример кода на JavaScript
const square = (num) => {
    return num * num;
};
    </pre>
</code>
<code>
    <<span>p</span>>Вставляем тег p в виде простого текста <<span>/p</span>>
</code>
```



### Дополнительная информация + Домашка
[Интерактивный курс "HTML для начинающих" (!!! ДОМАШКА)](https://ru.code-basics.com/languages/html)
[WebReference](https://webref.ru/course/html-basics)
[Основы HTML](https://webref.ru/course/html-basics)
[Содержимое в HTML](https://webref.ru/course/html-content)
[Самоучитель HTML](https://webref.ru/course/html-tutorial)
[Разделы веб-страницы](https://webref.ru/course/section)
[Формы в HTML](https://webref.ru/course/html5-form)
