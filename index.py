td=int(input("enter the total amount of working days:   "))
ta=int(input("enter the amount of days you were absent:   "))
tpr=td-ta
tp=(tpr/td*100)
if tp>75:
    print("you can give your exam")
else:
   print("you cannot give your exam")
