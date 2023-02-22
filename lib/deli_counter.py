katz_deli = []

def line(name):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line = len(katz_deli)
        return print(f"The line is currently: {line}. {name}")
    
# "The line is currently: 1. Logan 2. Avi 3. Spencer
line(katz_deli)


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    line = len(katz_deli) 
    print(f"Welcome, {name}. You are number {line} in line.")
    # print(katz_deli)
    
take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")
line(katz_deli)




def now_serving():
    pass

