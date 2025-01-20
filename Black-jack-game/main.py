import random
from art import logo


def sum_score_card(cards_list):
    total_score = 0
    for k in range(len(cards_list)):
        total_score += cards_list[k]

    if total_score == 21 and len(cards_list) == 2:
        return 0
    else:
        return total_score

def check_black_jack(card_list):
    score_card = sum_score_card(card_list)
    if score_card == 21:
        return True
    else:
        return False

def check_score(u_score, c_score):
    if u_score == c_score :
        return "Draw 🙃"
    elif u_score == 0:
        return "You win with a Blackjack 😎"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"

    elif u_score > 21:
        return "You lose 😤"
    elif c_score > 21:
        return "You win 😁"

    elif u_score > c_score:
        return "You win 😃"
    elif u_score < c_score:
        return "You lose 😤"

    else:
        pass

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(f"Welcome to Black Jack game!!!")
start_game = "y"
print(logo)
#play_game = input("Do you want to play Black Jack? Type 'y' or 'n': ")

while input("Do you want to play Black Jack? Type 'y' or 'n': ")== "y":
    #user_card = []
    user_card = random.sample(cards,2)
    score_user_card = sum_score_card(user_card)

    com_card = random.sample(cards,2)
    score_com_card = sum_score_card(com_card)


    is_game_over = False
    while not is_game_over:
        print(f"Your card: {user_card}, current score: {score_user_card}")

        if score_user_card == 0 or score_com_card == 0 or score_user_card > 21:
            #play_game = "n"
            is_game_over = True

        else:
            draw_card = input("Type 'y' to get another card,type 'n' to pass: ")

            if draw_card == "y":
                new_card = random.sample(cards,1)
                user_card.append(new_card[0])
                score_user_card = sum_score_card(user_card)
                #print(f"Your card: {user_card}, current score: {score_user_card}")
                is_game_over = False
                #print(is_game_over)
            else:
                is_game_over = True
                #print(is_game_over)


    while score_com_card != 0 and score_com_card < 17:
        draw_com = random.sample(cards, 1)
        com_card.append(draw_com[0])
        score_com_card = sum_score_card(com_card)
        #print(f"com card : {com_card}, score: {score_com_card}")

    print(f"Your final card: {user_card}, final score: {score_user_card}")
    print(f"Computer's final hand: {com_card}, final score: {score_com_card}")
    print(check_score(score_user_card, score_com_card))

    #play_game = input("Do you want to play Black Jack? Type 'y' or 'n': ")