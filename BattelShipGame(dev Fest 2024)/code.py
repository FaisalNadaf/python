
n=10
game=False

player1=False
player2=False

player1Score=0
player2Score=0

playerGround =[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

# playerGround = [[0 for _ in range(100)] for _ in range(100)]
# print (playerGround)


while game==False:

    # Chcking ship in ground
    for i in range(0,n):  
        for j in range(0,n):
            if(playerGround[i][j]==1):
                game=True
                break
        if(game==True):
            break

    print("Select Player DEFENCER enter 1 |0R| ATTACER enter 2")
    inputedPlayer = int(input("Entern Player :"))
    
    
    if inputedPlayer==1:
        player1=True
        a = int(input("Enter Ship Size below 3 :"))
        if a<=3:     
            for i in range(0,a):
                    hp1=int(input("Enter Hit Point row {a} :"))
                    hp2=int(input("Enter Hit Point colomn {a}:"))
                    playerGround[hp1][hp2]=1
    else:
        player2=True
        for fire in range(0,3):
              row=int(input("Enter the row :"))
              col=int(input("Enter the col :"))
              if playerGround[row][col]==1:
                print("HIT!!")
                playerGround[row][col]=0
                
                # Chcking ship in ground
                for i in range(0,n):  
                    for j in range(0,n):
                        if(playerGround[i][j]==1):
                            game=True
                            break
                    if(game==True):
                        break

              else:
                print("MISS!!")
    
    
          
    