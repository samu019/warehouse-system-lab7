"""
Приложение для обслуживания склада
Warehouse Management System - Laboratorio 7
"""
class Warehouse:
    def __init__(self):
        self.inventory = {}
        self.orders = []
        self.total_value = 0
    
    def add_item(self, item_id, name, quantity, price):
        """Añadir producto al almacén"""
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        if price < 0:
            raise ValueError("Цена должна быть положительной")
        
        self.inventory[item_id] = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'total': quantity * price
        }
        self.total_value += quantity * price
        return True
    
    def remove_item(self, item_id):
        """Eliminar producto del almacén"""
        if item_id in self.inventory:
            self.total_value -= self.inventory[item_id]['total']
            del self.inventory[item_id]
            return True
        return False
    
    def update_quantity(self, item_id, new_quantity):
        """Actualizar cantidad de producto"""
        if item_id not in self.inventory:
            return False
        if new_quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        
        old_total = self.inventory[item_id]['total']
        self.inventory[item_id]['quantity'] = new_quantity
        self.inventory[item_id]['total'] = new_quantity * self.inventory[item_id]['price']
        self.total_value += self.inventory[item_id]['total'] - old_total
        return True
    
    def get_low_stock(self, threshold=10):
        """Productos con stock bajo"""
        return {k: v for k, v in self.inventory.items() if v['quantity'] < threshold}
    
    def create_order(self, items):
        """Crear pedido de productos"""
        order_id = len(self.orders) + 1
        total = 0
        for item_id, quantity in items:
            if item_id in self.inventory:
                if self.inventory[item_id]['quantity'] >= quantity:
                    total += self.inventory[item_id]['price'] * quantity
                else:
                    raise ValueError(f"Недостаточно товара {item_id}")
            else:
                raise ValueError(f"Товар {item_id} не найден")
        
        self.orders.append({
            'id': order_id,
            'items': items,
            'total': total,
            'status': 'pending'
        })
        return order_id
    
    def get_statistics(self):
        """Estadísticas del almacén"""
        return {
            'total_items': len(self.inventory),
            'total_value': self.total_value,
            'total_orders': len(self.orders),
            'low_stock': len(self.get_low_stock())
        }
