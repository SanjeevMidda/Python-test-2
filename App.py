user_weight = float(input("What is your weight?"))
weight_measurement = input("(K)g or (L)bs:")

if weight_measurement == "K":
    print("Weight in Lbs: " + str((user_weight * 2.205)))
elif weight_measurement == "L":
    print("Weight in Kg: " + str((user_weight / 2.205)))