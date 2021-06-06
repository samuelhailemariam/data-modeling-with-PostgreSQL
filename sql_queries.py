# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays (
                             songplay_id SERIAL,
                             start_time TIMESTAMP NOT NULL,
                             user_id INT NOT NULL,
                             level TEXT,
                             song_id TEXT NOT NULL,
                             artist_id TEXT NOT NULL,
                             session_id TEXT,
                             location TEXT,
                             user_agent TEXT,
                             PRIMARY KEY (songplay_id)
                            );
""")

user_table_create = ("""CREATE TABLE users (
                         user_id INT,
                         first_name TEXT NOT NULL,
                         last_name TEXT NOT NULL,
                         gender TEXT,
                         level TEXT NOT NULL,
                         PRIMARY KEY (user_id)
                        );
""")

song_table_create = ("""CREATE TABLE songs (
                         song_id TEXT,
                         title TEXT NOT NULL,
                         artist_id TEXT,
                         year INT,
                         duration NUMERIC,
                         PRIMARY KEY (song_id)
                        );
""")

artist_table_create = ("""CREATE TABLE artists (
                             artist_id TEXT,
                             name TEXT NOT NULL,
                             location TEXT,
                             latitude NUMERIC,
                             longitude numeric,
                             PRIMARY KEY (artist_id)
                            );
""")

time_table_create = ("""CREATE TABLE time (
                         start_time TIME,
                         hour INT NOT NULL,
                         day INT NOT NULL,
                         week INT NOT NULL,
                         month INT NOT NULL,
                         year INT NOT NULL,
                         weekday INT NOT NULL,
                         PRIMARY KEY (start_time)
                        );
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays 
                            (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            values(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) 
                          VALUES (%s, %s, %s, %s, %s) 
                          ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) 
                        VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                          VALUES (%s, %s, %s, %s, %s) 
                          ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s) 
                          ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT DISTINCT songs.song_id, artists.artist_id
                    FROM songs
                    JOIN artists ON songs.artist_id = artists.artist_id
                    WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]