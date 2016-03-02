#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
# Author - John Person

import psycopg2
import random
from contextlib import contextmanager


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Connection to database failed")


def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute('DELETE FROM matches;')


def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as cursor:
        cursor.execute('DELETE FROM players;')


def countPlayers():
    """Returns the number of players currently registered."""
    with get_cursor() as cursor:
        cursor.execute('SELECT COUNT(*) AS NUM FROM players;')
        count = cursor.fetchall()
        return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as cursor:
        cursor.execute('INSERT INTO players (name) VALUES (%s);', (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM player_standings;")
        rows = cursor.fetchall()
        return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO matches (winner_id, loser_id, bye)  \
                    VALUES (%s, %s, false);", (winner, loser,))


def reportByeMatch(player_id):
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO matches (winner_id, bye)  \
                    VALUES (%s, true);", (player_id,))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    rows = playerStandings()
    match_list = []

    """ If there are an odd number of players,
         assign bye to random player who has not received one yet
    """
    if len(rows) % 2 == 1:
        while True:
            row_num = random.randint(0, len(rows) - 1)
            if awardedBye(rows[row_num][0]) == False:
                break

        reportByeMatch(rows[row_num][0])
        del rows[row_num]

    """Compiles matches into one list"""
    for i in range(0, len(rows) / 2):
        player_one = rows[2 * i]
        player_two = rows[2 * i + 1]

        match_list.append(
                [player_one[0], player_one[1], player_two[0], player_two[1]]
         )

    return match_list


def awardedBye(player_id):
    with get_cursor() as cursor:
        cursor.execute('SELECT bye FROM matches  \
            WHERE bye = true AND winner_id = %s', (player_id,))

        if len(cursor.fetchall()) == 1:
            return True
        else:
            return False


@contextmanager
def get_cursor():
    """
    Query helper function using context lib. Creates a cursor from a database
    connection object, and performs queries using that cursor.
    """
    conn = connect()
    cursor = conn.cursor()
    try:
        yield cursor
    except:
        raise
    else:
        conn.commit()
    finally:
        cursor.close()
        conn.close()
