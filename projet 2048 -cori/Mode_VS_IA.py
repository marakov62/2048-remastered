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

class Window5(QMainWindow):
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
		if (jeu.win3(jeu.Tab)==False) and (jeu.lose(jeu.Tab)==False) :

			#regarde si la touche pressé est bien la flèche gauche et si ce coup est possible
			if event.key()==Qt.Key_Left and (jeu.check(jeu.Tab,"Left")) :
				
				#Déplacement du 2048 vers la gauche
				jeu.left(jeu.Tab)
				
				#Si le 2048 n'est pas plein , il s'implemente
				if jeu.Plein(jeu.Tab)!=True :
					jeu.implemante(jeu.Tab)
					
				#au tour de l'IA    
				self.tourIA()
				
			if (event.key()==Qt.Key_Up) and (jeu.check(jeu.Tab,"Up")) :
				jeu.up(jeu.Tab)
				
				if jeu.Plein(jeu.Tab)!=True :
					jeu.implemante(jeu.Tab)
				self.tourIA()
				
			if event.key()==Qt.Key_Right and (jeu.check(jeu.Tab,"Right")) :
				jeu.right(jeu.Tab)
				

				if jeu.Plein(jeu.Tab)!=True :
					jeu.implemante(jeu.Tab)
				self.tourIA()

			if event.key()==Qt.Key_Down and (jeu.check(jeu.Tab,"Down")) :
				jeu.down(jeu.Tab)
				

				if jeu.Plein(jeu.Tab)!=True :
					jeu.implemante(jeu.Tab)
				self.tourIA()

			self.update()
						   

			if jeu.win3(jeu.Tab)==True :
				self.victoireLabel()

			if jeu.lose(jeu.Tab)==True :
				self.defaiteLabel()


	def tourIA(self):
		#regarde si le 2048 est dans un état de victoire ou de défaite
		if (jeu.win3(jeu.Tab)==False) and (jeu.lose(jeu.Tab)==False) :

			#meilleursCoups est un tableau rangé dans l'ordre des meilleurs coups réalisableS
			meilleursCoups=jeu.IA(jeu.Tab)

			#si le premier coup n'est pas jouable, i s'implemente
			#et c'est la i ème meilleurs option qui est choisie
			for i in range(4):
				
				#regarde quel est la meilleur option à la position i
				if meilleursCoups[i]=="left" :

					#vérifie si le coup est jouable
					if jeu.check(jeu.Tab,"Left") :
						#déplacement vers la gauche
						jeu.left(jeu.Tab)

						#Si le 2048 n'est pas plein , il s'implemente
						if jeu.Plein(jeu.Tab)!=True :
							jeu.implemante(jeu.Tab)

						break


				if meilleursCoups[i]=="up" :
					if jeu.check(jeu.Tab,"Up") :                
						jeu.up(jeu.Tab)

						if jeu.Plein(jeu.Tab)!=True :
							jeu.implemante(jeu.Tab)
						break

				if meilleursCoups[i]=="down" :
					if jeu.check(jeu.Tab,"Down") :
						jeu.down(jeu.Tab)

						if jeu.Plein(jeu.Tab)!=True :
							jeu.implemante(jeu.Tab)
						break

				if meilleursCoups[i]=="right" :
					if jeu.check(jeu.Tab,"Right") : 
						jeu.right(jeu.Tab)

						if jeu.Plein(jeu.Tab)!=True :
							jeu.implemante(jeu.Tab)
						break

		self.update()

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


