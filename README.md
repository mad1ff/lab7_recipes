# Лабораторная работа №7: ООП. Классы и объекты

## Вариант 8 (Рецепты: Вок, Бургер, Пицца)
## GUI фреймворк: guizero (вариант 9)

---

## Задача

Переписать лабораторную работу №6 с использованием классов и объектов.

В коде должны присутствовать:
- абстрактный базовый класс и соответствующие декораторы для методов
- иерархия наследования
- managed-атрибуты (property, setter, getter)
- минимум 2 dunder-метода у каждого класса

---

## Решение

### Структура проекта
lab7_recipes/
├── main.py
├── requirements.txt
├── README.md
└── recipes_pkg/
├── init.py
├── ingredients.py
├── dish.py
├── report.py
└── gui.py

### Описание модулей

| Модуль | Назначение |
|--------|------------|
| `ingredients.py` | Абстрактный класс `Ingredient`, класс `IngredientsDB` (Singleton), функции для работы с БД |
| `dish.py` | Абстрактный класс `Dish`, классы блюд `Wok`, `Burger`, `Pizza`, фабрика `DishFactory` |
| `report.py` | Функции сохранения отчётов в `.docx` и `.xlsx` |
| `gui.py` | GUI на guizero, класс `RecipeApp` |
| `main.py` | Точка входа в программу |

### Реализованные требования

| Требование | Где реализовано |
|------------|-----------------|
| Абстрактный базовый класс | `Ingredient(ABC)`, `Dish(ABC)` |
| Декораторы `@abstractmethod` | `get_info()`, `get_recipe_description()`, `get_cooking_time()` |
| Иерархия наследования | `Ingredient` → `SimpleIngredient`, `Dish` → `Wok`/`Burger`/`Pizza` |
| Managed-атрибуты (`@property`) | `name`, `calories`, `protein`, `fat`, `carbs`, `price` в `Ingredient`; `name`, `ingredients` в `Dish` |
| Dunder-методы | `__str__`, `__repr__`, `__len__`, `__contains__` |
| Паттерн Singleton | `IngredientsDB` |
| Паттерн Factory | `DishFactory` |

### Формулы расчёта

- **Калории** = Σ (калорийность_ингредиента × вес_ингредиента / 100)
- **Белки** = Σ (белки_ингредиента × вес_ингредиента / 100)
- **Жиры** = Σ (жиры_ингредиента × вес_ингредиента / 100)
- **Углеводы** = Σ (углеводы_ингредиента × вес_ингредиента / 100)
- **Стоимость** = Σ (цена_ингредиента × вес_ингредиента / 100)

---

## Скриншоты

### Главное окно программы

<img width="1075" height="810" alt="Снимок экрана 2026-05-21 032404" src="https://github.com/user-attachments/assets/73a61645-9c0a-4aff-a805-7996b5315178" />


### Сохранение отчёта в Excel

<img width="372" height="416" alt="Снимок экрана 2026-05-21 032551" src="https://github.com/user-attachments/assets/6da48f61-f2fd-426f-90f7-922652caa3da" />


*Рисунок 3 — Отчёт в формате Excel*

### Сохранение отчёта в Word

<img width="1015" height="621" alt="Снимок экрана 2026-05-21 032439" src="https://github.com/user-attachments/assets/d143fcaa-4d45-4c8a-8932-e72878c94088" />


---

## Пример работы

**Входные данные (Бургер):**
- булка — 67 г
- курица — 52 г
- сыр — 42 г
- салат — 1486 г 


**Результаты расчёта:**

| Показатель | Значение |
|------------|----------|
| Калории | 636 ккал |
| Белки | 53 г |
| Жиры | 19 г |
| Углеводы | 75 г |
| Стоимость | 1065 руб. |

**Описание блюда:** Сэндвич с котлетой, сыром, овощами

**Время приготовления:** 10 минут

---

## Используемые материалы

1. [guizero документация](https://guizero.readthedocs.io/)
2. [python-docx](https://python-docx.readthedocs.io/)
3. [openpyxl](https://openpyxl.readthedocs.io/)
4. [ABC — абстрактные базовые классы](https://docs.python.org/3/library/abc.html)

---

## Запуск программы

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск
python main.py
