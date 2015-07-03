use platform;

insert into User(nickName) values("sb01"), ("sb02"), ("sb03");
insert into Act(actName, actNum) values("gobang", 2), ("siguo", 4);
insert into Room values(1, 1), (2, 2);
update User set roomID = 1 where userID = 1;
update User set roomID = 2 where userID = 2;
update User set roomID = 1 where userID = 3;

