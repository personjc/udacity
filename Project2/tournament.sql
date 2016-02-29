-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches;
DROP VIEW IF EXISTS player_standings;

--Create players
CREATE TABLE players (
id serial primary key,
name text);

--Create matches
CREATE TABLE matches (
id serial primary key,
winner_id integer references players (id),
loser_id integer references players (id));

CREATE VIEW player_standings AS
    SELECT players.id, 
            players.name, 
            (SELECT COUNT(winner_id) as wins FROM matches m where players.id = m.winner_id) as wins, 
            ((SELECT COUNT(winner_id) as wins FROM matches m where players.id = m.winner_id) +
                (SELECT COUNT(loser_id) as losses FROM matches m where players.id = m.loser_id)) as matchTotal
    FROM players ORDER BY wins desc, matchTotal asc;

  






