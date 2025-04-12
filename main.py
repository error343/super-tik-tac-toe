import pygame

pygame.init()

# OX KA CORD 
borad = [[ "" for _ in range(9)] for _ in range(9)]
big_borad = [[ "" for _ in range(3)] for _ in range(3)]

image_size = 88
a = 90 * 9
dis = pygame.display.set_mode((a, a))
blue = (0, 0, 255)
black = (0, 0, 0)
blackss = (100, 100, 100)
white = (255, 255, 255)
game_quit = False
o = pygame.image.load('o.png')
x = pygame.image.load('x.png')
new_o = pygame.transform.scale(o ,(image_size, image_size))
new_x = pygame.transform.scale(x, (image_size, image_size))
new_oo = pygame.transform.scale(o ,(810, 810))
new_xx = pygame.transform.scale(x, (810, 810))
big_o = pygame.transform.scale(o, (268, 268))
big_x = pygame.transform.scale(x, (268, 268))
pop_audio = pygame.mixer.Sound('pop.mp3')
game= 0
x_cord = -657
y_cord = -433
first_attempt = False
alright = False
allright = False
ek_do_tin = [0, 3, 6]
o_wins = False
x_wins = False
x = 0
respons_list = [( 0 , 0 ), ( 1 , 0 ), ( 2 , 0 ), ( 0 , 1 ), ( 1 , 1 ), ( 2 , 1 ), ( 0 , 2 ), ( 1 , 2 ), ( 2 , 2 ),
                ( 3 , 0 ), ( 4 , 0 ), ( 5 , 0 ), ( 3 , 1 ), ( 4 , 1 ), ( 5 , 1 ), ( 3 , 2 ), ( 4 , 2 ), ( 5 , 2 ),
                ( 6 , 0 ), ( 7 , 0 ), ( 8 , 0 ), ( 6 , 1 ), ( 7 , 1 ), ( 8 , 1 ), ( 6 , 2 ), ( 7 , 2 ), ( 8 , 2 ),
                ( 0 , 3 ), ( 1 , 3 ), ( 2 , 3 ), ( 0 , 4 ), ( 1 , 4 ), ( 2 , 4 ), ( 0 , 5 ), ( 1 , 5 ), ( 2 , 5 ),
                ( 3 , 3 ), ( 4 , 3 ), ( 5 , 3 ), ( 3 , 4 ), ( 4 , 4 ), ( 5 , 4 ), ( 3 , 5 ), ( 4 , 5 ), ( 5 , 5 ),
                ( 6 , 3 ), ( 7 , 3 ), ( 8 , 3 ), ( 6 , 4 ), ( 7 , 4 ), ( 8 , 4 ), ( 6 , 5 ), ( 7 , 5 ), ( 8 , 5 ),
                ( 0 , 6 ), ( 1 , 6 ), ( 2 , 6 ), ( 0 , 7 ), ( 1 , 7 ), ( 2 , 7 ), ( 0 , 8 ), ( 1 , 8 ), ( 2 , 8 ),
                ( 3 , 6 ), ( 4 , 6 ), ( 5 , 6 ), ( 3 , 7 ), ( 4 , 7 ), ( 5 , 7 ), ( 3 , 8 ), ( 4 , 8 ), ( 5 , 8 ),
                ( 6 , 6 ), ( 7 , 6 ), ( 8 , 6 ), ( 6 , 7 ), ( 7 , 7 ), ( 8 , 7 ), ( 6 , 8 ), ( 7 , 8 ), ( 8 , 8 )]

#LIST of the suitable POISTION 
A1 = [( 0 , 0 ), ( 3 , 0 ), ( 6 , 0 ), ( 0 , 3 ), ( 3 , 3 ), ( 6 , 3 ), ( 0 , 6 ), ( 3 , 6 ), ( 6 , 6 ),]
A2 = [( 1 , 0 ), ( 4 , 0 ), ( 7 , 0 ), ( 1 , 3 ), ( 4 , 3 ), ( 7 , 3 ), ( 1 , 6 ), ( 4 , 6 ), ( 7 , 6 ),]
A3 = [( 2 , 0 ), ( 5 , 0 ), ( 8 , 0 ), ( 2 , 3 ), ( 5 , 3 ), ( 8 , 3 ), ( 2 , 6 ), ( 5 , 6 ), ( 8 , 6 ),]
A4 = [( 0 , 1 ), ( 3 , 1 ), ( 6 , 1 ), ( 0 , 4 ), ( 3 , 4 ), ( 6 , 4 ), ( 0 , 7 ), ( 3 , 7 ), ( 6 , 7 ),]
A5 = [( 1 , 1 ), ( 4 , 1 ), ( 7 , 1 ), ( 1 , 4 ), ( 4 , 4 ), ( 7 , 4 ), ( 1 , 7 ), ( 4 , 7 ), ( 7 , 7 ),]
A6 = [( 2 , 1 ), ( 5 , 1 ), ( 8 , 1 ), ( 2 , 4 ), ( 5 , 4 ), ( 8 , 4 ), ( 2 , 7 ), ( 5 , 7 ), ( 8 , 7 ),]
A7 = [( 0 , 2 ), ( 3 , 2 ), ( 6 , 2 ), ( 0 , 5 ), ( 3 , 5 ), ( 6 , 5 ), ( 0 , 8 ), ( 3 , 8 ), ( 6 , 8 ),]
A8 = [( 1 , 2 ), ( 4 , 2 ), ( 7 , 2 ), ( 1 , 5 ), ( 4 , 5 ), ( 7 , 5 ), ( 1 , 8 ), ( 4 , 8 ), ( 7 , 8 ),]
A9 = [( 2 , 2 ), ( 5 , 2 ), ( 8 , 2 ), ( 2 , 5 ), ( 5 , 5 ), ( 8 , 5 ), ( 2 , 8 ), ( 5 , 8 ), ( 8 , 8 ),]

AA = [A1, A2, A3, A4, A5, A6, A7, A8, A9]

#LIST FOR THE SUITABLE POISTION
b1 = [( 0 , 0 ), ( 1 , 0 ), ( 2 , 0 ), ( 0 , 1 ), ( 1 , 1 ), ( 2 , 1 ), ( 0 , 2 ), ( 1 , 2 ), ( 2 , 2 )]
b2 = [( 3 , 0 ), ( 4 , 0 ), ( 5 , 0 ), ( 3 , 1 ), ( 4 , 1 ), ( 5 , 1 ), ( 3 , 2 ), ( 4 , 2 ), ( 5 , 2 )]
b3 = [( 6 , 0 ), ( 7 , 0 ), ( 8 , 0 ), ( 6 , 1 ), ( 7 , 1 ), ( 8 , 1 ), ( 6 , 2 ), ( 7 , 2 ), ( 8 , 2 )]
b4 = [( 0 , 3 ), ( 1 , 3 ), ( 2 , 3 ), ( 0 , 4 ), ( 1 , 4 ), ( 2 , 4 ), ( 0 , 5 ), ( 1 , 5 ), ( 2 , 5 )]
b5 = [( 3 , 3 ), ( 4 , 3 ), ( 5 , 3 ), ( 3 , 4 ), ( 4 , 4 ), ( 5 , 4 ), ( 3 , 5 ), ( 4 , 5 ), ( 5 , 5 )]
b6 = [( 6 , 3 ), ( 7 , 3 ), ( 8 , 3 ), ( 6 , 4 ), ( 7 , 4 ), ( 8 , 4 ), ( 6 , 5 ), ( 7 , 5 ), ( 8 , 5 )]
b7 = [( 0 , 6 ), ( 1 , 6 ), ( 2 , 6 ), ( 0 , 7 ), ( 1 , 7 ), ( 2 , 7 ), ( 0 , 8 ), ( 1 , 8 ), ( 2 , 8 )]
b8 = [( 3 , 6 ), ( 4 , 6 ), ( 5 , 6 ), ( 3 , 7 ), ( 4 , 7 ), ( 5 , 7 ), ( 3 , 8 ), ( 4 , 8 ), ( 5 , 8 )]
b9 = [( 6 , 6 ), ( 7 , 6 ), ( 8 , 6 ), ( 6 , 7 ), ( 7 , 7 ), ( 8 , 7 ), ( 6 , 8 ), ( 7 , 8 ), ( 8 , 8 )]

BB = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

#FUNCTIONS OF THE GAME
def draw_grid():
    for a in range(17):
        pygame.draw.line(dis, blackss,(a* 90 -1, 0-1), (a*90 -1, 810-1), 2)
        pygame.draw.line(dis, blackss,(0-1, a* 90-1), (810-1, a*90 -1), 2)    

    for a in range(3):
        pygame.draw.line(dis, white ,( a * 270 -1, 0 -1), (a * 270 -1 , 810-1), 2)
        pygame.draw.line(dis, white ,(0-1 , a * 270-1), (810-1 , a * 270-1), 2)

#   EK ALAG FUNCTION IMAGE K LIYE
def draw_ox():
    for i in range(9):
        for k in range(9):
            if borad[i][k] == "o":
                dis.blit(new_o ,(k * 90 + 1, i * 90 + 1))

            elif borad[i][k] == "x":
                dis.blit(new_x ,(k * 90 + 1, i * 90 + 1) )

#BIG OX K LIYR FUNCTION
def draw_big_ox():
    global big_borad, big_o, big_x
    for i in range(3):
        for k in range(3):
            if big_borad[i][k] == "o":
                dis.blit(big_o , (k * 270 + 1, i * 270 + 1))
            
            elif big_borad[i][k] == "x":
                dis.blit(big_x , (k * 270 + 1, i * 270 + 1))

# GIVENING NEXT BOX FUNCTION
def rules(x_cord, y_cord):
    global respons_list, first_attempt, alright, allright
    

    if first_attempt:
        if (x_cord, y_cord) in respons_list or allright:
            alright = True

        else:
            alright = False
    
            
    else :
        alright = True            

    if alright:
        for i in range(9):
            for k in range(9):
                if AA[i][k] == (x_cord , y_cord):
                    respons_list = BB[i]
                    # print(BB[i])

def printing_staites():
    global respons_list, first_attempt, alright

    if alright == True :
        print('sab thik hai bhai!')
    elif alright == False:
        print('chutiya hai kiya bhai!')        

def point():
    global borad, ek_do_tin, big_borad 
    # for | point
    for i in ek_do_tin:
        for k in range(9):
            if borad[i][k] == borad[i + 1][k] == borad[i +2][k] == 'o':
                borad[i][k] = 'a' 
                borad[i + 1][k] = 'a' 
                borad[i + 2][k] = 'a'
                if big_borad[ek_do_tin.index(i)][k//3] == '':
                    big_borad[ek_do_tin.index(i)][k//3] = 'o'
            elif borad[i][k] == borad[i + 1][k] == borad[i +2][k] == 'x':
                borad[i][k] = 'b' 
                borad[i + 1][k] = 'b' 
                borad[i +2][k] = 'b'
                if big_borad[ek_do_tin.index(i)][k//3] == '':
                    big_borad[ek_do_tin.index(i)][k//3] = 'x'
                
    # for - point
    for k in range(9):
        for i in ek_do_tin:
            if borad[k][i] == borad[k][i + 1] == borad[k][i + 2] == 'o':
                borad[k][i] = 'a' 
                borad[k][i + 1] = 'a'
                borad[k][i + 2] = 'a'
                if big_borad[k//3][ek_do_tin.index(i)] == '':
                    big_borad[k//3][ek_do_tin.index(i)] = 'o'
            elif borad[k][i] == borad[k][i + 1] == borad[k][i + 2] == 'x':
                borad[k][i] = 'b' 
                borad[k][i + 1] = 'b'
                borad[k][i + 2] = 'b'
                if big_borad[k//3][ek_do_tin.index(i)] == '':
                    big_borad[k//3][ek_do_tin.index(i)] = 'x'


    # for \ point
    for k in ek_do_tin:
        for i in ek_do_tin:
            if borad[i][k] == borad[i + 1][k + 1] == borad[i +2][k+ 2] == 'o':
                borad[i][k] = 'a' 
                borad[i + 1][k + 1] = 'a'
                borad[i +2][k+ 2] = 'a'
                if big_borad[ek_do_tin.index(i)][k//3] == '':
                    big_borad[ek_do_tin.index(i)][k//3] = 'o'        
            elif borad[i][k] == borad[i + 1][k + 1] == borad[i +2][k+ 2] == 'x':
                borad[i][k] = 'b' 
                borad[i + 1][k + 1] = 'b'
                borad[i +2][k+ 2] = 'b'
                if big_borad[ek_do_tin.index(i)][k//3] == '':
                    big_borad[ek_do_tin.index(i)][k//3] = 'x'        

    # for / point
    for k in ek_do_tin:
        for i in ek_do_tin:
            if borad[i+2][k] == borad[i + 1][k + 1] == borad[i][k+2] == 'o':
                borad[i][k + 2] = 'a' 
                borad[i + 1][k + 1] = 'a'
                borad[i +2][k] = 'a'
                if big_borad[ek_do_tin.index(i)][k//3] == '':
                    big_borad[ek_do_tin.index(i)][k//3] = 'o'        
            elif borad[i+2][k] == borad[i + 1][k + 1] == borad[i][k+2] == 'x':
                borad[i][k + 2] = 'b' 
                borad[i + 1][k + 1] = 'b'
                borad[i +2][k] = 'b'
                if big_borad[ek_do_tin.index(i)][k//3] == '':
                    big_borad[ek_do_tin.index(i)][k//3] = 'x'        

def checking_first_attempt():
    global first_attempt, respons_list, allright, xyz, x
    if first_attempt:
        for i in range(9):
            if borad[respons_list[i][1]][respons_list[i][0]] == 'a':
                allright = True
                
            elif borad[respons_list[i][1]][respons_list[i][0]] == 'b':
                allright = True


    if first_attempt:
        for i in range(9):
            if borad[respons_list[i][1]][respons_list[i][0]] != '':
                x += 1
                    
        if x == 9:
            allright = True

def big_point():
    global big_borad, o_wins, x_wins
    for i in range(3):
        for k in range(1):
            if big_borad[i][k] == big_borad[i][k+ 1] == big_borad[i][k+ 2] == 'o':
                o_wins = True
                print('o wins !')
            elif big_borad[i][k] == big_borad[i][k+ 1] == big_borad[i][k+ 2] == 'x':
                x_wins = True
                print('x wins !') 
    for i in range(1):
        for k in range(3):
            if big_borad[i][k] == big_borad[i+ 1][k] == big_borad[i + 2][k] == 'o':
                o_wins = True
                print('o wins !')
            elif big_borad[i][k] == big_borad[i+ 1][k] == big_borad[i + 2][k] == 'x':
                x_wins = True
                print('x wins !')
    for i in range(1):
        for k in range(1):
            if big_borad[i][k] == big_borad[i+ 1][k+ 1] == big_borad[i + 2][k+ 2] == 'o':
                o_wins = True
                print('o wins !')
            elif big_borad[i][k] == big_borad[i+ 1][k+ 1] == big_borad[i + 2][k+ 2] == 'x':
                x_wins = True
                print('x wins !')
    for i in range(3):
        for k in range(3):
            if big_borad[i - 2][k - 2] == big_borad[i - 1][k  - 1] == big_borad[i][k] == 'o':
                o_wins = True
                print('o wins !')
            elif big_borad[i - 2][k - 2] == big_borad[i - 1][k - 1] == big_borad[i][k] == 'x':
                x_wins = True
                print('x wins !')
 
while not game_quit:

    dis.fill(black)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_cord = event.pos[0] // 90
            y_cord = event.pos[1] // 90
            # print("(",x_cord,",", y_cord,"),")
            checking_first_attempt()
            rules(x_cord, y_cord)
            if alright:
                if borad[y_cord][x_cord] == "":
                    if game % 2 == 0:
                        borad[y_cord][x_cord] = 'o'
                        pop_audio.play()
                        game += 1
                        
                    else:
                        borad[y_cord][x_cord] = 'x'    
                        pop_audio.play()
                        game += 1
            printing_staites()
            point()
            big_point()
            first_attempt = True
            allright = False
            alright = False
            x = 0
    draw_ox()
    draw_big_ox()        
    if o_wins:
        dis.blit(new_oo, (0, 0 ,810, 810))
    if x_wins:
        dis.blit(new_xx, (0, 0 ,810, 810))

    pygame.display.update()

pygame.quit()
quit()