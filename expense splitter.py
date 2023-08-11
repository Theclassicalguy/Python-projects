
def expense_splitter():
    total_expense=float(input("Enter the total amount:"))
    number_of_people=int(input("Enter the number of people to split between:"))
    total_div_for_each_person=total_expense/number_of_people
    print(f"The amount that {number_of_people} people will have to pay for {total_expense} is: {total_div_for_each_person}")


def main():
    print("Welcome to Expense splitter")
    expense_splitter()


main()
