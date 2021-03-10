
import pyxel
import math
import random
import gcommon
import enemy

# 自機
class MyShip:
	def __init__(self):
		super().__init__()
		self.sprite = 1
		self.shotMax = 3
		self.left = 6
		self.top = 6
		self.right = 9
		self.bottom = 10
		self.cnt = 0
		# 1:ゲーム中 2:爆発中 3:復活中
		self.sub_scene = 1
		self.shotCounter = 0
		self.prevFlag = False
		self.setStartPosition()
		
	def update(self):
		if self.sub_scene == 1:
			# ゲーム中
			self.actionButtonInput()
		elif self.sub_scene == 2:
			# 爆発中
			if self.cnt > 90:
				if gcommon.remain == 0:
					gcommon.app.startGameOver()
					#start_gameover()
					#print("GAME OVER")
				else:
					gcommon.remain -= 1
					#--restart_game()
					self.sub_scene=3
					gcommon.bomRemain = gcommon.START_BOM_REMAIN
					self.cnt = 0
					gcommon.power = gcommon.START_MY_POWER
					self.sprite = 1
					self.setStartPosition()
					self.y = 256
		elif self.sub_scene == 3:
			# 復活中
			self.y -= 1
			if self.y == 200:
				self.cnt = 0
				self.sub_scene = 4
		else: # sub_scene=4
			# 無敵中
			self.actionButtonInput()
			if self.cnt == 120:
				self.cnt = 0
				self.sub_scene=1

		self.cnt += 1

	
	
	def actionButtonInput(self):
		self.sprite = 1
		if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
			self.x = self.x -2
			self.sprite = 3
			if self.x < 0:
				self.x = 0
		elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
			self.x = self.x +2
			self.sprite = 2
			if self.x > 240:
				self.x = 240
		if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP):
			self.y = self.y -2
			if self.y < 16:
				self.y = 16
		elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
			self.y = self.y +2
			if self.y > 240:
				self.y = 240
		if gcommon.checkShotKey() and gcommon.game_timer > 30:
			if self.prevFlag:
				self.shotCounter += 1
				if self.shotCounter > 5:
					self.shotCounter = 0
					self.shot()
			else:
				self.prevFlag = True
				self.shotCounter = 0
				self.shot()
		else:
			self.prevFlag = False
			self.shotCounter = 0
			
		if gcommon.checkBomKey() and gcommon.ObjMgr.myBom == None and gcommon.bomRemain > 0:
			self.startBom(self.x +7, self.y +7)
	
	def draw(self):
		if self.sub_scene == 1:
			self.drawMyShip()
		elif self.sub_scene == 2:
			pyxel.circ(self.x +7, self.y +7, self.cnt % 16, 10)
			pyxel.circ(self.x +7, self.y +7, (self.cnt+8) % 16, 7)
			r = 0
			for i in range(1,50):
				pyxel.pset(							\
					self.x +7 * math.cos(r) * ((self.cnt/2+i)%20),	\
					self.y +7 * math.sin(r) * ((self.cnt/2+i)%20),	\
					7 + int(self.cnt%2)*3)
				# kore ha tekito
				r += 0.11 + i*0.04
		elif self.sub_scene==3 or self.sub_scene==4:
			if self.cnt%2 ==0:
				self.drawMyShip()

	def drawMyShip(self):
		if gcommon.set_color_shadow():
			pyxel.blt(self.x +16, self.y +16, 0, self.sprite * 16, 0, 16, 16, gcommon.TP_COLOR)
			pyxel.pal()
		pyxel.blt(self.x, self.y, 0, self.sprite * 16, 0, 16, 16, gcommon.TP_COLOR)

	def shot(self):
		if len(gcommon.ObjMgr.shotGroups) < self.shotMax:
			shotGroup = MyShotGroup()
			if gcommon.power == 1:
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x-6, self.y -8, 0, -8)))
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x+6, self.y -8, 0, -8)))
			elif gcommon.power == 2:
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x, self.y -8, 0, -8)))
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x-8, self.y -8, -0.4, -7.6)))
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x+8, self.y -8,  0.4, -7.6)))
			elif gcommon.power == 3:
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x, self.y -8, 0, -8)))
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x-8, self.y -8, -0.4, -7.6)))
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x+8, self.y -8,  0.4, -7.6)))
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x-8, self.y -8, -1, -7)))
				gcommon.ObjMgr.shots.append(shotGroup.append(self.createShot(self.x+8, self.y -8,  1, -7)))
			else:
				return
			#if pyxel.play_pos(0) == -1:
			#	pyxel.play(0, 0)
			gcommon.sound(gcommon.SOUND_SHOT)
			gcommon.ObjMgr.shotGroups.append(shotGroup)
	
	def createShot(self, x, y, dx, dy):
		s = MyShot()
		s.init(x, y, dx, dy)
		return s
	
	def startBom(self, x, y):
		gcommon.ObjMgr.myBom = MyBom(x, y)
		gcommon.bomRemain -= 1
	
	def setStartPosition(self):
		self.x = pyxel.width/2 -8
		self.y = pyxel.height*5/6

class MyBom:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.state = 1
		self.cnt = 0
		self.removeFlag = False

	def update(self):
		if self.state==1:
			self.cnt += 1
			if self.cnt>15:
				#pyxel.play(0, 5)
				gcommon.sound(gcommon.SOUND_BOM_EXP)
				self.state=2
				self.cnt=0
		elif self.state==2:
			self.cnt+=1
			if self.cnt>60:
				self.state=0
				self.cnt=0
				self.removeFlag = True

	def draw(self):
		if self.state==1:
			pyxel.circ(self.x, self.y, (self.cnt+1)*4, 7)
		elif self.state==2:
			if self.cnt%2 ==0:
				# 128,16 40x40
				#blt(64,8,24,24,self.x-36,self.y-36,
				#72-bom.cnt%4,72-self.cnt%4,
				#self.cnt%4==0,not(self.cnt%4==0))
				dx = 1
				dy = 1
				if self.cnt & 3==0:
					dx = -1
				if self.cnt & 7==0:
					dy = -1
				pyxel.blt(self.x-36*2, self.y-36*2, 0, 0, 64, 144*dx, 144*dy, gcommon.C_COLOR_KEY)


class MyShot:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.left = 2
		self.top = 0
		self.right = 13
		self.bottom = 15
		self.dx = 0
		self.dy = 0
		self.group = None
		self.removeFlag = False

	def init(self, x, y, dx, dy):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy

	def update(self):
		if self.removeFlag == False:
			self.x = self.x + self.dx
			self.y = self.y + self.dy
			if self.y < -16:
				self.removeFlag = True
				self.group.remove(self)
				if len(self.group.shots) == 0:
					gcommon.ObjMgr.shotGroups.remove(self.group)

	def draw(self):
		pyxel.blt(self.x, self.y, 0, 64, 0, 16, 16, gcommon.TP_COLOR)

class MyShotGroup:
	def __init__(self):
		self.shots = []
	
	def append(self, s):
		self.shots.append(s)
		s.group = self
		return s

	def remove(self, s):
		self.shots.remove(s)
		return len(self.shots)


