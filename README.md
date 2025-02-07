# Lab-4

## Лабораторная работа №4

**Задание**

Используя ```tkinter```, реализовать программу, генерирующую ключ для некоего программного обеспечения (мы осуждаем пиратство) с соответствующим оформлением пользовательского интерфейса.

* Выберите любимую игру, найдите по ней арт или связанную картинку в поисковике.
* Реализуйте форму генератора ключа, которая должна включать в себя как минимум поле для ввода данных, поле для генерируемого ключа, кнопку запуска и найденную картинку на фоне.
* Реализуйте генератор ключа. Ключ состоит из набора символов, состоящих из латинских букв **A-Z** и цифр **0-9**. В зависимости от варианта может потребоваться ввод первой части ключа (указан в варианте). Ключ генерируется по некоторым правилам. В заданиях со сдвигом считать, что буквы и цифры последовательно как бы нанесены на бесконечную ленту, которую можно двигать влево и вправо.

**Варианты**

| Вариант | Вводная часть | Формат ключа | Правило генерации |
| ------- | ------------- | ------------ | ----------------- |
| 1 | нет | XXXXX-XXXXX-XXXXX |	Каждый блок имеет две цифры и три буквы в случайном порядке |
| 2 | нет | XXXX-XXXX-XXXX-XXXX |	Каждый блок имеет одну цифру и три буквы в случайном порядке |
| 3 | HEX-число 5 знаков |	XXXXX-XXXXX-XXXXX XX |	Вводная часть ключа - число в HEX, которое необходимо перевести в DEC. Первые три цифры числа в DEC должны быть по одному в каждом блоке, последние две цифры - в конце ключа |
| 4 | нет | XXXX-XXXX-XXXX | Назначить весовые коэффициенты символам, генерировать с учётом, чтобы сумма весовых коэффициентов одного блока попала в интервал |
| 5 | 1 блок ключа | XXXXX-XXXXX-XXXXX | Опираясь на введённый фрагмент ключа, сгенерировать остаток ключа так: 2 блок - сдвиг на 3 символа вправо, 3 блок - сдвиг на 5 символов влево |
| 6 | нет | XXXXX-XXXX-XXXX	| Назначить весовые коэффициенты символам, генерировать с учётом, чтобы среднее значение суммы из одного блока попало в интервал |
| 7 | слово 6 букв | XXX-XXXXXX-XXX | 1 и 3 блок - только буквы, взятые из введённого слова, 2 блок - только цифры, соответвующие порядковым номерам букв в алфавите (десятки отбросить) |
| 8 | DEC-число 3 знака | XXXXX-XXXX-XXX-XX | 1 блок - случайная комбинация букв и цифр, каждый последующий блок убирает 1 символ и выполняет сдвиг на последующую цифру из введённого числа. Направление сдвига чередуется. |	
| 9	| нет | XX XXXXXXX XX | 1 и 3 блок - порядковые числа букв в алфавите (не больше 26) - обозначение границ интервала, 2 блок заполняется буквами из этого интервала в случайном порядке |
| 10 | DEC-число 6 знаков |	XXXXX-XXXXX XXXX | 1 и 2 блок должны содержать 4,5,6 и 1,2,3 цифры введенного числа соответственно, остальное - случайные буквы, 3 блок - результат сложения чисел, получившихся в 1 и 2 блоках |

**Допзадание**

Добавить музыку (8-bit желательно) на фоне и анимацию.

**Дополнительно**

DEC-число - число в десятичном формате  
HEX-число - число в шестнадцатеричном формате  
Для перевода HEX в DEC можно воспользоваться конструкцией ```dec = int(hex, 16)```
