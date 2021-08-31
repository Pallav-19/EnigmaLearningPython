firstPlayer = [1, 1]
secondPlayer = [1, 1]
print("\ninitially : ""\nplayer number 1:", firstPlayer, "\nplayer 2:", secondPlayer)
def p1moves():
    p1movesPlay = input('\nAttack/Split P1  : ')
    if p1movesPlay == 'A' or p1movesPlay == 'a':
        p1moves_attack = input('type combination L = left H R = Right H, combination (LR/LL/RL/RR): ')
        if p1moves_attack == 'lr' or p1moves_attack == 'LR' or  p1moves_attack == 'rl' or p1moves_attack == 'RL':
            secondPlayer[1] += firstPlayer[0]
            if(secondPlayer[1] >= 5):
                secondPlayer[1] = 0
        if p1moves_attack == 'll' or p1moves_attack == 'LL' or  p1moves_attack == 'rr' or p1moves_attack == 'RR':
            secondPlayer[0] += firstPlayer[0]
            if(secondPlayer[0] >= 5):
                secondPlayer[0] = 0
    if p1movesPlay == 'S' or p1movesPlay == 's':
        possibility = input('(L_ _/R_ _)  ')
        p1moves_H = possibility[0]
        p1movesLH = int(possibility[1])
        p1movesRH = int(possibility[2])

        if(p1moves_H == 'l' or p1moves_H == 'L'):
                if(firstPlayer[0] > 1):
                    firstPlayer[0] = p1movesLH
                    firstPlayer[1] = p1movesRH
                else:
                    print('\nInvalid Move')
                    p1moves()
        if(p1moves_H == 'r' or p1moves_H == 'R'):
                if(firstPlayer[1] > 1):
                    firstPlayer[0] = p1movesLH
                    firstPlayer[1] = p1movesRH
                else:
                    print('\nInvalid Move')
                    p1moves()
print("\ninitially : ""\nplayer number 1:", firstPlayer, "\nplayer 2:", secondPlayer)
def p2moves():
    p2movesPlay = input('\nEnter move for Player 2 : ')
    if p2movesPlay == 'A' or p2movesPlay == 'a':
        p2moves_attack = input(' combination (LR/LL/RL/RR) : ')
        if p2moves_attack == 'lr' or p2moves_attack == 'LR' or p2moves_attack == 'rr' or p2moves_attack == 'RR':
            firstPlayer[1] += secondPlayer[0]
            if(firstPlayer[1] >= 5):
                firstPlayer[1] = 0
                
        if p2moves_attack == 'll' or p2moves_attack == 'LL' or p2moves_attack == 'rl' or p2moves_attack == 'RL':
            firstPlayer[0] += secondPlayer[0]
            if(firstPlayer[0] >= 5):
                firstPlayer[0] = 0
                
    if p2movesPlay == 'S' or p2movesPlay == 's':
        possibility = input('combination (L * */R * *)  ')
        p2moves_H = possibility[0]
        p2movesLH = int(possibility[1])
        p2movesRH = int(possibility[2])
        if(p2moves_H == 'l' or p2moves_H == 'L'):
                if(secondPlayer[0] > 1):
                    secondPlayer[0] = p2movesLH
                    secondPlayer[1] = p2movesRH
                else:
                    print('\nNot Valid ')
                    p2moves()
        if(p2moves_H == 'r' or p2moves_H == 'R'):
                if(secondPlayer[1] > 1):
                    secondPlayer[0] = p2movesLH
                    secondPlayer[1] = p2movesRH
                else:
                    print('\nInvalid Move')
                    p2moves()
    print("\nCurrently : ""\nplayer 1:",firstPlayer, "\nplayer 2:", secondPlayer)
while ((firstPlayer[0] != 0 or firstPlayer[1] != 0) and (secondPlayer[0] != 0 or secondPlayer[1] != 0)):
    p1moves()
    p2moves()
if(firstPlayer[0] == 0 and firstPlayer[1] == 0):
    print('\nWinner => 2\n')
if(secondPlayer[0] == 0 and secondPlayer[1] == 0):
    print('\nWinner => 1\n')
