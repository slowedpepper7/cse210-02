from game.card import Card


class Director:

    def __init__(self):

        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(1):
            draw = Card()
            self.card.append(draw)
    def gather_input(self):
        h_or_l = input("Is the next card higher or lower? (h/l)")
        return h_or_l

    def start_game(self):

        store_card = [1, 1]
        count = 0
        points = 300
        (self.do_updates(store_card))
        print(f'You drew a {store_card[-1]}')        

        while self.is_playing:
            store_card.pop(0)
            self.get_inputs()
            direction = self.gather_input()
            self.do_updates(store_card)
            self.do_outputs(count)
            print(f'You drew a {store_card[-1]}')
            self.score = 0
            if direction == 'h':
                if store_card[2] > store_card[1]:
                    points += 100
                else:
                    points -= 70
            else:
                if store_card[1] > store_card[2]:
                    points += 100
                else:
                    points -= 70
            count += 1
            print(f'You have {points} points')
            if points <= 0:
                self.is_playing = False
        

    def get_inputs(self):

        play = input("Would you like to play? [y/n] ")
        self.is_playing = (play == "y")
       
    def do_updates(self, store_card):
        if not self.is_playing:
            return 

        for i in range(len(self.card)):
            draw = self.card[i]
            store_card.append(draw.draw())
            self.score += draw.points 
        self.total_score += self.score

    def do_outputs(self, count):
        if not self.is_playing:
            return
        values = ""
        for i in range(len(self.card)):
            draw = self.card[i]
            values += f"{draw.value} "
        self.is_playing == (self.score > 0)
        
