import pygame, sys

blue = (55, 75, 155)

pygame.init()
pygame.display.set_caption('pygame - using sound effect')
size = [460, 100]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# load sound file
#pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.init()

pygame.mixer.music.set_volume(0.5)
sound = pygame.mixer.Sound("bird.ogg")
#snd_array = pygame.sndarray.array(sound)
#snd_out = pygame.sndarray.make_sound(snd_array)
#   snd_out.play()

mychannel = pygame.mixer.find_channel()
while pygame.mixer.find_channel is None:
    print (pygame.mixer.find_channel)
allchannels = pygame.mixer.get_num_channels()
print ('all channels - ', allchannels)
print ('duration -', sound.get_length(), ' seconds')
print ('press 1 - play sound')
print ('press 2 - play sound in a loop')
print ('press 3 - play sound with 9 seconds fade-in effect')
print ('press 4 - play sound just for 9 seconds')
print ('press 5 - play sound 3 more times')
print ('press 9 - stop playing with fadeout effect set 9 ')
print ('press 0 - stop playing instantly')
print ('press up arrow key - up volume')
print ('press down arrow key - down volume')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                sound.play()
            if event.key == pygame.K_2:
                sound.play(-1)
            if event.key == pygame.K_3:
                sound.play(-1, fade_ms=9000)
            if event.key == pygame.K_4:
                sound.play(-1, 9000)
            if event.key == pygame.K_5:
                sound.play(3)
            if event.key == pygame.K_9:
                sound.fadeout(9000)
            if event.key == pygame.K_0:
                sound.stop()
            if event.key == pygame.K_UP:
                sound.set_volume(sound.get_volume() + 0.1)
                print(sound.get_volume())
            if event.key == pygame.K_DOWN:
                sound.set_volume(sound.get_volume() - 0.1)
                print(sound.get_volume())
    screen.fill(blue)
    pygame.display.update()
    clock.tick(10)