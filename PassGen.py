import secrets 
import string

def generate_password(length: int = 10): #Defines the function that takes the parameter 'length'
    alphabet = string.ascii_letters + string.digits + string.punctuation #A string variable is created to contain all uppercase & lowercase letters
    password = ''.join(secrets.choice(alphabet) for _ in range(length)) #Constructs the password
    return password

password = generate_password() #Calling of the function
print(f"Generated Password: {password}") #Prints the generated password
