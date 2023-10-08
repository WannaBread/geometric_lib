# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Документация для модулей circle.py, triangle.py и rectangle.py

## circle.py

### Модуль для работы с кругами

```python
import math

def area(r):
    '''Вычисляет площадь круга.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Площадь круга.
    '''
    return math.pi * r * r

def perimeter(r):
    '''Вычисляет длину окружности.

    Args:
        r (float): Радиус окружности.

    Returns:
        float: Длина окружности.
    '''
    return 2 * math.pi * r
```

## triangle.py

### Модуль для работы с треугольниками

```python
def area(a, h):
    '''Вычисляет площадь треугольника.

    Args:
        a (float): Длина основания треугольника.
        h (float): Длина высоты, опущенной к основанию.

    Returns:
        float: Площадь треугольника.
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''Вычисляет периметр треугольника.

    Args:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Returns:
        float: Периметр треугольника.
    '''
    return a + b + c
```
## rectangle.py

### Модуль для работы с прямоугольниками

```python
def area(a, b):
    '''Вычисляет площадь прямоугольника.

    Args:
        a (float): Длина первой стороны прямоугольника.
        b (float): Длина второй стороны прямоугольника.

    Returns:
        float: Площадь прямоугольника.
    '''
    return a * b

def perimeter(a, b):
    '''Вычисляет периметр прямоугольника.

    Args:
        a (float): Длина первой стороны прямоугольника.
        b (float): Длина второй стороны прямоугольника.

    Returns:
        float: Периметр прямоугольника.
    '''
    return (a + b) * 2
```
## История изменений

- `598d38e`: Изменен `rectangle.py` и добавлен `triangle.py`.
- `15ce109`: Добавлен `rectangle.py`.
- `d078c8d`: Добавлена документация.
- `8ba9aeb`: Добавлены модули `circle.py` и `square.py`.