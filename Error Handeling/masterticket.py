TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100 

def calculate_price(amount):
	return (TICKET_PRICE * amount) + SERVICE_CHARGE

while tickets_remaining >= 1:
	print("There are {} tickets remaining.".format(tickets_remaining))
	name = input("What is your name: ")
	try:
		ticket_amount = int(input("Hey {}! How many tickets you would like to purchase? ".format(name)))
		if ticket_amount > tickets_remaining:
			raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
	except ValueError as err:
		# Include the error text in the output
		print("There was an issue. {}. Please try again...".format(err))
	else:
		price = calculate_price(ticket_amount)			   
		print("Total: ${}".format(price))
		proceed = input("Do you want to proceed the order? (Y/N) ")
		if proceed.lower() == 'y':
			# TODO: gather credit card information and process it.
			print("SOLD!")
			tickets_remaining -= ticket_amount
		else:
			print("Thank you for being with us, {}!".format(name))
print("Whoops.. Tickets has been sold out!")