import random
import os
import sys

# ---------- UI helpers ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg="Press Enter to continue..."):
    input(msg)

# ---------- Card / Deck ----------
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUE = {**{str(n): n for n in range(2, 11)}, "J": 10, "Q": 10, "K": 10, "A": 11}

def new_deck():
    deck = [(r, s) for s in SUITS for r in RANKS]
    random.shuffle(deck)
    return deck

def draw(deck):
    if not deck:
        deck.extend(new_deck())
    return deck.pop()

def hand_value(hand):
    total = sum(VALUE[r] for r, _ in hand)
    aces = sum(1 for r, _ in hand if r == "A")
    # Downgrade Aces from 11 -> 1 until not bust
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def card_str(card):
    r, s = card
    return f"{r}{s}"

def render_cards(cards):
    # Simple but readable “cards”
    lines = []
    for (r, s) in cards:
        top = "┌─────┐"
        mid1 = f"│{r:<2}   │"
        mid2 = f"│  {s}  │"
        mid3 = f"│   {r:>2}│"
        bot = "└─────┘"
        lines.append([top, mid1, mid2, mid3, bot])

    out = []
    for i in range(5):
        out.append("  ".join(block[i] for block in lines))
    return "\n".join(out)

def render_hidden(cards):
    # Show first card, hide second
    shown = [cards[0]]
    hidden = ("?", "?")
    lines = []
    for card in shown + [hidden]:
        r, s = card
        top = "┌─────┐"
        if r == "?":
            mid1 = "│░░░░░│"
            mid2 = "│░░░░░│"
            mid3 = "│░░░░░│"
        else:
            mid1 = f"│{r:<2}   │"
            mid2 = f"│  {s}  │"
            mid3 = f"│   {r:>2}│"
        bot = "└─────┘"
        lines.append([top, mid1, mid2, mid3, bot])

    out = []
    for i in range(5):
        out.append("  ".join(block[i] for block in lines))
    return "\n".join(out)

# ---------- Game ----------
ASCII = r"""
 _     _            _    _            _               _____
| |   | |          | |  (_)          | |             |A .  | _____
| |__ | | __ _  ___| | ___  __ _  ___| | __          | /.\ ||A ^  | _____
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /          |(_._)|| / \ ||A _  | _____
| |_) | | (_| | (__|   <| | (_| | (__|   <           |  |  || \ / || ( ) ||A_ _ |
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\          |____V||  .  ||(_'_)||( v )|
                       _/ |                                 |____V||  |  || \ / |
                      |__/                                         |____V||  .  |
                                                                          |____V|
"""

def ask_choice(prompt, valid):
    while True:
        ans = input(prompt).strip().lower()
        if ans in valid:
            return ans
        print(f"Type one of: {', '.join(valid)}")

def round_result(player, dealer):
    pv, dv = hand_value(player), hand_value(dealer)

    if pv > 21:
        return "LOSE", f"You busted with {pv}. Congrats, you played yourself."
    if dv > 21:
        return "WIN", f"Dealer busted with {dv}. For once, luck likes you."
    if pv == dv:
        return "PUSH", f"Push. Both at {pv}. Nobody wins, capitalism survives."
    if pv == 21 and len(player) == 2 and not (dv == 21 and len(dealer) == 2):
        return "WIN", "BLACKJACK! Immediate serotonin."
    if dv == 21 and len(dealer) == 2 and not (pv == 21 and len(player) == 2):
        return "LOSE", "Dealer has Blackjack. The house remains undefeated."
    return ("WIN", f"You win {pv} vs {dv}!") if pv > dv else ("LOSE", f"You lose {pv} vs {dv}.")

def play():
    deck = new_deck()
    dealer = [draw(deck), draw(deck)]
    player = [draw(deck), draw(deck)]

    while True:
        clear()
        print(ASCII)
        print("DEALER (one card hidden):")
        print(render_hidden(dealer))
        print("\nYOU:")
        print(render_cards(player))
        print(f"\nYour score: {hand_value(player)}")

        pv = hand_value(player)
        dv = hand_value(dealer)

        # Instant checks (natural blackjack)
        if pv == 21 or dv == 21:
            break

        if pv > 21:
            break

        choice = ask_choice("\nHit (h) or Stand (s)? ", {"h", "s"})
        if choice == "h":
            player.append(draw(deck))
        else:
            break

    # Dealer turn (reveal + draw to 17)
    while hand_value(player) <= 21 and hand_value(dealer) < 17:
        dealer.append(draw(deck))

    clear()
    print(ASCII)
    print("DEALER:")
    print(render_cards(dealer))
    print(f"Dealer score: {hand_value(dealer)}\n")
    print("YOU:")
    print(render_cards(player))
    print(f"Your score: {hand_value(player)}\n")

    verdict, message = round_result(player, dealer)
    print(f"Result: {verdict}\n{message}\n")

def main():
    clear()
    print(ASCII)
    start = ask_choice("Play Blackjack? (y/n): ", {"y", "n"})
    if start != "y":
        print("Goodbye. Responsible choices are suspicious, but accepted.")
        return

    while True:
        play()
        again = ask_choice("Play again? (y/n): ", {"y", "n"})
        if again != "y":
            print("Bye. Try not to gamble your future away.")
            return

if __name__ == "__main__":
    main()
