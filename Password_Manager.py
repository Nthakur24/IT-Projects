#Written by Nikhil Thakur
# Description of module:
# To create a program to allow for username and passwords to be stored on a passwords.txt file. The passwords
# are encrypted using Fernet symmetric encryption and the randomly generated key is stored used to view the encryted
# passwords by the user.


from cryptography.fernet import Fernet

''' How the key.key was created
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 
write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# master_pwd = input("What is the master password?")
key = load_key() #+ master_pwd.encode()   #Master password is required to be coverted in bytes as key is in bytes
fer = Fernet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
           data = line.rstrip() #strip of the caridge return
           user, passw = data.split ("|")
           print("User:", user,"| Password:", 
           fer.decrypt(passw.encode()).decode())

#Create a new file if the file storing the password does not exist and add the password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:   #automatically closes file 'with', 'a' mode is append and allows to add to the file or if not found create a new file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit?")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue