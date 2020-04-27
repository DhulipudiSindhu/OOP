iBHubs

Home
AssignmentID - OOP009
Pokemon
Submission Guidelines
Task1
Pokemon
Pikachu
Squirtle
Pidgey
Swanna
Zapdos
Task2
Island
Task3
Trainer
Task4
Task5
Task6
Task7
Task8
Task9
# Pokemon

You might have played or at least heard about the famous Pokemon game. It's based on the popular Pokemon series.

In this assignment, lets try to simulate some pokemon and some trainers to "catch 'em all".

# Submission Guidelines
Exam Duration - 5 hr 30 mins
Create a folder /home/ec2-user/environment/oop/oop_submissions/oop_assignment_009. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/oop/oop_submissions/oop_assignment_009/
To submit your assignment execute the below code snippet in the assignment folder i.e /home/ec2-user/environment/oop/oop_submissions/oop_assignment_009
cloud9$ ./submit_assignment
On submission you will get results.txt in your assignment folder. results.txt gives you the test case results.
Coding Guidelines:

Write all your code in pokemon.py file
All the class, attributes and methods should be same as given in the example
# Task1
# Pokemon
A pokemon is described by it's name and level.

name is any non-empty string &
level is a positive integer
These two details should be mentioned while creating any pokemon. In case of invalid inputs, raise ValueError as mentioned below:

if name is empty - raise ValueError with "name cannot be empty" as error message
if level <=0 - raise ValueError with "level should be > 0" as error message
In this assignment, you have to simulate the following pokemon.

# Pikachu
Pikachu is an electric pokemon. Behavior of Pikachu is mentioned below.

It can make its unique sound (mentioned below)
It can run
It can attack - Magnitude of the attack depends on the level of pikachu. It is 10 times the level of the attacking pikachu. (10 x level)
>>> my_pikachu = Pikachu(name="Ryan", level=1)
>>> my_pikachu.name
Ryan
>>> my_pikachu.level
1
>>> print(my_pikachu)
Ryan - Level 1

>>> my_pikachu.make_sound()  # Print
Pika Pika
>>> my_pikachu.run()  # Print
Pikachu running...

>>> my_pikachu.level
1
>>> my_pikachu.attack()  # Print
Electric attack with 10 damage

>>> another_pikachu.level
2
>>> another_pikachu.attack()  # Print
Electric attack with 20 damage
# Squirtle
Squirtle is a water pokemon. Behavior of Squirtle is mentioned below.

It can make its unique sound (mentioned below)
It can run
It can swim
It can can attack - Magnitude of the attack depends on the level of Squirtle. It is 9 times the level of the attacking squirtle (9 x level)
>>> my_squirtle = Squirtle(name="Ryan")
>>> my_squirtle.name
Ryan
>>> my_squirtle.level
1
>>> print(my_squirtle)
Ryan - Level 1

>>> my_squirtle.make_sound()  # Print
Squirtle...Squirtle

>>> my_squirtle.run()  # Print
Squirtle running...

>>> my_squirtle.swim()  # Print
Squirtle swimming...

>>> my_squirtle.level
1
>>> my_squirtle.attack()  # Print
Water attack with 9 damage

>>> another_squirtle.level
2
>>> another_squirtle.attack()  # Print
Water attack with 18 damage
# Pidgey
Pidgey is a flying pokemon. Behavior of Pidgey is mentioned below.

It can make its unique sound (mentioned below).
It can fly
It can can attack - Magnitude of the attack is 5 times the level of the attacking pidgey (5 x level)
>>> my_pidgey = Pidgey(name="Tom")
>>> my_pidgey.name
Tom
>>> my_pidgey.level
1
>>> print(my_pidgey)
Tom - Level 1

>>> my_pidgey.make_sound()  # Print
Pidgey...Pidgey

>>> my_pidgey.fly()  # Print
Pidgey flying...

>>> my_pidgey.level
1
>>> my_pidgey.attack()  # Print
Air attack with 5 damage

>>> another_pidgey.level
2
>>> another_pidgey.attack()  # Print
Air attack with 10 damage
# Swanna
Swanna is a water & flying pokemon. Behavior of Swanna is mentioned below.

It can make its unique sound (mentioned below).
It can fly
It can swim
It can can attack
As it is both water and flying pokemon, Swanna does double damage i.e
A water attack with 9 x swanna level and
An air attack with 5 x swanna level
>>> my_swanna = Swanna(name="Misty")
>>> my_swanna.name
Misty
>>> my_swanna.level
1
>>> print(my_swanna)
Misty - Level 1

>>> my_swanna.make_sound()  # Print
Swanna...Swanna

>>> my_swanna.fly()  # Print
Swanna flying...

>>> my_swanna.swim()  # Print
Swanna swimming...

>>> my_swanna.level
1
>>> my_swanna.attack()  # Print
Water attack with 9 damage
Air attack with 5 damage

>>> another_swanna.level
2
>>> another_swanna.attack()  # Print
Water attack with 18 damage
Air attack with 10 damage
# Zapdos
Zapdos is an electic & flying pokemon. Behavior of Zapdos is mentioned below.

It can make its unique sound (mentioned below).
It can fly
It can can attack
As it is both electric and flying pokemon, Zapdos does double damage i.e
An electric attack with 10 x zapdos level and
An air attack with 5 x zapdos level
>>> my_zapdos = Zapdos(name="Ryan")
>>> my_zapdos.name
Ryan
>>> my_zapdos.level
1
>>> print(my_zapdos)
Ryan - Level 1

>>> my_zapdos.make_sound()  # Print
Zap...Zap

>>> my_zapdos.fly()  # Print
Zapdos flying...

>>> my_zapdos.level
1
>>> my_zapdos.attack()  # Print
Electric attack with 10 damage
Air attack with 5 damage
>>> another_zapdos.level
2
>>> another_zapdos.attack()  # Print
Electric attack with 20 damage
Air attack with 10 damage
# Task2
# Island
An island in the game is described by

its name
the maximum number of pokemon it can hold
total food available on the island
number of pokemon left to catch on the island
On creating a new island pokemon_left_to_catch should be 0
>>> island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
>>> island.name
Island1
>>> island.max_no_of_pokemon
5
>>> island.total_food_available_in_kgs
10000
>>> island.pokemon_left_to_catch
0
>>> print(island)
Island1 - 0 pokemon - 10000 food 
You can add pokemon to an Island.
>>> island.pokemon_left_to_catch
0
>>> island.add_pokemon(pokemon)
>>> island.pokemon_left_to_catch
1
You can add only a maximum of max_no_of_pokemon pokemon to the Island.
>>> island.pokemon_left_to_catch
5
>>> island.max_no_of_pokemon
5
>>> island.add_pokemon(pokemon)  # Print
Island at its max pokemon capacity
>>> island.pokemon_left_to_catch
5
# Task3
# Trainer
A Pokemon trainer is described by his/her

name: any string with which a trainer is referred, just like a name for humans.
experience: represents the experience of the trainer. experience is 100 for a newly created trainer. Every time a trainer catches a pokemon, his/her experience is increased (details are mentioned at catch method below)
max_food_in_bag: represents the max amount of food a trainer can carry along with him/her. max_food_in_bag increases with the trainers experience. i.e max_food_in_bag is equal to 10 x experience.
food_in_bag: represents the current amount of food a trainer has.
>>> trainer = Trainer(name="Bot") 
>>> trainer.name
Bot
>>> trainer.experience
100
>>> print(trainer)
Bot
>>> trainer.max_food_in_bag
1000
>>> trainer.food_in_bag
0
# Task4
Trainers travel from one island to another to catch pokemon and gather food. Trainers should be shown all the available islands.

>>> Island.get_all_islands()
[Island1 - 100 pokemon - 10000 food,
Island2 - 24 pokemon - 12300 food,
Island3 - 82 pokemon - 11830 food,
Island4 - 192 pokemon - 101238 food]
Should return a list of island objects

# Task5
Trainer can move from one island to another.
>>> trainer.move_to_island(island1)
>>> trainer.current_island == island1
True
>>> trainer.current_island  
Island1 - 0 pokemon - 10000 - food
If trainer is not on any island current_island should return the message mentioned below.
>>> trainer.current_island  # Print
You are not on any island
# Task6
Trainers can collect food from the island and store it in their bag.
>>> trainer.move_to_island(island)
>>> island.total_food_available_in_kgs
10000
>>> trainer.food_in_bag
0
>>> trainer.collect_food()
>>> island.total_food_available_in_kgs
9000
>>> trainer.food_in_bag
1000
Trainer fills his/her bag with food just by calling the collect_food method once.
>>> island.total_food_available_in_kgs
9900
>>> trainer.food_in_bag
1000
>>> trainer.max_food_in_bag
1000
>>> trainer.collect_food()
>>> trainer.food_in_bag
1000
>>> island.total_food_available_in_kgs
9900
When a trainer collects food from an island, food in the island is decreased by the same amount.

If the trainer bag is full i.e., food_in_bag is equal to max_food_in_bag then collect_food doesn't decrease food on the island and also doesn't increase the food_in_bag.

If trainer is not on any island collect_food should behave as mentioned below.

>>> trainer.current_island  # Print
You are not on any island

>>> trainer.collect_food()  # Print
Move to an island to collect food
If the food on the island is less than the food required by the trainer, then your code should behave as below.
>>> island.total_food_available_in_kgs
90
>>> trainer.food_in_bag
0
>>> trainer.experience
100
>>> trainer.max_food_in_bag
1000
>>> trainer.collect_food()
>>> trainer.food_in_bag
90
>>> island.total_food_available_in_kgs
0
# Task7
A trainer can catch a pokemon.
>>> pokemon.name
Pigetto
>>> pokemon.level 
1
>>> trainer.experience
100
>>> trainer.catch(pokemon)  # Print
You caught Pigetto
Every time a trainer catches a pokemon, their experience increases by the pokemon level x 20 points.
>>> pokemon.name
Pigetto
>>> pokemon.level 
1
>>> trainer.experience
100
>>> trainer.catch(pokemon)  # Print
You caught Pigetto
>>> trainer.experience
120
A trainer can catch a pokemon only if his/her experience >= 100 x pokemon.level
>>> pokemon.name
Pigetto
>>> pokemon.level 
2
>>> trainer.experience
100
>>> trainer.catch(pokemon)  # Print
You need more experience to catch Pigetto
# Task8
A trainer can see the list of all pokemon he/she has caught.
>>> trainer.get_my_pokemon()
[Pigetto - Level 1]
get_my_pokemon should return a list of pokemon objects the trainer has caught.

# Task9
A pokemon remembers its trainer.

>>> pokemon.name
Pigetto
>>> pokemon.level 
1
>>> pokemon.master  # Print
No Master
>>> trainer.catch(pokemon)
>>> pokemon.master == trainer 
True





ANSWER:


class Pokemon:
    sound = ""
    def __init__(self, name = None, level = 1):
        if name == "":
            raise ValueError("name cannot be empty")
        if level <= 0:
            raise ValueError("level should be > 0")
        self._name = name 
        self._level = level
        self._electrical_level = 10 * self._level
        self._water_level = 9 * self._level
        self._air_level = 5 * self._level
        self._master = None
        
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @property
    def electrical_level(self):
        return self._electrical_level
    @property
    def water_level(self):
        return self._water_level
    @property
    def air_level(self):
        return self._air_level
       
    def __str__(self):
        return f'{self._name} - Level {self._level}'
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @property
    def master(self):
        if self._master == None:
            print("No Master")
        else:
            return self._master

class Swim:
    swimming = ""
    @classmethod 
    def swim(cls):
        print(cls.swimming)
        
class Fly:
    flying = ""
    @classmethod
    def fly(cls):
        print(cls.flying)

class Run:
    running = ""
    @classmethod
    def run(cls):
        print(cls.running)

class Pikachu(Pokemon, Run):
    sound = "Pika Pika"
    running = "Pikachu running..."
    
    def attack(self):
        print("Electric attack with {} damage".format(self.electrical_level))

class Squirtle(Pokemon, Run, Swim):
    sound = "Squirtle...Squirtle"
    running = "Squirtle running..."
    swimming = "Squirtle swimming..."
    
    def attack(self):
        print("Water attack with {} damage".format(self.water_level))

class Pidgey(Pokemon, Fly):
    sound = "Pidgey...Pidgey"
    flying = "Pidgey flying..."
    def attack(self):
        print("Air attack with {} damage".format(self.air_level))
        
class Swanna(Pokemon, Swim, Fly):
    sound = "Swanna...Swanna"
    swimming = "Swanna swimming..."
    flying = "Swanna flying..."
    def attack(self):
        print("Water attack with {} damage".format(self.water_level))
        print("Air attack with {} damage".format(self.air_level))


class Zapdos(Pokemon, Fly):
    sound = "Zap...Zap"
    flying = "Zapdos flying..."
    def attack(self):
        print("Electric attack with {} damage".format(self._electrical_level))
        print("Air attack with {} damage".format(self.air_level))



class Island:
    _island_list = []
    def __init__(self, name = None, max_no_of_pokemon = 0,total_food_available_in_kgs=0):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self._island_list.append(self)
        
    @property
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    def __str__(self):
        return f'{self._name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food'
    
    def add_pokemon(self, pokemon):
        self.pokemon = 1
        if self._pokemon_left_to_catch == self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")        
        else:
            self._pokemon_left_to_catch += self.pokemon
            
    @classmethod
    def get_all_islands(cls):
        return cls._island_list

class Trainer(Pokemon):
    def __init__(self, name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 10 * self._experience
        self._food_in_bag = 0
        self.pokemon_list = []
        self._current_island = None
        
    @property 
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag

    def __str__(self):
        return f'{self._name}'
    
    def catch(self,pokemon):
        pokemon._master = self
        if self._experience >= 100 * pokemon.level:
            print("You caught {}".format(pokemon.name))
            self._experience += 20
            self.pokemon_list.append(pokemon)
        else:
            print("You need more experience to catch {}".format(pokemon.name))
            
    def get_my_pokemon(self):
        return self.pokemon_list
        
    @property    
    def current_island(self):
        if self._current_island == None:
           print("You are not on any island")
        else:
            return self._current_island
        
    def move_to_island(self, island):
        self._current_island = island
            

    def collect_food(self):
        if self._current_island == None:
            print("Move to an island to collect food")
            
        else:
            if self._current_island._total_food_available_in_kgs > self._max_food_in_bag:
                if self._food_in_bag < self._max_food_in_bag:
                    self._current_island._total_food_available_in_kgs -= self._max_food_in_bag
                    self._food_in_bag += self._max_food_in_bag
                else:
                    self._food_in_bag = self._max_food_in_bag
            
            else:
                self._food_in_bag = self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs = 0
                
                
                
'''
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
island = Island(name="Island2", max_no_of_pokemon=10, total_food_available_in_kgs=10000)
island = Island(name="Island3", max_no_of_pokemon=20, total_food_available_in_kgs=10000)
print(island.get_all_islands())
'''
