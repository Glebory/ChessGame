# send board data between players and to spectators
import socket as sock
import pickle as rick
import time
import game as g
import GUI as gooey
from _thread import start_new_thread

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

serv = 'localhost'
port = 3456
addr = (serv, port)
ip = sock.gethostbyname(addr)
global conns
conns = 0
global specs
specs = 0

try:
    s.bind(addr)

except sock.error as e:
    print('uh oh, %s' % e)



def getSpectators():
    global ids
    ids = []
    try:
        with open("specs.txt", "r") as file:
            for line in file:
                ids.append(line.strip())
    except:
        print("[ERR] specs.txt not found, creating one now")
        open("specs.txt", "w")
        
def client(conn, game, isSpec):
    if not isSpec: # player protocol
        board = gooey.GameBoard(game)
        global conns
        #set color
        if conns % 2 == 1:
            playerid = 'b'
        else:
            playerid = 'w'
        
        data = rick.dumps(board)


        if playerid == 'b':
            board.ready = True
            board.startTime = time.time()

        conn.send(data)
        conns += 1

        while True:
            try:
                recv = conn.recv(4096)
                data = recv.decode('utf-8')

                if not recv:
                    break
                else:
                    if data.count('select') > 0: # fix
                        info = data.split(' ')
                        col = int(info[1])
                        row = int(info[2])
                        color = int(info[3])
                        board.mouseDown(col, row, color)

                    if data.count('name') == 1:
                        name = data.split(' ')[1]
                        if playerid == 'b':
                            board.bname = name
                        elif playerid == 'w':
                            board.name = name

                    if data == 'b wins':
                        board.winner = 'b'
                        print('Black Wins!')

                    if data == 'w wins':
                        board.winner = 'w'
                        print('White Wins!')

                    if data == 'update':
                        board.update()

                    if board.ready:
                        if board.changeColour == 'b':
                            board.btime = 300 - (time.time() - board.startTime)
                        else:
                            board.wtime = 300 - (time.time() - board.startTime)

                    send = rick.dumps(board)

                conn.sendall(send)

            
            except Exception as e:
                print(e)
                    
        
    else:
        available_games = 0# figure this out
        game_ind = 0
        board = gooey.GameBoard(game)
        board.start_user = "s"
        data = rick.dumps(board)
        conn.send(data)
        global specs

        while True:
            available_games = 0# figure this out
            board = gooey.GameBoard(game)
            try:
                d = conn.recv(128)
                data = d.decode("utf-8")
                if not d:
                    break
                else:
                    try:
                        if data == "forward":
                            print("[SPECTATOR] Moved Games forward")
                            game_ind += 1
                            if game_ind >= len(available_games):
                                game_ind = 0
                        elif data == "back":
                            print("[SPECTATOR] Moved Games back")
                            game_ind -= 1
                            if game_ind < 0:
                                game_ind = len(available_games) -1

                        board = gooey.GameBoard(game)
                    except:
                        print("[ERROR] Invalid Game Recieved from Spectator")

                    sendData = rick.dumps(board)
                    conn.sendall(sendData)

            except Exception as e:
                print(e)

        print("[DISCONNECT] Spectator left game", game)
        specs -= 1
        conn.close()
                    

while True:
    getSpectators()
    if conns < 6:
        conn, addr = s.accept()
        spec = False
        g = -1
        print("[CONNECT] New connection")

        for game in games.keys():
            if games[game].ready == False:
                g = game

        if g == -1:
            try:
                g = list(games.keys())[-1]+1
                games[g] = Board(8,8)
            except:
                g = 0
                games[g] = Board(8,8)
        

        print("[DATA] Number of Connections:", conns+1)
        print("[DATA] Number of Games:", len(games))

        start_new_thread(client, (conn, g, spec))

                

