import random 
  
name = input("What is your name? ") 
  
print("Good Luck ! ", name) 
  
words = ['remainder', 'computer', 'science', 'programming',  
         'python', 'mathematics','engineerinng', 'player', 'condition',  
         'reverse', 'water', 'board', 'kitty', 'hydrogen' , 'complex', 'keratine','kreatimine', 'kepler']  
  
word = random.choice(words) 
  
  
print("Guess the characters") 
  
guesses = '' 
  
turns = 12
  
  
while turns > 0: 
    failed = 0
      
    for char in word:  
          
        if char in guesses:  
            print(char) 
              
        else:  
            print("_") 
              
            failed += 1
              
  
    if failed == 0: 
        print("You Win")  
          
        print("The word is: ", word)  
        break
      
    guess = input("guess a character:") 
      
    
    guesses += guess  
      
 
    if guess not in word: 
          
        turns -= 1
           
        print("Oh no, you was close \n Try again you have , + turns , more chances to guess")         
          
        if turns == 0: 
            print("Better luck next time and answer was {n}. \n GAME OVER")
