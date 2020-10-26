import random
import string
class Password:

    def __init__(self,charset,length):
        self.charset=charset
        self.length=length
        self.char_list=[]
        self.password=[]
    def char_in_the_pass(self):
        if ('l' in self.charset):
            self.char_list.append(string.ascii_lowercase)
        if ('u' in self.charset):
            self.char_list.append(string.ascii_uppercase)
        if ('d' in self.charset):
            self.char_list.append(string.digits)
        if ('s' in self.charset):
            self.char_list.append(string.punctuation)
    def generate_the_password(self):
        for i in range(self.length):
            outer=random.randrange(0,len(self.char_list))
            inner=random.randrange(0,len(self.char_list[outer]))
            self.password.append(self.char_list[outer][inner])
    def get_password(self):
        return ''.join(self.password)

