"""
Question 1: Beginner Number Guessing Game
 
Create a simple number guessing game with these requirements:
 
Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
   
Example
 
    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.
 
    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.
 
    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.
 
    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!
 
"""
def test_random():
    random_number = random.randint(1,20)
   
    print(random_number)
   
    print("เรามาเดาเลขกัน")
    print("ทายเลข 1-20")
    print("คุณมีโอกาส6ครั้ง")
for i in range(6):
   
    print(f"ความพยายามครั่งที่ {i+1}")
    guess_number = int(input("what id your guess number(1-20)?: "))
 
    if   test_random == guess_number:  
     print("correct")
 
    elif guess_number < test_random:  
     print("little")
 
    elif guess_number > test_random:  
     print("too much")
 
