AssignmentID - OOP005
Submission Guidelines
Coding Guidelines
Item
Query
Store
# Store
Let’s say, you have built a store that is filled with different grocery items. You have observed that customers are facing difficulty to find an item. So you have decided to write a program that would make it easy for users to search for items.

# Submission Guidelines
Create a folder /home/ec2-user/environment/oop/oop_submissions/oop_assignment_005. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/oop/oop_submissions/oop_assignment_005/

Copy your code file to the submission folder. Make use of the below example command
$ cp store.py /home/ec2-user/environment/oop/oop_submissions/oop_assignment_005
# Coding Guidelines
Write all your code in store.py file
Write the following classes to complete the assignment

# Item
An item has the following properties

name: Name of the item
price: Price of the item > 0
category: Category to which the item belongs to (any string value)
Coding Guidelines:

Write Item class in store.py file. It should behave as shown below.
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> print(item)  
Oreo Biscuits@30-Food  

>>> item = Item(name="Oreo Biscuits", price=0, category="Food")  
ValueError: Invalid value for price, got 0  

# Query
A query is a request from the customer to the store. It has the following properties

field: Properties of Item on which customer is searching . In our case name or price or category
value: Value to which the item property is to be matched with
operation: Operations mentioned below
Coding Guidelines:

Write Query class in store.py file. It should behave as shown below.
>>> query = Query(field="name", operation="EQ", value="Oreo Biscuits")  
>>> print(query)  
name EQ Oreo Biscuits  

# Store
A store is a collection of items. Customers can search for relevant items in the store. It should support the following functionality.

# Add item:
Adds a new item to the store

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  

# Display all items:
Displays all the items in the store

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> print(store)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food

# Filter:
A filter method should filter the items in a store based on users preference (a Query object) and returns a Store object containing the filtered results.

Customers provide thier preference as Query object which represents their needs.

You code should be have as below.

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Butter", price=10, category="Grocery")  
>>> store.add_item(item)  
>>> query = Query(field="category", operation="IN", value=["Food"])  
>>> results = store.filter(query)  
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  

Equals condition:
   >>> query = Query(field="name", operation="EQ", value="Oreo Biscuits")  
   >>> results = store.filter(query)  
   >>> print(results)  
   Oreo Biscuits@30-Food  

Explanation:

Query(field="name", operation="EQ", value="Oreo Biscuits")

Should filter all the items which have "Oreo Biscuits" as value for the field "name"

Greater Than condition:
>>> query = Query(field="price", operation="GT", value=20)  
>>> results = store.filter(query) 
>>> print(results)  
Oreo Biscuits@30-Food  

Explanation:

Query(field="price", operation="GT", value=20)

Should filter all the items which have value greater than 20 for the field "price"

Greater Than or Equal condition: "GTE"
>>> query = Query(field="price", operation="GTE", value=20)  
    >>> results = store.filter(query) 
    >>> print(results)  
    Oreo Biscuits@30-Food  
    Boost Biscuits@20-Food 

Explanation:

Query(field="price", operation="GTE", value=20)

Should filter all the items which have value greater than or equal to 20 for the field "price"

Less Than: "LT"
>>> query = Query(field="price", operation="LT", value=20)  
>>> results = store.filter(query) 
>>> print(results)  
Butter@10-Grocery

Explanation:

Query(field="price", operation="LT", value=20)

Should filter all the items which have value less than 20 for the field "price"

Less Than or Equal : "LTE"
>>> query = Query(field="price", operation="LTE", value=20)  
>>> results = store.filter(query) 
>>> print(results)  
Boost Biscuits@20-Food
Butter@10-Grocery

Explanation:

Query(field="price", operation="LTE", value=20)

Should filter all the items which have value less than or equal to 20 for the field "price"

StartsWith: "STARTS_WITH"
 >>> query = Query(field="name", operation="STARTS_WITH", value="Bu")  
>>> results = store.filter(query) 
>>> print(results)  
Butter@10-Grocery

Explanation:

Query(field="name", operation="STARTS_WITH", value="bu")

Should filter all the items which have value that starts with "bu" for the field "name"

EndsWith: "ENDS_WITH" - is used to as condition in Query object to filter items with field value that ends with the query value
>>> query = Query(field="name", operation="ENDS_WITH", value="cuits")  
>>> results = store.filter(query) 
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food 

Explanation:

Query(field="name", operation="ENDS_WITH", value="cuits")

Should filter all the items which have value that ends with "cuits" for the field "name"

Contains: "CONTAINS"
>>> query = Query(field="name", operation="CONTAINS", value="uit")  
>>> results = store.filter(query) 
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food

Explanation:

Query(field="name", operation="CONTAINS", value="cuits")

Should filter all the items which have value that contains "cuits" for the field "name"

In: "IN"
>>> query = Query(field="name", operation="IN", value=["Oreo Biscuits", "Boost Biscuits" ])  
>>> results = store.filter(query) 
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food

Explanation:

Query(field="name", operation="IN", value=["Oreo Biscuits", "Boost Biscuits" ]) 

Should filter all the items which have value one of “Oreo Biscuits” or “Boost Biscuits” for the field "name"

Filter should return a new store object which has only the selected items.
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.filter(query) # filter all items whose price is greater than 15 
>>> type(results)  # this is to show that results is another store object
<class '__main__.Store'>
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  

Incase of empty results. Store should be have as below.
>>> query = Query(field="name", operation="STARTS_WITH", value="bu")  
>>> results = store.filter(query) 
>>> print(results)
No items

# Exclude:
exclude is very similar to filter but works in an opposite way.
Similar to filter, It takes Query as a parameter
It returns a new Store object that contains all the items in the store except the ones which match the query.
>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")  
>>> store.add_item(item)  
>>> print(store)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  
ParleG Biscuits@10-Food  
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.exclude(query)  # exclude all items whose price is greater than 15 
>>> print(results)  
ParleG Biscuits@10-Food  

Exclude should return a new store object which has all the items that doesn’t match the query.
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.filter(query) # filter all items whose price is greater than 15 
>>> type(results)  # this is to show that results is another store object
<class '__main__.Store'>
>>> print(results)  
ParleG Biscuits@10-Food

# Chaining:
Queries can be chained i.e users should be able to perform further queries on the result of a query.

Hint: filter and exclude methods should return a new store object with filtered items.

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")  
>>> store.add_item(item)  
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.filter(query)  
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  
>>> new_query =  Query(field="name", operation="CONTAINS", value='Boost')  
>>> updated_results = results.exclude(new_query)  
>>> print(updated_results)  
Oreo Biscuits@30-Food  



# Count:
Count of items in the store

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")  
>>> store.add_item(item)  
>>> store.count()  
3

# Query
Should allow only the following operations.
IN
EQ
GT
GTE
LT
LTE
STARTS_WITH
ENDS_WITH
CONTAINS
Should raise a ValueError incase of invalid input.
>>> query = Query(field="name", operation="random", value="Oreo Biscuits")  
ValueError: Invalid value for operation, got random  

Back






class Item:
    
    def __init__(self, name = None, price = 0, category = None): 
        if price <= 0:
            raise ValueError("Invalid value for price, got {}".format(price))
            
        self.name = name
        self.price = price
        self.category = category
        
    def __str__(self):
        return self.name + "@" + str(self.price) + "-" + self.category
        

class Query:
    
    operations = ['IN', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']
    def __init__(self, field = None, operation = None, value = None):
        self.field = field
        if  operation not in self.operations:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        self.operation = operation
        self.value = value
     
    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'


class Store:
    def __init__(self):
        self.item_list = []
    
    def add_item(self, item = None):
        self.item_list.append(item)

    def __str__(self):
        if len(self.item_list) > 0:
            return "\n".join(map(str,self.item_list))
        else:
            return "No items"
            
    def count(self):
        return len(self.item_list)
        
    def filter(self, query):
        store_obj = Store()
        if query.operation == 'IN':
            for prod in self.item_list:
                if (prod.name in query.value) or (prod.price in query.value) or (prod.category in query.value):
                    store_obj.add_item(prod)
        
        
        elif query.operation == 'EQ':
            for prod in self.item_list:
                if query.value == prod.name:
                    store_obj.add_item(prod)
                if query.value == prod.price:
                    store_obj.add_item(prod)
                if query.value == prod.category:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'GT':
            for prod in self.item_list:
                if prod.price > query.value:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'GTE':
            for prod in self.item_list:
                if prod.price >= query.value:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'LT':
            for prod in self.item_list:
                if prod.price < query.value:
                     store_obj.add_item(prod)
            
        elif query.operation == 'LTE':
            for prod in self.item_list:
                if prod.price <= query.value:
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'STARTS_WITH':
            for prod in self.item_list:
                if prod.name.startswith(query.value):
                    store_obj.add_item(prod)
                if prod.category.startswith(query.value):
                    store_obj.add_item(prod)
            
            
        
        elif query.operation == 'ENDS_WITH':
            for prod in self.item_list:
                if prod.name.endswith(query.value): 
                    store_obj.add_item(prod)
                if prod.category.endswith(query.value):
                    store_obj.add_item(prod)
        
            
            
        elif query.operation == 'CONTAINS':
            for prod in self.item_list:
                if (query.field == 'name' and prod.name.__contains__(query.value)) or (query.field == 'category' and prod.category.__contains__(query.value)):
                     store_obj.add_item(prod)
            
        return store_obj
            
    def exclude(self, query):
            
        store_obj = Store()
        if query.operation == 'IN':
            for prod in self.item_list:
                if (prod.name not in query.value) and  (prod.price not in query.value) and (prod.category not in query.value):
                    store_obj.add_item(prod)
            
            
        elif query.operation == 'EQ':
            for prod in self.item_list:
                if query.value != prod.name and query.value != prod.price and query.value != prod.category:
                    store_obj.add_item(prod)

            
        
        elif query.operation == 'GT':
            for prod in self.item_list:
                if query.value >= prod.price:
                    store_obj.add_item(prod)

            
        elif query.operation == 'GTE':
            for prod in self.item_list:
                if query.value > prod.price:
                    store_obj.add_item(prod)
                    
        elif query.operation == 'LT':
            for prod in self.item_list:
                if  query.value <= prod.price:
                    store_obj.add_item(prod)

            
        elif query.operation == 'LTE':
            for prod in self.item_list:
                if query.value < prod.price:
                    store_obj.add_item(prod)
                    
                    
        elif query.operation == 'STARTS_WITH':
            for prod in self.item_list:
                if not(prod.name.startswith(query.value) or prod.category.startswith(query.value)):
                    store_obj.add_item(prod)
              
        
        elif query.operation == 'ENDS_WITH':
            for prod in self.item_list:
                if not(prod.name.endswith(query.value) or prod.category.endswith(query.value)): 
                    store_obj.add_item(prod)
            
        elif query.operation == 'CONTAINS':
            if query.field == "name":
                for prod in self.item_list:
                    if not(prod.name.__contains__(query.value)):
                        store_obj.add_item(prod)
                        
            else:
                for prod in self.item_list:
                    if not(prod.category.__contains__(query.value)):
                        store_obj.add_item(prod)
            
        return store_obj   
            
'''  
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item) 
query = Query(field="name", operation="EQ", value="Food")  
results = store.filter(query) 
print(results)              
'''
