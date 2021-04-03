class Zoo:
    __animals = 0
    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "birds":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name_zoo}: {', '.join(self.fish)}\n"
        elif species == "birds":
            result += f"Birds in {self.name_zoo}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name = input()
zoo = Zoo(zoo_name)

count = int(input())

for number in range(count):
    data = [x for x in input().split()]
    species = data[0]
    name_animal = data[1]

    zoo.add_animal(species, name_animal)

animal_kind = input()

print(zoo.get_info(animal_kind))


