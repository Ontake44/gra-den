import pyxel
import math
import random

import gcommon
import enemy

#
#  タイトル表示
#
class TitleScene:
	def __init__(self):
		gcommon.map_y = 0
		self.cnt = 0
		pyxel.image(1).load(0,0,"assets\gra-den1.png")
		pyxel.tilemap(0).refimg = 1
		self.menuPos = 0
		self.timer = 0
		self.state = 0
		gcommon.loadSettings()
	
	def update(self):
		if self.cnt >= 6*60:
			self.cnt = 0
			gcommon.map_y = 0
		self.timer += 1
		if self.timer >= 60 * 3600:
			self.timer = 0
		
		gcommon.map_y += 0.4
		
		if self.state == 0:
			
			if gcommon.checkShotKey() and self.timer > 30:
				if self.menuPos == 0:
					gcommon.sound(gcommon.SOUND_GAMESTART)
					self.state = 1
					self.cnt = 0
				else:
					gcommon.app.startOption()
				#app.startStageClear()
			
			if gcommon.checkUpP() or gcommon.checkDownP():
				self.menuPos = (self.menuPos + 1) & 1
		else:
			# GAME START
			if self.cnt > 40:
				gcommon.app.startGame(gcommon.START_STAGE)
			
		
		self.cnt+=1

	def draw(self):
		pyxel.cls(0)
		pyxel.bltm(0,-8+gcommon.map_y%8, 0, 0,(256-33)-(int)(gcommon.map_y/8),32,33)
		pyxel.blt(64, 88, 0, 0, 208, 128, 32, gcommon.TP_COLOR)
		if self.state == 0:
			gcommon.Text2(110, 150, "GAME START", 7, 5)
		else:
			if self.cnt & 2 == 0:
				gcommon.Text2(110, 150, "GAME START", 7, 5)
			else:
				gcommon.Text2(110, 150, "GAME START", 8, 5)
		gcommon.Text2(110, 165, "OPTION", 7, 5)
		pyxel.blt(98, 149 + self.menuPos * 15, 0, 0, 32, 8, 8, gcommon.TP_COLOR)
		
