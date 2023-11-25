import tools

def main():
    while(True):
        tools.playgame()
        playagain = input("請問是否要繼續(y/n)?")
        if playagain == "n":
            break
            
    print("遊戲結束")
    print(__name__)

if __name__ == "__main__":
    main()
