import time

print("Welcome player!")
print("")
time.sleep(3)

print("To proceed enter your name")
print("")
time.sleep(2)
name = input()
print("")
print("Welcome! ", name, ", now please enter your age")
print("")
age = input()
print("")
print("Excellent! Have fun!")

time.sleep(5)
print("")
print("Collected player data:")
print("")
print(name, ", aged ", age)