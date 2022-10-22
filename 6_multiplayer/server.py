import socket, threading, json, time


#-----------------------------------------------
#Define socket copnstants to be us3ed and ALTERED
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

#Define pygame constants to be used and ALTERED
ROOM_SIZE = 400
PLAYER_SIZE = 20
FPS = 15
ROUND_TIME = 45
TOTAL_PLAYERS = 4


#Room must be divisible by player size for correct gameplay, adjust as needed.
while ROOM_SIZE % PLAYER_SIZE != 0:
    PLAYER_SIZE += 1


#Maximum number of players allowed is 4!
if TOTAL_PLAYERS > 4:
    TOTAL_PLAYERS = 4

#-----------------------------------------------
#Define Classes
class Connection():
    '''A socket connection class to be used as a server'''
    def __init__(self):
        '''Init of the connection class'''
        pass

class Player():
    '''A class store a connected clients player information'''
    def __init__(self):
        '''Init of the connection class'''
        pass


    def set_player_info(self, player_info):
        '''Set the player info to the given info from the client (coord and status flags)'''
        pass

    def reset_player(self):
        '''Reset player values for a new round on the server side'''
        pass

class Game():
    '''A class to handle all operations of gameplay'''
    def __init__(self, connection):
        '''Init of the game class'''
        pass
    def connect_players(self):
        '''Connect ANY incoming player to the game'''
        pass

    def broadcast(self):
        '''Broadcast information to ALL players'''
        pass

    def ready_game(self, player, player_socket):
        '''Ready the game to be played for a Specific player'''
        pass
    def reset_game(self, player):
        '''Restart the game and wipe information for a Specific player'''
        pass
    def send_player_info(self, player, player_socket):
        '''Send specific information about THIS player to the given client'''
        pass

    def recieve_pregame_player_info(self, player, player_socket):
        '''Recoeve specific info about THIS player pregame'''
        pass

    def recieve_game_player_info(self, player, player_socket):
        '''Recieve specific info about THIS player during the game'''
        pass

    def process_game_state(self, player, player_socket):
        '''Process the given player info and update the games state'''
        pass
    def send_game_state(self, player_socket):
        '''Send the current game state of ALL players to THIS given player'''
        pass


#Start the server
my_connection = Connection()
my_game = Game(my_connection)

#Listen for incomming connections
print("Server is listening for incomming connections...\n")
my_game.connect_players()
