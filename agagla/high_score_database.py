import pymysql
from pymysql import Error

class HighScoreDatabase:
    def __init__(self):
        self.host = 'agaglahighscores.ctozcqhjjpwh.us-east-2.rds.amazonaws.com'
        self.user = 'agagla'
        self.password = 'PHwSIKYdEzQn1zX8KL5a'
        self.database = 'agaglahighscores'
        self.highscores = 0

    def add_high_score(self, name, score):

        try:
            connection = pymysql.connect(host=self.host,
                                         database=self.database,
                                         user=self.user,
                                         password=self.password)
            if connection.open:
                cursor = connection.cursor()
                cursor.execute('SELECT ag_rank, game_name, high_score FROM highscores ORDER BY ag_rank;')
                self.highscores = cursor.fetchall()
                rank = self._findrank(score, self.highscores)
                updatequery = 'UPDATE highscores SET game_name =\'' + name + '\', high_score =' + str(
                    score) + ' WHERE ag_rank = ' + str(rank) + ';'
                if rank == 10:
                    cursor.execute(updatequery)
                    connection.commit()
                    return True
                elif rank < 10:
                    for i in range(len(self.highscores)-1, rank, -1):
                        updatequery = 'UPDATE highscores SET game_name =\'' + self.highscores[i-1][1] + '\', high_score =' + str(
                            self.highscores[i-1][2]) + ' WHERE ag_rank = ' + str(i+1) + ';'
                        cursor.execute(updatequery)
                    updatequery = 'UPDATE highscores SET game_name =\'' + name + '\', high_score =' + str(score) + ' WHERE ag_rank = ' + str(rank+1) + ';'
                    cursor.execute((updatequery))
                    connection.commit()
                    return True
                else:
                    return False

        except Error as e:
            print("Error while connecting to MySQL", e)
            return False
        finally:
            if connection.open:
                cursor.close()
                connection.close()

        return True

    def get_high_score(self):
        try:
            connection = pymysql.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            if connection.open:
                cursor = connection.cursor()
                cursor.execute('SELECT ag_rank, game_name, high_score FROM highscores ORDER BY ag_rank;')
                self.highscores = cursor.fetchall()

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.open:
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                return self.highscores

    def _findrank(self, score, highscores):
        for i in range(0, len(highscores)):
            if highscores[i][2] >= score:
                continue
            else:
                print(i)
                return i
        return 100
