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
winner integer REFERENCES players (id),
loser integer REFERENCES players (id));

--create records
CREATE TABLE records (
player_id integer REFERENCES players (id),
wins integer,
losses integer);

--Get info
SELECT p.id, p.name, COUNT(m.winner) AS wins, COUNT(m.loser) as losses
FROM players p JOIN matches m
ON p.id = m.winner
group by p.id
ORDER BY wins DESC, losses asc;

SELECT * 
FROM players p, 
(SELECT COUNT(*) FROM matches m GROUP BY m.winner) as wins,
(SELECT COUNT(*) FROM matches m GROUP BY m.loser) as losses


  






