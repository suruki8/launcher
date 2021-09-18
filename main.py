from PyQt5 import QtCore, QtGui, QtWidgets
import ui
from os import system 
import requests

class Game:
    def __init__(self, info) -> None:
        self.name =  info["name"]
        self.appid = info["appid"]
        self.logo = f"http://media.steampowered.com/steamcommunity/public/images/apps/{self.appid}/{info['img_logo_url']}.jpg"
        self.playtime = info["playtime_forever"]
    def run(self):
        print(f"[INFO] Running game {self.name}\n" + '--'*10)
        system(f"start steam://rungameid/{self.appid}")
        
    def getimg(self):
        return self.logo

    def __str__(self) -> str:
        return self.name + ':' + str(self.appid)

def get_games(id):
    key = "A9508EC2E9B74E44ABCFD01ADA3FB24E"
    uri = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={id}&format=json&include_appinfo=true"
    responce = requests.get(uri)
    games =  responce.json()['response']['games']
    return games
user_id = input ("Enter ID")
user_id = float
class MW(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.games = get_games(user_id)
        self.games = [Game(x) for x in self.games]
        self.pushButton_1.clicked.connect(self.function)
        self.pushButton_2.clicked.connect(self.function) 


    def function(self):
        self.sender
        self.games[15].run()
        #system('start steam://rungameid/293860')
         
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MW()
    ui.show()
    sys.exit(app.exec_())