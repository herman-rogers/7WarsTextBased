from sys import exit
from time import sleep
from random import randint, choice, random

guard_alive = True
					
class Game(object):
	'''Everything referencing a M means Xenian Mind Talent, a G means Xenian Guard'''
	
	def __init__(self, start):
		
		self.start = start
		self.enemy = ['xenian_guard', 'xenian_mt']
		self.name = 'Daiy'
		self.g_statements = [
			'You find a Xenian Guard standing in front of you, grasping a crystal sword...',
			'You walk in and see a Xenian Guard grab his Shifting Axe...',
			'You find yourself facing another guard...our races hate each other...what happened to us?',
			'A Xenian Guard...he\'s so young...his eyes slowly fog over <Battle Preparation>.'
			]
		self.m_statements = [
			'Standing in a protective stance you feel the MindTalent assault your psyche!',
			'A MindTalent Xenian finishes his protective circle, his weary gaze falls on you.',
			'You open the door finding a Xenian Mind Talent hands forward in Psychic preparation.'
			]
		self.health = 400
		self.focus = 70
		self.energy = 45
		self.mind_hp = 165
		self.guard_hp = 265
		self.dagger_talent = [10,18,20,80,165]
		self.dual_strong = [14, 20]
		self.dual_weak = [30, 34]
		self.player_attack = randint(20,28)
		self.player_talent = randint(20,28)
		self.mind_attack = randint(12,20)
		self.guard_attack = randint(14,20)
		self.bonus = randint(10,20)
		self.room = []
		self.hitem = 0
		self.sitem = 0
		self.hvial = 120
		self.svial = 40 
		self.generator = True
		self.door2close = False
		
	def play(self):
		next_room_name = self.start
		
		while True:
			print '\n------------'
			room = getattr(self, next_room_name)
			next_room_name = room()

		
	def death(self):
		print 'The world fades away as your knees buckle...you crumple to the ground...'
		sleep(2)
		cont = raw_input('Would you like to continue Yes/No? > ')
		while True:
			if cont == 'Yes' or cont == 'yes':
				return self.room[0]
			if cont == 'No' or cont == 'no':
				print 'The End'
				exit(0)
			else:
				'I couldn\'t understand you'	
	
	def guards(self):
		'''This tells the game whether a player killed a guard using Talents or if the guard is still alive for each room. If the guard is alive it assigns a random unit.'''
		
		if guard_alive == False:
			print 'You walk in and find the body of a Xenian talent-mind. Pushing his body to the side you walk into a large corridor leading closer to the center of the building.'
			return 'room_list'
		elif guard_alive == True:
			rdm_enemy = self.enemy[randint(0,len(self.enemy)-1)]
			if rdm_enemy == 'xenian_guard':
				return 'combat_system'
			elif rdm_enemy == 'xenian_mt':
				return 'combat_system_2'

			
	def combat_system(self):
		'''Interactive Combat System for Daiy and Guards'''
		
		print self.g_statements[randint(0,len(self.g_statements)-1)]
		sleep(1)
		print '\n	Xenian Guard HP: %r || Daiy\'s HP: %r | Focus: %r | Energy: %r' %(self.guard_hp, self.health, self.focus, self.energy)
		print '\n	<Command = Dagger for weapon, Talent for psych, Charge for Skills>'
		print '	<You can also use combos with command = dagger+talent etc.>\n'
		
		while self.health > 0 and self.guard_hp > 0:
			print '\nInventory: HP Vial:%r | Talent Vial: %r | use Vial FE or H to recharge' %(self.hitem, self.sitem)
			print '\n	Xenian Guard HP: %r || Daiy\'s HP: %r | Focus: %r | Energy: %r' %(self.guard_hp, self.health, self.focus, self.energy)
			print '	Dagger = -15E, +10F | Talent = -20F, +5E | Charge Energy/Focus = +10E, +20F\n '
			attack = raw_input('Ability > ')
			
			if self.health > 0:
				print '\n%s attacks Daiy for %r' %('Xenian Guard', self.guard_attack)
				self.health -= self.guard_attack
				sleep(1)
			
			if self.energy > 45:
				self.energy = 45
			
			if self.focus > 70:
				self.focus = 45
					
			if attack == 'talent' and self.focus >= 20:
				self.guard_hp -= self.player_talent + self.bonus
				self.focus -= 20
				if self.energy < 45:
					self.energy += 5
				print '\nYou Used your Psych, burning a hole in the Xenian Guard\'s mind  | DMG = %r + Bonus %r. (Uses 20 Focus, adds 5 energy)' %(self.player_talent, self.bonus)
			
			elif attack == 'dagger' and self.energy >= 15:
				self.guard_hp -= self.player_attack - self.bonus
				print '\nYou used your Dagger. It reflects off the Xenian Guard\'s armor. | DMG = %r - %r Resistance. (Uses 15 Energy, adds 10 Focus)' %(self.player_attack, self.bonus)
				self.energy -= 15
				if self.focus < 70:
					self.focus += 10
				if self.player_attack < 15:
					print '(These daggers are dull...)'
			
			elif attack == 'charge energy' and self.energy < 45:
				print '<<You Charge 10 Energy>>'
				self.energy += 10
				
			elif attack == 'charge focus' and self.focus < 70:
				print '<<You Charge 20 Focus>>'
				self.focus += 20
			
			elif attack == 'charge energy' and self.energy >= 45:
				print 'Your Energy is at Maximum.'
				
			elif attack == 'charge focus' and self.focus >= 70:
				print 'Your Focus is at Maximum.'
				
			elif attack == 'charge energy' and self.focus >= 70 and self.energy >= 45 or attack == 'charge focus' and self.focus >= 70 and self.energy >= 45:
				print 'All levels are at Maximum'
			
			elif attack =='dagger+talent' and self.focus >= 35 and self.energy >= 25 or attack == 'talent+dagger' and self.focus > 45 and self.energy > 25:
				rnd_atk = choice(self.dagger_talent)
				self.guard_hp -= rnd_atk
				self.focus -= 40
				self.energy -=25
				print '\nYou wield your Dagger and Talent together causing %r DMG. (Uses 40 Focus and 25 energy, adds nothing)' %rnd_atk
				if rnd_atk < 30:
					print 'This attack varies from strong to weak...'
				if self.focus < 40 or self.energy < 25:
					print 'You need 40 focus and 25 energy for dagger+talent.'
			
			elif attack == 'dagger+dagger' and self.energy >= 35:
				dual_low = choice(self.dual_weak)
				print 'You separate your Dagger, named Gog and Magog, in two. The deadly wield causes uses 35 Energy, and recharges nothing. | DMG %r - %r Resistance' %(dual_low, self.bonus)
				self.guard_hp -= dual_low - self.bonus
				self.energy -= 35
			
			elif attack == 'talent+talent' and self.focus >= 50:
				dual_high = choice(self.dual_strong)
				print 'You place your hands together and channeling Dual Psych Energy. (uses 50 Focus, adds nothing) | DMG %r + %r Bonus.' %(dual_high, self.bonus)
				self.guard_hp -= dual_high + self.bonus
				self.focus -= 50
				
			elif attack == 'vial h' and self.hitem > 0:
				print '\nYou squeeze the top off of a vial, the liquid chills your thoat replenishing your health.'
				self.health += self.hvial
				self.hitem -= 1
			
			elif attack == 'vial h' and self.hitem <= 0 or attack == 'vial fe' and self.sitem <= 0:
				print 'You have no Vials Left!'
			
			elif attack == 'vial fe' and self.sitem > 0:
				print '\nYou squeeze the top off of a vial, a warm fog engulfs your head streching your psyche, replenishing your focus and energy.'
				self.focus += self.svial
				self.energy += self.svial
				self.sitem -= 1
				
			elif attack == 'OP':
				self.guard_hp -= 265
			
			else:
				print '\nCheck you Energy/Focus Levels.'
				print 'hint: (no spaces in talent+dagger)'
		
		if self.guard_hp <= 0:
			print 'You have defeated the Xen Guard (Use Items to Recharge). Daiy\'s End-Battle HP: %r' %self.health
			print '\nThe guard\'s body shudders as the life drains from his eyes..'
			sleep(4)
			return self.room[0]
			
		elif self.health <= 0:
			del self.room[0]
			self.room.append('room_one')
			return 'death'
			
	def combat_system_2(self):
		'''Interactive Combat System for Daiy and Mindtalents'''
		
		print self.m_statements[randint(0,len(self.m_statements)-1)]
		sleep(1)
		print '\nInventory: HP Vial:%r | Talent Vial: %r' %(self.hitem, self.sitem)
		print '\n	MindTalent HP: %r || Daiy HP: %r | Focus: %r | Energy: %r' %(self.mind_hp, self.health, self.focus, self.energy)
		print '\n	<Command = Dagger for weapon, Talent for psych, Charge for Skills>'
		print '	<You can also use combos with command = Dagger+Talent etc.>\n'
		
		while self.health > 0 and self.mind_hp > 0:
			print '\nInventory: HP Vial:%r | Talent Vial: %r | use Vial FE or H to recharge' %(self.hitem, self.sitem)
			print '\n	MindTalent HP: %r || Daiy\'s HP: %r | FOCUS: %r | Energy: %r' %(self.mind_hp, self.health, self.focus, self.energy)
			print '	Dagger = -15E, +10F | Talent = -20F, +5E | Charge Energy/Focus = +10E, +20F\n'
			attack = raw_input('Ability > ')
			
			if self.health > 0:
				print '\n%s attacks Daiy for %r' %('Xenian MindTalent', self.mind_attack)
				self.health -= self.mind_attack
				sleep(1)
			
			if self.energy > 45:
				self.energy = 45
			
			if self.focus > 70:
				self.focus = 70
			
			if attack == 'talent' and self.focus >= 20:
				self.mind_hp -= self.player_talent - self.bonus
				self.focus -= 20
				if self.energy < 45:
					self.energy += 10
				print '\nYou used your Psych. It tears into the MindTalent | DMG = %r - %r Resistance. (Uses 20 Focus/Adds 10 Energy)' %(self.player_talent, self.bonus)
				if self.player_talent < 30:
					print '(Your Psyche feels stretched while up against another MindTalent..)'
			
			elif attack == 'dagger' and self.energy >= 15:
				self.mind_hp -= self.player_attack + self.bonus
				self.energy -= 15
				if self.focus < 70:
					self.focus += 20
				print '\nYou used your Dagger! It tears into the MindTalent | DMG = %r + %r Bonus. (Uses 15 Energy/Adds 20 Focus)' %(self.player_attack, self.bonus)
				
			elif attack == 'charge energy' and self.energy < 45:
				print '<<You Charge 10 Energy>>'
				self.energy += 10
				
			elif attack == 'charge focus' and self.focus < 70:
				print '<<You Charge 20 Focus>>'
				self.focus += 20
			
			elif attack == 'charge energy' and self.energy >= 45:
				print 'Your Energy is at Maximum.'
				
			elif attack == 'charge focus' and self.focus >= 70:
				print 'Your Focus is at Maximum.'
				
			elif attack == 'charge energy' and self.focus >= 70 and self.energy >= 45 or attack == 'charge focus' and self.focus >= 70 and self.energy >= 45:
				print 'All levels are at Maximum'
			
			elif attack == 'dagger+talent' or attack == 'talent+dagger' and self.focus > 40 and self.energy > 25:
				rnd_atk = choice(self.dagger_talent)
				self.mind_hp -= rnd_atk
				self.focus -= 40
				self.energy -= 25
				print '\nYou dual wield Dagger and Talent causing %r damage, (Uses 40 Focus and 25 engery, adds nothing)' %rnd_atk
				if rnd_atk < 30:
					print 'This attack varies from strong to weak...'
				if self.focus < 40 or self.energy < 25:
					print 'You need 40 focus and 25 energy for dagger+talent.'
			
			elif attack == 'dagger+dagger' and self.energy >= 35:
				dual_high = choice(self.dual_strong)
				print '\nYou separate your Dagger, aptly Gog and Magog, in two. The deadly wield causes (Uses 25 Energy, adds nothing) | DMG: %r + %r Bonus' % (dual_high, self.bonus)
				self.mind_hp -= dual_high + self.bonus
				self.energy -= 35
			
			elif attack == 'talent+talent' and self.focus >= 50:
				dual_low = choice(self.dual_weak)
				print 'You form your hand together and trace out Dual Psych Symbols. (uses 50 Focus). DMG: %r - %r Resistance.' %(dual_low, self.bonus)
				print 'Appears to be weak against MindTalents.'
				self.mind_hp -= dual_low - self.bonus
				self.focus -= 50
			
			elif attack == 'vial h' and self.hitem > 0:
				print '\nYou squeeze the top off of a vial, the liquid chills your thoat replenishing your health.'
				self.health += self.hvial
				self.hitem -= 1
			
			elif attack == 'vial h' and self.hitem <= 0 or attack == 'vial fe' and self.sitem <= 0:
				print 'You have no Vials Left!'
			
			elif attack == 'vial fe' and self.sitem > 0:
				print '\nYou squeeze the top off of a vial, a warm fog engulfs your head streching your psyche, replenishing your focus and energy.'
				self.focus += self.svial
				self.energy += self.svial
				self.sitem -= 1
			
			elif attack == 'OP':
				self.mind_hp -= 165
			
			else:
				print '\nCheck you Energy/Focus Levels.'
				print 'hint: (no spaces in combos [i.e. talent+dagger])'
		
		if self.mind_hp <= 0:
			print 'You have defeated the Xen MindTalent (Use Items to Recharge). Daiy\'s End-Battle HP: %r' %self.health
			print '\nThe ground shakes as a bright light engulfs the MindTalent. He implodes with his focus energy..'
			sleep(4)
			return self.room[0]
		
		elif self.health <= 0:
			del self.room[0]
			self.room.append('room_one')
			return 'death'
			
	def intro(self):
		skip = raw_input('Press S to Skip intro (Don\'t press if Noobie!) > ')
		if skip == 'S':
			return 'room_one'
		print '			<< 7Wars...The preclude to a beginning >> \n'
		print 'This is a simple text based adventure...just enter the text and hope the script recognizes it. Just remeber that all choices will be Capitalized such as...\n'
		raw_input ('It will look Just like this...where just is the command <Press Enter>')
		print '\nOther than that you have the option to always go back to previous rooms. You can also use items while out of combat. Enjoy!\n'
		begin = raw_input('Ready to Embark? (Y/N) > ')
		if begin == 'Y' or begin == 'y':
			print 'Let\'s Begin!!!\n\n\n\n'
		elif begin == 'N' or begin == 'n':
			print 'Too bad! You\'re gonna start anyways.\n\n\n\n'
		print 'It was a clear night, you could smell rain on the air...'
		sleep(3)
		print '\nBelow you could feel the your village sleep, the slow rise and fall of breath calmed the night...it was peaceful...'
		sleep(6)
		print '\nSeven years ago things were always peaceful..but now things had changed.'
		print 'Ever since Hydra Alpha appeared in the sky, brighter than any star...'
		sleep(6)
		print '\nFor ages religions across the world predicted the end of our planet, who knew they would be right.'
		sleep(6)
		print '\n*You look at the quiet Xenos village, Cheron*'
		print '\nXenos and the Nara have existed peacfully for generations, as much as any species could sharing a planet. However, these wars were unprecedented. Violent and terrible. Certainty in the face of death could do that.'
		sleep(6)
		raw_input('\nOur mission was simple, to discover how to protect Nara cities from the omnipotent Alpha Hydra. This of course meant using \'Talents\'. <Press Enter>')
		print '\nThe Factory, the center of most villages must be where the Talents are...where the secret lies.'
		sleep(4)
		print '\n"Daiy, we have to make way to the factory don\'t we?" muttered Cade'
		sleep(4)
		print '\n*You nod your head*'
		sleep(3)
		print 'Ever since Alpha Hydra shown itself the night sky had been dimly lit. Outlined in the light were two paths to the Factory. One through the sewers the other through a hidden stone walkway.'
		sleep(3)
		return 'room_one'
		
	'''Main Room'''
	def room_one(self):
		while True:
			self.hitem = 2
			self.sitem = 2
			print '\nShould you choose the Walkway or the Sewers?'
			entrance = raw_input ('> ')
			if entrance == 'Walkway' or entrance == 'walkway':
				return 'walkway'
				break
			elif entrance == 'Sewers' or entrance == 'sewers':
				return 'sewers'
				break
			elif entrance == 'Back' or entrance == 'back':
				print 'Do you want to exit (Yes/No)?'
				exit = raw_input ('> ')
				if exit == 'Yes' or exit == 'yes':
					exit(0)
				elif exit == 'No' or exit == 'no':
					return 'room_one'
				else:
					print 'I assume you mean "No".'
					return 'room_one'
			else:
				print '\nYou wait a few seconds, trying to decide which path is best.'
				return 'room_one'
			
	'''Starting Area 1'''	
	def sewers(self):
	
		print '\nYou walk up to the large sewer drain and pry open the grate. Cade walks around the side to the walkway.'
		print """\nYou see a long dark corridor, the sound of running water was almost overwhelming. You could make out the frame of two doors on the north side of the stone wall."""
		while 1:
			print ('Should you open the First or Second door?')
			door = raw_input ('> ')
			if door == 'First' or door == 'first':
				return 'sewer_door1'
				break
			if door == 'Second' or door == 'second' and self.door2close == False:
				return 'sewer_door2'
				break
			elif door == 'Second' or door == 'second' and self.door2close == True:
				print 'You step back up to the second doorway...but the ceiling collaspe. Could our battle have caused that?' 
			elif door == 'Back' or door == 'back':
				return 'room_one'
				break
			else:
				print '\nYou listen intently to the running water...'
				
	'''Corridor_Sewer'''
	def sewer_door1(self):
		
		global guard_alive
		print 'You walk up to the door but suddenly you head starts to ache. Your Psyche Talent pushes its way into your consciousness.'
		while 1:
			print 'Your Talent shows you an outline of the next room, in it a Xenian. Should you Open the door for a quick ambush or use your Mindform ability?'
			attack = raw_input('> ')
			if attack == 'Mindform' or attack == 'mindform':
				print '\nYou use your Mindform ability pushing into the mind of the guard. Slowly you feel his body slump to the ground, his mind fades.'
				guard_alive = False
				sleep(2)
				print '\nYou can now Open the door safely.'
				open = raw_input('> ')
				if open == 'Open' or open == 'open' and guard_alive == False:
					del self.room[0]
					self.room.append('corridor_sewer')
					return 'guards'
				else:
					return 'guards'
			elif attack == 'Open' or attack == 'open':
				print 'Pushing your Talent aside you prepare to ambush the Xenian...\n'
				self.room.append('corridor_sewer')
				return 'guards'
			else:
				print 'The guards\' outline fades...but your focus returns.\n'
				sleep(1)
	
	'''Walkway_Path 1'''
	def sewer_door2(self):
		'''This is where I attempt to break up linear game play'''
		
		print 'You step up to the second door, the rusty surface feels rough under your hand. Should you focus your psych Talent to feel for enemies or Open the door?'
		door = raw_input ('> ')
		
		while 1:
			if door ==  'Talent' or door == 'talent':
				print '\nYou search out with your mind to feel any enemies, you don\'t feel anything living. You push into the room and notice two vials one the groud. "Health and FE vials..." you say to no one in particular.'
				print '\n* You gained one Health Vial and one Focus/Energy Vials*\nUse the Vial H/FE command to replenish full health or focus.\n'
				if self.hvial or self.svial > 2:
					self.hvial += 1
					self.svial += 1
				else:
					print 'You don\'t have enough pouches to hold all these...'
				sleep(2)
				print '\nShould you Open the door in front of you or head Back to the Sewers?'
			
			if door == 'vial h' and self.hitem > 0:
				print '\nYou squeeze the top off of a vial, the liquid chills your thoat replenishing your health.'
				self.health += self.hvial
				self.hitem -= 1
			
			if door == 'vial fe' and self.sitem > 0:
				print '\nYou squeeze the top off of a vial, a warm fog engulfs your head stretching your psyche, replenishing your focus and energy.'
				self.focus += self.svial
				self.energy += self.svial
				self.sitem -= 1

				door1 = raw_input('> ')
				if door1 == 'Open' or door1 == 'open':
					print 'You decide to go through the rusted door in front of you.. the sound of the sewer\'s water fading with each step.'
					return 'walkway_path1'
				if door1 == 'Back' or door1 == 'back':
					print '\nYou decide to go back to the sewers.'
					return 'sewers'
				else:
					print 'You hesitate as you decide to open the door or leave.'
		
		while 1:
			if door == 'Open' or door == 'open':
				print '\nYou push open the door, the sound of years grating in the hinges. You glance around the room and notice nothing but a door at the far side of the room.'
				sleep(1)
				print 'Should you Open the door in front of you or head Back to the Sewers.'
				door2 = raw_input('> ')
				if door2 == 'Open' or door2 == 'open':
					print 'You decide to go through the door in the back, the sound of the sewer\'s running water fading.'
					return 'walkway_path1'
				elif door2 == 'Back' or door2 == 'back':
					print '\nYou decide to go back to the sewers.'
					return 'sewers'
				else:
					print 'You hesitate as you decide to open the door or leave.'
	
	'''Starting Area. Goes to Corridor_Walkway'''
	def walkway(self):
		
		print 'You step into a large walkway, metal grates cover the ground as water passes underneath. There is a strong wind current in this room propelled by a large fan opposite side of the room. Sitting on both sides of the narrow walkway lie two turbines sitting motionless to the left and to the right.\n'
		print 'Usually these fan rooms cool of large vectors of generators...the center of the factory must be close but how to get to it?\n'
		print '*The ground shakes softly, the tremor seems to challenge the strength of the foundation*\n'
		print '"Alpha Hydra is getting closer to our planet every minute...we need to find this protection talent" you thought aloud.\n'
		print 'Should you move through the Right fan, Left fan, or Back to the sewers?\n'
		door = raw_input('> ')
		
		while True:
			if door == 'Right' or 'right':
				print '\nYou walk along the right side of the railing, hand grazing over the damp texture. Suddenly your mindmeld starts to pulsate in your mind, the ache intensifies. Should you use your Mindmeld talent or Open the door?\n'
				fan_1 = raw_input('> ')
				while True:
					if fan_1 == 'Open' or fan_1 == 'open':
						print '\nYou push your talent out of your mind and open the door.'
						del self.room[0]
						self.room.append('corridor_walkway')
						return 'guards'
					if fan_1 == 'Mindmeld' or fan_1 == 'mindmeld':
						print 'You place your hand against your temple...slowly the outline of a Xenian guard slowly fades into your mind. *Sweat builds on your brow*\n'
						sleep(1)
						print 'Gently you push into the mind of the Xenian...abruptly you violently tear apart his mind...his consciousness disappears'
						print 'You walk up to the door and step into another narrow corridor.'
						return 'corridor_walkway'
					else:
						print 'The talent trembles in your thoughts but you force your focus.'
			
			elif door == 'Back' or door == 'back':
				print 'You step back into the previous room.\n'
				return 'room_one'
			
			elif door == 'Left' or door == 'left':
				print '\nYou walk through the fan on the left side of the room, pushing the blades slowly out of the way. Suddenly feeling very vulnerable to any sudden updrafts.\n'
				print 'You look around the room and notice a crack in the wall, light flooding in from Alpha Hydra. How could a rock dictate the outcome of so many lives?\n'
				print 'As you glance from the large crack you notice a small chest in the corner of the room...maybe there is something useful in there.\n'
				print '\nShould you Open the chest or go Back to the main room?'
				fan_2 == raw_input('> ')
				
				while True:	
					if fan_2 == 'Back' or fan_2 == 'back':
						print 'You decide to leave the chest where its at and walk back into the antechamber.'
						return 'walkway'
					elif fan_2 == 'Open' or fan_2 == 'open' and self.hitem > 4 or self.sitem > 4:
						self.hitem =+ 2
						self.sitem =+ 1
						print '\nYou walk up to the chest and pry it open finding a couple of health vials and one energy vial...these will come in handy if I run into any guards.\n'
						print 'You have %r HP vials and %r focus/energy vials.'
						raw_input ('<Press Enter When Done>')
						print 'Turning around you walk back into the main walkway.'
						return 'walkway'
					elif fan_2 == 'Open' or fan_2 == 'open' and self.hitem < 4 or self.sitem < 4:
						print '\nUnfortunately you don\'t have enough pouches to carry this many vials...a pitty truly.'
						print '\nYou have no choice but to go back to the walkway.\n'
						return 'walkway'
					else:
						print 'You hesitate in making a decision.'
			
			else:
				print 'You lose yourself in the air currents...slowly you thoughts are brought back to the present.'
		
		'''Walkway_Return'''
	
	def walkway_path1(self):
		
		self.door2close = True
		print 'You walk onto a narrow pathway water spilling out over the edge of some unseen cliff, the ground fading into darkness hundreds of feet down.'
		print 'You glance up and notice cade sitting on the ground, pulling his sword out of some unsuspecting Xenian.'
		print 'Have you found the central hub?'
		sleep(1)
		print 'Cade: "Nothing yet Daiy. I did find a schematic for the electric grid. There is a shield surrounding the factory core, I think we have to disable that source."'
		print '"There\'s a second pathway up ahead, I think thats where the Source Talent is stored" Cade muttered, almost to himself.'
		print 'Ok I\'ll head to the... *You Glance Towards the second walkway, your Mindmeld starts to lightly burn in your mind* Should you go through the Second walkway or go Back the way you came?'
		door = raw_input('> ')
		
		if door == 'Second' or door == 'second':
			print 'You walk past Cade glancing at the wounds he had sustained...just more suffering...'
			print 'Suddenly you mindmeld forces your focus as two Xenians step from the shadows waiting for you to be off your guard...You back up to Cade, already preparing the talent tracings. You unsheathe your dagger.'
			del self.room[0]
			self.room.append('walkway_return')
			return 'guards'
			
		elif door == 'vial h' and self.hitem > 0:
			print '\nYou squeeze the top off of a vial, the liquid chills your thoat replenishing your health.'
			self.health += self.hvial
			self.hitem -= 1
			
		elif door == 'vial fe' and self.sitem > 0:
			print '\nYou squeeze the top off of a vial, a warm fog engulfs your head stretching your psyche, replenishing your focus and energy.'
			self.focus += self.svial
			self.energy += self.svial
			self.sitem -= 1
			
		elif door == 'Back' or door == 'back':
			print 'You don\'t think going back is the right thing to do now...There could be more guards...and your last fight left you drained.'
		
		elif door == 'Mindmeld' or door == 'mindmeld':
			print 'Vaguely outlined you see two guards preparing for you..'
			print 'Slowly you warn Cade about the oncoming attack...both of you prepare you defenses giving you +150 health and full energy/focus.'
			self.energy = 45
			self.focus = 70
			self.health + 150
			del self.room[0]
			self.room.append('walkway_return')
			return 'guards'
		else:
			print 'The last battle must have affected you more that you realized...you re-focus on the situation.'
	
	'''returning to walkway starting area or 2 after the guard fight with Cade, '''
	def walkway_return(self):
		
		print '\nYou push over the Xenian\'s body the heavy weight of the equipment quickly causes him to fall to the ground.'
		print 'From afar you hear a loud crash...something has collaspe...could our talents have done that??'
		sleep(1)
		print 'Glancing over at cade you realize he is nursing his right hand, the bone slightly deformed.'
		print '"You should head back to the others" you muttered, caution...friends were more important than...'
		sleep(2)
		print '\nCade: "Daiy..."\n It\'s important that we continue on...I can\'t go back now...we have to protect our people from Alpha Hydra.'
		print 'You examine your companion...admire his bravery. If you were in the same situation you might of...*You walk over to Cade helping him to his feet*'
		sleep(2)
		print '"\nIf it had been different times we wouldn\'t have to be here now...we could be happier" Cade said disdainfully.'
		print '"One day..." then you look at Cade, giving a strong nod, and head towards the walkway while he split off into the opposite direction.'
		door = raw_input('\nReturn to the Second Walkway or the one leading to the Generator?')
		while True:
		
			if door == 'One' or door == 'one':
				print 'You head back to the main hallway...to find this generator.'
				return 'walkway_path2'
			elif door == 'Two' or door == 'two':
				print 'You walk up to the railing side and leap to the narrow sewer-way.'
				return 'corridor_sewer'
			else:
				print 'You wait a second, waiting for the right moment.'
	
	
	'''Walkway'''
	def walkway_path2(self):
		print '\nYou step onto a large pathway...you could hear the fall of water far in the distance.\n'
		print 'As you look to the right you notice a large glass dome...inside it three spinning gears pulsating a pale-bluish light.\n'
		print 'That must be the generator\n.'
		print 'The large center of the machine proved the mastery needed for such a device. Its electrical currents extended far upon the shaft of the machine...up to the rafters fading off into the darkness of the night..\n'
		sleep(2)
		print 'You notice a patrol walking around the generator...that will prove hard to get past.\n'
		print 'There also seems to be a pattern to their movement...it might be best to sneak by this patrol when we find the doorway to the generator.\n'
		print 'You glance around the narrow walkway and notice a small hole in the wall...leading into a room beyond. Should you Walk through the door or continue Forward?\n'
		door = raw_input(' >')
		while True:
			if door == 'Walk' or door == 'walk':
				print '\nYou crouch down and swing your body into a narrow room. In front of you is a small chest...should you Open the chest or head Back?'
				door_2 == raw_input(' >')
				while True:	
					if door_2 == 'Open' or door_2 == 'open':
						print '/nYou walk up to the chest but you hear a loud click. A bright light flashes and strikes you body causing %r damage.\n' %self.bonus
						self.health =- self.bonus
						print 'You writhe in agony as the pain in your chest subsides. Slowly you roll back out of the room.\n'
						print 'Gaining your bearings you step forward off the secondary walkway onto a grated platform.'
						return 'walkway'
					elif door_2 == 'Back' or door_2 == 'back':
						print 'You step back out of the small hole in the wall. Quickly you jump off the secondary platform and onto a grated walkway.'
						return 'walkway'
			elif door == 'Forward' or door == 'forward':
				print '\nQuickly you step forward into a small opening leading to a wind cooling room.\n'
				return 'walkway'
	
	'''Walkway path2'''
	def corridor_sewer(self):
		
		print '\nYou step into a narrow sewer hallway, water rushing around your leather boots. Above you you can see the glow from Alpha Hydra leak through the cracks. "It amazing this place has held together this long." you mutter to yourself.'
		sleep(2)
		print '\nTo your right lies a map outlining the sewer treatment facility.\n'
		print ' _ENTRANCE_______________________'
		print '|      _    |~~~|                |'
		print '|    _| |___|~~~|      SWR       |'
 		print '|____|      |~~~|      LVL       |'
 		print '|__   X     |~~~|       2        |'
 		print '|~~|    (M) |~~~|________________|'
 		print '|~~|  _     |~~~|    _____ GEN   |'
 		print '|~~|_| |____|__~|    |===|       |'
 		print '|~~|________   ||________________|'
 		print '|~~~~~~~~~~|   | Current Position: X'
 		print '|__________|   |'
 		sleep(4)
 		print '\nYou can recharge your talents with "meditate" in this room.\n'
 		print 'Looks like there are two doors, [One] on the left and [Two] the other in front of you. There also is a Mediation circle that recharges your Talents.'
 		print 'You notice that the generator room seems to have some importance. Maybe, if the electricity is shut off then the Talent energy protecting the Central Factory would be shut off? But how do you get there?\n'
 		sleep(1)
 		while 1:
 		
 			sewer_door = raw_input('\nDoor One or Two? >')
 			if sewer_door == 'door one' or sewer_door == 'one':
 				print '\nYou step up to the right door, you Mindmeld burns in your consciousness but its effect is lost on the water'
 				print '\nYou walk through the door to see what is beyond.'
 				sleep(4)
 				del self.room[0]
 				self.room.append('walkway_path2')
 				return 'guards'
 			
 			elif sewer_door == 'Meditate' or sewer_door == 'meditate':
 				print 'You feel the world inside your mind, you can see beyond the 7 Wars and the Suns. You feel reinvigorated.'
 				self.health = 400
 				self.energy = 45
 				self.focus = 70
 	
 			elif sewer_door == 'door two' or sewer_door == 'two':
 				print '\nYou walk past the first door, feet sloshing in the water as it runs underneath the walkway grates.'
 				print '\nYou walk up to the door directly in front of you, you can hear wind blowing against the door as it lightly closes and opens. You pull the door open and step out onto a walkway.'
 				sleep(4)
 				del self.room[0]
 				self.room.append('sewer_generator')
 				return 'guards'
 				
 			elif sewer_door == 'vial h' and self.hitem > 0:
				print '\nYou squeeze the top off of a vial, the liquid chills your thoat replenishing your health.'
				self.health += self.hvial
				self.hitem -= 1
			
			elif sewer_door == 'vial fe' and self.sitem > 0:
				print '\nYou squeeze the top off of a vial, a warm fog engulfs your head streching your psyche, replenishing your focus and energy.'
				self.focus += self.svial
				self.energy += self.svial
				self.sitem -= 1
 			
 			elif sewer_door == 'Back' or sewer_door == 'back':
 				print 'Are you sure you want to go back to the Central Sewer Main?'
 				back = raw_input('Y/N >')
 				if back == 'yes':
 					return 'sewers'
 				else:
 					print 'You head aches.'
 			else:
 				print 'The water dulls your abilities, Talents seem to have some interruption when surrounded with running water...'
 		
 	'''Pathway to the final room // Sewers'''
	def corridor_walkway(self):
		
		print '\nYou step from the main walkway to a narrow grated hall. You notice that the sudden feelin of intoxication overwhelms you...the spiraling of the room almost knocks you off balance.\n'
		print 'As you mind settles you notice a large doorway surrounded by a bright electrical shield, chaotic in it\'s orderliness. This must be where the talent is...the grid preventing entry.\n'
		print 'There must be some power source...\n' 
		print 'Underneath the metal floor grates you notice an opening, a brick layout resembling the sewer. "The circularity of this place is astonishing" you muse. Kneeling down you lift the grate, grunting at the effort. Across a pool of water you could dimly see the other side.\n'
		print 'Should you attempt to Open the large doorway, go Back to the walkway or head into the Sewers?'
		door = raw_input('> ')
		
		while True:
			if door == 'Open' or door == 'open' and self.generator == False:
				print '\nYou walk up to the doorway and place your hands lightly upon the electrical curent, your Talent bent on understanding its chaotic flow. You reach through the current and shut off the generator...the layout now lying clearly in your mind.\n'
				print 'As the current slows to a peaceful glow Cade joins you at your side. Together you look towards the door then at each other...both of you knew this was the moment.\n'
				print 'Cade steps through the door with you quickly on his heels.'
				return 'final_room'
			elif door == 'Open' or door == 'open' and self.generator == True: 
				print 'The electrical current is too powerful for you to control...you need to understand the energy source before you can attempt to control the stream.\n'
				print 'You take a step back and walk into the sewers to find the generator.'
				return 'sewers'
			elif door == 'Sewers' or door == 'sewers':
				print 'You decide to head towards the sewers...maybe the energy source is this way.'
				return 'sewers'
			elif door == 'Back' or door == 'back':
				print 'Quickly you jog back to the main walkway eager to find another way.'
				return 'walkway'
			else:
				print 'You stay kneeled for a moment recharging your energy.'
	
	'''Walkway'''
	def sewer_generator(self):
		print '\nYou walk into a large antechamber, a loud humming noise pulsates from the room in front of you. You pull out your hands and sense the generator in the next room.\n'
		sleep(1)
		print 'There is a patrol of five Xenians...*there\'s no way we can get past that*\n'
		print 'As you hold out your hands you can feel the guards minds. None of them mindtalents\n'
		print '*Maybe this will work*\n'
		sleep(1)
		print 'Slowly you turn your hands inward and cast Mindmolt...a slow warm feeling engults your body removing yourself from the sight of the 5 guards within the room.\n'
		print 'You open the door slightly, sliding your body into the room with the generator.\n'
		print 'In the middle stands the massive machine...the teal bluish light flooding the room engulfing everything.\n'
		print 'All you need to do is touch it...to feel out its current...to control its power.\n'
		sleep(1)
		print 'Quickly you avoid the guards and place a hand on the machine...you can see its complete layout...you know how to get past the energy fields it emits.'
		sleep(1)
		return 'walkway'
		
	'''Collecting the Final Talent'''
	def final_room(self):
		print 'Daiy walks into a large room...the ceiling electrified tracing out talent markings...in the center stands three Xenians, two powerful Mindtalents and a Iicik Guard.'
		sleep(1)
		print 'Isis..we have two Nara\'s apporaching us..'
		print 'Isis gazes into Cades eyes...the color draining from it.'
		sleep(2)
		print 'Congrats you reached the end of the game! In the future I\'ll make this into a 2D SideScroller. Then we will find out what happens to Daiy and Cade!'
		print 'Thank you for playing!'
		sleep(2)
		exit(0)
		

wars = Game('intro')
wars.play()