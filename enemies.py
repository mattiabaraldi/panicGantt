import pygame
import random
import math
from activity import Activity

class Enemies(pygame.sprite.Sprite):

    def __init__(self, bg):

        super(Enemies, self).__init__()

        # load comm file
        self.comms = ["20151 KLIMAOPREMA, PK-VS 0316-VIS 2"]
        try:
            with open("comm.txt", "r") as f:
                for line in f.readlines():
                    self.comms.append(line.removesuffix("\n"))
        except:
            pass

        self.activityRarity = 0.998
        
        self.GANTT = []
        self.busyRow = []
        self.activitiesToAdd = []
        for i in range(0, bg.prog):
            self.busyRow.append(False)
        self.groupGANTT = pygame.sprite.Group()

        self.maxActivities = 15
        self.maxRows = min(15, bg.prog)

    def add(self, enemyType, bg, row, frame, score):

        # DA OTTIMIZZARE
        if enemyType == 'activity':
            newActivity = Activity(bg, row, frame, random.choice(self.comms), score)
            self.GANTT.append(newActivity)
            self.groupGANTT.add(newActivity)

    def remove(self, enemyType, element):

        # DA OTTIMIZZARE
        if enemyType == 'activity':
            self.GANTT.remove(element)

    def updateAll(self, frame, player):

        self.updateGANTT(frame, player)
    
    def spawnAll(self, bg, score):

        self.spawnActivity(bg, score)

    def spawnActivity(self, bg, score):

        if not ((bg.steps % 7 == 5) or (bg.steps % 7 == 6)):
            
            for row in self.activitiesToAdd:
                actPerType = self.maxRows / 3
                activityType = math.floor(row / actPerType)
                self.add('activity', bg, row, activityType, score)

            self.activitiesToAdd.clear()

        for row in range(0, self.maxRows):
            if not self.busyRow[row]:
                if random.random() > self.activityRarity:

                    self.busyRow[row] = True
                    if(bg.steps % 7 == 5) or (bg.steps % 7 == 6):
                        self.activitiesToAdd.append(row)
                    else:
                        actPerType = self.maxRows / 3
                        activityType = math.floor(row / actPerType)
                        self.add('activity', bg, row, activityType, score)

    
    def updateGANTT(self, frame, player):

        actToRemove = []
        for activity in self.GANTT:
            whatToDo = activity.update(frame)
            if whatToDo == 1:
                self.busyRow[activity.row] = False
            elif whatToDo == 2:
                neatScore = activity.maxHP - activity.HP
                player.score += neatScore
                player.cazziatoni += activity.maxHP - neatScore
                actToRemove.append(activity)

        for activity in actToRemove:
            self.GANTT.remove(activity)
