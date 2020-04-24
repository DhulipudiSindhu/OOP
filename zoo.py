class Animal:
    sound = ""
    food_in_kg = 0
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if required_food_in_kgs <=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
  
    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs += self.food_in_kg

class land_animals:
    @classmethod
    def breathe(cls):
        print("Breathe in air")
        
class water_animals:
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
        
        
class Hunting:
    animal = ""
    def hunt(self, zoo):
        c = 0 
        for i in zoo.animal_list:
            if type(i).__name__ == self.animal[0]:
                zoo.animal_list.remove(i)
                c = 1
                break
            if c == 0:
                print(f'No {self.animal[1]} to hunt')
        
class Deer(Animal, land_animals):
    sound = "Buck Buck"
    food_in_kg = 2
    
class Lion(Animal, land_animals, Hunting):
    sound = "Roar Roar"
    food_in_kg = 4
    animal = ["Deer", "deers"]
    
class Shark(Animal, water_animals, Hunting):
    sound = "Shark Sound"
    food_in_kg = 8
    animal = ["GoldFish", "GoldFish"]

    
class GoldFish(Animal, water_animals):
    sound = "Hum Hum"
    food_in_kg = 0.2

class Snake(Animal, land_animals, Hunting):
    sound = "Hiss Hiss"
    food_in_kg = 0.5
    animal = ["Deer", "deers"]

class Zoo:
    
    total_animal = []
    
    def __init__(self, reserved_food_in_kgs = 0):
        self.animal_list = []
        self._reserved_food_in_kgs = reserved_food_in_kgs
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    
    def add_animal(self, obj = None):
        self.animal_list.append(obj)
        Zoo.total_animal.append(obj)
        
    def add_food_to_reserve(self, food):
        self._reserved_food_in_kgs += food
        
    def count_animals(self):
        return len(self.animal_list)
        
    def feed(self, obj_value):
        if self._reserved_food_in_kgs != 0:
            self._reserved_food_in_kgs -= obj_value.required_food_in_kgs
            obj_value.grow()
        
    @classmethod
    def count_animals_in_all_zoos(self):
        return len(self.total_animal)
    
    @staticmethod
    def count_animals_in_given_zoos(zoo_list):
        count = 0
        for obj in zoo_list:
            count += obj.count_animals()
        return count
        
