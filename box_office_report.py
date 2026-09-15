#Charles Ajjan, cmp131, Week 4, Lab 1, box office report, started on 09/10/2026
Movie=input("Enter Movie Name   ")
Adult=int(input("Enter Amount of Adult Tickets Sold   "))
Child=int(input("Enter Amount of Child Tickets Sold   "))
Gross=float(Adult*10+Child*6)
Theater_net=(float(Gross*0.20))
Distributor=Gross-Theater_net
Amount=(float(Gross-Theater_net))
Distributor=(float(Amount-Theater_net*0.80))


print()
print()
print("TICKET INFORMATION")
print(Movie)
print (f"Adult tickets sold",Adult)
print(f"Child tickets sold",Child)
print()
print("ACCOUNTS DIVISION")
print("Gross:",f"${Gross:.2f}")
print("Theater_net:",f"${Theater_net:.2f}")
print("Amount:",f"${Amount:.2f}")
print("Distibutor",f"${Distributor:.2f}")