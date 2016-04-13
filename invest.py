def invest(amount, rate, time):
	print("principal amount: $", amount)
	print("annual rate of return:", rate)
	for year in range(0, time):
		amount = amount + (rate * amount)
		print("year",year +1,":",amount )


invest(100, .05, 8)
invest(2000, .025, 5)

