import pygame
import random
import math
from activity import Activity
from accollo import Accollo

class Enemies(pygame.sprite.Sprite):

    def __init__(self, bg, ui):

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
        self.accolloRarity = 0.993
        
        self.accolloList = []
        self.GANTT = []
        self.busyRow = []
        self.activitiesToAdd = []
        self.progList = ui.progList[:]
        self.progDuty = ui.progDuty[:]
        for i in range(0, bg.prog):
            self.busyRow.append(False)
        self.groupGANTT = pygame.sprite.Group()
        self.groupAccolli = pygame.sprite.Group()

        self.maxActivities = 15
        self.prog = bg.prog


    def add(self, enemyType, bg, row, activityType, score):

        if enemyType == 'activity':
            newActivity = Activity(bg, row, activityType, random.choice(self.comms), score)
            self.GANTT.append(newActivity)
            self.groupGANTT.add(newActivity)

        if enemyType == 'accollo':
            newAccollo = Accollo(bg)
            self.accolloList.append(newAccollo)
            self.groupAccolli.add(newAccollo)


    def remove(self, enemyType, element):

        if enemyType == 'activity':
            self.GANTT.remove(element)
    

    def spawnAll(self, bg, score):

        self.spawnActivity(bg, score)
        self.spawnAccollo(bg, score)

    def spawnAccollo(self, bg, score):

        if len(self.groupAccolli) < math.log10(max(score, 1)):
            if random.random() > self.accolloRarity:
                self.add('accollo', bg, 0, 0, 0)

    def spawnActivity(self, bg, score):

        if not ((bg.steps % 7 == 5) or (bg.steps % 7 == 6)):
            
            for row in self.activitiesToAdd:
                activityType = self.progDuty[row]
                self.add('activity', bg, row, activityType, score)

            self.activitiesToAdd.clear()

        for row in range(0, self.prog):
            if not self.busyRow[row]:
                if random.random() > self.activityRarity:

                    self.busyRow[row] = True
                    if(bg.steps % 7 == 5) or (bg.steps % 7 == 6):
                        self.activitiesToAdd.append(row)
                    else:
                        activityType = self.progDuty[row]
                        self.add('activity', bg, row, activityType, score)


    def updateAll(self, frame, player, tick):

        self.updateGANTT(frame, player)
        self.updateAccolli(tick, player)


    def updateAccolli(self, tick, player):

        accToRemove = []
        for accollo in self.accolloList:
            whatToDo = accollo.update(tick, player)
            if whatToDo == 0:
                accToRemove.append(accollo)
            elif whatToDo == 2:
                if accollo in self.groupAccolli:
                    accollo.kill()

        for accollo in accToRemove:
            self.accolloList.remove(accollo)
            

    def updateGANTT(self, frame, player):

        actToRemove = []
        for activity in self.GANTT:
            whatToDo = activity.update(frame)
            if whatToDo == 1:
                self.busyRow[activity.row] = False
            elif whatToDo == 2:
                neatScore = activity.maxHP - activity.HP
                player.score += neatScore
                player.cash += neatScore
                player.cazziatoni += activity.maxHP - neatScore
                actToRemove.append(activity)

        for activity in actToRemove:
            self.GANTT.remove(activity)
            activity.kill()
