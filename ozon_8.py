from copy import deepcopy

CARDS_POWER = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

ALL_CARDS = (
    '2S', '2C', '2D', '2H',
    '3S', '3C', '3D', '3H',
    '4S', '4C', '4D', '4H',
    '5S', '5C', '5D', '5H',
    '6S', '6C', '6D', '6H',
    '7S', '7C', '7D', '7H',
    '8S', '8C', '8D', '8H',
    '9S', '9C', '9D', '9H',
    'TS', 'TC', 'TD', 'TH',
    'JS', 'JC', 'JD', 'JH',
    'QS', 'QC', 'QD', 'QH',
    'KS', 'KC', 'KD', 'KH',
    'AS', 'AC', 'AD', 'AH'
    )

def calc_power(card1, card2, card3):
    '''функция считает и возвращает силу комбинации'''
    if card1[0] == card2[0] == card3[0]:
        pwr = CARDS_POWER[card1[0]]
        pwr = pwr * 100

    elif card1[0] == card2[0]:
        pwr = CARDS_POWER[card1[0]]
        pwr = pwr * 10

    elif card1[0] == card3[0]:
        pwr = CARDS_POWER[card1[0]]
        pwr = pwr * 10

    elif card2[0] == card3[0]:
        pwr = CARDS_POWER[card2[0]]
        pwr = pwr * 10

    else:
        pwr = max(CARDS_POWER[card1[0]], CARDS_POWER[card2[0]], CARDS_POWER[card3[0]])
    
    return pwr

n = int(input())

ans = []

for i in range(n):
    m = int(input())
    combinations_dealt = []
    cards_dealt = []
    
    for j in range(m):
        
        s = input().split()
        combinations_dealt.append(s)
        cards_dealt.extend(s)

    cards_in_the_deck = [i for i in ALL_CARDS if i not in cards_dealt]

    temp = deepcopy(combinations_dealt)
    
    cards_to_win = []
    for card in cards_in_the_deck:
        
        [i.append(card) for i in combinations_dealt]
        combinations_power = []
  
        for comb in combinations_dealt:
            
            true_power = calc_power(comb[0], comb[1], comb[2])
            combinations_power.append(true_power)

        if max(combinations_power) == combinations_power[0]:
            cards_to_win.append(card)

        combinations_dealt = deepcopy(temp)

    ans.append(len(cards_to_win))
    if cards_to_win:
        ans.extend(cards_to_win)


print(*ans, sep='\n') 


