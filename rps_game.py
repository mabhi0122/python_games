import random

while True: # it's continuously playing until keybord interrupts
	def play():
		user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
		computer = random.choice(['r', 'p', 's'])

		if user == computer:
			return 'It\'s a tie' 

		# r > s, s > p, p > r
		if is_win(user, computer):
			return 'You won!'

		return 'You lost!'


	def is_win(user,opponant):
		# returns true if the player wins
		# r > s , s > p , p > r

		if (user == 'r' and opponant == 's') or (user == 's' and opponant == 'p') or (user == 'p' and opponant == 'r'):
			return True

	print(play())