class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pet = None

    def adopt_pet(self, pet):
        self.pet = pet
        print(f"{self.name} приютил к себе {pet.name}.")

    def take_pet_for_walk(self):
        if self.pet:
            print(f"{self.name} Гуляет с {self.pet.name}.")
            self.pet.happiness += 10
        else:
            print(f"{self.name} Нескем погулять")

class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.happiness = 50

    def __str__(self):
        return f"{self.name} {self.animal_type} Счастье: {self.happiness}"

human = Human("Александр99", 30)
pet = Pet("кот", "собак")

human.adopt_pet(pet)
human.take_pet_for_walk()
print(pet)
