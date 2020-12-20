import pygame
pygame.init()
import math
import time

def primes(upto):
    primes=[2] # apparently 2 is a prime too, so we begin there
    for num in range(3,upto+1,2):
        isprime=True
        for factor in range(3,1+int(math.sqrt(num)),2):
             if not num % factor: isprime=False; break
        if isprime: primes.append(num)
    return primes

if __name__ == '__main__':
    running = True
    width = 1800
    rectnum = 20
    margin = 5
    rectwidth = ((width-margin)/rectnum)-margin
    screen = pygame.display.set_mode([1800, round(rectwidth + 2* margin)])
    colors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple' ]
    color = 0
    numprime = 10000
    primelist = primes(numprime)
    state = {}
    for i in range(numprime):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for rect in range(rectnum):
            pygame.draw.rect(screen, '#FFFFFF', (margin+rect*(rectwidth+0.5*margin), margin, rectwidth-margin, rectwidth-margin) )
        if i in primelist:
            color += 1
            if color == colors.__len__():
                color = 0
            print("{0:b}".format(i))
            for pos in range("{0:b}".format(i).__len__()):
                if "{0:b}".format(i)[pos] == '1':
                    state[pos] = colors[color]
        for i in range(rectnum):
            try:
                pygame.draw.circle(screen, state[i], (margin + 0.5 * rectwidth + (i)*(rectwidth+0.5*margin), margin+0.5*rectwidth), rectwidth*0.3)
            except Exception:
                pass
        time.sleep(0.3)
        pygame.display.flip()