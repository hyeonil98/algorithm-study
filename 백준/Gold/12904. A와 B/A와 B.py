
def exec():
    S = input()
    T = input()

    while len(S) != len(T):
        target = T[-1]
        T = T[:-1]
        if target == 'B':
            T = T[::-1]

        
    if S == T:
        return 1
    else:
        return 0

if __name__ == "__main__":
    answer = exec()
    print(answer)    