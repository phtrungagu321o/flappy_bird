import pygame
from random import randint
# khởi tạo
pygame.init()
# set màn hình
screen = pygame.display.set_mode((400,600))
# đặt tiêu đề
clock=pygame.time.Clock()
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
x_bird=50
y_bird=350
tube1_x=400
tube2_x=600
tube3_x=800
tube_width=50
tube1_height=randint(100,400)
tube2_height=randint(100,400)
tube3_height=randint(100,400)

# khoảng cách 2 tupe đối điện nhau
d_2tupe=150
# vận tốc rơi
bird_drop_velocity=0
# trọng lực
gravity=0.5
# thể hiện khaongr cách giữa cách ống
tube_velocity=2
#điểm
score=0
font=pygame.font.SysFont('san',20)
# game over
fontover=pygame.font.SysFont('san',40)
# load san
san_img=pygame.image.load('images/sand.png')
san_img=pygame.transform.scale(san_img,(400,30))
# load background

background_img=pygame.image.load('images/background.png')
background_img=pygame.transform.scale(background_img ,(400,600))
# load sound
sound=pygame.mixer.Sound('no6.wav')
# load con chim
bird_img=pygame.image.load('images/bird.png')
# chuyển con về về định dạng cho sẵn
bird_img=pygame.transform.scale(bird_img,(35,35))
# load ống
tupe_img=pygame.image.load('images/tube.png')
# load ống đối diẹn
tube_op_img=pygame.image.load('images/tube_op.png')
#check ống đi qua con chim chưa
tube1_pass=False
tube2_pass=False
tube3_pass=False
pausing=False

running=True
while running:
    pygame.mixer.Sound.play(sound)
    clock.tick(60)
    screen.fill(WHITE)
    # chèn background_img
    screen.blit(background_img,(0,0))
    # vẽ san_img
    sand = screen.blit(san_img, (0, 570))
    sandOn = screen.blit(san_img,(0,50))
    # ép ảnh ống và vẽ ống
    tube1_img=pygame.transform.scale(tupe_img,(tube_width,tube1_height))
    tube1=screen.blit(tube1_img,(tube1_x,0))
    tube2_img = pygame.transform.scale(tupe_img, (tube_width, tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x, 0))
    tube3_img = pygame.transform.scale(tupe_img, (tube_width, tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x, 0))
    #ống đối diện
    tupe1_op_img=pygame.transform.scale(tube_op_img,(tube_width,600-(tube1_height+d_2tupe)))
    tube1_op=screen.blit(tupe1_op_img,(tube1_x,tube1_height+d_2tupe))
    tupe2_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600 - (tube2_height + d_2tupe)))
    tube2_op = screen.blit(tupe1_op_img, (tube2_x, tube2_height + d_2tupe))
    tupe3_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600 - (tube3_height + d_2tupe)))
    tube3_op = screen.blit(tupe1_op_img, (tube3_x, tube3_height + d_2tupe))
    # ống di chuyển sang trái
    tube1_x -= tube_velocity
    tube2_x -= tube_velocity
    tube3_x -= tube_velocity
    # tạo ống mới
    if tube1_x < -tube_width:
        tube1_x=550
        tube1_height=randint(100,400)
        tube1_pass=False
    if tube2_x < -tube_width:
        tube2_x=550
        tube2_height=randint(100,400)
        tube2_pass = False
    if tube3_x < -tube_width:
        tube3_x=550
        tube3_height=randint(100,400)
        tube2_pass = False


    # chèn con chim
    bird=screen.blit(bird_img,(x_bird,y_bird))
    #chim rơi
    y_bird+=bird_drop_velocity
    bird_drop_velocity+=gravity
    #ghi điểm
    score_txt=font.render("Score: "+str(score),True,RED)
    screen.blit(score_txt,(5,5))
    #công điểm
    if tube1_x+tube_width<=x_bird and tube1_pass==False:
        score+=1
        tube1_pass=True
    if tube2_x+tube_width<=x_bird and tube2_pass==False:
        score+=1
        tube2_pass=True
    if tube3_x+tube_width<=x_bird and tube3_pass==False:
        score+=1
        tube3_pass=True
    # kiểm tra sự va chạm
    tubes=[tube1,tube2,tube3,tube1_op,tube2_op,tube3_op,sand,sandOn]
    for tube in tubes:
        if bird.colliderect(tube):
            pygame.mixer.pause()
            tube_velocity=0
            bird_drop_velocity=0
            game_over_txt=fontover.render("Game over, Score: "+str(score),True,RED)
            screen.blit(game_over_txt,(85,260))
            space_txt = font.render("Press space to continue!", True, BLUE)
            screen.blit(space_txt, (120, 290))
            pausing=True

    for event in pygame.event.get():
        # tắt nút QUIT
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_drop_velocity=0
                bird_drop_velocity-=7
                if pausing:
                    pygame.mixer.unpause()
                    x_bird = 50
                    y_bird = 350
                    tube1_x = 400
                    tube2_x = 600
                    tube3_x = 800
                    tube_velocity=2
                    score=0
                    pausing=False


        # tất cả những gi vẽ trên màn hình hiển thi
    pygame.display.flip()
# sau khi chạy xong sẽ xóa hết dữ liệu
pygame.quit()
