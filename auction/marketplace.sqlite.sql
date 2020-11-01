BEGIN TRANSACTION;
DROP TABLE IF EXISTS "users";
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(100) NOT NULL,
	"emailid"	VARCHAR(100) NOT NULL,
	"password_hash"	VARCHAR(255) NOT NULL,
	"contact_number"	INTEGER NOT NULL,
	"address"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "watchlists";
CREATE TABLE IF NOT EXISTS "watchlists" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"item_id"	INTEGER,
	"date_added"	DATETIME,
	FOREIGN KEY("item_id") REFERENCES "items"("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "bids";
CREATE TABLE IF NOT EXISTS "bids" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"item_id"	INTEGER,
	"bid_amount"	INTEGER NOT NULL,
	"date_added"	DATETIME,
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	FOREIGN KEY("item_id") REFERENCES "items"("id"),
	UNIQUE("bid_amount"),
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "items";
CREATE TABLE IF NOT EXISTS "items" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(100) NOT NULL,
	"description"	VARCHAR(200) NOT NULL,
	"artist"	VARCHAR(100) NOT NULL,
	"genre"	VARCHAR(80) NOT NULL,
	"year"	INTEGER NOT NULL,
	"designation"	VARCHAR(80) NOT NULL,
	"image"	VARCHAR(400) NOT NULL,
	"starting_value"	INTEGER NOT NULL,
	"status"	VARCHAR(80) NOT NULL,
	"user_id"	INTEGER,
	"current_value"	INTEGER,
	"bid_number"	INTEGER,
	"date_posted"	TEXT NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	PRIMARY KEY("id")
);
INSERT INTO "users" ("id","name","emailid","password_hash","contact_number","address") VALUES (1,'TESTINGUSER','TESTINGEMAIL@EMAIL.COM','pbkdf2:sha256:150000$I34FSKv4$cd9d5f84510089375d57f09b6cd1f01cd4e16bc619ccd3adfd88bf99a2a8d974',4444,'1 TEST ADDRESS'),
 (2,'TESTINGUSER2','TESTINGEMAIL2@EMAIL.COM','pbkdf2:sha256:150000$ld2O9m94$7cced5426f5f8d18cd75213e3f4fec2ad168be1001f1132cd47e1fb64f8284b8',55555,'2 TEST ADDRESS'),
 (3,'TESTUSER3','TESTEMAIL3@GMAIL.COM','pbkdf2:sha256:150000$t6zi9mog$ea84440fa8ec070099e942e4b6e2214747655764cf90d455476223078198b5f9',6666666,'3 TEST ADDRESS');
INSERT INTO "bids" ("id","user_id","item_id","bid_amount","date_added") VALUES (1,2,26,42,'2020-10-28 15:31:10.399027'),
 (2,1,26,50,'2020-10-28 15:43:36.322917'),
 (3,1,26,55,'2020-10-28 16:05:57.724701'),
 (4,1,25,25,'2020-10-28 16:12:56.523009'),
 (5,1,26,70,'2020-10-28 16:20:35.347833'),
 (6,3,26,80,'2020-10-28 16:33:27.982803'),
 (7,3,2,89,'2020-10-31 16:32:39.745511'),
 (8,3,3,93,'2020-10-31 16:33:52.811846'),
 (9,3,3,98,'2020-10-31 16:34:01.435136'),
 (10,3,25,32,'2020-10-31 16:43:31.785949'),
 (11,3,24,33,'2020-10-31 17:50:11.518948'),
 (12,3,24,34,'2020-10-31 17:51:00.477953'),
 (13,3,24,44,'2020-10-31 17:53:09.101805'),
 (14,3,24,45,'2020-10-31 17:53:30.641337'),
 (15,3,25,43,'2020-10-31 17:55:32.067136'),
 (16,3,26,83,'2020-10-31 17:56:21.742082'),
 (17,3,26,90,'2020-10-31 17:57:29.621617'),
 (18,3,26,95,'2020-10-31 18:07:19.617800');
INSERT INTO "items" ("id","name","description","artist","genre","year","designation","image","starting_value","status","user_id","current_value","bid_number","date_posted") VALUES (2,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','Dummies','Rock',1984,'12-inch','../static/images/record2.jpg',84,'OPEN',2,89,1,'2020-10-11 11:33:22. 123'),
 (3,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Blues',1989,'12-inch','../static/images/record3.jpg',68,'OPEN',2,98,2,'2020-10-11 17:33:22. 123'),
 (4,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Hip Hop',1999,'12-inch','../static/images/record2.jpg',35,'OPEN',2,35,0,'2020-09-11 11:33:22. 123'),
 (5,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','EDM',2005,'10-inch','../static/images/record5.jpg',65,'OPEN',NULL,65,0,'2020-10-11 09:33:22. 123'),
 (6,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Rock',1973,'10-inch','../static/images/record6.jpg',23,'OPEN',NULL,23,0,'2020-10-01 11:33:22. 123'),
 (7,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Country',1974,'12-inch','../static/images/record7.jpg',77,'OPEN',NULL,77,0,'2020-10-06 11:33:22. 123'),
 (8,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Jazz',1993,'7-inch','../static/images/record8.jpg',56,'OPEN',NULL,56,0,'2020-10-09 11:32:22. 123'),
 (9,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Hip Hop',1998,'7-inch','../static/images/record9.jpg',86,'OPEN',NULL,86,0,'2020-10-04  19:33:22. 123'),
 (10,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Techno',2000,'12-inch','../static/images/record2.jpg',34,'OPEN',NULL,34,0,'2020-02-11 11:39:22. 123'),
 (11,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Rock',2002,'7-inch','../static/images/record9.jpg',65,'OPEN',NULL,65,0,'2020-08-11 11:33:22. 123'),
 (13,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Rock',2009,'12-inch','../static/images/record1.jpg',64,'OPEN',NULL,64,0,'2020-09-11 11:23:22. 123'),
 (14,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Blues',1977,'7-inch','../static/images/record4.jpg',75,'OPEN',NULL,75,0,'2020-09-11 14:33:22. 123'),
 (15,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Hip Hop',1992,'12-inch','../static/images/record9.jpg',34,'OPEN',NULL,34,0,'2020-10-12 11:53:22. 123'),
 (16,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','EDM',2007,'10-inch','../static/images/record2.jpg',99,'OPEN',NULL,99,0,'2020-10-11 01:33:22. 123'),
 (17,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Rock',1989,'12-inch','../static/images/record6.jpg',78,'OPEN',NULL,78,0,'2020-10-10 11:13:22. 123'),
 (18,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Country',1984,'12-inch','../static/images/record2.jpg',79,'OPEN',NULL,79,0,'2020-09-23 11:33:22. 123'),
 (19,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Jazz',1982,'12-inch','../static/images/record1.jpg',45,'OPEN',NULL,45,0,'2020-09-26 11:33:22. 123'),
 (20,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Hip Hop',1997,'7-inch','../static/images/record8.jpg',34,'OPEN',NULL,34,0,'2020-09-29 11:31:22. 123'),
 (21,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Techno',2008,'12-inch','../static/images/record9.jpg',94,'OPEN',NULL,94,0,'2020-09-22 14:33:22. 123'),
 (22,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Rock',1974,'12-inch','../static/images/record7.jpg',25,'OPEN',NULL,25,0,'2020-09-30 11:33:22. 123'),
 (23,'Best of The Dummies','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua','The Dummies','Pop',1994,'12-inch','../static/images/record4.jpg',34,'OPEN',NULL,34,0,'2020-08-12 11:13:22. 123'),
 (24,'test','test desc','test artist','Hip Hop',1999,'8-inch','/static/images/record5.jpg',22,'OPEN',3,45,4,'2020-10-27'),
 (25,'test','test desc','test artist','EDM',1988,'7-inch','/static/images/record3.jpg',24,'OPEN',3,43,3,'2020-10-27 18:10:56.419048'),
 (26,'bidtester','bidtester','bidtester','Jazz',2000,'12-inch','/static/images/methode_times_prod_web_bin_cfa57f30-919b-11e8-a10e-53179592953e.jpg',20,'OPEN',2,95,7,'2020-10-28 15:10:47.360519');
DROP INDEX IF EXISTS "ix_users_name";
CREATE UNIQUE INDEX IF NOT EXISTS "ix_users_name" ON "users" (
	"name"
);
DROP INDEX IF EXISTS "ix_users_emailid";
CREATE INDEX IF NOT EXISTS "ix_users_emailid" ON "users" (
	"emailid"
);
DROP INDEX IF EXISTS "ix_items_artist";
CREATE INDEX IF NOT EXISTS "ix_items_artist" ON "items" (
	"artist"
);
DROP INDEX IF EXISTS "ix_items_name";
CREATE INDEX IF NOT EXISTS "ix_items_name" ON "items" (
	"name"
);
DROP INDEX IF EXISTS "ix_items_genre";
CREATE INDEX IF NOT EXISTS "ix_items_genre" ON "items" (
	"genre"
);
DROP INDEX IF EXISTS "ix_items_status";
CREATE INDEX IF NOT EXISTS "ix_items_status" ON "items" (
	"status"
);
COMMIT;
