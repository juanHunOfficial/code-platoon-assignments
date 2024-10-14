class GuessingGame():
    def __init__(self, answer: int) -> None:
        self.answer = answer
    
    def guess(self, guess: int) -> str:
        self.guess = guess
        if guess == self.answer:
            return "correct"
        elif guess > self.answer:
            return "high"
        else:
            return "low"
    
    def solved(self):
        if self.guess == self.answer:
            return True
        else: 
            return False