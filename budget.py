
class Category:
#	title=""
#	ledger=[]
	def __init__(self,c):
		self.title=c
		self.ledger=[]
		
	
	def __str__(self):
		
		#A title line of 30 characters where the name of the category is centered in a line of * characters.

		texto=self.title.center(30,'*')+"\n"
		for item in self.ledger:
			if len(item["description"])<=23:
				texto += item["description"].ljust(23)
			else: texto += item["description"][0:23].ljust(23)
			texto += "{:0.2f}".format(item["amount"]).rjust(7)+ "\n"
		return texto.strip() + "\n" + "Total: " + "{:0.2f}".format(self.get_balance())	
	
	def deposit(self,amount,description=""):
		self.ledger.append({"amount": amount, "description": description})
		#print(self.ledger)
		
	def withdraw(self,amount,description=""):
		#the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
		if self.check_funds(amount):
			succes=True
			self.ledger.append({"amount": 0-amount, "description": description})
		else: succes=False
		#print(self.ledger)
		return succes

	def get_balance(self):
		#method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
		balance=0
		for action in self.ledger:
			#print(action["amount"]+balance)
			balance += action["amount"]
			#print(str(balance) + "  "+ str(action["amount"]))
		return round(balance,2)

	def transfer(self,amount,categories):
		#The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
		title= self.title
		if self.withdraw(amount,"Transfer to " +categories.title) == True:
			categories.deposit(amount,"Transfer from %s" %title)
			succes= True
		else: succes= False
		return succes
	def check_funds(self,amount):
		#It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
		if amount> self.get_balance():
			return False
		else: return True
	
	





def create_spend_chart(categories):
	chart="Percentage spent by category" +"\n"
	porcentajes=[]
	total=0
	nombres="    -"
	titles=[]
	aux=[]

	elementos={10:"100| ",9:" 90| ",8:" 80| ",7:" 70| ",6:" 60| ",5:" 50| ",4:" 40| ",3:" 30| ",2:" 20| ",1:" 10| ",0:"  0| "}
	#para cada categoria extraemos las cantidades de withdraw y las sumamos
	for category in categories:
		nombres = nombres.rstrip() +"---"
		porcentaje=0
		for item in category.ledger:
			if item["amount"] < 0:
				porcentaje += item["amount"]
		porcentajes.append(0-porcentaje)
		total += (0-porcentaje)
		#ademas construimos los nombres en listas
		titles.append(list(category.title))
		aux.append(len(list(category.title)))
	#calculamos los porcentajes y añadimos los respectivos "o" y los espacios en blanco	
	for i in range(len(porcentajes)):
		#sacamos el porcentaje
		porcentajes[i] = porcentajes[i]/total*100
		#lo redondeamos al decimo inferior
		porcentajes[i]= int(porcentajes[i]//10)
		for j in range(porcentajes[i]+1):
			elementos[j] += "o  "
		for j in range(porcentajes[i]+1,11):
			elementos[j] += "   "
			#print(elementos)

	#construimos los nombres en vertical	
	for i in range (max(aux)):
		nombres += "\n"+"   "
		for j in range (len(categories)):
			if i < len(titles[j]):
				nombres += "  "+titles[j][i]
			else: nombres += "   "
		nombres += "  "

		#construimos el string de resultados		
	for key in elementos:
		chart += elementos[key] +"\n"
	
	return chart + nombres