from random import randint
### Part 1 - - Keeping it Classy

class Product:
    def __init__(self, name=None, price=10, weight=20, flammability=0.5, 
                identifier=randint(1000000, 9999999)):
        self.name = name 
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

### Part 2 - Objects that Go!
    def stealability(self):
        stealability = self.price / self.weight
        if stealability < 0.5:
            return "Not so stealable..."
        elif stealability < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"
    
    def explode(self):
        e = self.flammability * self.weight
        if e < 10:
            return "...fizzle."
        elif e < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

### Part 3 - A Proper Inheritance

class BoxingGlove(Product):
    def __init__(self, name=None, price=10, weight=10, flammability=0.5, 
                identifier=randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight, 
                        flammability=flammability, identifier=identifier)
    
    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
             return "Hey that hurt!"
        else:
            return "OUCH!"