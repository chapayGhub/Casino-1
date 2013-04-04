from random import *

class Player:
    def __init__(self):
        self.cash = 1500

    def getCash(self):
        return self.cash
    
    def addCash(self, money):
        self.cash += money
        return self.cash
        
    def subtractCash(self, money):
        self.cash -= money
        return self.cash
    
class Spin:
    val = "y"
    w1 = 0
    w2 = 0
    w3 = 0
    
    #randomly gets three numbers for the three wheels of the slot machine
    def getRanNum(self):
        self.w1 = randrange(0,3)
        self.w2 = randrange(0,3)
        self.w3 = randrange(0,3)
        #print(self.w1,self.w2,self.w3)
        #print()
        return self.w1,self.w2,self.w3
    
def main():
    player = Player()
    bet = 1
    spin = Spin()
    spinAgain = "y"
    win = 0
    loss = 0
    lossStreak = 0

    #Loop to allow user to choose when to activate the slot machine
    while spinAgain != "n" and (player.getCash() != 0):
        spinAgain = input("do you want to spin? (y/n)\n")
        print()
        if spinAgain != "n":
            #print(type(bet), type(player.getCash()))
            print("Your cash total is: ", player.getCash()) 
            bet = eval(input("How much do you want to bet?\n"))
            print()
            #if bet <= int(player.getCash()):
                #if bet > 0:
            while bet > int(player.getCash()) or bet <= 0:
                print("Your cash total is: ", player.getCash()) 
                bet = eval(input("How much do you want to bet?\n"))
                print()
                #print("bet = ",bet, "player cash = ", player.getCash(),type(int(player.getCash())))
        if spinAgain != "n":
            spin.getRanNum()
            #Wheel spun three matching numbers
            if spin.w1 == spin.w2 == spin.w3:
                print(spin.w1,spin.w2,spin.w3)
                print("YOU HAVE WON!")
                player.addCash(bet)
                win += 1
                lossStreak = 0
                print()
                #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
            #If on a losing streak force wheel to select three matching numbers
            elif lossStreak > 4:
                called = 0
                lossStreak = 0
                while (spin.w1 != spin.w2) or (spin.w1 != spin.w3):
                    spin.getRanNum()
                    called += 1
                print(spin.w1,spin.w2,spin.w3)
                #print("called = ", called)
                #print(spin.w1,spin.w2,spin.w3)
                #print()
                print("YOU HAVE WON!")
                player.addCash(bet)
                win += 1
                print()
                #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
            #Wheel did not spin three matching numbers
            else:
                print(spin.w1,spin.w2,spin.w3)
                print("YOU LOSE")
                player.subtractCash(bet)
                loss += 1
                lossStreak += 1
                print()
                #print("win = ",win,"loss = ",loss,"lossStreak = ",lossStreak)
        else:
            print("You won ",win," times, but lost ",loss," times")
            print("Your total winnings are: $", player.getCash()-1500)
            print("You are walking away from the slot machine with: $",player.getCash())
            print("Game Over. Good Bye.")

    if player.getCash() == 0:
        print("You won ",win," times, but lost ",loss," times")
        print("You lost all your money :(")
        print("Game Over. Good Bye.")

main()
    


#Items still to address:
#
