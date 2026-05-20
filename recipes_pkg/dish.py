from abc import ABC, abstractmethod
from recipes_pkg.ingredients import get_ingredient_info


class Dish(ABC):
    def __init__(self, name):
        self._name = name
        self._ingredients = {}
    
    @property
    def name(self):
        return self._name
    
    def add_ingredient(self, name, weight):
        if weight <= 0:
            raise ValueError("Вес должен быть больше 0")
        get_ingredient_info(name)
        self._ingredients[name] = weight
    
    def remove_ingredient(self, name):
        if name in self._ingredients:
            del self._ingredients[name]
    
    def clear(self):
        self._ingredients.clear()
    
    def _calculate_nutrition(self):
        total_cal = total_prot = total_fat = total_carb = total_cost = 0.0
        for name, weight in self._ingredients.items():
            cal, prot, fat, carb, price = get_ingredient_info(name)
            factor = weight / 100
            total_cal += cal * factor
            total_prot += prot * factor
            total_fat += fat * factor
            total_carb += carb * factor
            total_cost += price * factor
        return {
            'calories': round(total_cal, 2),
            'protein': round(total_prot, 2),
            'fat': round(total_fat, 2),
            'carbs': round(total_carb, 2),
            'cost': round(total_cost, 2)
        }
    
    @abstractmethod
    def get_recipe_description(self):
        pass
    
    @abstractmethod
    def get_cooking_time(self):
        pass
    
    def get_full_info(self):
        nutrition = self._calculate_nutrition()
        return {
            'name': self._name,
            'ingredients': self._ingredients.copy(),
            'nutrition': {
                'calories': nutrition['calories'],
                'protein': nutrition['protein'],
                'fat': nutrition['fat'],
                'carbs': nutrition['carbs']
            },
            'cost': nutrition['cost']
        }
    
    def __len__(self):
        return len(self._ingredients)


class Wok(Dish):
    def get_recipe_description(self):
        return "Азиатское блюдо из лапши, мяса и овощей"
    def get_cooking_time(self):
        return 15


class Burger(Dish):
    def get_recipe_description(self):
        return "Сэндвич с котлетой, сыром, овощами"
    def get_cooking_time(self):
        return 10


class Pizza(Dish):
    def get_recipe_description(self):
        return "Итальянское блюдо из тонкого теста с начинкой"
    def get_cooking_time(self):
        return 20


class DishFactory:
    @staticmethod
    def create_dish(dish_type):
        if dish_type == "Вок":
            return Wok("Вок")
        elif dish_type == "Бургер":
            return Burger("Бургер")
        elif dish_type == "Пицца":
            return Pizza("Пицца")
        else:
            raise ValueError(f"Неизвестный тип блюда: {dish_type}")