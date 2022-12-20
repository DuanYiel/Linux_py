import random


PRICE_ARCHER = 100
PRICE_AXEMAN = 120
MAX_HP_ARCHER = 100
MAX_HP_AXEMAN = 120
DAMAGE_ARCHER_EAGLE_DEMON = 20
DAMAGE_ARCHER_WOLF_DEMON = 80
DAMAGE_AXEMAN_EAGLE_DEMON = 80
DAMAGE_AXEMAN_WOLF_DEMON = 20


ling_shi = 1000


forests = []


for i in range(7):
  forest = {"name": f"Forest {i+1}"}
  monster_type = random.choice(["eagle demon", "wolf demon"])
  forest["monster"] = monster_type
  forests.append(forest)

print("Monsters in the forests:")
for forest in forests:
  print(f"{forest['name']}: {forest['monster']}")


soldiers = []


while True:
  print("You have", ling_shi, "Ling Shi remaining.")
  print("Enter the number of archers and axemen you want to hire, or enter 'done' to start the journey:")
  line = input()
  if line.lower() == "done":
    break
  try:
    num_archers, num_axemen = map(int, line.split())
  except ValueError:
    print("Invalid input. Try again.")
    continue
  cost = num_archers * PRICE_ARCHER + num_axemen * PRICE_AXEMAN
  if cost > ling_shi:
    print("You don't have enough Ling Shi to hire these soldiers. Try again.")
    continue
  ling_shi -= cost
  for i in range(num_archers):
    name = input("Enter a name for the archer: ")
    soldier = {
      "name": name,
      "type": "archer",
      "max_hp": MAX_HP_ARCHER,
      "hp": MAX_HP_ARCHER,
      "damage_eagle_demon": DAMAGE_ARCHER_EAGLE_DEMON,
      "damage_wolf_demon": DAMAGE_ARCHER_WOLF_DEMON,
    }
    soldiers.append(soldier)
  for i in range(num_axemen):
    name = input("Enter a name for the axeman: ")
    soldier = {
      "name": name,
      "type": "axeman",
      "max_hp": MAX_HP_AXEMAN,
      "hp": MAX_HP_AXEMAN,
      "damage_eagle_demon": DAMAGE_AXEMAN_EAGLE_DEMON,
      "damage_wolf_demon": DAMAGE_AXEMAN_WOLF_DEMON,
    }
    soldiers.append(soldier)

for forest in forests:
  print(f"Entering {forest['name']}...")
  monster = forest["monster"]
  print(f"There is a {monster} in this forest.")
  while True:
    print("Select a soldier to send:")
    for i, soldier in enumerate(soldiers):
      print(f"{i}: {soldier['name']} ({soldier['type']}, HP: {soldier['hp']})")
    line = input()
    try:
      index = int(line)
      soldier = soldiers[index]
    except (ValueError, IndexError):
      print("Invalid input. Try again.")
      continue
    if monster == "eagle demon":
      damage = soldier["damage_eagle_demon"]
    elif monster == "wolf demon":
      damage = soldier["damage_wolf_demon"]
    soldier["hp"] -= damage
    if soldier["hp"] <= 0:
      print(f"{soldier['name']} has been killed by the {monster}.")
      soldiers.remove(soldier)
    else:
      print(f"{soldier['name']} has defeated the {monster}.")
      break
  print(f"{forest['name']} cleared.")
  while True:
    print("Do you want to use a Holy Stone to nourish your soldiers? (y/n)")
    line = input()
    if line.lower() == "y":
      for soldier in soldiers:
        if soldier["hp"] < soldier["max_hp"]:
          soldier["hp"] += 1
          ling_shi -= 1
      print("Soldiers nourished.")
      break
    elif line.lower() == "n":
      break
    else:
      print("Invalid input. Try again.")


print("You have reached the capital.")
print("You have", ling_shi, "Ling Shi remaining.")
