# send board data between players and to spectators
import socket as sock
import pickle as rick
import time
import game as g
import GUI as gooey

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

serv = 'localhost'
port = 3456
addr = (serv, port)
ip = sock.gethostbyname(addr)
conns = 0
specs = 0
game = gooey.GameBoard(GUI)

try:
    sock.bind(addr)

except sock.error as e:
    print('uh oh, %s', e)



def getSpectators():
    return
    
def client(conn, game, isSpec):
    if not isSpec: # player protocol
        board = GameBoard(game)

        #set color
        if conns % 2 == 1:
            playerid = 'b'
        else:
            playerid = 'w'
        
        data = rick.dumps(board)


        if playerid == 'b':
            board.ready = True
            board.startTime = time()

        conn.send(data)
        conns += 1

        while True:
            try:
                recv = conn.recv(4096)
                data = recv.decode('utf-8')

                if not recv:
                    break
                else:
                    if data.count('select') > 0:
                        info = data.split(' ')
                        col = int(info[1])
                        row = int(info[2])
                        color = int(info[3])
                        board.select(col, row, color)

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
                        if board.turn == 'b':
                            board.btime = 300 - (time() - board.startTime)
                        else:
                            board.wtime = 300 - (time() - board.startTime)

                    send = rick.dumps(board)

                conn.sendall(send)

            
            except Exception as e:
                print(e)
                    
        
    else: # TODO spectator protocol
        return
                    



                

