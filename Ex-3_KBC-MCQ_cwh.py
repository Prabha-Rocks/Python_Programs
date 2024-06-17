ques = [
    "What is the capital of France?",
    "Who wrote 'Hamlet'?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal?"
]
option = [
    ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
    ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
    ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"]
]
ans = ['C', 'B', 'B', 'B']
prize = [1000, 5000, 10000, 50000]
tot_amt = 0


def ask_ques(ques, option, ans, prize):
    global tot_amt
    print(ques)
    for opt in option:
        print(opt)
    player_ans = input("Enter ans(A/B/C/D):")
    if player_ans == ans:
        tot_amt += prize
        print(f"Correct! You've won {prize}. Total amount {tot_amt}\n")
        return True
    else:
        print(f"Wrong answer. The correct answer was {ans}.")
        return False


for i in range(len(ques)):
    if not ask_ques(ques[i], option[i], ans[i], prize[i]):
        break
print(f"Game over! You've won a total of {tot_amt}.")





