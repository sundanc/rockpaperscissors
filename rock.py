import random

player_score = 0
cpue_score = 0

while(True):
    player_choice = int(input('enter 1 for rock 2 for paper 3 for scissors: '))
    cpu_choice = random.randint(1, 3)

    if player_choice == cpu_choice:
        print("its a tie no points will be awarded")

    elif player_choice == 1:
        if cpu_choice == 2:
            print('cpu chose paper and won this raund')
            cpue_score += 1
            print('cpu score: ' + str(cpue_score) + '\n' +
                  'your score: ' + str(player_score))

        if cpu_choice == 3:
            print('cpu chose paper and won this raund')
            cpue_score += 1
            print('cpu score: ' + str(cpue_score) + '\n' +
                  'your score: ' + str(player_score))
    elif player_choice == 2:
        if player_choice == 1:
            print('cpu chose rock. You won this raund')
            player_score += 1
            print('cpu score: ' + str(cpue_score) + '\n' +
                  'your score: ' + str(player_score))

        if cpu_choice == 3:
            print('cpu chose paper and won this raund')
            cpue_score += 1
            print('cpu score: ' + str(cpue_score) + '\n' +
                  'your score: ' + str(player_score))

    else:
        if cpu_choice == 1:
            print('cpu chose rock and won this raund')
            cpue_score += 1
            print('cpu score: ' + str(cpue_score) + '\n' +
                  'your score: ' + str(player_score))

        if cpu_choice == 2:
            print('cpu chose paper. and You won this raund')
            cpue_score += 1
            print('cpu score: ' + str(cpue_score) + '\n' +
                  'your score: ' + str(player_score))
    if player_score == 2:
        print('You won! Best two out of 3! ')
        break
    if cpue_score == 2:
        print("cpu won, sorry but you have lost! ")
        break
