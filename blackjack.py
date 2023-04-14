import random

# Kart değerlerini ve isimlerini tanımlıyoruz
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
CARD_NAMES = list(CARD_VALUES.keys())

# Oyuncunun ve krupiye(n)in elini temsil eden sınıf
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace_count = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += CARD_VALUES[card]
        if card == 'A':
            self.ace_count += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.ace_count > 0:
            self.value -= 10
            self.ace_count -= 1

# Oyunu temsil eden sınıf
class BlackjackGame:
    def __init__(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_chips = 100
        self.bet_amount = 0
    
    def take_bet(self):
        while True:
            try:
                self.bet_amount = int(input("Enter bet amount (1-{}): ".format(self.player_chips)))
                if self.bet_amount <= 0 or self.bet_amount > self.player_chips:
                    raise ValueError
                break
            except ValueError:
                print("Invalid bet amount. Please enter a valid amount.")
    
    def deal_cards(self):
        self.player_hand.add_card(random.choice(CARD_NAMES))
        self.dealer_hand.add_card(random.choice(CARD_NAMES))
        self.player_hand.add_card(random.choice(CARD_NAMES))
        self.dealer_hand.add_card(random.choice(CARD_NAMES))
    
    def player_hit(self):
        self.player_hand.add_card(random.choice(CARD_NAMES))
        self.player_hand.adjust_for_ace()
    
    def dealer_hit(self):
        self.dealer_hand.add_card(random.choice(CARD_NAMES))
        self.dealer_hand.adjust_for_ace()
    
    def player_turn(self):
        while True:
            choice = input("Do you want to hit or stand? ").lower()
            if choice == 'hit':
                self.player_hit()
                self.show_player_hand()
                if self.player_hand.value > 21:
                    print("Player busts! Dealer wins.")
                    self.player_chips -= self.bet_amount
                    break
            elif choice == 'stand':
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")
    
    def dealer_turn(self):
        self.show_dealer_hand()
        while self.dealer_hand.value < 17:
            self.dealer_hit()
            self.show_dealer_hand()
            if self.dealer_hand.value > 21:
                print("Dealer busts! Player wins.")
                self.player_chips+= self.bet_amount
                return
            if self.player_hand.value > self.dealer_hand.value:
                print("Player wins!")
                self.player_chips += self.bet_amount
            elif self.dealer_hand.value > self.player_hand.value:
                print("Dealer wins!")
                self.player_chips -= self.bet_amount
            else:
                print("It's a tie!")
    def show_player_hand(self):
        print("Player hand: {}".format(self.player_hand.cards))
        print("Player hand value: {}".format(self.player_hand.value))

    def show_dealer_hand(self):
        print("Dealer hand: {}".format(self.dealer_hand.cards[1:]))

    def play_again(self):
        while True:
            choice = input("Do you want to play again? (y/n) ").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
            while True:
                game = BlackjackGame()
                print("Welcome to Blackjack!")
                print("Player chips: {}".format(game.player_chips))
                while game.player_chips > 0:
                    game.take_bet()
                    game.deal_cards()
                    game.show_player_hand()
                    game.show_dealer_hand()
                    game.player_turn()
                    if game.player_hand.value <= 21:
                        game.dealer_turn()
                    if game.play_again():
                        continue
                    else:
                        print("Thanks for playing!")
                        break
                else:
                    print("Out of chips. Game over!")
                    break
def main():
    # Oyun döngüsü
    while True:
        game = BlackjackGame()
        print("Welcome to Blackjack!")
        print("Player chips: {}".format(game.player_chips))

        while game.player_chips > 0:
            game.take_bet()
            game.deal_cards()
            game.show_player_hand()
            game.show_dealer_hand()
            game.player_turn()
            if game.player_hand.value <= 21:
                game.dealer_turn()
            if game.play_again():
                continue
            else:
                print("Thanks for playing!")
                break
        else:
            print("Out of chips. Game over!")
            break

if __name__ == "__main__":
    main()

        
