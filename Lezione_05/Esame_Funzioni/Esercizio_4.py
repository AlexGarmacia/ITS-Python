def blackjack_hand_total(cards: list[int]) -> int:
    
    totale = 0

    for card in cards:
        totale += card

    while totale > 21 and 11 in cards: 
        totale -= 10  # Riduci 11 a 1

    return totale
print(blackjack_hand_total([10, 2, 3]))
print(blackjack_hand_total([10, 11, 3]))  
