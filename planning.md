# Markdown planning sheet with the four computational thinking responses.

## Decomposition: 
1. Create the Plant class.
2. Create the Zombie class.
3.Create two Plant objects with different damage values.
4. Create one Zombie object.
5. Make the plants attack the Zombie.
6. Make the Zombie move toward the plants.
7. Make the Zombie attack a plant when it reaches distance 0.
8. Check the health of all characters and determine the winner.

## Pattern Recognition:
- Each living plant attacks once every turn.
- The Zombie moves one step closer each turn.
- The Zombie attacks when its distance reaches 0.
- Health decreases when a character takes damage.
- The game checks after actions whether either side has won.

## Abstraction:
### Plant needs:
- Name
- Health
- Damage
- Attack method
- Take-damage method
### Zombie:
- Name
- Health
- Damage
- Distance
- Move method
- Attack method
- Take-damage method

## Algorithm Design:
1. Create two Plant objects and one Zombie object.
2. Display their starting information.
3. Start a turn.
4. Each living plant attacks the Zombie in order.
5. Check if the Zombie is defeated.
6. If not defeated, the Zombie moves one step closer if its distance is greater than 0.
7. If its distance is 0, the Zombie attacks the first living plant.
8. Check whether both plants are defeated.
9. If either side wins, stop the game and display the result.
10. Otherwise, repeat the turn.
