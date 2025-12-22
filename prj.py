def wallet(inner):
    budget = inner

    def manager(action, amount=0):
        nonlocal budget
        if action == "add":
            budget += amount
            print(f"your salary and income is {amount} and u now have {budget}")
            
        elif action == "spend":
            if budget < amount:
                print("access denied")
            else:
                budget -= amount
                print(f"u have spent {amount} and now have {budget}")
        elif action == "get":
            print(f"your current budget is {budget}")
            
        else:
            print("invalid choice")


        return budget
    
    return manager
    

my_wallet = wallet(2000)
(my_wallet("add", 500))#if we ont use the return manager we cannot access the inside of the fucn
my_wallet("get")#my wallet is now the child func(manager)

