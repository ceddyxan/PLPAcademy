#File Read & Write Challenge 🖋️

#Opening a file in read mode
open("WeekFour.txt","r") 
file = open("WeekFour.txt","r")
print(file.read()) #reading entire file

#Append a new line to the file and create a new file
file = open("WeekFour.txt","a") 
file.write("\nThis is a new line added to the file.")
print("Extra content appended successfully!")
file.close() 

#Opening the file in read mode again to check if the new line is added
file = open("WeekFour.txt","r") 
print(file.read()) #reading entire file
file.close()


#Error Handling Lab 🧪
#Ask the user for a filname and handle the error if the file does not exist
filename = input("Please enter the filename: ")
try:
    file = open(filename, "r")
    print(file.read())  #reading entire file
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")  #Handle the error
finally:
    print("File operation completed.")
