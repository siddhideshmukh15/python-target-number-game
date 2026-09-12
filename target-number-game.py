import random

target =random.randint(10,50)
score=0

print("=== Number Traget Game ===")
print("Target Number:",target)

while True:
    number =int(input("Enter a number:"))
    
    score += number
    
    print("Current Total:",score)
    
    if score ==target:
        print(" You reached the target!")
        break
    
    elif score >target:
        print("You crossed the target!")
        print("Game Over!")
        break
    else:
        print("keep going!")