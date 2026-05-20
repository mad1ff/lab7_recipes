"""Модуль с GUI на guizero"""

from guizero import App, Text, Combo, PushButton, TextBox, ListBox, info, error

# Прямые импорты (без recipes_pkg.)
from recipes_pkg.ingredients import get_available_ingredients
from recipes_pkg.dish import DishFactory
from recipes_pkg.report import save_to_docx, save_to_xlsx


class RecipeApp:
    def __init__(self):
        self.app = App(title="Калькулятор рецептов - ЛР7", width=750, height=650, layout="grid")
        
        self.get_available_ingredients = get_available_ingredients
        self.DishFactory = DishFactory
        self.save_to_docx = save_to_docx
        self.save_to_xlsx = save_to_xlsx
        
        self.current_dish = None
        
        self._setup_ui()
        self.change_dish()
    
    def _setup_ui(self):
        # Заголовок
        Text(self.app, text="🥗 Калькулятор рецептов 🍕", size=16, font="Arial", grid=[0, 0, 2, 1])
        
        # Выбор блюда
        Text(self.app, text="Выберите блюдо:", grid=[0, 1], align="left")
        self.dish_combo = Combo(self.app, options=["Вок", "Бургер", "Пицца"], 
                                 command=self.change_dish, grid=[1, 1], align="left")
        self.dish_combo.value = "Вок"
        
        # Добавление ингредиента
        Text(self.app, text="Ингредиент:", grid=[0, 2], align="left")
        all_ingredients = self.get_available_ingredients()
        self.ing_combo = Combo(self.app, options=all_ingredients, grid=[1, 2], align="left")
        if all_ingredients:
            self.ing_combo.value = all_ingredients[0]
        
        Text(self.app, text="Вес (г):", grid=[0, 3], align="left")
        self.weight_input = TextBox(self.app, grid=[1, 3], width=10, align="left")
        
        self.add_btn = PushButton(self.app, text="➕ Добавить", command=self.add_ingredient,
                                   grid=[2, 3], align="left")
        
        # Список ингредиентов
        Text(self.app, text="Ингредиенты:", grid=[0, 4], align="left")
        self.listbox = ListBox(self.app, items=[], grid=[0, 5, 2, 1], width=60, height=8)
        
        self.remove_btn = PushButton(self.app, text="❌ Удалить выбранный", command=self.remove_ingredient,
                                      grid=[2, 5], align="left")
        
        # Результаты
        Text(self.app, text="Результаты:", grid=[0, 6], align="left")
        self.result_text = TextBox(self.app, text="", grid=[0, 7, 2, 1], width=80, height=8, multiline=True)
        
        # Кнопки
        self.docx_btn = PushButton(self.app, text="📄 Сохранить в DOCX", command=self.save_docx,
                                    grid=[0, 8], align="left")
        self.xlsx_btn = PushButton(self.app, text="📊 Сохранить в XLSX", command=self.save_xlsx,
                                    grid=[1, 8], align="left")
        self.clear_btn = PushButton(self.app, text="🗑 Очистить всё", command=self.clear_all,
                                     grid=[2, 8], align="left")
    
    def change_dish(self):
        dish_name = self.dish_combo.value
        self.current_dish = self.DishFactory.create_dish(dish_name)
        self.clear_all()
    
    def add_ingredient(self):
        ing = self.ing_combo.value
        if not ing:
            error("Ошибка", "Выберите ингредиент")
            return
        try:
            weight = float(self.weight_input.value)
            if weight <= 0:
                raise ValueError
            self.current_dish.add_ingredient(ing, weight)
            self.listbox.append(f"{ing} - {weight} г")
            self.weight_input.value = ""
            self.update_result()
        except ValueError:
            error("Ошибка", "Введите вес > 0")
    
    def remove_ingredient(self):
        selected = self.listbox.value
        if selected:
            ing_name = selected.split(" - ")[0]
            self.current_dish.remove_ingredient(ing_name)
            self.listbox.remove(selected)
            self.update_result()
    
    def clear_all(self):
        if self.current_dish:
            self.current_dish.clear()
        self.listbox.clear()
        self.update_result()
    
    def update_result(self):
        if not self.current_dish:
            return
        info_data = self.current_dish.get_full_info()
        n = info_data['nutrition']
        text = f"Блюдо: {info_data['name']}\n\n"
        text += f"Калории: {n['calories']} ккал\n"
        text += f"Белки: {n['protein']} г\n"
        text += f"Жиры: {n['fat']} г\n"
        text += f"Углеводы: {n['carbs']} г\n\n"
        text += f"Стоимость: {info_data['cost']} руб.\n\n"
        text += f"Описание: {self.current_dish.get_recipe_description()}\n"
        text += f"Время приготовления: {self.current_dish.get_cooking_time()} мин"
        self.result_text.value = text
    
    def save_docx(self):
        if len(self.current_dish) == 0:
            error("Ошибка", "Нет ингредиентов для сохранения")
            return
        from tkinter import filedialog
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.asksaveasfilename(defaultextension=".docx")
        root.destroy()
        if filename:
            self.save_to_docx(self.current_dish.get_full_info(), filename)
            info("Успех", f"Сохранено")
    
    def save_xlsx(self):
        if len(self.current_dish) == 0:
            error("Ошибка", "Нет ингредиентов для сохранения")
            return
        from tkinter import filedialog
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx")
        root.destroy()
        if filename:
            self.save_to_xlsx(self.current_dish.get_full_info(), filename)
            info("Успех", f"Сохранено")
    
    def display(self):
        self.app.display()


def run_gui():
    app = RecipeApp()
    app.display()


if __name__ == "__main__":
    run_gui()