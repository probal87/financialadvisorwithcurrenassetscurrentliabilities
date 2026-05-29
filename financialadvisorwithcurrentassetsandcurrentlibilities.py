
current_assets=float(input("enter the value of current assets:"))
current_liabilities=float(input("enter the value of current liabilities:"))
current_ratio=(current_assets/current_liabilities)


working_capital=current_assets-current_liabilities
print(f"current ratio is {current_ratio}")

if current_ratio>1:
   print("company  has healthy liquidity,can meet obligations completely")
elif current_ratio==1 :
    print("company has exactly enough  to cover debts,but there is no safety margin")
else:
    print("company has liquidity risk,may not cover short term debts")
print(f"working capital is {working_capital}")
if working_capital<1:
    print("company has negative working capital,can not cover short term obligations,\nindicates liquidity problem,\npotential difficulties in paying bills \nrequires immediate attention to avoid cash flow crisis")
elif working_capital==1:
    print("current assets exactly equal current liabilities\ncompany has  just enough short term assets to cover obligations\n its not ideal for a buisness because buisness typically aim  higher for safety margin  ")
elif working_capital==0:
    print("there is no current assets\n company has no ability to pay short term obligations from current assets \nessentially insolvent in the short term")
else :
    print("positive working capital\n company can pay off all short term liabilities with existing assets")
