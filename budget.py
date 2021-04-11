from time import sleep

budget_database = [] # an array for storing all budject objects


class Budget(object):
	def __init__(self, category, balance):
		self.category = category
		self.balance = balance


	def withdraw(self, amt):
		if amt <= self.balance:
			if amt <= 0:
				print('Cannot withdraw this amount')
			else:
				print('Processing...\n')
				sleep(3)
				self.balance -= amt
				print('Take your cash!')
				print("New category balance is =N= {}".format(self.balance))
		else:
			print('Insufficient fund')

	def transfer(self, category, amt):
		if amt <= 0:
			print('Cannot transfer this amount!')
		else:
			if amt <= self.balance:
				print('Processing...')
				sleep(3)
				self.balance-=amt
				category.balance += amt
				print('Transfer was succesfull!') 
				print("New category balance is =N= {}".format(self.balance))
			else:
				print("Insufficient fund!")

		return category



	def deposit(self, amt):
		if amt <= 0 or amt > 50000:
			print('Amount not within acceptable range!')
		else:
			print('Processing...')
			sleep(3)
			self.balance+=amt
			print("Succesfull!")
			print("New category balance is =N={}".format(self.balance))

	def get_balance(self):
		print('\n The balance for {} category is =N= {}'.format(self.category, self.balance))



def input_integer(info, err_msg):
	try:
		integer = int(input(info))
	except:
		integer = 0
		print(err_msg)

	return integer



def verify_budget(database, category):
	for budget in database:
		if category == budget.category:
			return budget
	return None


def update_budget(mod_category):
	for i, u in enumerate(budget_database):
		if mod_category.category == u.category:
			del budget_database[i]
			break

	budget_database.insert(i, mod_category)

def process_budget(category):
	play = 'y'
	while play=='y':
		print('\n Budget : {} \t\t Balance: {} \n'.format(category.category, category.balance))
		print('1. Withdraw \t\t 3.Deposit \n')
		print('2. Transfer \t\t 4.See Balance \n')

		option = input_integer('Select an option: ', '\n Invalid input! \n')

		if option == 1:
			amt = input_integer('Enter amount to withdraw:\n =N= ', 'Invalid amount entered')
			category.withdraw(amt)
			update_budget(category)
			play = input("Do you want to perform another operation on budget {}? (y/n)\n".format(category.category))
		elif option == 2:
			cat = input('Enter category you want to transfer to:\n')
			cat = verify_budget(budget_database, cat)
			if cat is not None:
				amt = input_integer('Enter amount to transfer \n =N= ', 'Invalid amount entered')
				cat = category.transfer(cat, amt)
				update_budget(category)
				update_budget(cat)
			else:
				print('Invalid category selected!')
			play = input("Do you want to perform another operation on budget {}? (y/n)\n".format(category.category))
		elif option == 3:
			amt = input_integer('Enter amount to deposit\n =N= ', 'Invalid amount entered')
			category.deposit(amt)
			update_budget(category)
			play = input("Do you want to perform another operation on budget {}? (y/n)\n".format(category.category))
		elif option == 4:
			category.get_balance()
			play = input("Do you want to perform another operation on budget {}? (y/n)\n".format(category.category))
		else:
			print("Invalid option!\n")
			play = 'y'

def create_budget(budget_cat):
	balance = input_integer("Enter amount for the category:\n", "Invalid amount entered\n")

	if balance < 0:
		print('Invalid amount selected. Setting balance to zero!')
		balance = 0

	budget = Budget(category=budget_cat, balance=balance)
	budget_database.append(budget)
	print('\n Budget {} created succesfully!\n'.format(budget_cat))


def main():
	play = 'y'

	while play == 'y':

		print('Welcome to Zuri Budget handler\n')

		print('1. Create a budget \t\t 2.Select a budget \n')

		option = input_integer('Select an option: ', '\n Invalid input! \n')

		if option == 1:
			budget = input('Enter category of budget:\n')
			category = verify_budget(budget_database, budget)

			if category is None:
				create_budget(budget)
				play = input("Do you want to perform another operation on another budget? (y/n)\n")
			else:
				print('Category selected already exist!')
				play = input("Do you want to perform another operation on another budget? (y/n)\n")
			
		elif option == 2:
			budget = input('Enter category of budget:\n')
			category = verify_budget(budget_database, budget)

			if category is not None:
				process_budget(category)
				play = input("Do you want to perform another operation on another budget? (y/n)\n")
			else:
				print('Invalid category selected!')
				play = input("Do you want to perform another operation on another budget? (y/n)\n")

		else:
			print('Invalid option selected!')
			play = input("Do you want to perform another operation on another budget? (y/n)\n")



		
# ============== Testing ======================================

if __name__ == '__main__':

	# add some budgets into the database
	budget_database.append(Budget(category='food', balance=10000))
	budget_database.append(Budget(category='drinks', balance=20000))
	budget_database.append(Budget(category='cloths', balance=50000))

	main()






	

