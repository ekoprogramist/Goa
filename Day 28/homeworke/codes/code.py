#first codewars:
def digitize(n):
    list = []
    for i in str(n):
        list.append(int(i))
    return list[::-1]
    
#second codewars:
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    
    else:
        return f"{name} does not play banjo"

#third codewars:
def rps(p1, p2):
    
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
        
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
      
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
      
    elif p1 == p2:
        return "Draw!"
    
    else:
        return "Player 2 won!"
    
#forth codewars:
def quarter_of(month):
    if month <= 3:
        return 1
    
    elif month >=4 and month <=6:
        return 2
    
    elif month <=9:
        return 3
    
    else:
        return 4

#fofth codewars:
def count_sheep(n):
    result = ""
    for i in range(1,n+1):
        result += f"{i} sheep..."
    return result

#sixth codewars:
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    
    else:
        return "Hello guest"

#seventh codewars:
def rental_car_cost(d):
    cost = d * 40
    
    if d >= 7:
        return cost - 50
    
    elif d >= 3:
        return cost - 20
    return cost

#eightth codewars:
def remove_exclamation_marks(s):
    my_list = ""
    for i in s:
        if i != "!":
            my_list += i
            
            
            
            
    return my_list
