import pygame
import random
from activity import Activity

class Enemies(pygame.sprite.Sprite):

    def __init__(self, bg):

        super(Enemies, self).__init__()

        self.activityRarity = 0.995
        
        self.GANTT = []
        self.busyRow = []
        self.activitiesToAdd = []
        for i in range(0, bg.prog):
            self.busyRow.append(False)
        self.groupGANTT = pygame.sprite.Group()

    def add(self, enemyType, bg, row, frame):

        # DA OTTIMIZZARE
        if enemyType == 'activity':
            newActivity = Activity(bg, row, frame)
            self.GANTT.append(newActivity)
            self.groupGANTT.add(newActivity)

    def remove(self, enemyType, element):

        # DA OTTIMIZZARE
        if enemyType == 'activity':
            self.GANTT.remove(element)

    def updateAll(self, frame):

        self.updateGANTT(frame)
    
    def spawnAll(self, bg, frame):

        self.spawnActivity(bg, bg.steps)

    def spawnActivity(self, bg, frame):

        if not ((frame % 7 == 5) or (frame % 7 == 6)):
            
            for row in self.activitiesToAdd:
                self.add('activity', bg, row, frame)

            self.activitiesToAdd.clear()

        for row in range(0, bg.prog):
            if not self.busyRow[row]:
                if random.random() > self.activityRarity:

                    self.busyRow[row] = True
                    if(frame % 7 == 5) or (frame % 7 == 6):
                        self.activitiesToAdd.append(row)
                    else:
                        self.add('activity', bg, row, frame)

    
    def updateGANTT(self, frame):

        actToRemove = []
        for activity in self.GANTT:
            whatToDo = activity.update(frame)
            if whatToDo == 1:
                self.busyRow[activity.row] = False
            elif whatToDo == 2:
                actToRemove.append(activity)

        for activity in actToRemove:
            self.GANTT.remove(activity)
