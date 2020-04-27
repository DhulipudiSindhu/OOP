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
