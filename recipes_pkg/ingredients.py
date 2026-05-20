"""Модуль с базой данных ингредиентов"""

from abc import ABC, abstractmethod


class Ingredient(ABC):
    """Абстрактный класс для ингредиента"""
    
    def __init__(self, name, calories, protein, fat, carbs, price):
        self._name = name
        self._calories = calories
        self._protein = protein
        self._fat = fat
        self._carbs = carbs
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def calories(self):
        return self._calories
    
    @property
    def protein(self):
        return self._protein
    
    @property
    def fat(self):
        return self._fat
    
    @property
    def carbs(self):
        return self._carbs
    
    @property
    def price(self):
        return self._price
    
    def __str__(self):
        return f"{self._name}: {self._calories} ккал, {self._price} руб/100г"
    
    def __repr__(self):
        return f"Ingredient('{self._name}', {self._calories}, {self._protein}, {self._fat}, {self._carbs}, {self._price})"
    
    @abstractmethod
    def get_info(self):
        pass


class SimpleIngredient(Ingredient):
    """Конкретная реализация ингредиента"""
    
    def get_info(self):
        return {
            'name': self._name,
            'calories': self._calories,
            'protein': self._protein,
            'fat': self._fat,
            'carbs': self._carbs,
            'price': self._price
        }


class IngredientsDB:
    """Класс для управления базой ингредиентов"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_db()
        return cls._instance
    
    def _init_db(self):
        self._data = {}
        self._load_default_ingredients()
    
    def _load_default_ingredients(self):
        defaults = [
            ('курица', 165, 31, 3.6, 0, 120),
            ('говядина', 250, 26, 17, 0, 350),
            ('лапша удон', 138, 5, 1, 28, 100),
            ('перец болгарский', 31, 1.3, 0.3, 6, 80),
            ('булка', 270, 9, 4, 48, 40),
            ('котлета', 250, 22, 18, 0, 120),
            ('сыр', 350, 25, 28, 0, 200),
            ('салат', 15, 1.4, 0.2, 2.9, 60),
            ('помидор', 18, 0.9, 0.2, 3.9, 80),
            ('тесто пиццы', 290, 8, 7, 48, 50),
            ('соус томатный', 42, 1.5, 0.5, 9, 100),
            ('колбаса', 350, 14, 32, 0, 180),
        ]
        for item in defaults:
            ing = SimpleIngredient(*item)
            self._data[ing.name] = ing
    
    def get_ingredient(self, name):
        if name not in self._data:
            raise ValueError(f"Ингредиент '{name}' не найден")
        return self._data[name]
    
    def get_all_names(self):
        return list(self._data.keys())
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, name):
        return name in self._data


# ========== ГЛАВНЫЕ ФУНКЦИИ ДЛЯ ИСПОЛЬЗОВАНИЯ ==========

_db = IngredientsDB()


def get_ingredient_info(name):
    """Возвращает кортеж с данными ингредиента"""
    ing = _db.get_ingredient(name)
    return (ing.calories, ing.protein, ing.fat, ing.carbs, ing.price)


def get_available_ingredients():
    """Возвращает список всех доступных ингредиентов"""
    return _db.get_all_names()