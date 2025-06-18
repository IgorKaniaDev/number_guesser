

lower_bound = 1
upper_bound = 400

def too_many():
    
    global upper_bound
    upper_bound = r - 1
    print("Okey I changed range in(lowest, highest):",lower_bound , upper_bound)
    return upper_bound

def too_low():
    global lower_bound
    lower_bound = r + 1
    print("Okey I changed range in(lowest, highest):",lower_bound ,upper_bound)
    return lower_bound

while True:
    
    r = (lower_bound + upper_bound) // 2
    print(r)
    print("Enter if it's that number or not! You can write: yes, higher, lower")
    user_input = input("Enter answer: ")
        
    if lower_bound > upper_bound:
            print("❌ Error: Invalid range. You gave inconsistent answers.")
            break
    if lower_bound == upper_bound:
            print(f"⚠️ Only one number left: {lower_bound}, and you still didn't say 'yes'.")
            print("❌ Error: Contradictory input.")
            break


    if user_input.lower() == "higher":
        too_low()

    elif user_input.lower() == "lower":
        too_many()


        
    elif user_input.lower() == "yes":
        print("You predicted! It was: ",r)
        print("Last range was: ",lower_bound, upper_bound)
        break
    else:
        print("Wrong input!")
        continue
