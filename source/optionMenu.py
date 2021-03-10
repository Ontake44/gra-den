
import pyxel
import math
import gcommon


OPTIONMENU_PLAYER_STOCK = 0
OPTIONMENU_BOMB_STOCK = 1
OPTIONMENU_START_STAGE = 2
OPTIONMENU_SOUND = 3
OPTIONMENU_EXIT = 4

class OptionMenuScene:
	def __init__(self):
		self.menuPos = 0
	
	def update(self):
		if gcommon.checkUpP():
			self.menuPos -= 1
			if self.menuPos < 0:
				self.menuPos = 4
		if gcommon.checkDownP():
			self.menuPos += 1
			if self.menuPos > 4:
				self.menuPos = 0
		
		if gcommon.checkRightP():
			if self.menuPos == OPTIONMENU_PLAYER_STOCK:
				gcommon.START_REMAIN += 1
				if gcommon.START_REMAIN > 99:
					gcommon.START_REMAIN = 99
			elif self.menuPos == OPTIONMENU_BOMB_STOCK:
				gcommon.START_BOM_REMAIN += 1
				if gcommon.START_BOM_REMAIN > 5:
					gcommon.START_BOM_REMAIN = 5
			elif self.menuPos == OPTIONMENU_START_STAGE:
				gcommon.START_STAGE += 1
				if gcommon.START_STAGE > 3:
					gcommon.START_STAGE = 3
			elif self.menuPos == OPTIONMENU_SOUND:
				gcommon.SOUND_ON = not gcommon.SOUND_ON
		elif gcommon.checkLeftP():
			if self.menuPos == OPTIONMENU_PLAYER_STOCK:
				gcommon.START_REMAIN -= 1
				if gcommon.START_REMAIN < 1:
					gcommon.START_REMAIN = 1
			elif self.menuPos == OPTIONMENU_BOMB_STOCK:
				gcommon.START_BOM_REMAIN -= 1
				if gcommon.START_BOM_REMAIN < 0:
					gcommon.START_BOM_REMAIN = 0
			elif self.menuPos == OPTIONMENU_START_STAGE:
				gcommon.START_STAGE -= 1
				if gcommon.START_STAGE < 1:
					gcommon.START_STAGE = 1
			elif self.menuPos == OPTIONMENU_SOUND:
				gcommon.SOUND_ON = not gcommon.SOUND_ON
		
		if gcommon.checkShotKeyP() and self.menuPos == OPTIONMENU_EXIT:
			gcommon.saveSettings()
			gcommon.app.startTitle()

	def draw(self):
		pyxel.cls(1)
		pyxel.bltm(0, 0, 1, 0, 0, 32, 32)
		gcommon.Text2(8, 8, "OPTION MENU", 7, 5)
		y = 50
		gcommon.Text2(30, y, "DIFFICULTY", 6, 5)
		gcommon.Text2(120, y, "NORMAL", 6, 5)
		y += 20
		
		gcommon.Text2(30, y, "PLAYER STOCK", self.getOptionColor(OPTIONMENU_PLAYER_STOCK), 5)
		gcommon.Text2(120, y, str(gcommon.START_REMAIN), self.getOptionColor(OPTIONMENU_PLAYER_STOCK), 5)
		y += 20

		gcommon.Text2(30, y, "BOMB STOCK", self.getOptionColor(OPTIONMENU_BOMB_STOCK), 5)
		gcommon.Text2(120, y, str(gcommon.START_BOM_REMAIN), self.getOptionColor(OPTIONMENU_BOMB_STOCK), 5)
		y += 20

		gcommon.Text2(30, y, "START STAGE", self.getOptionColor(OPTIONMENU_START_STAGE), 5)
		gcommon.Text2(120, y, str(gcommon.START_STAGE), self.getOptionColor(OPTIONMENU_START_STAGE), 5)
		y += 20
		gcommon.Text2(30, y, "SOUND", self.getOptionColor(OPTIONMENU_SOUND), 5)
		if gcommon.SOUND_ON:
			gcommon.Text2(120, y, "ON", self.getOptionColor(OPTIONMENU_SOUND), 5)
		else:
			gcommon.Text2(120, y, "OFF", self.getOptionColor(OPTIONMENU_SOUND), 5)
	
		y += 20
		gcommon.Text2(30, y, "EXIT", self.getOptionColor(OPTIONMENU_EXIT), 5)


	def getOptionColor(self, index):
		if index == self.menuPos:
			return 8
		else:
			return 7
