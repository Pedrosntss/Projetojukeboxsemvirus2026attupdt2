create database jukebox;
use jukebox;

CREATE TABLE historico_musica(
	id BIGINT AUTO_INCREMENT,
    musica varchar(100),
    data_musica DATETIME
);