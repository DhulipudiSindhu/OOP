
Home
AssignmentID - OOP007
Zoo
Submission Guidelines
Deer
Lion
Shark
Gold Fish
Zoo
Snake
# Zoo

We are trying to simulate a Zoo with different types of animals in this assignment.

# Submission Guidelines
Create a folder /home/ec2-user/environment/oop/oop_submissions/oop_assignment_007. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/oop/oop_submissions/oop_asssignment_007/

Copy your code file to the submission folder. Once you are done with each part of the assignment. Make use of the below example command
$ cp zoo.py /home/ec2-user/environment/oop_submissions/oop_assignment_007
Coding Guidelines:

Write all your code in zoo.py file
All the class, attributes and methods should be same as given in the example
A zoo contains different types of animals which are mentioned below

# Deer
Write a Deer class to simulate the following:

Any new Deer object starts with age_in_months = 1
It can grow, when it grows its
age_in_months increases by 1
required_food_in_kgs increases by 2
It can make_sound
It can breathe
Incase of invalid data while creating a new object raise ValueError as mentioned below
hunt is detailed in Zoo description
Your code should behave as below

>>> from zoo import Deer
>>> deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
>>> deer.age_in_months
1
>>> deer.breed
"ELK"
>>> deer.required_food_in_kgs
10
>>> deer.grow()
>>> deer.required_food_in_kgs
12
>>> deer.age_in_months
2
>>> deer.make_sound() # Prints
"Buck Buck"
>>> deer.breathe() # Prints
"Breathe in air"
>>> deer = Deer(age_in_months=10, breed="ELK", required_food_in_kgs=10)
ValueError: Invalid value for field age_in_months: 10

# Lion
Write a Lion class to simulate the following:

Any new Lion object starts with age_in_months = 1
It can grow, when it grows its
age_in_months increases by 1
required_food_in_kgs increases by 4
It can make_sound
It can breathe
It can hunt . When it hunts
It kills a Deer in the Zoo which means there will be one less deer in the Zoo.
If there are no deers in the Zoo. It should print No deers to hunt
Incase of invalid data while creating a new object raise ValueError as mentioned in Deer class
hunt is detailed in Zoo description
Your code should behave as below.

>>> from zoo import Lion
>>> lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
>>> lion.age_in_months
1
>>> lion.breed
"African Lion"
>>> lion.required_food_in_kgs
15
>>> lion.grow()
>>> lion.required_food_in_kgs
19
>>> lion.age_in_months
2
>>> lion.make_sound() # Prints
"Roar Roar"
>>> lion.breathe() # Prints
"Breathe in air"

# Shark
Write a Shark class to simulate the following:

Any new Shark object starts with age_in_months = 1
It can grow, when it grows its
age_in_months increases by 1
required_food_in_kgs increases by 8
It can make_sound
It can breathe
It can hunt . When it hunts
It kills a GoldFish in the Zoo which means there will be one less goldfish in the Zoo.
If there are no deers in the Zoo. It should print No GoldFish to hunt
Incase of invalid data while creating a new object raise ValueError as mentioned in Deer class
hunt is detailed in Zoo description
Your code should behave as below.

>>> from zoo import Shark
>>> shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
>>> shark.age_in_months
1
>>> shark.breed
"Hunter Shark"
>>> shark.required_food_in_kgs
10
>>> shark.grow()
>>> shark.required_food_in_kgs
18
>>> shark.age_in_months
2
>>> shark.make_sound() # Prints
"Shark Sound"
>>> shark.breathe() # Prints
"Breathe oxygen from water"

# Gold Fish
Write a GoldFish class to simulate the following:

Any new GoldFish object starts with age_in_months = 1
It can grow, when it grows its
age_in_months increases by 1
required_food_in_kgs increases by 0.2
It can make_sound
It can breathe
Incase of invalid data while creating a new object raise ValueError as mentioned in Deer class
Your code should behave as below.

>>> from zoo import GoldFish
>>> gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
>>> gold_fish.age_in_months
1
>>> gold_fish.breed
"Nemo"
>>> gold_fish.required_food_in_kgs
0.5
>>> gold_fish.grow()
>>> gold_fish.required_food_in_kgs
0.7
>>> gold_fish.age_in_months
2
>>> gold_fish.make_sound() # Prints
"Hum Hum"
>>> gold_fish.breathe() # Prints
"Breathe oxygen from water"

Hint: You can remove the duplication of breathe by using inheritance appropirately.
# Zoo
A Zoo contains different types of animals which are mentioned above. Zoo has food reserve to feed animals.

Write a Zoo class to implement this need and has the following features.

add_food_to_reserve - Updates the amount of food in reserve
>>> from zoo import Zoo
>>> zoo = Zoo()
>>> zoo.reserved_food_in_kgs
0
>>> zoo.add_food_to_reserve(10000000)
>>> zoo.reserved_food_in_kgs
10000000

count_animals should return all the animals count in that zoo
>>> zoo.count_animals()
0

add_animal - should add a new animal to the zoo
>>> gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
>>> zoo.add_animal(gold_fish)
>>> zoo.count_animals()
1

feed : On feeding an animal it grows and the food in zoo reserve should be reduced by required_food_in_kgs of the animal.
>>> zoo.reserved_food_in_kgs
10000000
>>> zoo.feed(gold_fish)
>>> zoo.reserved_food_in_kgs
9999999.5
>>> gold_fish.age_in_months
2

count_animals_in_all_zoos should return the total of all the animals in all zoos (Hint: use whichever is appropriate among classmethod, staticmethod)

count_animals_in_given_zoos should take a list of Zoo objects and return the number of animals in the given list of zoos (Hint: use whichever is appropriate among classmethod, staticmethod)

>>> nehru_zoological_park = Zoo()
>>> zoo.add_food_to_reserve(10000000)
>>> lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
>>> nehru_zoological_park.add_animal(lion)
>>> nehru_zoological_park.count_animals()
1
>>> Zoo.count_animals_in_all_zoos()
2
>>> Zoo.count_animals_in_given_zoos([zoo])
1

>>> from zoo import Deer
>>> deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
>>> nehru_zoological_park.add_animal(deer)
>>> nehru_zoological_park.count_animals()
2
>>> lion.hunt(nehru_zoological_park)
>>> nehru_zoological_park.count_animals()
1
>>> lion.hunt(nehru_zoological_park) # Prints
No deers to hunt

Now lets add one more animal to the zoo.
Note: If you have applied all the OOP concepts correctly, you wouldn’t be needing any changes to the previous classes

# Snake
Write a Snake class to simulate the following:

Any new Snake object starts with age_in_months = 1
It can grow, when it grows its
age_in_months increases by 1
required_food_in_kgs increases by 0.5
It can make_sound
It can breathe
It can hunt . When it hunts
It kills a Deer in the Zoo which means there will be one less deer in the Zoo.
If there are no deers in the Zoo. It should print No deers to hunt
Incase of invalid data while creating a new object raise ValueError as mentioned in Deer class
hunt is detailed in Zoo description
Your code should behave as below.

>>> from zoo import Snake
>>> snake = Snake(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=5)
>>> snake.age_in_months
1
>>> snake.breed
"Indian Cobra"
>>> snake.required_food_in_kgs
5
>>> snake.grow()
>>> snake.required_food_in_kgs
5.5
>>> snake.age_in_months
2
>>> snake.make_sound() # Prints
"Hiss Hiss"
>>> snake.breathe() # Prints
"Breathe in air"









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
        
