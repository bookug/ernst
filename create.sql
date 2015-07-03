create database if not exists platform character set utf8;
use platform;

create table if not exists User (
		userID		integer		auto_increment,
		nickName	varchar(30)	not null,
		roomID		integer		not null default 0,
		primary key (userID), 
		unique index (userID ASC)
);

create table if not exists Act (
		actID		integer		auto_increment,
		actName		varchar(30)	not null,
		actNum		integer		not null,
		primary key (actID),
		unique index (actID ASC)
);

create table if not exists Room (
		roomID		integer		auto_increment,
		actID		integer		not null,
		leadID		integer		not null,
		primary key (roomID),
		foreign key (actID) references Act (actID),
		foreign key (leadID) references User (userID),
		unique index (roomID ASC)
);

