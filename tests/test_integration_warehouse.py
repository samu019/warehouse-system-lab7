"""
Интеграционные тесты - Integration Tests
Приложение для обслуживания склада
"""
import pytest
import sys
sys.path.insert(0, '../src')
from src.warehouse import Warehouse

class TestWarehouseIntegration:
    def setup_method(self):
        self.wh = Warehouse()
    
    def test_complete_workflow(self):
        """Тест: Полный рабочий процесс склада"""
        # Добавляем товары
        self.wh.add_item(1, "Сервер", 2, 150000)
        self.wh.add_item(2, "Маршрутизатор", 5, 30000)
        
        # Создаем заказ
        order_id = self.wh.create_order([(1, 1), (2, 2)])
        assert order_id == 1
        
        # Проверяем статистику
        stats = self.wh.get_statistics()
        assert stats['total_items'] == 2
        assert stats['total_orders'] == 1
        assert stats['total_value'] == (2*150000) + (5*30000)
    
    def test_order_error_handling(self):
        """Тест: Обработка ошибок при заказах"""
        self.wh.add_item(1, "Монитор", 3, 20000)
        
        with pytest.raises(ValueError):
            self.wh.create_order([(1, 5)])
        
        with pytest.raises(ValueError):
            self.wh.create_order([(999, 1)])
