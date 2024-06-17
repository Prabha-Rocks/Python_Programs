# Game Rules:
# 1)GUN kills SNAKE
# 2)SNAKE Drinks WATER
# 3)WATER Destroys GUN
# SNAKE, WATER & GUN Game
SNAKE = 0
WATER = 1
GUN = 2
def winner(p1,p2):
    if p1 == p2:
        return "Its a draw!!"
    elif (p1==GUN and p2==SNAKE)or(p1==SNAKE and p2==WATER)or(p1==WATER and p2==GUN):
        return "Player 1 wins!!"
    else:
        return "Player 2 wins!!"
def main():
    choices=["Snake","Water","Gun"]

    p1=int(input("Player 1, enter your choice (Snake=0, Water=1, Gun=2): "))
    p2=int(input("Player 2, enter your choice (Snake=0, Water=1, Gun=2): "))

    print(f"Player 1 chose:{choices[p1]}")
    print(f"Player 2 chose:{choices[p2]}")

    print(winner(p1,p2))

if __name__ == "__main__":
    main()