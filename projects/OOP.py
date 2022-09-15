class Dog():
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old!')
    
    def talk(self):
        print('Woof Woof!')

class Cat(Dog):
    def talk(self):
        print('Meow!')

Dexter = Dog(1.5, 'Dexter')
Dexter.speak()
Dexter.talk()
Monte = Cat(5,'Monte')
Monte.speak()
Monte.talk()

    

    