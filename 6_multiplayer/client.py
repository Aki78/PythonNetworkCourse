import pygame, socket, threading, json

#----------------------------------------------------------------
#Define socket constants to be used and ALTERED
#DEST_IP should be of the form '192.168.1.*' or other addresses
DESt_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
#----------------------------------------------------------------
#Define Classes
class Connection():
    '''A socket connection class for players to connect to a server'''
    def __init__(self):
        '''Init for the connection class'''
        pass

class Player():
    '''A player class the client can control'''
    def __init__(self, connection):
        '''Initialization of the Player class'''
        pass

    def set_player_info(self, player_info):
        '''set the player info to the given information from the server'''
        pass

    def update(self):
        '''Update the player by changing their coordinates in the game'''
        pass

    def reset_player(self):
        '''Reset player values for a new round on the client side'''
        pass

class Game():
    '''A game class to handle all operations of gameplay'''
    def __init__(self, connection, player, total_players):
        '''Initialization fo the Game class'''
        pass

    def ready_game(self):
        '''Ready the game to be played'''
        pass
    def start_game(self):
        '''Start the game'''
        pass

    def reset_game(self):
        '''Reset the game'''
        pass

    def send_player_info(self):
        '''Send specific info about this player to the server'''
        pass

    def recieve_player_info(self):
        '''Recieve specific info about this player from the server'''
        pass

    def recieve_pregame_state(self):
        '''Recieve ALL information about ALL players from the server before the game starts'''
        pass

    def recieve_game_state(self):
        '''Recieve all information about all players from the server during the game'''
        pass

    def process_game_state(self):
        '''Process the game state to update scores, winning player, and time, etc...'''
        pass

    def update(self):
        '''Update the game'''
        pass

    def draw(self):
        '''Draw the game and all game assets to the window'''
        pass

#Create a connection and get game window information from the server.
my_connection = Connection()

#Init pygame
pygame.init()

#Set game contants
WIDTH = 700
HEIGHT = 700
ROUND_TIME = 60
BLACK = (0,0,0)
WHITE = (255,255,255)
MAGENTA =(155,0,155)
FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont('gabriola', 28)

#Create a game window
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("~~Color Collide~~")

#Create player and game objects
my_player = Player(my_connection)
my_game = Game(my_connection, my_player, 4)

#The main game loop
running = True

while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the surface
    display_surface.fill(BLACK)

    #Update and draw Classes
    my_player.update()
    my_game.update()
    my_game.draw()

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)
