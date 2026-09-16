#Charles Ajjan 
#cmp131
#Week 4
#Lab 1
#box office report
#started on 09/10/2026
Movie=input("Enter Movie Name   ")
Adult=int(input("Enter Amount of Adult Tickets Sold   "))
Child=int(input("Enter Amount of Child Tickets Sold   "))
Gross=float(Adult*10+Child*6)
Adult_Tix=(Adult*10)
Child_Tix=(Child*6)
Theater_net=(float(Gross*0.20))
Distributor=(float(Gross-Theater_net))





print()
print()
print("TICKET INFORMATION")
print(Movie title: (Movie))
print (f"Adult tickets sold",Adult)
print("Adult_Ticket Returns:",f"${Adult_Tix:.2f}")
print()
print(f"Child tickets sold",Child)
print("Child_Ticket Returns:",f"${Child_Tix:.2f}")
print()
print("ACCOUNTS DIVISION")
print("Gross:",f"${Gross:.2f}")
print()
print("Theater_net:",f"${Theater_net:.2f}")
print()
print("Distibutor",f"${Distributor:.2f}")