import random
from main import BaseGame

class Game(BaseGame):
    def __init__(self):
        super().__init__("Blackjack")

    def get_score(self, hand):
        score = sum(hand)
        # Handle Aces (simplified: 11 becomes 1 if you bust)
        if score > 21 and 11 in hand:
            score -= 10
        return score

    def game_loop(self):
        playing = True
        while playing:
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
            player_hand = [random.choice(deck), random.choice(deck)]
            dealer_hand = [random.choice(deck), random.choice(deck)]

            # Inner loop: Current Round
            while True:
                print(f"\nYour hand: {player_hand} (Score: {self.get_score(player_hand)})")
                print(f"Dealer shows: {dealer_hand[0]}")

                if self.get_score(player_hand) > 21:
                    print("BUST! Dealer wins.")
                    break

                action = input("Do you want to (H)it, (S)tand, or (P)ause? ").upper()

                if action == 'P':
                    pause_choice = self.pause_menu()
                    if pause_choice == "EXIT": return
                    if pause_choice == "RESTART": break # Breaks to restart the hand
                    continue

                elif action == 'H':
                    player_hand.append(random.choice(deck))

                elif action == 'S':
                    while self.get_score(dealer_hand) < 17:
                        dealer_hand.append(random.choice(deck))

                    p_score = self.get_score(player_hand)
                    d_score = self.get_score(dealer_hand)

                    print(f"Dealer's final hand: {dealer_hand} (Score: {d_score})")
                    if d_score > 21:
                        print("Dealer BUSTS! You WIN!")
                    elif p_score > d_score:
                        print("You WIN!")
                    elif p_score < d_score:
                        print("Dealer WINS!")
                    else:
                        print("It's a PUSH (Tie)!")
                    break

            # After the round ends:
            choice = input("\n[1] Play Another Round\n[2] Return to Main Menu\nChoice: ")
            if choice != '1':
                playing = False