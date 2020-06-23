import random
import string

class PasswordGenerator:
    def __init__(self):
        self.container = ["", string.ascii_lowercase, string.digits, string.punctuation]
    
    def generatePWD(self, n, strength):
        if strength not in range(1, len(self.container)+1):
            raise ValueError('Password strength out of range: 1-{}.'.format(len(self.container)))
        
        return ''.join(random.choices(string.ascii_uppercase + ''.join(self.container[:strength]), k=n)) 


#Example
gen = PasswordGenerator()
print(gen.generatePWD(10,10))