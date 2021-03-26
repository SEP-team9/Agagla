import pymysql
from pymysql import Error

host = 'agaglahighscores.ctozcqhjjpwh.us-east-2.rds.amazonaws.com'
user = 'agagla'
password = 'PHwSIKYdEzQn1zX8KL5a'
database = 'agaglahighscores'
highscorequery = 'SELECT ag_rank, game_name, high_score FROM highscores ORDER BY ag_rank;'

class HighScoreDatabase:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.highscores = 0

    def add_high_score(self, name, score):
        self.highscores = self.get_high_score()

        connection = self._get_connection()
        if connection == False:
            return False
        cursor = connection.cursor()
        rank = self._findrank(score, self.highscores)
        updatequery = 'UPDATE highscores SET game_name =\'' + name + '\', high_score =' + str(
            score) + ' WHERE ag_rank = ' + str(rank) + ';'
        if rank == 10:
            cursor.execute(updatequery)
            connection.commit()
            self._close_connection(connection, cursor)
            return True
        elif rank < 10:
            for i in range(len(self.highscores)-1, rank, -1):
                updatequery = 'UPDATE highscores SET game_name =\'' + self.highscores[i-1][1] + '\', high_score =' + str(
                    self.highscores[i-1][2]) + ' WHERE ag_rank = ' + str(i+1) + ';'
                cursor.execute(updatequery)
            updatequery = 'UPDATE highscores SET game_name =\'' + name + '\', high_score =' + str(score) + ' WHERE ag_rank = ' + str(rank+1) + ';'
            cursor.execute(updatequery)
            connection.commit()
            self._close_connection(connection, cursor)
            return True
        else:
            return False

    def get_high_score(self):
            connection = self._get_connection()
            if connection == False:
                return 0
            cursor = connection.cursor()
            cursor.execute(highscorequery)
            self.highscores = cursor.fetchall()
            self._close_connection(connection, cursor)
            return self.highscores

    def _findrank(self, score, highscores):
        for i in range(0, len(highscores)):
            if highscores[i][2] >= score:
                continue
            else:
                return i
        return 100

    def _get_connection(self):
        try:
            connection = pymysql.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            if connection.open:
                return connection

        except Error as e:
            print("Error while connecting to MySQL", e)
            return False

    def _close_connection(self, connection, cursor):
            if connection.open:
                cursor.close()
                connection.close()