﻿# Задание 1
Автомат принимает накопительные скидочные карты
и при своем расчете учитывает количество баллов, 
по которому начисляет процент скидки:

- От 0 до 100 баллов - скидка 1%
- От 100 до 200 баллов - скидка 3 %
- От 200 до 500 баллов - скидка 5%
- От 500 баллов - скидка 10%

Задание: Составить такой набор тестовых данных для автомата, 
при котором мы гарантированно будем знать, что в соответствии
со своими накопленными баллами покупатель получит верную скидку.
Результат: Выложить отдельным файлом с названием TaskTestData.md


| Класс |  Значения  |Тестовые значения|Ожидаемая скидка|
|-------|:----------:|:---------------:|----------------|
|       |            |       0         |                |
|Класс 1|    0-99    |       50        |        1       |
|       |            |       99        |                |
|       |            |                 |                |
|       |            |       100       |                |
|Класс 2|   100-199  |       150       |        3       |
|       |            |       199       |                |
|       |            |                 |                |
|       |            |       200       |                |
|Класс 3|   200-499  |       300       |        5       |
|       |            |       499       |                |
|       |            |                 |                |
|       |            |       500       |                |
|Класс 4| 500 и более|       1731      |        10      |


