def main():
    student = get_student()
    if student['name']== "hello":
        student["home"]="bye"
    print(f"{student['name']} from {student['home']}")

def get_student():
    student= {}
    name = input("Name: ")
    home = input("Home: ")
    return {"name": name, "home": home}

if __name__=="__main__":
    main()