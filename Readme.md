# teachpyby.github.io

## Создание слайдов для нового урока

- Создаем md файл в нужном нам блоке. Например 000-basics
- Дополняем файл toc.txt в этом блоке строчкой вида `%путь к файлу% %тема урока%`
- Вызываем `make gen_static` в корне репозитория

## Make

```
$ make serve         # Запустить локально
$ make gen_static    # Перегенерировать html страницы с уроками
$ make gen_rating    # Перегенерировать html страницы с рейтингом
$ make gen_all       # Перегенерировать все
```
