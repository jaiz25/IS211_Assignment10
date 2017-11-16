CREATE TABLE artists
(id INTEGER PRIMARY KEY,
 artist_name CHAR(100));

CREATE TABLE albums
(id INTEGER,
 album_name CHAR(100),
 FOREIGN KEY (id)
	REFERENCES artists(id));
 
CREATE TABLE songs
(id INTEGER,
 song_name CHAR(100),
 track_number INTEGER,
 song_length INTEGER,
 FOREIGN KEY (id)
	REFERENCES albums(album_name));