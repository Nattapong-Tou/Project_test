BEGIN TRANSACTION;
CREATE TABLE "Customers" (
	"ID"	INTEGER NOT NULL,
	"CustomerName"	TEXT,
	"ContactName"	TEXT,
	"Address"	TEXT,
	"City"	TEXT,
	"PostalCode"	INTEGER,
	"Country"	TEXT,
	PRIMARY KEY("ID")
);
INSERT INTO "Customers" VALUES(1,'Alfreds Futterkiste','Maria Anders','Obere Str. 57','Berlin',12209,'Germany');
INSERT INTO "Customers" VALUES(2,'Ana Trujillo Emparedados y helados','Ana Trujillo','Avda. de la Constitución 2222','México D.F.',5021,'Mexico');
INSERT INTO "Customers" VALUES(3,'Antonio Moreno Taquería','Antonio Moreno','Mataderos 2312','México D.F.',5023,'Mexico');
INSERT INTO "Customers" VALUES(4,'Around the Horn','Thomas Hardy','120 Hanover Sq.','London',0,'UK');
INSERT INTO "Customers" VALUES(5,'Berglunds snabbköp','Christina Berglund','Berguvsvägen 8','Luleå',0,'Sweden');
INSERT INTO "Customers" VALUES(6,'Blauer See Delikatessen','Hanna Moos','Forsterstr. 57','Mannheim',68306,'Germany');
INSERT INTO "Customers" VALUES(7,'Blondel père et fils','Frédérique Citeaux','24, place Kléber','Strasbourg',67000,'France');
INSERT INTO "Customers" VALUES(8,'Bólido Comidas preparadas','Martín Sommer','C/ Araquil, 67','Madrid',28023,'Spain');
INSERT INTO "Customers" VALUES(9,'Bon app''','Laurence Lebihans','12, rue des Bouchers','Marseille',13008,'France');
INSERT INTO "Customers" VALUES(10,'Bottom-Dollar Marketse','Elizabeth Lincoln','23 Tsawassen Blvd.','Tsawassen',0,'Canada');
INSERT INTO "Customers" VALUES(11,'B''s Beverages','Victoria Ashworth','Fauntleroy Circus','London',0,'UK');
INSERT INTO "Customers" VALUES(12,'Cactus Comidas para llevar','Patricio Simpson','Cerrito 333','Buenos Aires',1010,'Argentina');
INSERT INTO "Customers" VALUES(13,'Centro comercial Moctezuma','Francisco Chang','Sierras de Granada 9993','México D.F.',5022,'Mexico');
INSERT INTO "Customers" VALUES(14,'Chop-suey Chinese','Yang Wang','Hauptstr. 29','Bern',3012,'Switzerland');
INSERT INTO "Customers" VALUES(15,'Comércio Mineiro','Pedro Afonso','Av. dos Lusíadas, 23','São Paulo',0,'Brazil');
INSERT INTO "Customers" VALUES(16,'Consolidated Holdings','Elizabeth Brown','Berkeley Gardens 12 Brewery','London',0,'UK');
INSERT INTO "Customers" VALUES(17,'Drachenblut Delikatessend','Sven Ottlieb','Walserweg 21','Aachen',52066,'Germany');
INSERT INTO "Customers" VALUES(18,'Du monde entier','Janine Labrune','67, rue des Cinquante Otages','Nantes',44000,'France');
INSERT INTO "Customers" VALUES(19,'Eastern Connection','Ann Devon','35 King George','London',0,'UK');
INSERT INTO "Customers" VALUES(20,'Ernst Handel','Roland Mendel','Kirchgasse 6','Graz',8010,'Austria');
INSERT INTO "Customers" VALUES(21,'Familia Arquibaldo','Aria Cruz','Rua Orós, 92','São Paulo',0,'Brazil');
INSERT INTO "Customers" VALUES(22,'FISSA Fabrica Inter. Salchichas S.A.','Diego Roel','C/ Moralzarzal, 86','Madrid',28034,'Spain');
INSERT INTO "Customers" VALUES(23,'Folies gourmandes','Martine Rancé','184, chaussée de Tournai','Lille',59000,'France');
INSERT INTO "Customers" VALUES(24,'Folk och fä HB','Maria Larsson','Åkergatan 24','Bräcke',0,'Sweden');
INSERT INTO "Customers" VALUES(25,'Frankenversand','Peter Franken','Berliner Platz 43','München',80805,'Germany');
INSERT INTO "Customers" VALUES(26,'France restauration','Carine Schmitt','54, rue Royale','Nantes',44000,'France');
INSERT INTO "Customers" VALUES(27,'Franchi S.p.A.','Paolo Accorti','Via Monte Bianco 34','Torino',10100,'Italy');
INSERT INTO "Customers" VALUES(28,'Furia Bacalhau e Frutos do Mar','Lino Rodriguez','Jardim das rosas n. 32','Lisboa',1675,'Portugal');
INSERT INTO "Customers" VALUES(29,'Galería del gastrónomo','Eduardo Saavedra','Rambla de Cataluña, 23','Barcelona',8022,'Spain');
INSERT INTO "Customers" VALUES(30,'Godos Cocina Típica','José Pedro Freyre','C/ Romero, 33','Sevilla',41101,'Spain');
INSERT INTO "Customers" VALUES(31,'Gourmet Lanchonetes','André Fonseca','Av. Brasil, 442','Campinas',0,'Brazil');
INSERT INTO "Customers" VALUES(32,'Great Lakes Food Market','Howard Snyder','2732 Baker Blvd.','Eugene',97403,'USA');
INSERT INTO "Customers" VALUES(33,'GROSELLA-Restaurante','Manuel Pereira','5ª Ave. Los Palos Grandes','Caracas',1081,'Venezuela');
INSERT INTO "Customers" VALUES(34,'Hanari Carnes','Mario Pontes','Rua do Paço, 67','Rio de Janeiro',0,'Brazil');
INSERT INTO "Customers" VALUES(35,'HILARIÓN-Abastos','Carlos Hernández','Carrera 22 con Ave. Carlos Soublette #8-35','San Cristóbal',5022,'Venezuela');
INSERT INTO "Customers" VALUES(36,'Hungry Coyote Import Store','Yoshi Latimer','City Center Plaza 516 Main St.','Elgin',97827,'USA');
INSERT INTO "Customers" VALUES(37,'Hungry Owl All-Night Grocers','Patricia McKenna','8 Johnstown Road','Cork',NULL,'Ireland');
INSERT INTO "Customers" VALUES(38,'Island Trading','Helen Bennett','Garden House Crowther Way','Cowes',0,'UK');
INSERT INTO "Customers" VALUES(39,'Königlich Essen','Philip Cramer','Maubelstr. 90','Brandenburg',14776,'Germany');
INSERT INTO "Customers" VALUES(40,'La corne d''abondance','Daniel Tonini','67, avenue de l''Europe','Versailles',78000,'France');
INSERT INTO "Customers" VALUES(41,'La maison d''Asie','Annette Roulet','1 rue Alsace-Lorraine','Toulouse',31000,'France');
INSERT INTO "Customers" VALUES(42,'Laughing Bacchus Wine Cellars','Yoshi Tannamuri','1900 Oak St.','Vancouver',0,'Canada');
INSERT INTO "Customers" VALUES(43,'Lazy K Kountry Store','John Steel','12 Orchestra Terrace','Walla Walla',99362,'USA');
INSERT INTO "Customers" VALUES(44,'Lehmanns Marktstand','Renate Messner','Magazinweg 7','Frankfurt a.M.',60528,'Germany');
INSERT INTO "Customers" VALUES(45,'Let''s Stop N Shop','Jaime Yorres','87 Polk St. Suite 5','San Francisco',94117,'USA');
INSERT INTO "Customers" VALUES(46,'LILA-Supermercado','Carlos González','Carrera 52 con Ave. Bolívar #65-98 Llano Largo','Barquisimeto',3508,'Venezuela');
INSERT INTO "Customers" VALUES(47,'LINO-Delicateses','Felipe Izquierdo','Ave. 5 de Mayo Porlamar','I. de Margarita',4980,'Venezuela');
INSERT INTO "Customers" VALUES(48,'Lonesome Pine Restaurant','Fran Wilson','89 Chiaroscuro Rd.','Portland',97219,'USA');
INSERT INTO "Customers" VALUES(49,'Magazzini Alimentari Riuniti','Giovanni Rovelli','Via Ludovico il Moro 22','Bergamo',24100,'Italy');
INSERT INTO "Customers" VALUES(50,'Maison Dewey','Catherine Dewey','Rue Joseph-Bens 532','Bruxelles',0,'Belgium');
INSERT INTO "Customers" VALUES(51,'Mère Paillarde','Jean Fresnière','43 rue St. Laurent','Montréal',0,'Canada');
INSERT INTO "Customers" VALUES(52,'Morgenstern Gesundkost','Alexander Feuer','Heerstr. 22','Leipzig',4179,'Germany');
INSERT INTO "Customers" VALUES(53,'North/South','Simon Crowther','South House 300 Queensbridge','London',0,'UK');
INSERT INTO "Customers" VALUES(54,'Océano Atlántico Ltda.','Yvonne Moncada','Ing. Gustavo Moncada 8585 Piso 20-A','Buenos Aires',1010,'Argentina');
INSERT INTO "Customers" VALUES(55,'Old World Delicatessen','Rene Phillips','2743 Bering St.','Anchorage',99508,'USA');
INSERT INTO "Customers" VALUES(56,'Ottilies Käseladen','Henriette Pfalzheim','Mehrheimerstr. 369','Köln',50739,'Germany');
INSERT INTO "Customers" VALUES(57,'Paris spécialités','Marie Bertrand','265, boulevard Charonne','Paris',75012,'France');
INSERT INTO "Customers" VALUES(58,'Pericles Comidas clásicas','Guillermo Fernández','Calle Dr. Jorge Cash 321','México D.F.',5033,'Mexico');
INSERT INTO "Customers" VALUES(59,'Piccolo und mehr','Georg Pipps','Geislweg 14','Salzburg',5020,'Austria');
INSERT INTO "Customers" VALUES(60,'Princesa Isabel Vinhoss','Isabel de Castro','Estrada da saúde n. 58','Lisboa',1756,'Portugal');
INSERT INTO "Customers" VALUES(61,'Que Delícia','Bernardo Batista','Rua da Panificadora, 12','Rio de Janeiro',0,'Brazil');
INSERT INTO "Customers" VALUES(62,'Queen Cozinha','Lúcia Carvalho','Alameda dos Canàrios, 891','São Paulo',0,'Brazil');
INSERT INTO "Customers" VALUES(63,'QUICK-Stop','Horst Kloss','Taucherstraße 10','Cunewalde',1307,'Germany');
INSERT INTO "Customers" VALUES(64,'Rancho grande','Sergio Gutiérrez','Av. del Libertador 900','Buenos Aires',1010,'Argentina');
INSERT INTO "Customers" VALUES(65,'Rattlesnake Canyon Grocery','Paula Wilson','2817 Milton Dr.','Albuquerque',87110,'USA');
INSERT INTO "Customers" VALUES(66,'Reggiani Caseifici','Maurizio Moroni','Strada Provinciale 124','Reggio Emilia',42100,'Italy');
INSERT INTO "Customers" VALUES(67,'Ricardo Adocicados','Janete Limeira','Av. Copacabana, 267','Rio de Janeiro',0,'Brazil');
INSERT INTO "Customers" VALUES(68,'Richter Supermarkt','Michael Holz','Grenzacherweg 237','Genève',1203,'Switzerland');
INSERT INTO "Customers" VALUES(69,'Romero y tomillo','Alejandra Camino','Gran Vía, 1','Madrid',28001,'Spain');
INSERT INTO "Customers" VALUES(70,'Santé Gourmet','Jonas Bergulfsen','Erling Skakkes gate 78','Stavern',4110,'Norway');
INSERT INTO "Customers" VALUES(71,'Save-a-lot Markets','Jose Pavarotti','187 Suffolk Ln.','Boise',83720,'USA');
INSERT INTO "Customers" VALUES(72,'Seven Seas Imports','Hari Kumar','90 Wadhurst Rd.','London',0,'UK');
INSERT INTO "Customers" VALUES(73,'Simons bistro','Jytte Petersen','Vinbæltet 34','København',1734,'Denmark');
INSERT INTO "Customers" VALUES(74,'Spécialités du monde','Dominique Perrier','25, rue Lauriston','Paris',75016,'France');
INSERT INTO "Customers" VALUES(75,'Split Rail Beer & Ale','Art Braunschweiger','P.O. Box 555','Lander',82520,'USA');
INSERT INTO "Customers" VALUES(76,'Suprêmes délices','Pascale Cartrain','Boulevard Tirou, 255','Charleroi',0,'Belgium');
INSERT INTO "Customers" VALUES(77,'The Big Cheese','Liz Nixon','89 Jefferson Way Suite 2','Portland',97201,'USA');
INSERT INTO "Customers" VALUES(78,'The Cracker Box','Liu Wong','55 Grizzly Peak Rd.','Butte',59801,'USA');
INSERT INTO "Customers" VALUES(79,'Toms Spezialitäten','Karin Josephs','Luisenstr. 48','Münster',44087,'Germany');
INSERT INTO "Customers" VALUES(80,'Tortuga Restaurante','Miguel Angel Paolino','Avda. Azteca 123','México D.F.',5033,'Mexico');
INSERT INTO "Customers" VALUES(81,'Tradição Hipermercados','Anabela Domingues','Av. Inês de Castro, 414','São Paulo',0,'Brazil');
INSERT INTO "Customers" VALUES(82,'Trail''s Head Gourmet Provisioners','Helvetius Nagy','722 DaVinci Blvd.','Kirkland',98034,'USA');
INSERT INTO "Customers" VALUES(83,'Vaffeljernet','Palle Ibsen','Smagsløget 45','Århus',8200,'Denmark');
INSERT INTO "Customers" VALUES(84,'Victuailles en stock','Mary Saveley','2, rue du Commerce','Lyon',69004,'France');
INSERT INTO "Customers" VALUES(85,'Vins et alcools Chevalier','Paul Henriot','59 rue de l''Abbaye','Reims',51100,'France');
INSERT INTO "Customers" VALUES(86,'Die Wandernde Kuh','Rita Müller','Adenauerallee 900','Stuttgart',70563,'Germany');
INSERT INTO "Customers" VALUES(87,'Wartian Herkku','Pirkko Koskitalo','Torikatu 38','Oulu',90110,'Finland');
INSERT INTO "Customers" VALUES(88,'Wellington Importadora','Paula Parente','Rua do Mercado, 12','Resende',0,'Brazil');
INSERT INTO "Customers" VALUES(89,'White Clover Markets','Karl Jablonski','305 - 14th Ave. S. Suite 3B','Seattle',98128,'USA');
INSERT INTO "Customers" VALUES(90,'Wilman Kala','Matti Karttunen','Keskuskatu 45','Helsinki',21240,'Finland');
INSERT INTO "Customers" VALUES(91,'Wolski','Zbyszek','ul. Filtrowa 68','Walla',0,'Poland');
CREATE TABLE "OrderDetails" (
  "OrderDetailID" INTEGER(255) NOT NULL,
  "OrderID" INTEGER(255),
  "ProductID" INTEGER(255),
  "Quantity" INTEGER(255),
  PRIMARY KEY ("OrderDetailID")
);
INSERT INTO "OrderDetails" VALUES(1,10248,11,12);
INSERT INTO "OrderDetails" VALUES(2,10248,42,10);
INSERT INTO "OrderDetails" VALUES(3,10248,72,5);
INSERT INTO "OrderDetails" VALUES(4,10249,14,9);
INSERT INTO "OrderDetails" VALUES(5,10249,51,40);
CREATE TABLE "Products" (
  "ProductID" INTEGER(255) NOT NULL,
  "ProductName" TEXT(255),
  "SupplierID" INTEGER(255),
  "CategoryID" INTEGER(255),
  "Unit" text,
  "Price" INTEGER(255),
  PRIMARY KEY ("ProductID")
);
INSERT INTO "Products" VALUES(1,'Chais',1,1,'10 boxes x 20 bags',18);
INSERT INTO "Products" VALUES(2,'Chang',1,1,'24 - 12 oz bottles',19);
INSERT INTO "Products" VALUES(3,'Aniseed Syrup',1,2,'12 - 550 ml bottles',10);
INSERT INTO "Products" VALUES(4,'Chef Anton''s Cajun Seasoning',2,2,'48 - 6 oz jars',22);
INSERT INTO "Products" VALUES(5,'Chef Anton''s Gumbo Mix',2,2,'36 boxes',21.35);
COMMIT;
