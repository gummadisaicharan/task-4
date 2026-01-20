# loop_tasks.py
# Demonstration of loops and iterations in Python

print("🔹 FOR LOOP: Printing numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n")


print("🔹 WHILE LOOP: Countdown Timer")
count = 10
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("🚀 Countdown Finished!\n")


print("🔹 BREAK and CONTINUE Example")
for num in range(1, 11):
    if num == 5:
        print("Skipping number 5 using continue")
        continue
    if num == 8:
        print("Stopping loop at 8 using break")
        break
    print(num)
print()


print("🔹 ITERATING OVER STRING CHARACTERS")
name = "Python"
for char in name:
    print(char)
print()


print("🔹 MULTIPLICATION TABLE")
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print()


print("🔹 RANGE WITH STEPS (Even Numbers 0–20)")
for i in range(0, 21, 2):
    print(i, end=" ")
print("\n")


print("🔹 LOOP WITH CONDITIONS (Real-world Example)")
marks = [45, 67, 89, 34, 90, 76]

for mark in marks:
    if mark >= 50:
        print(f"{mark} → Pass")
    else:
        print(f"{mark} → Fail")
