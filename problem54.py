# Poker
# 5 cards

card_to_val = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def unpack_hand(hand):
    """ Returns list of vals and list of suits """
    suits = [c[1] for c in hand]
    vals = [c[0] for c in hand]
    return vals, suits

def high_card(hand):
    vals, suits = unpack_hand(hand)
    vals.sort()
    vals.reverse()
    return vals

def one_pair(hand):
    vals, suits = unpack_hand(hand)
    vals.sort()
    vals.reverse()
    for v in vals:
        if vals.count(v) >= 2:
            vals.remove(v)
            return [v] + vals
    else:
        return False

def two_pairs(hand):
    vals, suits = unpack_hand(hand)
    vals.sort()
    vals.reverse()
    val1 = 0
    for v in vals:
        if vals.count(v) >= 2:
            if not val1:
                val1 = v
            elif v != val1:
                return [v] + vals
    return False

def three_of_a_kind(hand):
    vals, suits = unpack_hand(hand)
    for v in vals:
        if vals.count(v) >= 3:
            return max(vals)
    else:
        return False    

def straight(hand):
    vals, suits = unpack_hand(hand)
    vals.sort()
    # print(vals)
    should = list(range(vals[0], vals[0]+5))
    # print(should)
    if vals == should:
        return max(vals)
    else:
        return False

def flush(hand):
    vals, suits = unpack_hand(hand)
    # print(suits)
    if suits.count(suits[0]) == 5:
        # print("its a flush")
        return max(vals)
    else:
        return False

def full_house(hand):
    vals, suits = unpack_hand(hand)
    if len(set(vals)) == 2:
        c = vals.count(vals[0])
        if c == 2 or c == 3:
            return max(vals)
    return False

def four_of_a_kind(hand):
    vals, suits = unpack_hand(hand)
    for v in vals:
        if vals.count(v) >= 4:
            return max(vals)
    return False

def straight_flush(hand):
    if flush(hand):
        return straight(hand)
    else:
        return False
    
def royal_flush(hand):
    if flush(hand):
        vals, suits = unpack_hand(hand)
        vals.sort()
        if vals == [10, 11, 12, 13, 14]:
            return max(vals)
        else:
            return False
    return False

def test():
    rf = [(14, "H"), (10, "H"), (12, "H"), (11, "H"), (13, "H")] # AH JH QH TH KH"
    if royal_flush(rf) != 14:
        raise "royal flush failed"

    sf = [(9, "H"), (10, "H"), (12, "H"), (11, "H"), (13, "H")]
    if straight_flush(sf) != 13:
        raise "straight flush failed"

    fl = [(7, "H"), (10, "H"), (12, "H"), (11, "H"), (13, "H")]
    if flush(fl) != 13:
        raise "flush failed"

    stra = [(7, "H"), (10, "H"), (8, "H"), (11, "H"), (9, "H")]
    if straight(stra) != 11:
        raise "straight failed"

    foak = [(7, "H"), (7, "A"), (7, "D"), (13, "H"), (7, "W")]
    if four_of_a_kind(foak) != 13:
        raise "four of a kind failed"

    fh = [(7, "H"), (7, "A"), (7, "D"), (13, "H"), (13, "W")]
    if full_house(fh) != 13:
        raise "full house failed"

funcs = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair, high_card]

def player1_wins(hand):
    h1 = hand[0:5]
    h2 = hand[5:]

    for func in funcs:
        # print(func)
        r1 = func(h1)
        r2 = func(h2)

        # print("func =", func, "r1 =", r1, "r2 =",r2)
        if not r1 and not r2:
            continue
        elif r1 and r2:
            for i in range(len(r1)):
                if r1 == r2:
                    continue
                else:
                    return r1 > r2
            raise "ERRORROOR"
        else:
            return bool(r1)

test()

with open('p054_poker.txt') as f:
    t = f.read()
hands = t.split('\n')[:-1]
hands = [s.split(" ") for s in hands]
hands = [[(card_to_val[c[0]], c[1]) for c in h] for h in hands]

count = 0
for i,hand in enumerate(hands):
    w = player1_wins(hand)
    print("Game ", i, " Player 1 wins: ", w)
    count += w

print("Total wins: ", count)