# tictactoe

Dies ist eine Implementation für eine Multiplayer Umsetzung des Spiels TicTacToe. Dieses kann auf zwei verteilten Systemen mittels Sockets gespielt werden.
Dabei gibt es einen host und eine verbindende Person.

Spielablauf:

-Host-

1.  Der Host muss hierbei die Datei in einer Commandozeilen Umbebung per: "python .../.../host.py" ausführen.

2.  Nun muss der Host seine IP-Adresse mittels einem neuen Commandofenster ermitteln: "ipconfig"
    Diese wird nun notiert.

3.  Der Host wird aufgefordert die IP-Adresse 1:1 in das Fenster einzutragen.

4.  Als nächstes wird der Host gefragt eine Portnummer zwischen 9000-9999 einzugeben.

-Zweiter Spieler-

5. Die verbindende Person muss die zweite Datei in einer Commandozeilen Umgebung ausführen: "python .../.../connecting_person.py"

6. Als nächstes muss der zweite Spieler die IP-Adresse von dem Host eintragen.

7. Zuletzt muss die gleiche Portnummer des Hosts eingetragen werden.

-Beide-

8. Nun kann das Spiel begonnen werden und jeder kann seinen Zug machen bis das Spiel beendet ist.

Quellen:
Auf alle QUellen wurde zuletzt am 12.01.2022 um 13:15 zugegriffen.

https://www.geeksforgeeks.org/sockets-python/
https://www.askpython.com/python/examples/tic-tac-toe-using-python
https://www.youtube.com/watch?v=s6HOPw_5XuY
https://www.python.org/doc/
https://docs.python.org/3/library/threading.html
