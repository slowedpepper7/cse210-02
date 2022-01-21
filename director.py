from card import Card


class Director:

    def set(self):
        pass
        
    def begin_game(self):
        pass

    def user_input(self):
        card_guess = input("Will the next card be higher or lower? H/L")
        self.is_playing = (card_guess == "H") or (card_guess == "L"
       
    def update(self):
        pass

    def do_output(self):
        pass
