import os
contact={}

def clsr():
    os.system("pause")
    os.system("cls")

def title(args):
    print("=============================")
    print("        Contact Book")
    print("=============================")
    print(">> " + args)
    
def menu():
    title("Menu")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Display Contact")
    print("0. Exit")
    choose = int(input("Choose : "))
    return choose

def isKey(key):
    global contact
    if key in contact.keys():
        return True
    else:
        return False

def add_contact():
    global contact
    title("Add Contact")
    name = input("Nama  : ")
    nohp = input("No Hp : ")
    if not isKey(name):
        contact[name] = nohp
    else:
        print("Sorry your name was here")
    
def del_contact():
    global contact
    title("Delete Contact")
    key = input("Name : ")
    if isKey(key=key):
        del contact[key]
    else:
        print("Maaf"+key+"tidak ada di kontak anda")

def display_contact():
    global contact
    print(contact)
    
def main():
    i = -1
    while i != 0:
        i = menu()
        clsr()
        if i == 1:
            add_contact()
        elif i == 2:
            del_contact()
        elif i == 3:
            display_contact()
        else:
            print("All data deleted after this!")  
            
if __name__ == "__main__":
    main()