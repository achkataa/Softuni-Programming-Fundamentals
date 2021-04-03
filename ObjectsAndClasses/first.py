class Person:
    def __init__(self, hair_color, weight, height):
        self.hair_color = hair_color
        self.weight = weight
        self.height = height
    def eat(self, name):
        self.name = name
        self.height += 1
        return f"{name} is eating right now"

person = Person("black", 60, 160)
person_2 = Person("brown", 70, 180)
person_3 = Person("blond", 80, 200)

print(person.eat("Gohso"))



