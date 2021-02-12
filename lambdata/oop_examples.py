''' This is an example of OOP inside a module'''

class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        '''
        constructor for complex numbers
        complex numbers are part real and part imaginary 
        '''
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex)
        '''
        takes another complex number and adds it to itself
        '''
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return"({},{}i)".format(self.r, self.i)
        
class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)
    
    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes
    
    def is_popular(self):
        return self.upvotes > 100


class Animal:
    '''general representation of animals'''
    def __init__(self, name, weight, location, diet_type):
        self.name = name
        self.weight = weight
        self.location = location
        self.diet_type = diet_type

    def eat(self, food):
        return "huge fan of that" + food

    def run(self):
        return "vroom vroom I go quick"

class Sloth(Animal):
    def __init__(self, name, weight, location, num_naps=24, diet_type)
    super().__init__(name, weight, diet_type, location) 
    self.num_naps = num_naps

    def say_something(self):
        return "this is a sloth typing"
    def run(self):
        return "I am a slow guy - I dont run"



if __name__ =='__main__':
    user1 = SocialMediaUser(name='Karl', location='United States')
    user2 = SocialMediaUser(name='Carolton', location='Costa Rica')
    user3 = SocialMediaUser(name='Carlos', location='Argentina', upvotes=531)
    user4 = SocialMediaUser(name='George Washington', location='Djibouti', upvotes=16)


