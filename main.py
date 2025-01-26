# 1) Create file called students.txt
with open("students.txt","w") as file:

# 2) Add lines to enter members of the class
  file.write("Layla Adebutu Oladunni\n")
  file.write("Alessandro Baldassari\n")
  file.write("Marlee Carballo\n") 
  file.write("Tao Carboni Joaqui\n")
  file.write("Joseph Culmer\n")
  file.write("Rafael Di Iorio Andrade Ferreira\n")
  file.write("Maisie Fletcher\n")
  file.write("Oliver Gerling\n")
  file.write("Selma Grafstrom\n")
  file.write("Bram Gunneweg\n")
  file.write("Bayne Higgins\n")
  file.write("Lida Mann\n")
  file.write("Oliver Manning\n")
  file.write("Aaron Paul Maunders\n")
  file.write("Letlotlo Mosotho\n")
  file.write("Amelia Osborne\n")
  file.write("Benjamin Perry\n")
  file.write("Tara Rennie\n")
  file.write("Isabella Sinodinos\n")
  file.write("Leila Skinner\n")
  file.write("Sofia Stucchi Dutto\n")
  file.write("Harry Voke\n")
  file.write("Jolie White\n")
  file.write("Ken Wilderotter\n")

# 3) Loop through the lines and output each one

with open("students.txt","r") as file:
    print("The name of the students are:")
    for line in file:
        print(line.strip())

# 4) Print out the second letter in everyone's name
with open("students.txt","r") as file:
    print("The second letter of everyone's name is:")
    for line in file:
        print(line[1])  

# 5) Print out every name that is over 6 letters long

with open("students.txt", "r") as file:
    print("Names with more than 6 letters long")
    for line in file:
        name = line.strip()
        if len(name) > 6:
            print(name)


# 6) Get the user to add a new name to the file

new_line = input("Enter a new name:")

with open("students.txt","a") as file:
     file.write(new_line + "\n")
