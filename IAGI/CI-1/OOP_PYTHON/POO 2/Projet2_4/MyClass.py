from com.person import Person, Order

p1 = Person(1, "John", "New York")
p2 = Person(2, "Paul", "Paris")
o1 = Order(101, "2023-10-12", 200.5)
o2 = Order(102, "2023-10-13", 300.5)
p1.set_order(o1)
p1.set_order(o2)
p2.set_order(o1)


o1.set_person(p1)
o2.set_person(p1)

p1.set_order(o1)
p1.set_order(o2)

p1.display_order()
print(p1.toString())

o1.display_person()
o2.display_person()


