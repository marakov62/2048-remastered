#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import time
from alpha import *

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()

    def initUI(self):
        p = self.palette();
        p.setColor(QPalette.ButtonText,QColor(125,125,125))
        p.setColor(QPalette.WindowText,QColor(243, 136, 8))
        self.setPalette(p)

class RenderArea(QWidget):
    def __init__(self, parent=None):
        super(RenderArea,self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        pass

    def paintEvent(self,event):
        painter=QPainter(self)     

        for i in range (4):
            for j in range (4):
                image=QImage()
                #sélectionne dans le dossier Image, l'image correspondant au nombre dans le tableau.
                image.load("Image/%d.png"%jeu.Tab[i][j])
                painter.drawImage((self.width()/2)-200+j*100,(self.height()/2)-200+i*100,image)

        for i in range (4):
            for j in range (4):
                #sélectionne dans le dossier Image, image 1 represante une case noir
                if jeu.Tab2[i][j]==1:
                    image=QImage()
                    image.load("Image/%d.png"%jeu.Tab2[i][j])
                    painter.drawImage((self.width()/2)-200+j*100,(self.height()/2)-200+i*100,image)
                

class Window4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def closeEvent(self,event):
        QCoreApplication.instance().quit()

    def initUI(self):

        # création de la fenêtre du menu
        self.setFixedSize(1000,600)
        
        # affiche une image en arrière plan
        self.setStyleSheet("background-image: url(image2.jpg)")

        self.setRenderArea()
        self.setCenter()
        self.show()


    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setRenderArea(self):
        self.renderArea = RenderArea()
        self.setCentralWidget(self.renderArea)


    def keyPressEvent(self,event):
        
        #regarde si le 2048 est dans un état de victoire ou de défaite
        if (jeu.win2(jeu.Tab)==False) and (jeu.lose(jeu.Tab)==False) :

            #regarde si la touche pressé est bien la flèche gauche et si ce coup est possible
            if event.key()==Qt.Key_Left and (jeu.check(jeu.Tab,"Left")) :
                #Déplacement du 2048 vers la gauche
                jeu.left(jeu.Tab)

                #x est une variable qui, à une certaine valeur, permet changer les emplacements des cases cachées
                jeu.x=jeu.x+1

                #Si le 2048 n'est pas plein , il s'implemente
                if jeu.Plein(jeu.Tab)!=True :
                    jeu.implemante(jeu.Tab)
                    
            if (event.key()==Qt.Key_Up) and (jeu.check(jeu.Tab,"Up")) :
                jeu.up(jeu.Tab)
                jeu.x=jeu.x+1

                if jeu.Plein(jeu.Tab)!=True :
                    jeu.implemante(jeu.Tab)              

            if event.key()==Qt.Key_Right and (jeu.check(jeu.Tab,"Right")) :
                jeu.right(jeu.Tab)
                jeu.x=jeu.x+1

                if jeu.Plein(jeu.Tab)!=True :
                    jeu.implemante(jeu.Tab)
                    
            if event.key()==Qt.Key_Down and (jeu.check(jeu.Tab,"Down")) :
                jeu.down(jeu.Tab)
                jeu.x=jeu.x+1

                if jeu.Plein(jeu.Tab)!=True :
                    jeu.implemante(jeu.Tab)

            #chaque fois que 25 coups ont été joués, change les emplacements des cases cachées
            if jeu.x%25==0 :
                jeu.Tab2=jeu.generateBlind()
                jeu.x=jeu.x+1
            
            self.update()

            if jeu.win2(jeu.Tab)==True :
                self.victoireLabel()

            if jeu.lose(jeu.Tab)==True :
                self.defaiteLabel()

    def victoireLabel(self):
        dialog = QMessageBox(self)
        dialog.setText("VICTOIRE !!!")
        dialog.setIcon(QMessageBox.Question)
        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialog.setDefaultButton(QMessageBox.Ok)
        buttonY = dialog.button(QtGui.QMessageBox.Ok)
        buttonY.setText('Recommencer')
        buttonN = dialog.button(QtGui.QMessageBox.Cancel)
        buttonN.setText('Comtempler ma partie')
        if dialog.exec_()==QMessageBox.Ok:
            jeu.Tab=jeu.generate()

    def defaiteLabel(self):
        dialog = QMessageBox(self)
        dialog.setText("Pas très bon hein...")
        dialog.setIcon(QMessageBox.Question)
        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialog.setDefaultButton(QMessageBox.Ok)
        buttonY = dialog.button(QMessageBox.Ok)
        buttonY.setText('Recommencer')
        buttonN = dialog.button(QMessageBox.Cancel)
        buttonN.setText('Comtempler ma partie')
        if dialog.exec_()==QMessageBox.Ok:
            jeu.Tab=jeu.generate()
            
jeu=fonction()
