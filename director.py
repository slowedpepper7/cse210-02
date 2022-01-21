from card import Card


class Director:

    def set(self):
        pass
        
    def begin_game(self):
        #A loop That uses all the functions, until the game is over. Score gets to 0, or they choose to not continue 

    def user_input(self):
        #Asks if the user is playing again
        continue_playing = input("Play Again? [y/n] ")
        self.is_playing = (continue_playing == "y")
        #Gathers the Users input on weather they think it will be higher or lower
        card_guess = input("Will the next card be higher or lower? H/L")
       
    def update(self):
        pass
        #Updates the Score

    def do_output(self):
        pass
        #Displays the Score
