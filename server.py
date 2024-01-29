from flask import Flask, Response
from flask_cors import CORS
import random
import uuid
import json
import flask_json
from flask_socketio import SocketIO

from flask_socketio import send, emit


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)
flask_json.FlaskJSON(app)
from flask import request
from flask_socketio import join_room, leave_room

from flask import send_from_directory

#@app.after_request
def do_something_whenever_a_request_has_been_handled( msg="", response=None):
    # we have a response to manipulate, always return one
    #if("ignore" not in  response.__dict__) :
        socketio.emit("update","")
        socketio.emit("notif",msg)
    #return response

@socketio.on('join')
def joinRoom(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)

@app.route("/game/new")
def newGame():
    np = int(request.args.get('np', default="4"))
    game = Game(np)
    res = json.dumps(game.tojson(None), default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    socketio.emit("init_game", game.uid)
    result = Response(res, mimetype='application/json')
    result.ignore = True
    do_something_whenever_a_request_has_been_handled(f"new game initiated <a href=\"origin?game_uid={game.uid}\">go</a>")
    return result

@app.route("/game/<guid>/join")
def joinGame(guid):
    game = games[guid]
    p = game.joinGame()
    res = p.uid
    socketio.emit("joind_game", guid+"/"+p.uid)
    result = Response(res, mimetype='application/json')
    result.ignore = True
    do_something_whenever_a_request_has_been_handled(f"new player joined game "+guid)
    return result

@app.route("/game/<guid>/new")
def newRound(guid):
    game = games[guid]
    round = game.newRound()
    res = json.dumps(round.tojson(None), default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    socketio.emit("init_round", round.uid)
    result = Response(res, mimetype='application/json')
    result.ignore = True
    do_something_whenever_a_request_has_been_handled(f"new round initiated <a href=\"origin?game_uid={game.uid}&round_uid={round.uid}&user_uid=[puid]\">go to</a>")
    return result


@app.route("/game/<guid>/<ruid>/<puid>/join")
def joinRound(guid,ruid,puid):
    game = games[guid]
    player = game.joinRound(ruid, puid)
    res = json.dumps(player.tojson(None), default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    socketio.emit("joind_round", guid+"/"+ruid+"/"+puid)
    result = Response(res, mimetype='application/json')
    result.ignore = True
    do_something_whenever_a_request_has_been_handled(f"user joined round {ruid}")
    return result



@app.route("/game/<guid>/<ruid>/init")
def giveRoundCards(guid, ruid):
    game = games[guid]
    round = game.rounds[ruid]
    round.initRound()
    res = json.dumps(round.tojson(None), default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    socketio.emit("init_round", round.uid)
    result = Response(res, mimetype='application/json')
    result.ignore = True
    do_something_whenever_a_request_has_been_handled(f"give cards ${ruid}")
    return result
"""

@app.route("/game/<guid>/join")
def joinGame(guid):

    if(guid in games):
        game = games[guid]
        
        p = game.GetPlayer(ip)
        if(p == None):
            p = game.GetPlayer(ip, True)
            if(p!=None):
                do_something_whenever_a_request_has_been_handled(str(p.order) + " "+p.name+" joined game")
        if(p != None):
            game = game.tojson(p.uid)
        else:
             game = game.tojson(None)
        

    res = json.dumps(game, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    result = Response(res, mimetype='application/json')
    result.ignore = True
    return result
"""

@app.route("/game/<guid>/<ruid>/<puid>")
def getRound(guid, ruid, puid):
    if((guid in games) and (ruid in games[guid].rounds)):
        game = games[guid]
        round = game.rounds[ruid]

        p = game.GetPlayer(puid)

        res = json.dumps(round.tojson(puid), default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        return Response(res, mimetype='application/json')
    return Response({"ok" : 1}, mimetype='application/json')



@app.route("/game/<guid>/<ruid>/<puid>/get")
def getCard(guid, ruid, puid):
    game = games[guid]
    round = game.rounds[ruid]

    p = game.GetPlayer(puid)
    round.giveToPlayer(p.order)
    
    #res = json.dumps(game, default=lambda o: o.__dict__, 
    #        sort_keys=True, indent=4)
    do_something_whenever_a_request_has_been_handled(str(p.order) + " "+p.name+" get card")
    return Response({"ok":True}, mimetype='application/json')

@app.route("/game/<guid>/<puid>/name")
def changeName(guid,puid):
    name = request.args.get('name')
    
    if(guid in games):
        game = games[guid]
        p = game.GetPlayer(puid)
        p.name = name
    
        #res = json.dumps(game, default=lambda o: o.__dict__, 
        #        sort_keys=True, indent=4)
        do_something_whenever_a_request_has_been_handled(str(p.order) + " changed name to "+p.name )
    return Response({"ok":True}, mimetype='application/json')

@app.route("/game/<guid>/<ruid>/<puid>/getthrown")
def gethrown(guid, ruid, puid):
    if(guid in games):
        game = games[guid]
        round = game.rounds[ruid]
        p = game.GetPlayer(puid)
        card = round.giveToPlayerFromThrown(p.order)
    
        #res = json.dumps(game, default=lambda o: o.__dict__, 
        #        sort_keys=True, indent=4)
        do_something_whenever_a_request_has_been_handled(str(p.order) +" "+p.name+" get from thrown " + str(card.number)+" "+card.color )
    return Response({"ok":True}, mimetype='application/json')

@app.route("/game/<guid>/<ruid>/<puid>/revert")
def revert(guid, ruid, puid):
    if(guid in games):
        game = games[guid]
        round = game.rounds[ruid]

    p = game.GetPlayer(puid)
    round.revert()
    #socketio.emit("revert", p.order)
    
    #res = json.dumps(game, default=lambda o: o.__dict__, 
    #        sort_keys=True, indent=4)
    do_something_whenever_a_request_has_been_handled(str(p.order) +" "+p.name+" reverted")
    return Response({"ok":True}, mimetype='application/json')

@app.route("/game/<guid>/<ruid>/<puid>/sort/<tp>")
def sortCards(guid, ruid, puid, tp):
    cards = request.args.get('cards')
    game = games[guid]
    round = game.rounds[ruid]

    p = game.GetPlayer(puid)
    round.sort(p.order, [int(ic) for ic in cards.split(',')], int(tp))

    return Response({"ok":True}, mimetype='application/json')

@app.route("/game/<guid>/<ruid>/<puid>/down")
def getDownCards(guid, ruid, puid):
    cards = request.args.get('cards')
    game = games[guid]
    round = game.rounds[ruid]

    p = game.GetPlayer(puid)
    round.getDown(p.order, [int(ic) for ic in cards.split(',')])

    do_something_whenever_a_request_has_been_handled(str(p.order) +" "+p.name+ " get down")
    return Response({"ok":True}, mimetype='application/json')

@app.route("/game/<guid>/<ruid>/<puid>/downcard")
def getDownCards2(guid, ruid, puid):
    ps = [x.split(",") for x in request.args.get('possible').split(";")]
    game = games[guid]
    round = game.rounds[ruid]

    p = game.GetPlayer(puid)
    if(len(ps)>0):
        pr = ps[0]
        round.getDownCard(p.order, int(pr[0]), int(pr[1]), int(pr[2]),int(pr[3]) )

    do_something_whenever_a_request_has_been_handled(str(p.order) +" "+p.name+ " get down card ")
    return Response({"ok":True}, mimetype='application/json')


@app.route("/game/<guid>/<ruid>/<puid>/<ic>")
def throwCard(guid, ruid, puid, ic):
    game = games[guid]
    round = game.rounds[ruid]
    

    p = game.GetPlayer(puid)
    card = round.throwCard(p.order, int(ic))
    if(card != None):
        do_something_whenever_a_request_has_been_handled(str(p.order) +" "+ p.name +" throw card " + str(card.number)+ " " +card.color)
    return Response({"ok":True}, mimetype='application/json')


import os
@app.route('/<path:path>')
def send_report(path):
    if(os.path.exists("dist/"+path)):
        return send_from_directory('dist', path)
    elif(path == "myproject.git"):
        return  send_from_directory('./', ".git")
    else:
        return defau()

@app.route('/')
def defau():
    path ="index.html"

    resp =  send_from_directory('dist', path)
    return resp

colors = ['hearts', 'diamonds', 'clubs', 'spades']




class Card:
    def __init__(self, number, color, id) -> None:
        self.number = number
        self.color = color
        self.id = id

class Player:

    cards : list[Card] = []
    cardsDown :list[Card] = []
    order:int = -1
    uid:str
    def __init__(self) -> None:
        self.taken = False
        self.order = -1
        self.cards = []
        self.cardsDown = []
        self.uid = str(uuid.uuid4())
        self.name = ""

    def tojson(self, verbose:bool) -> dict:
        dic = {"cardsDown":self.cardsDown, "order":self.order, "name":self.name}
        if(verbose):
            dic["cards"] =self.cards
            dic["uid"] = self.uid
        else:
            dic["cards"] = [[] for i in self.cards]
        return dic
    


class Round:
    players : list[Player]
    cards : list[Card] 
    thrownCards : list[Card]

    def getDownCard(self, ip, ic, ip2, id2, ic2):
        p1 = self.players[ip]

        p2 = self.players[ip2]
        card = [c for c in p1.cards if c.id == ic][0]
        down2 = p2.cardsDown[id2]
        self.players[ip].cards.remove(card)
        down2.append(card)
        self.actions.append(["downcard", ip, ic, ip2, id2])

    def revertDownCard(self, ip, ic, ip2, id2):
        p2 = self.players[ip2]
        card = [c for c in p2.cardsDown[id2] if c.id == ic][0]
        p2.cardsDown[id2].remove(card)
        self.players[ip].cards.append(card)

    def tojson(self, puid):
        result = { "uid":self.uid, "cards":len(self.cards), "thrownCards":self.thrownCards[max(len(self.thrownCards) - 4, 0):], 
                  "players":[ p.tojson(p.uid == puid) for p in self.players]}
        return result
    

    def __init__(self) -> str:
        initialCards = [[i%13, colors[int(i/26)], i] for i in range(104)] + [[0, '', 104], [0, '', 105],[0, '', 106],[0, '', 107]]
        #random.seed()
        initialCards = sorted(initialCards, key=lambda c : random.random())
        #random.shuffle(initialCards)
        self.cards = [Card(c[0], c[1], c[2]) for c in initialCards]
        self.players = []
        self.thrownCards = []
        self.uid = str(uuid.uuid4())
        self.actions = []

    def revert(self):
        if(len(self.actions) == 0):
            return 
        else:
            action = self.actions[len(self.actions)-1]
            match action[0]:
                case "give" : self.returnCard(action[1], action[2])
                case "givethrown" :  self.throwCard(action[1], action[2], False)
                case "throw": self.giveToPlayerFromThrown(action[1], False)
                case "down": self.revertDown(action[1])
                case "downcard": self.revertDownCard(action[1], action[2], action[3], action[4])
            self.actions.pop()
            
    def revertDown(self, ip:int):
        cards = self.players[ip].cardsDown.pop()
        for c in cards:
            self.players[ip].cards.append(c)
    
    def giveToPlayer(self, ip:int, c:int = 1, history = True):
        for j in range(c):
            card = self.cards.pop()
            self.players[ip].cards.append(card)
            if(history):
                self.actions.append(["give", ip, card.id])
    
    def returnCard(self, ip:int, ic:int):
        cards = self.players[ip].cards
        for card in  cards:
            if(card.id == ic):
                self.cards.append(card)
                self.players[ip].cards.remove(card)
                #self.actions.append[["throw", ip, card.id]]
                return card
    
    def giveToPlayerFromThrown(self, ip:int, history=True):

            card = self.thrownCards.pop()
            self.players[ip].cards.append(card)
            if(history):
                self.actions.append(["givethrown", ip, card.id])
            return card
    
    def throwCard(self, ip:int, ic:int, history=True) -> Card:
        cards = self.players[ip].cards
        for card in  cards:
            if(card.id == ic):
                self.thrownCards.append(card)
                self.players[ip].cards.remove(card)
                if(history):
                    self.actions.append(["throw", ip, card.id])
                return card

    def getDown(self, ip:int, ics:list[int]):
        nd = []
        self.players[ip].cardsDown.append(nd)
        self.actions.append(["down", ip])
        cards = self.players[ip].cards
        for ic in ics:
            for card in  cards:
                if(card.id == ic):
                    nd.append(card)
                    self.players[ip].cards.remove(card)
        
    def sort(self, ip:int, ics:list[int], tp):

        nd = []
        if(tp == 100):
            cards = self.players[ip].cards
        else:
            cards = self.players[ip].cardsDown[tp]
        for ic in ics:
            for card in  cards:
                if(card.id == ic):
                    nd.append(card)
        if(tp == 100):
            self.players[ip].cards = nd
        else:
            self.players[ip].cardsDown[tp] = nd
      
    
    def initRound(self):
        
        for i in range(7):
            if( i == 0):
                self.giveToPlayer(self.players[0].order, history=False)
            for p in self.players:
                self.giveToPlayer(p.order, 2, history=False)

    def end(self):
        pass


class Game:

    def joinGame(self) -> Player:
        for p in self.players.values():
            if(not p.taken):
                p.taken = True
                return p


    
    def joinRound(self, ruid, puid) -> Player:
        player = self.players[puid]
        round = self.rounds[ruid]
        
        if(player not in round.players):
            round.players.append(player)
            player.order = len(round.players) - 1
            return player

    def tojson(self, ip):
        result = { "uid":self.uid, 
                  "players":[ p.tojson(p.uid == ip and p.uid != "") for p in self.players.values()]}
        return result
    

    def __init__(self, np:int) -> None:
        self.rounds  : dict[str, Round] = {}
        self.uid = str(uuid.uuid4())
        self.players : dict[str, Player] = {}
        for ip in range(np):
            player = Player()
            self.players[player.uid] = player
        games[self.uid] = self

    
    def GetPlayer(self, puid:str) -> Player:
        for p in self.players.values():
            if(p.uid != "" and p.uid == puid):
                return p


        
    def newRound(self):
        round = Round()
        self.rounds[round.uid] = round
        return round
    

games : dict[str, Game] = {}


if(__name__ == "__main__"):
    context = ('certs/host.cert', 'certs/host.key')
    #socketio.run(app,host="0.0.0.0", ssl_context=context, port=8086)
    socketio.run(app,host="0.0.0.0", port=8086)

    game = Round()
    p1 = game.initPlayer()
    p2 = game.initPlayer()
    p3 = game.initPlayer()
    p4 = game.initPlayer()

    assert len(p1.cards) == 0, "player cards should be 0 at first"
    assert len(game.cards) == 108, "game cards should be 108 at first"
    assert len(game.players) == 4, "game players should be 4 at first"

    for i in range(7):
        if( i == 0):
            game.giveToPlayer(game.players[0].order)
        for p in game.players:
            game.giveToPlayer(p.order, 2)
        
    
    for p in game.players:
        if(p.order == 0):
            assert len(p.cards) == 15, f"player {p.order} cards should be 14 after init"
        else:
            len(p.cards) == 14, f"player {p.order} cards should be 14 after init"

    assert len(game.cards) == 51, "game cards should be 51 at first"

    c5 = p1.cards[5]
    game.throwCard(0, 5)
    assert len(p.cards) == 14, f"player {p.order} cards should be 14 after first throw"
    assert c5.number == game.thrownCards[0].number, "error throwing"
