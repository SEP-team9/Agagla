import pymysql
from pymysql import Error


class HighScoreDatabase:

    def add_high_score(self, name, score):
        highscores = self.get_high_score()
        connection = self._get_connection()
        if connection == False:
            return False
        cursor = connection.cursor()
        rank = self._findrank(score, highscores)
        if rank <= 10:
            for i in range(len(highscores) - 1, rank, -1):
                cursor.execute(self._get_update_query(highscores[i - 1][1], highscores[i - 1][2], (i + 1)))
            cursor.execute(self._get_update_query(name, score, rank + 1))
            connection.commit()
            self._close_connection(connection, cursor)
            return True
        else:
            self._close_connection(connection, cursor)
            return False

    def get_high_score(self):
        connection = self._get_connection()
        if connection == False:
            return 0
        cursor = connection.cursor()
        cursor.execute('SELECT ag_rank, game_name, high_score FROM highscores ORDER BY ag_rank;')
        highscores = cursor.fetchall()
        self._close_connection(connection, cursor)
        return highscores

    def _findrank(self, score, highscores):
        for i in range(0, len(highscores)):
            if highscores[i][2] >= score:
                continue
            else:
                return i
        return 100

    def _get_update_query(self, name, score, rank):
        return 'UPDATE highscores SET game_name =\'' + name + '\', high_score =' + str(
            score) + ' WHERE ag_rank = ' + str(rank) + ';'

    def _get_connection(self):
        try:
            connection = pymysql.connect(host='agaglahighscores.ctozcqhjjpwh.us-east-2.rds.amazonaws.com',
                                         database='agaglahighscores',
                                         user='agagla',
                                         password='PHwSIKYdEzQn1zX8KL5a')
            if connection.open:
                return connection
        except Error as e:
            print("Error while connecting to MySQL", e)
            return False

    def _close_connection(self, connection, cursor):
        if connection.open:
            cursor.close()
            connection.close()
