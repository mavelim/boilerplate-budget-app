# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

business = budget.Category("Business")
food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
food.deposit(900, "deposit")
food.withdraw(105.55, "milk, cereal, eggs, bacon, bread")
business.deposit(900, "deposit")
business.withdraw(10.99, "")
entertainment.deposit(900, "deposit")
entertainment.withdraw(33.40)



print(create_spend_chart([business, food, entertainment]))

print("++++++++++++++++++++++++++++++++++")
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
# Run unit tests automatically
main(module='test_module', exit=False)