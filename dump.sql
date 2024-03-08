-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 172.25.0.2    Database: Inventory
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `published_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` VALUES (4,'Снайперские винтовки: история и применение','Снайперская винтовка - это специализированное огнестрельное оружие, предназначенное для точной стрельбы на дальние дистанции. Она используется снайперами и специальными подразделениями вооруженных сил для нанесения точных и уничтожающих ударов по вражеским целям.\n\nИсторически, снайперские винтовки разрабатывались для обеспечения стрелковой поддержки и уничтожения целей на дальних дистанциях. Они часто имеют усиленную конструкцию и специальные оптические прицелы для повышения точности стрельбы.\n\nСовременные снайперские винтовки могут быть изготовлены из различных материалов, таких как сталь, алюминий и композитные материалы. Они также могут быть оснащены различными дополнительными приспособлениями, такими как подствольные гранатомёты и звукопоглощающие устройства.\n\nВ данной статье мы рассмотрим историю развития снайперских винтовок, их основные характеристики и применение в современном военном и спортивном мире.','2024-03-06 09:10:17'),(5,'Пистолеты: типы и особенности','Пистолет - это портативное стрелковое оружие, предназначенное для стрельбы одиночными выстрелами. Существует множество различных типов пистолетов, включая самозарядные, однозарядные, с двойным действием и многое другое. Каждый тип имеет свои особенности и преимущества.\n\nСамозарядные пистолеты, такие как Browning Hi-Power и Glock, оснащены механизмом, который автоматически загружает следующий патрон в ствол после выстрела. Однозарядные пистолеты, например, Smith & Wesson Model 10, требуют ручной перезарядки после каждого выстрела.\n\nПомимо типа заряжания, пистолеты могут различаться по калибру, размеру, материалу и конструкции. Некоторые пистолеты предназначены для самообороны, другие - для спортивной стрельбы или военного применения.\n\nВ данной статье мы рассмотрим различные типы пистолетов, их особенности и применение.','2024-03-06 09:10:21'),(6,'Штурмовые винтовки: сравнение моделей','Штурмовая винтовка - это стрелковое оружие, которое сочетает в себе характеристики винтовки и автомата. Она обладает высокой скорострельностью и удобством использования, что делает её популярным выбором в вооруженных силах и среди гражданских стрелков.\n\nСуществует множество различных моделей штурмовых винтовок, каждая из которых имеет свои уникальные характеристики и особенности. Некоторые из самых известных моделей включают в себя AK-47, M16, FN SCAR и H&K G36.\n\nПри выборе штурмовой винтовки необходимо учитывать такие факторы, как калибр, эффективная дальность стрельбы, надёжность и удобство в обращении. Кроме того, важно учитывать условия использования, такие как климатические особенности и тактические потребности.\n\nВ данной статье мы проведём сравнение нескольких популярных моделей штурмовых винтовок, чтобы помочь вам сделать более информированный выбор при покупке или использовании данного типа оружия.','2024-03-06 09:10:21'),(8,'Карабины: история и особенности','Карабин - это винтовка с короче стволом, чем у классической винтовки, что делает его более компактным и легким. Они широко используются как в военных, так и в гражданских целях, включая охоту и спортивную стрельбу.\n\nИсторически, карабины были созданы для использования кавалерией и другими войсками, которым требовалось легкое и удобное оружие. С течением времени они стали популярны среди охотников и стрелков благодаря их удобству и маневренности.\n\nСуществует множество различных моделей карабинов, включая болтовые, полуавтоматические и рычажные. Каждый тип имеет свои особенности и преимущества, в зависимости от условий использования.\n\nВ данной статье мы рассмотрим историю развития карабинов, их основные характеристики и применение в современном мире.','2024-03-07 07:55:06');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `type` varchar(50) DEFAULT NULL,
  `manufacturer` varchar(100) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (21,'Пистолет Макарова','Самозарядный пистолет Макарова','Пистолет','Ижмаш',1951,'СССР',300.00,8,'makarov.jpg'),(22,'Винтовка СВД','Снайперская винтовка','Винтовка','Ижмаш',1963,'СССР',1500.00,4,'svd.jpg'),(23,'Автомат АК-74','Автоматическая винтовка','Винтовка','Калашников',1974,'СССР',1000.00,7,'ak74.jpg'),(24,'Пулемет ПКМ','Пулемет Калашникова на машинной площадке','Пулемет','Калашников',1961,'СССР',2000.00,2,'pkm.jpg'),(25,'Пистолет ТТ','Пистолет Токарева','Пистолет','Тульский оружейный завод',1930,'СССР',4000.00,6,'tt.jpg'),(26,'Винтовка Мосина','Болтовая винтовка Мосина','Винтовка','Ижевский механический завод',1891,'СССР',600.00,3,'mosin.jpg'),(27,'Автомат Вепрь','Автомат калибра 7,62 мм','Автомат','Молот',2003,'Россия',1200.00,5,'vepr.jpg'),(28,'Ружье ИЖ-58','Двуствольное ружье','Ружье','Ижевский механический завод',1958,'СССР',700.00,4,'izh58.jpg'),(29,'Пистолет ПМ','Малогабаритный пистолет','Пистолет','Ижмаш',1951,'СССР',350.00,7,'pm.jpg'),(30,'Винтовка ТОЗ-34','Двуствольная винтовка','Винтовка','Тульский оружейный завод',1934,'СССР',5.00,2,'toz34.jpg'),(31,'Автомат АЕК-971','Автоматическая винтовка','Автомат','Ижмаш',1978,'СССР',18.00,3,'aek971.jpg'),(32,'Ружье Бекас','Охотничье ружье','Автомат','Ижмех',2000,'Россия',900.00,5,'bekas.jpg'),(33,'Пистолет ГШ-18','Пистолет самозарядный','Пистолет','ТСКИБ',2011,'Россия',650.00,4,'gsh18.jpg'),(34,'Винтовка ВСС Винторез','Снайперская винтовка','Винтовка','Тульский оружейный завод',1987,'СССР',1700.00,2,'vss.jpg'),(35,'Автомат АК-12','Автоматическая винтовка','Автомат','Ижмаш',2018,'Россия',2200.00,3,'ak12.jpg');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id_users` int NOT NULL AUTO_INCREMENT,
  `login` varchar(45) NOT NULL,
  `passw_hash` longtext NOT NULL,
  `salt` longtext NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_users`),
  UNIQUE KEY `login_UNIQUE` (`login`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'asd','71136620e088358820fd6dcea58ae8df14940c72d5298063b4bccd52dffacdf5','4169496a3a39e73a3f8dd48e44b5cd82e9a975b245c84d230bd644be2aa46667','asda'),(15,'qweqweqwe','7b261823fec254b785d542163b9aa33085324089f0048b580a2429fd85fe7bfc','01a8bff5cc408c5edb99d2c5bf1bf86d3ccf3604f702a2daec8a76fa8b5e0b5a','qweqweqwe');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-08 12:31:02
