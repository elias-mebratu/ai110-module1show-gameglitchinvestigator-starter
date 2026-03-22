
def get_range_for_difficulty(difficulty: str):  
    
    if difficulty == "Easy":
        
        return 1, 20

   
    if difficulty == "Normal":
        
        return 1, 100

    
    if difficulty == "Hard":
        
        return 1, 50

    
    return 1, 100


def parse_guess(raw: str):  
    
    if raw is None:
       
        return False, None, "Enter a guess."

    
    raw = raw.strip()

   
    if raw == "":
        
        return False, None, "Enter a guess."

    
    try:
        
        value = int(raw)

   
    except ValueError:
        
        return False, None, "That is not a whole number."

   
    return True, value, None



def check_guess(guess, secret):  
    
    if guess == secret:
      
        return "Win", "🎉 Correct!"

    
    if guess > secret:
        
        return "Too High", "📉 Too high! Go LOWER!"

    
    return "Too Low", "📈 Too low! Go HIGHER!"



def update_score(current_score: int, outcome: str, attempt_number: int):  # This defines a helper function that changes the score based on the outcome and the attempt number.
   
    if outcome == "Win":
        
        points = 100 - 10 * (attempt_number - 1)

       
        if points < 10:
           
            points = 10

       
        return current_score + points

    if outcome == "Too High":
       
        return current_score - 5

    if outcome == "Too Low":
        
        return current_score - 5

   
    return current_score