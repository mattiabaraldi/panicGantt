import pygame
from activity import Activity

class Enemies(pygame.sprite.Sprite):

    def __init__(self):

        super(Enemies, self).__init__()
        
        self.GANTT = []

    def add(self, enemyType, bg):

        # DA OTTIMIZZARE
        if enemyType == 'activity':
            self.GANTT.append(Activity(bg))

    def remove(self, element):

        # DA OTTIMIZZARE
        self.GANTT.remove(element)

    def updateAll(self, frame):

        self.updateGANTT(frame)
    
    def updateGANTT(self, frame):

        actToRemove = []
        for activity in self.GANTT:
            if activity.update(frame):
                actToRemove.append(activity)

        for activity in actToRemove:
            self.GANTT.remove(activity)
