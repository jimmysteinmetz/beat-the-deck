from random import shuffle
from random import randint
import csv
import pandas

deck_count = range(1,26)
win_pct_sims = []

for count in deck_count:

	wins = 0
	simulations = 1000000
	cards_remaining_list = []

	logging = "n"

	for deal in range(0,simulations):
		print(deal)
		suit = range(2,14)
		deck = []

		for i in suit:
			for n in range(0,4):
				deck.append(i)

		shuffle(deck)

		stacks = deck[0:count]
		cards_in_play = deck[count:]

		def eval_call(faceup, drawn):
			outcome = None
			midpoint = 8
			my_call = "ABOVE"
			if faceup > midpoint:
				my_call = "BELOW"
			elif faceup == midpoint:
				if randint(1, 101) < 50:
					my_call = "BELOW"
			if my_call == "BELOW":
				if drawn < faceup:
					outcome = drawn
			else:
				if drawn > faceup:
					outcome = drawn
				else:
					outcome = None
			if logging == "y":
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
			if logging == "y":
				print("starting deck " + str(counter))
			status = "LIVE"
			while status == "LIVE":
				if len(cards_in_play) == 0:
					status = "WIN"
					break
				next_card_cur, cards_in_play = next_card(cards_in_play)
				stack = eval_call(stack, next_card_cur)
				if type(stack) == type(None):
					status = "NEXT"
			if len(cards_in_play) == 0:
				if logging == "y":
					print("WIN")
				wins += 1
				break
			counter += 1
		cards_remaining_list.append(len(cards_in_play))
		if logging == "y":
			print(str(len(cards_in_play))+ " cards remaining")

	simulation_result = (count, wins, simulations)
	win_pct_sims.append(simulation_result)

	#print(str(wins) + " wins over")
	#print(str(simulations) + " simulations")
	#print(cards_remaining_list)

win_pct_sims_df = pandas.DataFrame(win_pct_sims)

print(win_pct_sims)

csvfile = "win_pct_sims.csv"

win_pct_sims_df.to_csv(csvfile)

'''
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in win_pct_sims:
        writer.writerow([val])    
'''