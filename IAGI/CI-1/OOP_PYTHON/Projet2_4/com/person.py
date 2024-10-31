class Person:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city
        self.order = []

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

    def set_order(self, order):
        self.order.append(order)

    def toString(self):
        return f"Person Details:\n- ID: {self.id}\n- Name: {self.name}\n- City: {self.city}\n"

    def display_order(self):
        if self.order:
            print(f"Orders for {self.name} (ID: {self.id}):")
            for index, order in enumerate(self.order, start=1):
                print(f"  Order {index}: {order.toString()}")
        else:
            print(f"{self.name} has no orders.\n")


class Order:
    def __init__(self, code, datecmd, total, person=None):
        self.code = code
        self.datecmd = datecmd
        self.total = total
        self.person = person

    def get_code(self):
        return self.code

    def get_datecmd(self):
        return self.datecmd

    def get_total(self):
        return self.total

    def set_code(self, code):
        self.code = code

    def set_datecmd(self, datecmd):
        self.datecmd = datecmd

    def set_total(self, total):
        self.total = total

    def set_person(self, person):
        self.person = person

    def toString(self):
        return f"Code: {self.code}, Date: {self.datecmd}, Total: {self.total} USD"

    def display_person(self):
        if self.person is not None:
            print(f"Order is linked to Person ID: {self.person.get_id()}")
        else:
            print("This order is not linked to any person.")
