

# Take parameter 1 values for different items 

pointX = []

while True:
    user_input = input("Enter a value for pointX (or type 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    try:
        # Convert input to a float (or int if you prefer)
        value = float(user_input)
        pointX.append(value)
    except ValueError:
        print("Please enter a valid number or 'stop' to finish.")



# Take parameter 2 values for different items 

pointY= []

while True:
    user_input = input("Enter a value for pointY (or type 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    try:
        # Convert input to a float (or int if you prefer)
        value = float(user_input)
        pointY.append(value)
    except ValueError:
        print("Please enter a valid number or 'stop' to finish.")


        

