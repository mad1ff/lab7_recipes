#!/usr/bin/env python3
"""Основная программа для ЛР7. ООП. Классы и объекты."""

import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from recipes_pkg.gui import run_gui

if __name__ == "__main__":
    run_gui()