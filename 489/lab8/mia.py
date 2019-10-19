from __future__ import print_function

def solve():
    while True:
        line = raw_input()
        if (line == "0 0 0 0"):
            break
        r1 = line[0:3].split(" ")
        r2 = line[4:].split(" ")
        if (r1[0] < r1[1]):
            temp = r1[1]
            r1[1] = r1[0]
            r1[0] = temp
        if (r2[0] < r2[1]):
            temp = r2[1]
            r2[1] = r2[0]
            r2[0] = temp
        
        r1S = "".join(r1)
        r1 = int(r1S)
        r2S = "".join(r2)
        r2 = int(r2S)
        #print(r1,r2)

        if (r1 == r2):
            print("Tie.")
        elif ((r1 == 12 or r1 == 21) and (r2 == 12 or r2 == 21)):
            print("Tie.")
        elif (r1 == 12 or r1 == 21):
            print("Player 1 wins.")
        elif (r2 == 12 or r2 == 21):
            print("Player 2 wins.")
        elif ((r1S[0] == r1S[1]) and (r2S[0] == r2S[1])):
            if (r1 > r2):
                print("Player 1 wins.")
            elif (r1 < r2):
                print("Player 2 wins.")
            else:
                print("Tie.")
        elif (r1S[0] == r1S[1]):
            print("Player 1 wins.")
        elif (r2S[0] == r2S[1]):
            print("Player 2 wins.")
        elif (r1 > r2):
            print("Player 1 wins.")
        else:
            print("Player 2 wins.")
    

def main():
    solve()

main()
