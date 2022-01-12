"""
 * Tic Tac Toe
 * @version python 3.9
 * @since 11.01.22
 * @author Nico Schultze s0569571
 * @description: Dieses Programm enthält das Spiel TicTacToe. Das Spiel kann gegen eine andere Person auf einer anderen Maschine gespielt werden.
"""
import threading
import socket

class TicTacToe:

    def __init__(self):
        """
        Initialisiert alle wichtigen Variablen für das Programm.
        """
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.p1 = "X"
        self.p2 = "0"
        self.game_winner = None
        self.turn = "X"
        self.game_over = False
        self.counter = 0


    def hosting(self, host, port):
        """
        Hostet den Server auf dem das Spiel gespielt wird. Hierbei wird eine Socket AF_INET und Socket SOCK_STREAM Adresse genutzt.
        Über einen ausgelagerten Thread, wird dann die game_func aufgerufen, welche die Verbindung verwaltet.

        Parameters:
                    host (string): String für Localhost oder IP-Adresse
                    port (int): Integer für Portnummer

        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

        client, addr = server.accept()
        self.p1 = "X"
        self.p2 = "0"
        threading.Thread(target=self.game_func, args = (client,)).start()
        server.close()


    def connecting(self, host, port):
        """
        Verbindet den zweiten Spieler zu dem Server und ruft die game_func auf.

        Parameters:
                    host (string): String für Localhost oder IP-Adresse
                    port (int): Integer für Portnummer

        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        self.p1 = "X"
        self.p2 = "0"
        threading.Thread(target=self.game_func, args=(client,)).start()

    def game_func(self, client):
        """
        Diese Funktion verwaltet die Verbindung und sorgt für einen Datenaustausch zwischen den Systemen mittels utf-8 Encodierung. 
        Zuerst wird der Spieler nach einer Eingabe gefragt, anschließend wird diese auf Richtigkeit überprüft und gesendet. 
        In einer weiteren Methode wird die Veränderung auf das Board übernommen. 
        Falls man nicht am Zug ist werden die Daten der gegnerischen Eingabe empfangen.

        Parameters:
                    client (string): Der zu übergebene Klient.
                    

        """
        while not self.game_over:
            if self.turn == self.p1:
                move = input("Bitte den Platz des Zeichens in folgendem Format angeben -> Reihe,Zeile -> Beispiel: 2,1")
                if self.is_valid(move.split(",")): 
                    client.send(move.encode("utf-8"))
                    self.confirm_move(move.split(","), self.p1)
                    self.turn = self.p2
                else: 
                    print("Ungültige Eingabe!")
            else:
                data = client.recv(1024)
                if not data:
                    break
                else:
                    self.confirm_move(data.decode("utf-8").split(","), self.p2)
                    self.turn = self.p1
        client.close()

    def confirm_move(self, move, player):
        """
        Mit dieser Methode wird der Move auf das Board übernommen und abgebildet. Außerdem wird die gewinnende Person oder ein Unentschieden festgestellt.

        Parameters:
                    move (array): Array für die Eingabe des Feldes.
                    player (int): Angabe des Spielers.
        Returns:
                    Bricht die Methode ab falls das Spiel beendet ist.

        """
        if self.game_over:
            return

        self.counter += 1
        self.board[int(move[0])][int(move[1])] = player
        self.display_board()

        if self.is_won():
            if self.game_winner == self.p1:
                print("Herzlichen Glückwunsch - du hast das Spiel gewonnen!")
            elif self.game_winner == self.p2:
                print("Schade, du verlierst leider!")
        else:
            if self.counter == 9:
                print("Unentschieden! Ein Kampf der Giganten.")
                exit()
    
    def is_valid(self, move):
        """
        Diese Methode überprüft, ob der eingebene Move gültig oder ungültig ist.

        Parameters:
                    move (array): Array für die Eingabe des Feldes.

        Returns:
                    Returns einen Boolean, ob der Move valide ist, oder nicht.
        """
        try:
            if int(move[0]) >= 3 or int(move[0]) < 0:
                return False
            if int(move[1]) >= 3 or int(move[1]) < 0:
                return False      
            if self.board[int(move[0])][int(move[1])] == " ":
                return True
            else:
                return False
        except ValueError:
            print("Bitte die Zeile und Reihe in folgendem Format eingeben: Zeile,Reihe\nBsp: 2,1")
            
    def is_won(self):
        """
        Beinhaltet die Logik für das Gewinnen des Spiels.

        Returns:
                    Returns einen Boolean, ob das Spiel gewonnen ist, oder nicht
        """
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.game_winner = self.board[row][0]
                self.game_over = True
                return True

        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                self.game_winner = self.board[0][column]
                self.game_over = True
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.game_winner = self.board[0][0]
            self.game_over = True
            return True
        
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            self.game_winner = self.board[0][0]
            self.game_over = True
            return True
        return False

    def display_board(self):
        """
        Zeigt das Spielfeld an.
        """
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("----------------")


game = TicTacToe()
print("Willkommen zum TicTacToe Spiel! Du bist der Host des Spiels. Bitte ermittle deine IPv4 Addresse über die cmd Zeile mit *ipconfig*\n")
adress = input("Bitte hier die Adresse eingeben:\n")
port = int(input("Außerdem bitte hier eine gültige portnummer von 9000-9999 wählen:\n"))
game.hosting(adress, port)