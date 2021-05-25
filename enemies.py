import pygame
from activity import Activity

class Enemies(pygame.sprite.Sprite):

    def __init__(self):

        super(Enemies, self).__init__()
        
        self.GANTT = []
        self.groupGANTT = pygame.sprite.Group()

    def add(self, enemyType, bg):

        # DA OTTIMIZZARE
        if enemyType == 'activity':
            newActivity = Activity(bg)
            self.GANTT.append(newActivity)
            self.groupGANTT.add(newActivity)

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
