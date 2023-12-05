# Описание
В данном репозитори вы найдете набор математических формул, предназначенных для вычисления площади и периметра различных геометрических фигур.
## Круг

$$ S = πr² $$
```python
def area(r):
    """ Возвращает площадь круга, радиуса r """ 
    return math.pi * r * r
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import circle; print(circle.area(2))'
12.566370614359172
```
$$ P = 2πr $$
```python
def perimeter(r):
    """ Возвращает периметр круга, радиуса r """ 
    return 2 * math.pi * r
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import circle; print(circle.perimeter(2))'
12.566370614359172
```
## Прямоугольник
$$ S = ab $$
```python
def area(a, b): 
    """ Возвращает площадь прямоугольника, со сторонами a,b """
    return a * b 
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import rectangle; print(rectangle.area(2,3)'     
6
```
$$ P = 2(a + b) $$
```python
def perimeter(a, b): 
    """ Возвращает периметр прямоугольника, со сторонами a,b """
    return 2*(a + b)    
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import rectangle; print(rectangle.perimeter(2,3)'
10
```
## Квадрат
$$ S = a² $$
```python
def area(a):
    """ Возвращает площадь квадрата, со стороной a """
    return a * a
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import square; print(square.area(2))'        
4
```
$$ P = 4a $$
```python
def perimeter(a):
    """ Возвращает периметр квадрата, со стороной a """
    return 4 * a
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import square; print(square.perimeter(2))'
8
```
## Треугольник
$$ S = ah/2 $$
```python
def area(a, h):
    """ 
    Возвращает площадь треугольника.
        
        Параметры:
            a - основание треугольника
            h - высота треугольника
    """ 
    return a * h / 2 
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import triangle; print(triangle.area(2,3))'   
3.0
```
$$ P = 4a $$
```python
def perimeter(a, b, c):
    """ Возврашает периметр треугольника, со сторонами a, b, c """
    return a + b + c 
```
Пример:
```powershell
PS C:\geometric_lib python -c 'import triangle; print(triangle.perimeter(2,3,4)'
9
```

## Unit - тестирование

### Отчёт о дефектах:
|        Модуль         | Пройдено | Провалено |                                        Дефекты                                        |
|:---------------------:|:--------:|:---------:|:-------------------------------------------------------------------------------------:|
|    Circle  (Area)     |    4     |     3     |             Неправильная работа программы при неккоректных входных данных             |
|  Circle (Perimeter)   |    4     |     3     |             Неправильная работа программы при неккоректных входных данных             |
|   Rectangle (Area)    |    4     |     3     |             Неправильная работа программы при неккоректных входных данных             |
| Rectangle (Perimeter) |    4     |     3     | Неправильная работа программы при неккоректных входных данных 
|     Square (Area)     |    4     |     3     |             Неправильная работа программы при неккоректных входных          |
|  Square (Perimeter)   |    4     |     3     |             Неправильная работа программы при неккоректных входных данных             |
|    Triangle (Area)    |    4     |     3     |             Неправильная работа программы при неккоректных входных данных             |
| Triangle (Perimeter)  |    4     |     3     |             Неправильная работа программы при неккоректных входных данных             |

#### Кол-во тестов всего: 32
#### Кол-во успешных тестов: 8
#### Кол-во ошибочных тестов: 24
## История изменений:

- e357392d455aeeaa4c30e0ac8a06fcec7c0d4e6c; new file: triangle.py; modified: rectangle.py; Autor: Ivan
- d540ac2cc0cfa32f885544afd3fc70d8e4f953b0;  new file: rectangle.py; Autor: Ivan
- d078c8d9ee6155f3cb0e577d28d337b791de28e2; L-03: Docs added; Autor: smartiqa
- 8ba9aeb3cea847b63a91ac378a2a6db758682460; L-03: Circle and square added; Autor: smartiqa
