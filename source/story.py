
import pyxel
import math
import random
import gcommon
import enemy
import boss

class Story:
	@classmethod
	def getStory1(cls):
		return [ \
			[120, enemy.Copter1,60 *2, -8*2, 70,0],  \
			[200, enemy.Copter1,90 *2, -8*2, 90,0],  \
			[220, enemy.Copter1,20 *2, -8*2, 80,0],  \
			[300, enemy.ItemCarrior, 50*2, -16*2, gcommon.C_ITEM_PWUP],	\
			[320, enemy.Copter1,20 *2,-8*2,70,0],	\
			[350, enemy.Copter1,90 *2,-8*2,90,0],	\
			[380, enemy.Copter1,40 *2,-8*2,80,0],	\
			# tank
			[440,enemy.Tank1,47*2,-16*2,6,60,180,300],		\
			[440,enemy.Copter1,20*2,-8*2,90,0],				\
			[470,enemy.Copter1,90*2,-8*2,70,0],			\
			[530,enemy.Copter1,70*2,-8*2,60,0],			\

			[660,enemy.Copter1,90*2,-8*2,80,0],			\
			[720,enemy.Tank1,-16*2,31*2,0,60,180,300],	\
			[780,enemy.Tank1,128*2,43*2,4,60,180,300],	\
			[880,enemy.MidTank1,90*2,-22*2,120,180,200,6,120],	\
			[940,enemy.Copter1,20*2,-8*2,90,0],		\
			[960,enemy.Copter1,40*2,-8*2,80,0],		\
			[980,enemy.Copter1,60*2,-8*2,70,0],		\

			[1100,enemy.Copter1,30*2,-8*2,80,0],	\
			[1120,enemy.Copter1,50*2,-8*2,80,0],	\
			[1140,enemy.Copter1,70*2,-8*2,80,0],	\

			[1200,enemy.ItemCarrior,80*2,-16*2,gcommon.C_ITEM_PWUP],	\

			[1300,enemy.Copter1,10*2,-8*2,80,0],	\
			[1320,enemy.Copter1,30*2,-8*2,80,0],	\
			[1340,enemy.Copter1,40*2,-8*2,80,0],	\

			#-[1370,T_TANK1,128,43,5,60,180,300],
			[1370,enemy.Tank1,-16*2,43*2,0,60,180,300],	\

			[1370,enemy.MidTank1,128*2,10*2,360,180,0,2,320],	\
			[1400,enemy.Copter1,70*2,-8*2,80,0],	\
			[1420,enemy.Copter1,80*2,-8*2,80,0],	\
			[1440,enemy.Copter1,100*2,-8*2,80,0],	\
			[1480,enemy.MidTank1,-20*2,0,180,180,0,0,120],		\
			[1500,enemy.Copter1,10*2,-8*2,90,0],	\
			[1520,enemy.Copter1,30*2,-8*2,80,0],	\
			[1540,enemy.Copter1,50*2,-8*2,70,0],	\
			[1700,enemy.Fighter1,90*2,-16*2,60,180,120],	\
			[1700,enemy.Tank1,128*2,0,4,60,180,300],	\
			[1800,enemy.Tank1,128*2,0,4,60,180,300],	\
			[1820,enemy.Fighter1,8*2,-16*2,60,180,120],	\
			[1940,enemy.Fighter1,60*2,-16*2,60,180,120],	\
			[2120,enemy.Tank1,-16*2,32*2,0,60,180,300],	\

			[2180,enemy.Tank1,128*2,40*2,4,60,180,300],	\
			[2180,enemy.Copter1,70*2,-8*2,60,0],		\
			[2200,enemy.Copter1,85*2,-8*2,70,0],		\
			[2220,enemy.Copter1,100*2,-8*2,80,0],		\
			[2220,enemy.Tank1,-16*2,32*2,0,60,180,300],	\
			[2320,enemy.Tank1,128*2,0*2,4,60,180,300],	\
			[2320,enemy.Copter1,10*2,-8*2,80,0],		\
			[2340,enemy.Copter1,25*2,-8*2,70,0],		\
			[2360,enemy.Copter1,40*2,-8*2,90,0],		\
			[2410,enemy.MidTank1,-20*2,0*2,180,180,0,0,120],	\

			[2420,enemy.Fighter1,90*2,-16*2,60,180,120],	\
			[2480,enemy.Fighter1,10*2,-16*2,60,180,120],	\
			[2530,enemy.Fighter1,40*2,-16*2,60,180,120],	\
			[2780,boss.Boss1,46*2,-32*2],		\
			[2820,enemy.Copter1,10*2,-8*2,80,0],	\
			[2840,enemy.Copter1,25*2,-8*2,70,0],	\
			[2860,enemy.Copter1,40*2,-8*2,90,0],	\
			[3000,enemy.Copter1,70*2,-8*2,60,0],	\
			[3020,enemy.Copter1,85*2,-8*2,70,0],	\
			[3040,enemy.Copter1,100*2,-8*2,80,0],	\
			[3100,enemy.MidTank1,-20*2,22*2,180,180,0,0,120],	\
			[3200,enemy.MidTank1,128*2,42*2,180,180,0,4,120],	\
		]

	@classmethod
	def getStory2(cls):
		return [ \
			[120,enemy.Copter1,60*2,-8*2,70,0],		\
			[200,enemy.Copter1,100*2,-8*2,80,0],	\
			[220,enemy.Copter1,10*2,-8*2,80,0],		\
			[300,enemy.ItemCarrior,80*2,-16*2, gcommon.C_ITEM_PWUP],
			[320,enemy.Copter1,10*2,-8*2,70,0],
			[350,enemy.Copter1,100*2,-8*2,80,0],
			[380,enemy.Copter1,20*2,-8*2,80,0],

			[440,enemy.Copter1,20*2,-8*2,90,0],
			[470,enemy.Copter1,90*2,-8*2,70,0],
			[530,enemy.Copter1,70*2,-8*2,60,0],


			[660,enemy.Copter1,90*2,-8*2,80,0],

			[800,enemy.Copter1,10*2,-8*2,70,0],
			[830,enemy.Copter1,100*2,-8*2,80,0],
			[860,enemy.Copter1,20*2,-8*2,80,0],

			[940,enemy.Copter1,20*2,-8*2,90,0],
			[960,enemy.Copter1,40*2,-8*2,80,0],
			[980,enemy.Copter1,60*2,-8*2,70,0],
			[980,enemy.Tank2,-16,16,60,120,
				[[56,1],[1800,0]]],

			[1020,enemy.Tank2,128,24,60,120,
			[[56,5],[1800,0]]],

			[1060,enemy.Tank2,128,16,60,120,
			[[88,5],[1800,0]]],

			[1080,enemy.Tank2,-16,20,60,120,
			[[88,1],[1800,0]]],

			[1100,enemy.Copter1,30*2,-8*2,80,0],
			[1120,enemy.Copter1,50*2,-8*2,80,0],
			[1140,enemy.Copter1,70*2,-8*2,80,0],

			[1200,enemy.ItemCarrior,80*2,-16*2,gcommon.C_ITEM_PWUP],

			[1300,enemy.Copter1,10*2,-8*2,80,0],
			[1320,enemy.Copter1,30*2,-8*2,80,0],
			[1340,enemy.Copter1,40*2,-8*2,80,0],

			[1360,enemy.Tank2,28,-16,60,60,
			[[88,7],[1800,0]]],

			[1380,enemy.Tank2,44,-16,60,60,
			[[88,7],[1800,0]]],

			[1380,enemy.Copter1,10*2,-8*2,80,0],
			[1400,enemy.Copter1,30*2,-8*2,80,0],
			[1420,enemy.Copter1,100*2,-8*2,80,0],

			[1500,enemy.Tank2,84,-16,60,60,
			[[88,7],[1800,0]]],

			[1580,enemy.Tank2,68,-16,60,60,
			[[88,7],[1800,0]]],

			[1580,enemy.Copter1,10*2,-8*2,80,0],
			[1600,enemy.Copter1,30*2,-8*2,80,0],
			[1620,enemy.Copter1,50*2,-8*2,80,0],

			[1720,enemy.Wall1,0,-24,0],
			[1720,enemy.Wall1,104,-24,1],

			[1880,enemy.Tank2,28,-16,60,60,
			[[56,7],[180,5]]],
			[1880,enemy.Tank2,84,-16,60,60,
			[[56,7],[180,1]]],

			[1940,enemy.Fighter1,60*2,-16*2,60,180,120],

			[2000,enemy.Wall1,0,-24,0],
			[2000,enemy.Wall1,104,-24,1],

			[2020,enemy.Tank2,-16,40,60,60,
			[[88,1],[180,7]]],

			[2060,enemy.Tank2,84,128,60,60,
			[[160,3],[320,1]]],

			[2180,enemy.Copter1,70*2,-8*2,60,0],

			[2200,enemy.Copter1,85*2,-8*2,70,0],
			[2220,enemy.Copter1,100*2,-8*2,80,0],
			[2260,enemy.Tank2,-16,32,60,60,[[60,1],[300,5]]],

			[2320,enemy.Tank2,128,42,60,60,
			[[86,5],[200,3],[1200,7]]],

			[2320,enemy.Copter1,10*2,-8,80,0],
			[2340,enemy.Copter1,25*2,-8,70,0],
			[2360,enemy.Copter1,40*2,-8,90,0],

			[2420,enemy.Fighter1,90*2,-16*2,60,180,120],
			[2480,enemy.Fighter1,10*2,-16*2,60,180,120],
			[2530,enemy.Fighter1,40*2,-16*2,60,180,120],
			[2840,boss.Boss2,48,-48]
		]

	@classmethod
	def getStory3(cls):
		return [ \
			[120,enemy.ItemCarrior2,8,-16*2,gcommon.C_ITEM_PWUP],	\
			[300,enemy.Fighter2Appear, 0, 20, 6, -1],		\
			[400,enemy.Fighter2Appear, 0, 20, 6, 1],		\
			[500,enemy.Battery2, 80, -16, 120, 60],		\
			[500,enemy.Battery2, 160, -16, 120, 60],		\
			[540,enemy.Battery2, 80, -16, 180, 60],		\
			[540,enemy.Battery2, 160, -16, 180, 60],		\
			[600,enemy.Fighter1B,200,-16*2,60,180,120],
			[600,enemy.Fighter2Appear, 0, 20, 6, -1],		\
			[660,enemy.Fighter1B,10*2,-16*2,60,180,120],
			[680,enemy.MidBattery1,112,-32,60,60,40],
			[720,enemy.Fighter1B,80,-16*2,60,180,120],
			[800,enemy.Fighter2Appear, 0, 20, 6, 1],		\
			[860,enemy.MidBattery1,112,-32,60,60,40],
			[1060,enemy.MidBattery1,88,-32,70,60,60],
			[1060,enemy.MidBattery1,136,-32,70,60,60],
			[1160,enemy.Battery2, 88, -16, 120, 60],		\
			[1160,enemy.Battery2, 152, -16, 120, 60],		\
			[1200,enemy.Fighter2Appear, 0, 20, 6, -1],		\
			[1200,enemy.Battery2, 88, -16, 180, 60],		\
			[1200,enemy.Battery2, 152, -16, 180, 60],		\
			[1300,enemy.Fighter2Appear, 0, 20, 6, 1],		\
			[1440,enemy.Battery2, 8, -16, 120, 60],		\
			[1440,enemy.Battery2, 232, -16, 120, 60],		\
			[1440,enemy.Fighter1B,180,-16*2,60,180,120],
			[1500,enemy.Battery2, 8, -16, 120, 60],		# 147	\
			[1500,enemy.Battery2, 232, -16, 300, 60],		\
			[1500,enemy.Fighter1B,40,-16*2,60,180,120],
			[1600,enemy.ItemCarrior2,170,-16*2,gcommon.C_ITEM_PWUP],	\
			# 艦上戦車
			[1780,enemy.MidTank2, 100, -40],		\
			[1880,enemy.Battery2, 8, -16, 120, 60],		# 128	\
			[1880,enemy.Battery2, 232, -16, 120, 60],		\
			[1940,enemy.Fighter2Appear, 0, 20, 6, -1],		\
			[1940,enemy.Battery2, 8, -16, 120, 60],		# 125	\
			[1940,enemy.Battery2, 232, -16, 120, 60],		\
			[2040,enemy.Fighter2Appear, 0, 20, 6, 1],		\
			[2040,enemy.Battery2, 8, -16, 120, 60],		# 120	\
			[2040,enemy.Battery2, 232, -16, 120, 60],		\
			[2100,enemy.Battery2, 8, -16, 120, 60],		# 117	\
			[2100,enemy.Battery2, 232, -16, 120, 60],		\
			[2300,enemy.Fighter1B,180,-16*2,60,180,120],
			[2400,enemy.Fighter1B,80,-16*2,60,180,120],
			[2500,enemy.Fighter1B,20,-16*2,60,180,120],
			[2520,enemy.Battery2, 8, -16, 120, 60],		# 96	\
			[2520,enemy.Battery2, 232, -16, 120, 60],		\
			[2580,enemy.Battery2, 8, -16, 120, 60],		# 93	\
			[2580,enemy.Battery2, 232, -16, 120, 60],		\
			[2580,enemy.Fighter2Appear, 0, 20, 6, 1],		\
			[2680,enemy.Battery2, 8, -16, 120, 60],		# 88	\
			[2680,enemy.Battery2, 232, -16, 120, 60],		\
			[2680,enemy.Fighter2Appear, 0, 20, 6, -1],		\
			[2740,enemy.Battery2, 8, -16, 120, 60],		# 85	\
			[2740,enemy.Battery2, 232, -16, 120, 60],		\
			[3360,enemy.Battery2, 96, -16, 120, 60],		# 56	\
			[3360,enemy.Battery2, 144, -16, 120, 60],		\
			[3420,enemy.Battery2, 96, -16, 120, 60],		# 53	\
			[3420,enemy.Battery2, 144, -16, 120, 60],		\
			[3600,boss.Boss3, 48, 256],		\
		]
