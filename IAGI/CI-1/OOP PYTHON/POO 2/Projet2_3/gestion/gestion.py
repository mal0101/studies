class Person:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_city(self):
        return self.city

    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_city(self, city):
        self.city = city
    
    def toString(self):
        print("ID: ", self.id)
        print("Name: ",self.name)
        print("City: ",self.city)
        
class Student(Person):
    def __init__(self, id, name, city, formation, level):
        super().__init__(id, name, city)
        self.formation = formation
        self.level = level
        
    def get_formation(self):
        print("Formation: ",self.formation)
    def get_level(self):
        print("Level: ",self.level)
    def set_formation(self, formation):
        self.formation = formation
    def set_level(self, level):
        self.level = level
    def toString(self):
        print("ID: ", self.id)
        print("Name: ",self.name)
        print("City: ",self.city)
        print("Formation: ",self.formation)
        print("Level: ",self.level)

class Employe(Person):
    def __init__(self, id, name, city, company, sal):
        super().__init__(id, name, city)
        self.company = company
        self.sal = sal
        
    def get_company(self):
        print("Company: ",self.company)
    def get_sal(self):
        print("Salary: ",self.sal)
        
    def set_company(self, company):
        self.company = company
    def set_sal(self, sal):
        self.sal = sal
    def toString(self):
        print("ID: ", self.id)
        print("Name: ",self.name)
        print("City: ",self.city)
        print("Company: ",self.company)
        print("Salary: ",self.sal)
