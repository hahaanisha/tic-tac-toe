def printBoard(xState, zState):
    print(f"{'X' if xState[0] else ('O' if zState[0] else 0)} | {'X' if xState[1] else ('O' if zState[1] else 1)} | {'X' if xState[2] else ('O' if zState[2] else 2)} ")
    print(f"--|---|---")
    print(f"{'X' if xState[3] else ('O' if zState[3] else 3)} | {'X' if xState[4] else ('O' if zState[4] else 4)} | {'X' if xState[5] else ('O' if zState[5] else 5)} ")
    print(f"--|---|---")
    print(f"{'X' if xState[6] else ('O' if zState[6] else 6)} | {'X' if xState[7] else ('O' if zState[7] else 7)} | {'X' if xState[8] else ('O' if zState[8] else 8)} ")

def check(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]  # Adjusted the winning combinations
    for win in wins:
        if xState[win[0]] == xState[win[1]] == xState[win[2]] == 1:
            print("X WON !!!!!!!!")
            return True
        if zState[win[0]] == zState[win[1]] == zState[win[2]] == 1:
            print("O WON !!!!!!!!")
            return True
    if 0 not in xState and 0 not in zState:
        print("No winner winner chicken dinner!")
        return True
    return False

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Anisha's Tic Tac Toe")
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("It's X's turn now:")
            value = int(input("Please enter a cell number (0-8): "))
            xState[value] = 1
            turn = 0
        else:
            print("It's O's turn now:")
            value = int(input("Please enter a cell number (0-8): "))
            zState[value] = 1
            turn = 1
        cwin=check(xState,zState)
        if cwin:
            print('Match Over')
            break
        
            
