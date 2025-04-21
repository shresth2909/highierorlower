import random
import game_data
import art

score = 0
game_should_end = False

def compare_contendors(A,B,choice,score):
    global game_should_end
    if choice == 'A' and A['follower_count'] > B['follower_count']:
        score += 1
        print(f'You opted the correct option!! and you score is {score}')
        B = random.choice(game_data.data)
        return A,B,score,False
    elif choice == 'B' and B['follower_count'] > A['follower_count']:
        score += 1
        print(f'You opted the correct option!! and you score is {score}')
        A = B
        B = random.choice(game_data.data)
        return A, B, score, False
    else:
        game_should_end = True
        print(f'You opted the wrong option!! and your score is {score}')
        return A,B,score,True

print(art.logo)

players = [2]
players = random.sample(game_data.data,2)
A = players[0]
B = players[1]

while not game_should_end:
    print(f'Compare A: {A["name"]},{A["description"]}, from {A["country"]}')
    print(art.vs)
    print(f'Compare B: {B["name"]},{B["description"]}, from {B["country"]}')
    choice = str(input('Who has more followers ?? Type "A" or "B":'))
    A,B,score,game_should_end = compare_contendors(A,B,choice,score)
