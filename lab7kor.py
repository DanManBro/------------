class Singleton:
    # Приватная переменная класса для хранения единственного экземпляра
    _instance = None

    def __new__(cls, *args, **kwargs):
        
        if cls._instance is None:
            
            cls._instance = super().__new__(cls)
        
        return cls._instance

    def __init__(self, value=None):
        
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value


# --- Блок проверки (демонстрация работы) ---
if __name__ == "__main__":
    # 1. Создаем первый объект
    s1 = Singleton("Первый")
    print(f"s1 value: {s1.get_value()}")
    
    # 2. Пытаемся создать второй объект с другим значением
    s2 = Singleton("Второй")
    print(f"s2 value: {s2.get_value()}") 
    
    # 3. Проверяем, изменилось ли значение в s1
    print(f"s1 value после создания s2: {s1.get_value()}")

    # 4. Проверяем, ссылаются ли переменные на один и тот же объект
    print(f"s1 и s2 — это один и тот же объект? {s1 is s2}")
    print(f"ID s1: {id(s1)}")
    print(f"ID s2: {id(s2)}")