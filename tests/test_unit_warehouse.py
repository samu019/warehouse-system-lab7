"""
Тесты модулей - Unit Tests
Приложение для обслуживания склада
"""
import pytest
import sys
sys.path.insert(0, '../src')
from src.warehouse import Warehouse

class TestWarehouseUnit:
    def setup_method(self):
        self.wh = Warehouse()
    
    def test_add_item_valid(self):
        """Тест: Добавление валидного товара"""
        result = self.wh.add_item(1, "Ноутбук", 10, 50000)
        assert result == True
        assert len(self.wh.inventory) == 1
        assert self.wh.total_value == 500000
    
    def test_add_item_negative_quantity(self):
        """Тест: Добавление с отрицательным количеством (должно падать)"""
        with pytest.raises(ValueError):
            self.wh.add_item(1, "Мышь", -5, 1000)
    
    def test_add_item_zero_price(self):
        """Тест: Добавление с нулевой ценой (должно падать)"""
        with pytest.raises(ValueError):
            self.wh.add_item(1, "Клавиатура", 10, 0)
    
    def test_remove_existing_item(self):
        """Тест: Удаление существующего товара"""
        self.wh.add_item(1, "Монитор", 5, 15000)
        result = self.wh.remove_item(1)
        assert result == True
        assert len(self.wh.inventory) == 0
    
    def test_update_quantity_valid(self):
        """Тест: Обновление количества"""
        self.wh.add_item(1, "Принтер", 3, 20000)
        result = self.wh.update_quantity(1, 5)
        assert result == True
        assert self.wh.inventory[1]['quantity'] == 5
        assert self.wh.inventory[1]['total'] == 100000
