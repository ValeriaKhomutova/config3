# Конфигурационное управление дз №3
## Общее описание
азработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.
Входной текст на языке json принимается из стандартного ввода. Выходной
текст на учебном конфигурационном языке попадает в стандартный вывод
##  Описание всех функций и настроек
Однострочные комментарии:
" Это однострочный комментарий
Многострочные комментарии:
%{
Это многострочный
комментарий
%}
Массивы:
<< значение, значение, значение, ... >>
Словари:
dict(
имя = значение,
имя = значение,
имя = значение,
...
)
Имена:
[_A-Z][_a-zA-Z0-9]*
Значения:
• Числа.
• Строки.
• Массивы.
• Словари.
Строки:
'Это строка'
Объявление константы на этапе трансляции:
let имя = значение;
Вычисление константы на этапе трансляции:
?{имя}
Результатом вычисления константного выражения является значение.
Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 2
примера описания конфигураций из разных предметных областей
##  Описание команд для сборки проекта.
1. Клонирование репозитория 

```https://github.com/ValeriaKhomutova/config3```

2. Переход в директорию Homework_config

```cd config_dz3```

3. Запуск скрипта для демонстрации возможностей Cli

```python3 homework3.py config.txt output.json```
## Примеры использования
![Screen]()
<!--описание коммитов-->
## Описание коммитов
| Название | Описание                                                                             |
|------------------|----------------------------------------------------------------------------- |
| first_commit    | Готовый проект                                                               |