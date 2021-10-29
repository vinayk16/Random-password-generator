import password_creator
a=input("u = Uppercase Alphabet\nl = lowercase Alphabet\nd = Numerical Digits\ns = Special Characters\n Enter the character set : ")
b=int(input("Enter the length of your password : "))
password=password_creator.Password(a,b)
password.char_in_the_pass()
password.generate_the_password()
print("The Randomly generated strong password : ",password.get_password())