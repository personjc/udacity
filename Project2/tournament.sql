-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Create players
CREATE TABLE players (
id serial primary key,
name text);

--Create matches
CREATE TABLE matches (
id serial primary key,
winner_id integer REFERENCES players (id),
loser_id integer REFERENCES players (id));

--Get info
SELECT players.id, players.name,
    (SELECT COUNT(winner) as wins FROM matches m where players.id = m.winner) as wins, 
    (SELECT COUNT(loser) as losses FROM matches m where players.id = m.loser) as losses
FROM players;


  






