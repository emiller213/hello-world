def hotel_cost(nights):
  #If Hotel equals $140 / night
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    reutrn 475
  else:
    return "unknown"
    
def rental_car_cost(days):
  base_cost = 40 * days
  if days >= 7:
    base_cost -= 50
  elif days >= 3:
    base_cost -= 20

def double(n):
  return n * 2

def spending_money(money):
  return money

def trip_cost(city, days, spending_money):
  return plane_ride_cost(city) + rental_car_cost(days) + spending_money + hotel_costs(days)

print trip_cost("Los Angeles", 5, 600)

print("Have a good day!")

