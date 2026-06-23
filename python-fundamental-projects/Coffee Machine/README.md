\# Coffee Machine



A command-line coffee machine simulation built in Python.



This project manages drink orders, checks available resources, processes coin payments, gives change, tracks machine profit, and updates inventory after each successful purchase.



\---



\## Files



\- `My\_Coffee\_Machine.py` - Python implementation of the Coffee Machine project.



\---



\## Concepts Covered



\- Functions

\- Dictionaries

\- Loops

\- Conditional statements

\- Resource tracking

\- Transaction handling

\- User input validation

\- State management



\---



\## Program Requirements



\### 1. Prompt the User



The program should ask:



```text

What would you like? (espresso/latte/cappuccino):

```



The prompt should appear again after each completed action, such as after a drink is dispensed.



\---



\### 2. Turn Off the Coffee Machine



Entering:



```text

off

```



should turn off the machine and end the program.



\---



\### 3. Print Report



Entering:



```text

report

```



should display the current machine resources and money earned.



Example:



```text

Water: 100ml

Milk: 50ml

Coffee: 76g

Money: $2.5

```



\---



\### 4. Check Sufficient Resources



When the user chooses a drink, the program should check whether there are enough resources to make it.



If there is not enough of an ingredient, the program should print a message such as:



```text

Sorry, there is not enough water.

```



\---



\### 5. Process Coins



If there are enough resources, the program should ask the user to insert coins.



Coin values:



```text

quarters = $0.25

dimes = $0.10

nickels = $0.05

pennies = $0.01

```



The program should calculate the total amount inserted.



\---



\### 6. Check Transaction



The program should verify that the user inserted enough money for the selected drink.



If the user did not insert enough money, the program should print:



```text

Sorry, that's not enough money. Money refunded.

```



If the user inserted enough money, the drink cost should be added to the machine's profit.



If the user inserted too much money, the program should return change rounded to 2 decimal places.



Example:



```text

Here is $2.45 in change.

```



\---



\### 7. Make Coffee



If the transaction is successful and resources are sufficient, the program should deduct the required ingredients from the machine resources.



Example report before purchasing a latte:



```text

Water: 300ml

Milk: 200ml

Coffee: 100g

Money: $0

```



Example report after purchasing a latte:



```text

Water: 100ml

Milk: 50ml

Coffee: 76g

Money: $2.5

```



After making the drink, the program should tell the user:



```text

Here is your latte ☕

```

