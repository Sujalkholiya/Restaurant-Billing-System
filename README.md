  # 🍕 Restaurant Billing System

A simple Python-based Restaurant Billing System that allows customers to place orders, calculate bills, apply discounts, and add home delivery charges.

## 📌 Features

* Menu-driven ordering system
* Multiple item ordering
* Quantity selection
* Automatic bill calculation
* Discount system

  * 10% discount on orders above ₹500
  * 15% discount on orders above ₹1000
* Home delivery option (+₹40)
* Itemized bill generation
* Customer name tracking

---

## 🛠 Technologies Used

* Python 3
* Dictionaries
* Lists
* Loops
* Conditional Statements
* User Input Handling

---

## 📋 Menu

### Pizza 🍕

| Size   | Price |
| ------ | ----- |
| Small  | ₹250  |
| Medium | ₹350  |
| Large  | ₹500  |

### Momos

| Size | Price |
| ---- | ----- |
| Half | ₹40   |
| Full | ₹70   |

### Burger 🍔

| Type          | Price |
| ------------- | ----- |
| Regular       | ₹40   |
| Double Cheese | ₹60   |

### Spring Roll

| Type    | Price |
| ------- | ----- |
| Regular | ₹50   |

### Milkshake 🧋

| Size  | Price |
| ----- | ----- |
| Half  | ₹40   |
| Large | ₹80   |

---

## 🎯 Discount Rules

| Order Amount  | Discount |
| ------------- | -------- |
| ₹500 or more  | 10%      |
| ₹1000 or more | 15%      |

---



## 📸 Sample Output

```text
Welcome to the Restaurant

Enter customer name: Rahul

Enter first item name: pizza
Enter size: medium
Enter quantity: 2

Added: pizza (medium) x 2
Current Bill: ₹700

Do you want another item? yes

Enter item: milkshake
Enter size: large
Enter quantity: 1

Current Bill: ₹780

Home delivery? yes

Delivery charge added: ₹40

Customer: Rahul

Items Ordered:
1. pizza (medium) x 2
2. milkshake (large) x 1

Total Amount: ₹780
Discount: ₹78
Final Bill: ₹742
```

---

## 📚 Learning Outcomes

This project helped me practice:

* Python dictionaries
* Nested data structures
* Loops and conditions
* User input handling
* String formatting
* Building a real-world console application

---

## 🔮 Future Improvements

* Input validation
* Error handling using try-except
* GUI version using Tkinter
* Database integration using SQLite/MySQL
* Web application using Flask/Django
* Admin panel for menu management

---

## 👨‍💻 Author

Created by **[Your Name]**

If you like this project, feel free to ⭐ the repository.
