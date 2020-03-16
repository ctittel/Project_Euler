# Monopoly: instead of two 6-sided dice, two 4-sided dice are used. Find the 6 digit modal string of the 3 most likely squares

# idea: init all squares with the same probability, iterate through the squares until nothing changes
probs = {i: 0.0 for i in range(0, 40)}
probs[0] = 1.0

dice = {}
dice_sides = 4

# ugly way to get all the probabilites of the dice combinations
dice = {i:0 for i in range(0,2*dice_sides*3)}
for d11 in range(1,dice_sides+1):
    for  d12 in range(1,dice_sides+1):
        p1 = (1/(dice_sides**2))
        s1 = d11+d12
        if d11 != d12:
            dice[s1] += p1
        else:
            for d21 in range(1,dice_sides+1):
                for d22 in range(1,dice_sides+1):
                    p2 = p1 * (1/(dice_sides**2))
                    s2 = s1 + d21 + d22
                    if d21 != d22:
                        dice[s2] += p2
                    else:
                        for d31 in range(1,dice_sides+1):
                            for d32 in range(1,dice_sides+1):
                                p3 = p2 * (1/(dice_sides**2))
                                s3 = s2 + d31 + d32
                                if d31 != d32:
                                    dice[s3] += p3
                                else:
                                    dice[0] += p3

square_GO = 0
square_JAIL = 10
square_G2J = 30
squares_CC = [2, 17, 33]
squares_CH = [7, 22, 36]
square_C1 = 11
square_E3 = 24
square_H2 = 39
square_R1 = 5

for i in range(20000):
    old_probs = probs.copy()
    for square, current_prob in old_probs.items(): 
        probs[square] -= current_prob
        for dice_val, dice_prob in dice.items():
            p = dice_prob * current_prob
            if dice_val == 0:
                probs[square_JAIL] += p
            else:
                new_square = square + dice_val
                new_square = new_square % 40
                if new_square == square_G2J:
                    probs[square_JAIL] += p
                elif new_square in squares_CC:
                    probs[square_GO] += p * (1/16)    
                    probs[square_JAIL] += p * (1/16)
                    probs[new_square] += p * (12/16)
                elif new_square in squares_CH:
                    probs[square_GO] += p * (1/16)
                    probs[square_JAIL] += p * (1/16)
                    probs[square_C1] += p * (1/16)
                    probs[square_E3] += p * (1/16)
                    probs[square_H2] += p * (1/16)
                    probs[square_R1] += p * (1/16)
                    next_R = 5 # railway
                    if new_square == 7:
                        next_R = 15
                    elif new_square == 22:
                        next_R = 25
                    probs[next_R] += p * (2/16)
                    next_U = 12 # next U
                    if new_square == 22:
                        next_U = 28
                    probs[next_U] += p * (1/16)
                    probs[new_square-3] += p * (1/16) # go back 3 squares
                    probs[new_square] += p * (6/16)
                else:
                    probs[new_square] += p

    # normalize - for some reason the probabilities diminish otherwise - 
    # either there is an error somewhere or the floats just continue to 
    # get smaller through the multiply and add operations
    s = sum([v for k,v in probs.items()])
    probs = {k:(v/s) for k,v in probs.items()}
print(probs)

# sort and order
t = [(k,v) for k,v in probs.items()]
t.sort(key=lambda x: x[1])
t.reverse()
print([k for k,v in t])

print("--- Top 3: ---")
for k, v in t[:3]:
    print(k, " : ", v)