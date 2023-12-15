import os
import pyxel
import math
import random
import sys

import gcommon
import enemy
from myShip import MyShip
from myShip import MyShot
from myShip import MyBom
import boss
import title
import optionMenu
import story

#
#  ゲームオーバー
#
class GameOver:
	def __init__(self):
		self.cnt = 0
	
	def update(self):
		self.cnt+=1
		if self.cnt > 5*60:
			gcommon.app.startTitle()
	
	def draw(self):
		pyxel.cls(0)
		gcommon.TextHCenter(60*2, "GAME OVER", 8, -1)

#
#  ステージクリアー
#
#  stage : クリアーしたステージ
class StageClear:
	def __init__(self, stage):
		self.cnt = 0
		self.stage = stage
	
	def update(self):
		self.cnt+=1
		if self.cnt > 5*60:
			gcommon.app.startStage(self.stage+1)
	
	def draw(self):
		pyxel.rect(0,0,255,255,0)
		pyxel.text(96, 88, "CONGRATULATIONS!", self.cnt & 15)
		pyxel.text(104, 60*2, "STAGE CLEAR", 8)

#
#  ゲームクリアー
#
class GameClear:
	def __init__(self):
		self.cnt = 0
	
	def update(self):
		self.cnt+=1
		if self.cnt > 5*60:
			gcommon.app.startTitle()
	
	def draw(self):
		pyxel.rect(0,0,255,255,0)
		pyxel.text(96, 88, "CONGRATULATIONS!", self.cnt & 15)
		gcommon.TextHCenter(60*2, "GAME CLEAR", 8, -1)

class MainGame:
	def __init__(self, stage):
		gcommon.ObjMgr.init()
		gcommon.ObjMgr.myShip = MyShip()
		gcommon.cur_scroll = 0.4
		self.story_pos = 0
		self.stage = stage
		self.mapOffsetX = 0
		self.star_pos = 0
		self.star_ary = []
		self.pause = False
		gcommon.game_timer = gcommon.START_GAME_TIMER
		gcommon.map_y = gcommon.cur_scroll * gcommon.game_timer
		self.initStory()
		if self.stage == 1:
			pyxel.images[1].load(0,0,os.path.join("assets", "gra-den1.png"))
			self.mapOffsetX = 0
			gcommon.draw_star = False
		elif self.stage == 2:
			pyxel.images[1].load(0,0,os.path.join("assets", "gra-den2.png"))
			self.mapOffsetX = 32
			gcommon.draw_star = False
		elif self.stage == 3:
			pyxel.images[1].load(0,0,os.path.join("assets", "gra-den3a.png"))
			pyxel.images[2].load(0,0,os.path.join("assets", "gra-den3b.png"))
			self.mapOffsetX = 64
			gcommon.draw_star = True
		pyxel.tilemap(0).imgsrc = 1
		
		for i in range(0,128):
			o = [int(random.randrange(0,256)), int(random.randrange(0,2)+5)]
			self.star_ary.append(o)
		
		
	def update(self):
		# PAUSE
		if self.pause:
			if pyxel.btnp(pyxel.KEY_F1) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
				self.pause = False
			else:
				return
		else:
			if pyxel.btnp(pyxel.KEY_F1) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
				self.pause = True
				return
		# 星
		if gcommon.draw_star:
			self.star_pos += 0.2
			if self.star_pos>255:
				self.star_pos -= 255

		self.ExecuteStory()
		
		# MAP
		gcommon.map_y += gcommon.cur_scroll
		if self.stage == 1:
			if gcommon.map_y>=1700:			# 1792
				gcommon.app.startStage(self.stage+1)
		else:
			pass
			
		
		gcommon.ObjMgr.myShip.update()
		
		newShots = []
		for shot in gcommon.ObjMgr.shots:
			shot.update()
			if shot.removeFlag == False:
				newShots.append(shot)
		gcommon.ObjMgr.shots = newShots

		if gcommon.ObjMgr.myBom != None:
			gcommon.ObjMgr.myBom.update()
			if gcommon.ObjMgr.myBom.removeFlag:
				gcommon.ObjMgr.myBom = None
	
		newObjs = []
		for obj in gcommon.ObjMgr.objs:
			if obj.layer == gcommon.C_LAYER_GRD 	\
				or obj.layer==gcommon.C_LAYER_HIDE_GRD \
				or obj.layer==gcommon.C_LAYER_EXP_GRD \
				or obj.layer==gcommon.C_LAYER_UPPER_GRD: \
				obj.y += gcommon.cur_scroll
			obj.update()
			obj.cnt = obj.cnt + 1
			if obj.removeFlag == False:
				newObjs.append(obj)
		gcommon.ObjMgr.objs = newObjs
		
		self.Collision()
		
		gcommon.game_timer = gcommon.game_timer + 1
	
	
	def draw(self):
		pyxel.cls(0)
		
		#pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
		#pyxel.blt(61, 66, 0, 0, 0, 38, 16)
		if self.stage == 1:
			pyxel.bltm(0,-8+gcommon.map_y%8, 0, 8*(self.mapOffsetX),8*((256-33)-(int)(gcommon.map_y/8)),32*8,33*8)
		elif self.stage == 2:
			if gcommon.draw_star:
				for i in range(0,128):
					pyxel.pset(self.star_ary[i][0], (self.star_pos+i*2)%255, self.star_ary[i][1])
				
			#for obj in gcommon.ObjMgr.objs:
			#	if obj.layer==gcommon.C_LAYER_UNDER_GRD:
			#		if obj.hitcolor1 !=0 and obj.hit:
			#			pyxel.pal(obj.hitcolor1, obj.hitcolor2)
			#		obj.draw()
			#		if obj.hitcolor1 !=0 and obj.hit:
			#			pyxel.pal(obj.hitcolor1, obj.hitcolor1)
			# map
			pyxel.bltm(0,-8+int(gcommon.map_y)%8, 0, 8*(self.mapOffsetX,(256-33)-(int)(gcommon.map_y/8)),8*32,8*33, gcommon.TP_COLOR)
		elif self.stage == 3:
			if gcommon.draw_star:
				for i in range(0,128):
					pyxel.pset(self.star_ary[i][0], (self.star_pos+i*2)%255, self.star_ary[i][1])
				
			for obj in gcommon.ObjMgr.objs:
				if obj.layer==gcommon.C_LAYER_UNDER_GRD:
					if obj.hitcolor1 !=0 and obj.hit:
						pyxel.pal(obj.hitcolor1, obj.hitcolor2)
					obj.draw()
					if obj.hitcolor1 !=0 and obj.hit:
						pyxel.pal(obj.hitcolor1, obj.hitcolor1)
			# map
			if gcommon.map_y < 1664:
				pyxel.bltm(0,-8+int(gcommon.map_y)%8, 0, 8*(self.mapOffsetX,(256-33)-(int)(gcommon.map_y/8)),8*32,8*33, gcommon.TP_COLOR)
		
		
		# enemy(ground)
		for obj in gcommon.ObjMgr.objs:
			if obj.layer==gcommon.C_LAYER_GRD or obj.layer==gcommon.C_LAYER_HIDE_GRD:
				if obj.hitcolor1 !=0 and obj.hit:
					pyxel.pal(obj.hitcolor1, obj.hitcolor2)
				
				obj.draw()
				if obj.hitcolor1 !=0 and obj.hit:
					pyxel.pal(obj.hitcolor1, obj.hitcolor1)

		# explosion(ground)
		for obj in gcommon.ObjMgr.objs:
			if obj.layer==gcommon.C_LAYER_EXP_GRD:
				obj.draw()

		# upper ground
		for obj in gcommon.ObjMgr.objs:
			if obj.layer==gcommon.C_LAYER_UPPER_GRD:
				obj.draw()

		# item
		for obj in gcommon.ObjMgr.objs:
			if obj.layer==gcommon.C_LAYER_ITEM:
				obj.draw()

		# my bom
		if gcommon.ObjMgr.myBom != None:
			gcommon.ObjMgr.myBom.draw()
		
		# enemy(sky)
		for obj in gcommon.ObjMgr.objs:
			if obj.layer==gcommon.C_LAYER_SKY:
				if obj.hitcolor1 !=0 and obj.hit:
					pyxel.pal(obj.hitcolor1, obj.hitcolor2)
				
				obj.draw()
				if obj.hitcolor1 !=0 and obj.hit:
					pyxel.pal(obj.hitcolor1, obj.hitcolor1)

		# enemy shot and explosion(sky)
		for obj in gcommon.ObjMgr.objs:
			if obj.layer==gcommon.C_LAYER_EXP_SKY or obj.layer==gcommon.C_LAYER_E_SHOT:
				obj.draw()

		# my shot
		for shot in gcommon.ObjMgr.shots:
		  shot.draw()

		# my ship
		gcommon.ObjMgr.myShip.draw()

		for obj in gcommon.ObjMgr.objs:
			if obj.layer==gcommon.C_LAYER_TEXT:
				obj.draw()
		
		# SCORE表示
		pyxel.text(4, 2, "SCORE " + str(gcommon.score), 7)
		
		# 残機
		pyxel.blt(232, 2, 0, 48, 32, 6, 8, gcommon.C_COLOR_KEY)
		pyxel.text(242, 4, str(gcommon.remain), 7)
		
		# BOM
		for i in range(0, gcommon.bomRemain):
			pyxel.blt(4 + i*6, 244, 0, 56, 32, 6, 8, gcommon.C_COLOR_KEY)
		
		#pyxel.text(0, 220, str(gcommon.game_timer), 7)
		# マップ位置表示
		#pyxel.text(0, 230, str(gcommon.map_y), 7)

		if self.pause:
			pyxel.rect(127 -24, 127 -10, 48, 20, 0)
			pyxel.rectb(127 -24, 127 -10, 48, 20, 7)
			gcommon.TextHCenter(127- 3, "PAUSE", 7, -1)

	def ExecuteStory(self):
		while True:
			if len(self.story) <= self.story_pos:
				return
		
			s = self.story[self.story_pos]
			if s[0] < gcommon.game_timer:
				pass
			elif s[0] != gcommon.game_timer:
				return
			else:
				t = s[1]	# [1]はクラス型
				obj = t(s)			# ここでインスタンス化
				gcommon.ObjMgr.objs.append(obj)
				obj.appended()
			self.story_pos = self.story_pos + 1

	# 衝突判定
	def Collision(self):
		# shot & enemy
		for obj in gcommon.ObjMgr.objs:
			if obj.removeFlag:
				continue
			obj.hit = False
			if obj.layer!=gcommon.C_LAYER_GRD and obj.layer!=gcommon.C_LAYER_SKY:
				continue
			
			for shot in gcommon.ObjMgr.shots:
				if shot.removeFlag == False and gcommon.check_collision(obj, shot):
					obj.hp -= gcommon.SHOT_POWER
					if obj.hp <= 0:
						obj.broken()
					else:
						obj.hit = True
					shot.removeFlag = True
					shot.group.remove(shot)
					if len(shot.group.shots) == 0:
						gcommon.ObjMgr.shotGroups.remove(shot.group)
						
					if obj.removeFlag:
						break
		
		# my bom & enemy
		if gcommon.ObjMgr.myBom != None:
			for obj in gcommon.ObjMgr.objs:
				if obj.layer==gcommon.C_LAYER_GRD \
					or obj.layer==gcommon.C_LAYER_SKY \
					or obj.layer==gcommon.C_LAYER_E_SHOT:
					if math.sqrt((obj.x+(obj.right-obj.left)/2-gcommon.ObjMgr.myBom.x)**2+	\
						(obj.y+(obj.bottom-obj.top)/2-gcommon.ObjMgr.myBom.y)**2) <=72:
						if obj.layer==gcommon.C_LAYER_E_SHOT:
							obj.removeFlag = True
						else:
							obj.hp -= gcommon.BOM_POWER
							if obj.hp<=0:
								obj.broken()
							else:
								obj.hit = True

		# my ship & enemy
		if gcommon.ObjMgr.myShip.sub_scene == 1:
			for obj in gcommon.ObjMgr.objs:
				if obj.layer==gcommon.C_LAYER_E_SHOT or obj.layer==gcommon.C_LAYER_SKY:
					if gcommon.check_collision(obj, gcommon.ObjMgr.myShip):
						self.my_broken()
						break
				elif obj.layer==gcommon.C_LAYER_ITEM:
					if gcommon.check_collision(obj, gcommon.ObjMgr.myShip):
						self.catch_item(obj)
						obj.removeFlag = True


	def catch_item(self, obj):
		if obj.itype == gcommon.C_ITEM_PWUP:
			#pyxel.play(0, 7)
			gcommon.sound(gcommon.SOUND_PWUP)
			if gcommon.power < 3:
				gcommon.power += 1

	def my_broken(self):
		gcommon.ObjMgr.myShip.sub_scene = 2
		gcommon.ObjMgr.myShip.cnt = 0
		gcommon.power = gcommon.START_MY_POWER
		gcommon.bomRemain = gcommon.START_BOM_REMAIN
		#sfx(4)
		#pyxel.play(0, 4)
		gcommon.sound(gcommon.SOUND_LARGE_EXP)
		m = gcommon.ObjMgr.myShip
		enemy.create_item(m.x+(m.right-m.left)/2, m.y+(m.bottom-m.top)/2, gcommon.C_ITEM_PWUP)

	def initStory(self):
		if self.stage == 1:
			self.story = story.Story.getStory1()
		elif self.stage == 2:
			self.story = story.Story.getStory2()
		elif self.stage == 3:
			self.story = story.Story.getStory3()

def parseCommandLine():
	idx = 0
	while(idx < len(sys.argv)):
		arg = sys.argv[idx]
		if arg == "-timer":
			if idx+1<len(sys.argv):
				gcommon.START_GAME_TIMER = int(sys.argv[idx+1])
		idx+=1

class App:
	def __init__(self):
		gcommon.app = self
	
		# コマンドライン解析
		parseCommandLine()
	
		#pyxel.init(256, 256, caption="GRA-DEN", fps=60)
		#                                                    0       1         2         3         4         5         6         7         8         9        10        11        12        13        14        15
		pyxel.init(256, 256, title="GRA-DEN", fps=60)
		pyxel.colors.from_list([0x000000, 0x1D2B53, 0x7E2553, 0x008751, 0xAB5236, 0x5F574F, 0xC2C3C7, 0xFFF1E8, 0xFF004D, 0xFFA300, 0xFFEC27, 0x00E436, 0x29ADFF, 0x83769C, 0xFF77A8, 0xFFCCAA])
 		
		pyxel.load(os.path.join("assets", "gra-den.pyxres"))
		pyxel.images[0].load(0,0,os.path.join("assets","gra-den0.png"))
		
		gcommon.init_atan_table()
		
		#self.scene = MainGame()
		self.scene = title.TitleScene()
		self.stage = 0
		pyxel.run(self.update, self.draw)

	def startTitle(self):
		self.scene = title.TitleScene()

	def startGame(self, stage):
		self.stage = stage
		gcommon.remain = gcommon.START_REMAIN
		gcommon.power = gcommon.START_MY_POWER
		gcommon.bomRemain = gcommon.START_BOM_REMAIN
		gcommon.score = 0
		self.scene = MainGame(stage)

	def startStage(self, stage):
		self.stage = stage
		self.scene = MainGame(stage)

	def startNextStage(self):
		self.startStage(self.stage+1)

	def startGameOver(self):
		self.scene = GameOver()

	def startStageClear(self, stage):
		self.scene = StageClear(stage)

	def startGameClear(self):
		self.scene = GameClear()

	def startOption(self):
		self.scene = optionMenu.OptionMenuScene()

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

		self.scene.update()

	def draw(self):
		self.scene.draw()

App()
