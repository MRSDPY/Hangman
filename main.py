import pygame
import sys
from random_word import get_word

pygame.init()

width = 1000
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game By MR.SD")

alpha_list = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z"]

coordinate = [((15, 146), (270, 310)), ((181, 312), (270, 310)), ((347, 478), (270, 310)), ((513, 644), (270, 310)),
              ((679, 810), (270, 310)), ((845, 976), (270, 310)), ((15, 146), (330, 370)), ((181, 312), (330, 370)),
              ((347, 478), (330, 370)), ((513, 644), (330, 370)), ((679, 810), (330, 370)), ((845, 976), (330, 370)),
              ((15, 146), (390, 430)), ((181, 312), (390, 430)), ((347, 478), (390, 430)), ((513, 644), (390, 430)),
              ((679, 810), (390, 430)), ((845, 976), (390, 430)), ((15, 146), (450, 490)), ((181, 312), (450, 490)),
              ((347, 478), (450, 490)), ((513, 644), (450, 490)), ((679, 810), (450, 490)), ((845, 976), (450, 490)),
              ((15, 146), (510, 550)), ((181, 312), (510, 550))]

game_over = False

word_place = {}

word_tracker = {}

word_all_poss = []

current_word = ""

guess_count = 1

last_guess = ""

mrsd = True

font_for_all = pygame.font.Font("Font/Roboto-Black.ttf", 30)


# This is all function defination part

# def draw_outline():
#     pygame.draw.line(win, (0, 0, 0), [0, 0], [width, 0], 5)
#     pygame.draw.line(win, (0, 0, 0), [width, 0], [width, height], 5)
#     pygame.draw.line(win, (0, 0, 0), [width, height], [0, height], 5)
#     pygame.draw.line(win, (0, 0, 0), [0, height], [0, 0], 5)


def select_random_word(isRestart):
    global current_word, guess_count, word_all_poss, word_tracker, word_place, last_guess, game_over

    if current_word == "" or isRestart:
        current_word = get_word().upper()
        word_all_poss = [(s, v) for s, v in enumerate(current_word)]
        guess_count = len(current_word) + 6
        word_place = {}
        word_tracker = {}
        last_guess = ""
        game_over = False
    else:
        pass


def update_guss_count(remain):
    guess_word = font_for_all.render(f"Remaining Guess : {str(remain)}", True, (0, 0, 0))
    win.blit(guess_word, [20, 100])


def disply_last_guess(value):
    last_guess = font_for_all.render(f"Last Guess : {str(value)}", True, (0, 0, 0))
    win.blit(last_guess, [400, 100])


def display_alphabets():
    gape = width // 6
    x = 0
    y = 250
    inc = 15
    end = 0
    hgape = 60
    count = 1

    for i in range(1, 26):
        if count >= 0 and count <= 6:
            pass
        elif count > 6 and count <= 12:
            hgape += 60
            end = 0
            x = 0
        elif count > 12 and count <= 18:
            hgape += 60
            end = 0
            x = 0
        elif count > 18 and count <= 24:
            hgape += 60
            end = 0
            x = 0
        elif count > 24 and count <= 26:
            hgape += 60
            end = 0
            x = 0
            for i in range(2):
                x += gape
                pygame.draw.line(win, (0, 0, 0), [end + inc, y + hgape], [x - 20, y + hgape], 6)
                pygame.draw.line(win, (0, 0, 0), [end + inc, y + hgape], [end + inc, (y + hgape) - 40], 6)
                pygame.draw.line(win, (0, 0, 0), [end + inc, (y + hgape) - 40], [x - 20, (y + hgape) - 40], 6)
                pygame.draw.line(win, (0, 0, 0), [x - 20, (y + hgape) - 40], [x - 20, y + hgape], 6)
                middle = ((((end + inc) + (x - 20)) // 2) - 8, ((((y + hgape) - 40) + (y + hgape)) // 2) - 15)
                alpha = font_for_all.render(alpha_list[count], True, (0, 0, 0))
                win.blit(alpha, [middle[0], middle[1]])
                end = x
                count += 1
            break
        else:
            pass

        for j in range(6):
            x += gape
            pygame.draw.line(win, (0, 0, 0), [end + inc, y + hgape], [x - 20, y + hgape], 6)
            pygame.draw.line(win, (0, 0, 0), [end + inc, y + hgape], [end + inc, (y + hgape) - 40], 6)
            pygame.draw.line(win, (0, 0, 0), [end + inc, (y + hgape) - 40], [x - 20, (y + hgape) - 40], 6)
            pygame.draw.line(win, (0, 0, 0), [x - 20, (y + hgape) - 40], [x - 20, y + hgape], 6)
            middle = ((((end + inc) + (x - 20)) // 2) - 8, ((((y + hgape) - 40) + (y + hgape)) // 2) - 15)
            alpha = font_for_all.render(alpha_list[count], True, (0, 0, 0))
            win.blit(alpha, [middle[0], middle[1]])
            end = x
            count += 1


def get_user_input(x, y):
    global guess_count
    count = 0
    for i in coordinate:
        count += 1
        if i[0][0] <= x <= i[0][1] and i[1][0] <= y <= i[1][1]:
            guess_count -= 1
            place_word_in_tracker(alpha_list[count])
            break


def draw_space_for_word():
    select_random_word(game_over)
    word = current_word.replace(" ", "")
    gape = width // len(word)
    x = 0
    y = 60
    inc = 15
    end = 0

    for i in range(len(word)):
        x += gape
        sy = end + inc
        ey = x - 20
        pygame.draw.line(win, (0, 0, 0), [sy, y], [ey, y], 6)
        if i in word_tracker:
            wd = font_for_all.render(word_tracker[i], True, (0, 0, 0))
            win.blit(wd, [(sy + ey) // 2, 19])
        end = x


def check_if_game_over(isWin=None):
    global win, current_word, game_status, font_for_all, height
    if guess_count == 0 or isWin:
        while True:
            if isWin:
                win.fill([0, 128, 0])
            else:
                win.fill([0, 0, 0])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_status = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True

            if isWin:
                display_wo = font_for_all.render("You are won !", True, [255, 255, 255])
                win.blit(display_wo, [(width // 2) - 200, height // 2])
            else:
                display_wo = font_for_all.render(f"Word is:-{current_word}", True, [255, 255, 255])
                win.blit(display_wo, [(width // 2) - 200, height // 2])
            restart = font_for_all.render("Please press R for restart", True, [255, 255, 255])
            win.blit(restart, [(width // 2) - 200, (height // 2) + 40])
            pygame.display.update()


def place_word_in_tracker(alpha):
    global word_tracker, current_word, last_guess, word_all_poss
    try:
        for ind, val in word_all_poss:
            if val == alpha:
                if ind in word_tracker:
                    break
                else:
                    word_tracker[ind] = val
                    word_all_poss.pop(word_all_poss.index((ind, val)))
                    break
        last_guess = alpha
        if word_all_poss == []:
            global current_word, guess_count, word_place, game_over
            current_word = get_word().upper()
            word_all_poss = [(s, v) for s, v in enumerate(current_word)]
            guess_count = len(current_word) + 6
            word_place = {}
            word_tracker = {}
            last_guess = ""
            game_over = False
    except Exception as e:
        last_guess = alpha


while mrsd:
    win.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            get_user_input(x_pos, y_pos)

    # draw_outline()
    game_over = check_if_game_over()
    draw_space_for_word()
    update_guss_count(guess_count)
    disply_last_guess(last_guess)
    display_alphabets()
    pygame.display.update()
