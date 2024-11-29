class FirstClass:               # определить объект класса

    def setdata(self, value):   # определить методы класса
        self.data = value       # self - экземпляр
    def display(self):
        print(self.data)        # self.data: для каждого экземпляра
x = FirstClass()  # создать два экземпляра
y = FirstClass()  # каждый представляет собой новое пространство имен
x.setdata('Ivan Ivanov')  # вызвать методы: self - это x
y.setdata(3.14159)
x.display() # self.data отличается в каждом экземпляре
y.display() # выполняется FirstClass.display
x.data = 'New value' # можно получить/установить атрибуты
x.display()
x.anothername = 'spam'

class SecondClass(FirstClass): # Наследует setdata
# наследуем все свойства и методы из FirstClass
    def display(self):  # Наследует setdata
        print(f'Текущие значение = {self.data}')


z = SecondClass()
z.setdata(42)  # находит setdata в FirstClass
z.display()  # находит переопределенный метод в SecondClass



