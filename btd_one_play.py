from random import shuffle
from random import randint

suit = range(1,13)
deck = []

for i in suit:
	for n in range(0,4):
		deck.append(i)

shuffle(deck)

stacks = deck[0:9]
cards_in_play = deck[9:]

def eval_call(faceup, drawn):
	outcome = None
	midpoint = 8
	my_call = "ABOVE"
	if faceup > midpoint:
		my_call = "BELOW"
	elif faceup == midpoint:
		if randint(1, 101) < 50:
			my_call = "BELOW"
	#print(my_call)
	if my_call == "BELOW":
		if drawn < faceup:
			outcome = drawn
	else:
		if drawn > faceup:
			outcome = drawn
		else:
			outcome = None
	print(faceup)
	print(my_call)
	print(drawn)
	print("----")
	return outcome

def next_card(playing_deck):
	cards_left = len(playing_deck)
	if cards_left > 0:		
		new_card = playing_deck[0]
		new_deck = playing_deck[1:]
	return new_card, new_deck

counter = 1

for stack in stacks:
	print("starting deck " + str(counter))
#	print(stack)
#	print(eval_call(stack,1))
	status = "LIVE"
	while status == "LIVE":
		#print(type(cards_in_play))
		if len(cards_in_play) == 0:
			status = "WIN"
			break
		next_card_cur, cards_in_play = next_card(cards_in_play)
		#print(stack)
		stack = eval_call(stack, next_card_cur)
		#print(next_card_cur)
		if type(stack) == type(None):
			status = "NEXT"
	if len(cards_in_play) == 0:
		print("WIN")
		break
	counter += 1

print(str(len(cards_in_play))+ " cards remaining")
'''

		stack = eval_call(stack, next_card(cards_in_play)[0])
		if len(cards_in_play) == 0:
			print("winner")
			status == "win"
		elif type(stack) == type(None):
			status == "next deck"
			print(status)
'''

