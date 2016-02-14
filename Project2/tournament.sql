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
player_one text foreign key,
player_two text foreign key,
result text);

--create records
CREATE TABLE records (
player_id serial primary key,
record text);

CREATE VIEW player_card (
SELECT p.id, p.name, r.record 
FROM players p
JOIN records r on
p.id = r.player_id);


