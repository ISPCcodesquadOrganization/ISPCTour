-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: ispc_tour
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `destino`
--

DROP TABLE IF EXISTS `destino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `destino` (
  `idDestino` int NOT NULL AUTO_INCREMENT,
  `nombreDestino` varchar(45) NOT NULL,
  `descripcion` varchar(500) DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `habilitado` tinyint DEFAULT '1',
  PRIMARY KEY (`idDestino`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destino`
--

LOCK TABLES `destino` WRITE;
/*!40000 ALTER TABLE `destino` DISABLE KEYS */;
INSERT INTO `destino` VALUES (1,'Bariloche','buen viaje',300,1),(2,'Jujuy','lindo viaje',500,0),(3,'El Calafate','espectacular',1000,1),(4,'Ushuaia','muy lindo',150,1);
/*!40000 ALTER TABLE `destino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoteles`
--

DROP TABLE IF EXISTS `hoteles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoteles` (
  `idHoteles` int NOT NULL AUTO_INCREMENT,
  `nombreHotel` varchar(45) NOT NULL,
  `direccionHotel` varchar(150) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `Destino_idDestino` int NOT NULL,
  PRIMARY KEY (`idHoteles`,`Destino_idDestino`),
  KEY `fk_Hoteles_Destino1_idx` (`Destino_idDestino`),
  CONSTRAINT `fk_Hoteles_Destino1` FOREIGN KEY (`Destino_idDestino`) REFERENCES `destino` (`idDestino`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoteles`
--

LOCK TABLES `hoteles` WRITE;
/*!40000 ALTER TABLE `hoteles` DISABLE KEYS */;
INSERT INTO `hoteles` VALUES (1,'Howard Johnson Jujuy','Gral. Güemes 864, San Salvador de Jujuy, Jujuy','0388 424-9800',2),(2,'Parque Hotel Jujuy','Gral. Alvear 1324, San Salvador de Jujuy, Jujuy','0388 15-682-1084',2),(3,'HOTEL ICONICO','Gral. Alvear 627, San Salvador de Jujuy, Jujuy','0388 422-2982',2),(4,'La Cantera Hotel','C. 306,  El Calafate, Santa Cruz','011 5365-8399',3),(5,'Lagos Del Calafate','Calle 998, Numero 59, El Calafate, Santa Cruz','02902 49-1777',3),(6,'Hotel Mirador del Lago','Av. del Libertador 2047,  El Calafate, Santa Cruz','02902 49-3213',3),(7,'Hotel NH Bariloche Edelweiss','San Martín 202, R8500ALP San Carlos de Bariloche, Río Negro','0294 444-5500',1),(8,'Selina Bariloche','Av. de los Pioneros 200, San Carlos de Bariloche, Río Negro','0294 15-412-0907',1),(9,'Hotel Concorde Bariloche','Libertad 131, San Carlos de Bariloche, Río Negro','0294 442-4500',1),(10,'Hotel Albatros','Av. Maipú 505, Ushuaia, Tierra del Fuego','02901 43-7300',4),(11,'De Los Andes Hotel','Av. San Martín 753, Tierra del Fuego','02901 42-1460',4),(12,'Canal Beagle Hotel','Av. Maipú 547,  Ushuaia, Tierra del Fuego','02901 42-1356',4);
/*!40000 ALTER TABLE `hoteles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paquetes`
--

DROP TABLE IF EXISTS `paquetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paquetes` (
  `idPaquetes` int NOT NULL AUTO_INCREMENT,
  `fechaInicio` date NOT NULL,
  `fechaFin` date NOT NULL,
  `Destino_idDestino` int NOT NULL,
  `TipoTransporte_idTipoTransporte` int NOT NULL,
  `cantidadViajantes` int NOT NULL,
  `Tipo de rol_idTipo de rol` int NOT NULL,
  PRIMARY KEY (`idPaquetes`,`Destino_idDestino`,`TipoTransporte_idTipoTransporte`,`Tipo de rol_idTipo de rol`),
  KEY `fk_Paquetes_Destino1_idx` (`Destino_idDestino`),
  KEY `fk_Paquetes_TipoTransporte1_idx` (`TipoTransporte_idTipoTransporte`),
  KEY `fk_Paquetes_Tipo de rol1_idx` (`Tipo de rol_idTipo de rol`),
  CONSTRAINT `fk_Paquetes_Destino1` FOREIGN KEY (`Destino_idDestino`) REFERENCES `destino` (`idDestino`),
  CONSTRAINT `fk_Paquetes_Tipo de rol1` FOREIGN KEY (`Tipo de rol_idTipo de rol`) REFERENCES `tipo de rol` (`idTipo de rol`),
  CONSTRAINT `fk_Paquetes_TipoTransporte1` FOREIGN KEY (`TipoTransporte_idTipoTransporte`) REFERENCES `tipotransporte` (`idTipoTransporte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paquetes`
--

LOCK TABLES `paquetes` WRITE;
/*!40000 ALTER TABLE `paquetes` DISABLE KEYS */;
/*!40000 ALTER TABLE `paquetes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas`
--

DROP TABLE IF EXISTS `personas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personas` (
  `idUsuarios` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nombreUsuario` varchar(45) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `direccionUsuario` varchar(150) NOT NULL,
  `contraseña` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUsuarios`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas`
--

LOCK TABLES `personas` WRITE;
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` VALUES (1,'Franco','Orellana','franco@gmail.com','franco','351-7894561','Sarmiento 123','1234'),(2,'Virginia','Falconi','virginia@gmail.com','virginia','351-3216547','San martin 45','1234'),(3,'Marcelo','Luna','marcelo@gmail.com','marcelo','351-5874321','Belgrano 654','1234'),(4,'Miguel','Gonzalez','miguel@gmail.com','miguel','351-7539696','Guemes 784','1234'),(5,'Marcos','Ugarte','marcos@gmail.com','marcos','351-8529631','Patria 156','1234'),(6,'javier','asdfklñj','fasd','javier','f','asdfasd','asdf'),(7,'asdf','asdf','asdf','javier1','asdf','asdf',''),(8,'Chanchin','ninguno','a@a.com','chanchin','12345798','asfdasf 1234','1234'),(9,'hola','quetal','asdf','hola','asdf','asdf','1234'),(10,'1324','1234','1234','1234','1234','1234','1234'),(11,'t','t','t','t','t','t','t'),(12,'w','w','w','w','w','w','w'),(13,'k','k','k','k','k','k','k'),(14,'v','v','v','v','v','v','v'),(15,'','','','g','','',''),(16,'hhh','hhh','h','i','h','hh','hhh'),(17,'','','','','','',''),(18,'b','b','b','b','b','b',''),(19,'c','c','c','c','c','c','c');
/*!40000 ALTER TABLE `personas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_has_paquetes`
--

DROP TABLE IF EXISTS `personas_has_paquetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personas_has_paquetes` (
  `Personas_idUsuarios` int NOT NULL,
  `Paquetes_idPaquetes` int NOT NULL,
  `Paquetes_Destino_idDestino` int NOT NULL,
  `Paquetes_TipoTransporte_idTipoTransporte` int NOT NULL,
  `Paquetes_Tipo de rol_idTipo de rol` int NOT NULL,
  PRIMARY KEY (`Personas_idUsuarios`,`Paquetes_idPaquetes`,`Paquetes_Destino_idDestino`,`Paquetes_TipoTransporte_idTipoTransporte`,`Paquetes_Tipo de rol_idTipo de rol`),
  KEY `fk_Personas_has_Paquetes_Paquetes1_idx` (`Paquetes_idPaquetes`,`Paquetes_Destino_idDestino`,`Paquetes_TipoTransporte_idTipoTransporte`,`Paquetes_Tipo de rol_idTipo de rol`),
  KEY `fk_Personas_has_Paquetes_Personas1_idx` (`Personas_idUsuarios`),
  CONSTRAINT `fk_Personas_has_Paquetes_Paquetes1` FOREIGN KEY (`Paquetes_idPaquetes`, `Paquetes_Destino_idDestino`, `Paquetes_TipoTransporte_idTipoTransporte`, `Paquetes_Tipo de rol_idTipo de rol`) REFERENCES `paquetes` (`idPaquetes`, `Destino_idDestino`, `TipoTransporte_idTipoTransporte`, `Tipo de rol_idTipo de rol`),
  CONSTRAINT `fk_Personas_has_Paquetes_Personas1` FOREIGN KEY (`Personas_idUsuarios`) REFERENCES `personas` (`idUsuarios`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_has_paquetes`
--

LOCK TABLES `personas_has_paquetes` WRITE;
/*!40000 ALTER TABLE `personas_has_paquetes` DISABLE KEYS */;
/*!40000 ALTER TABLE `personas_has_paquetes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas_has_tipo de rol`
--

DROP TABLE IF EXISTS `personas_has_tipo de rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personas_has_tipo de rol` (
  `Personas_idUsuarios` int NOT NULL,
  `Tipo de rol_idTipo de rol` int NOT NULL,
  PRIMARY KEY (`Personas_idUsuarios`,`Tipo de rol_idTipo de rol`),
  KEY `fk_Personas_has_Tipo de rol_Tipo de rol1_idx` (`Tipo de rol_idTipo de rol`),
  KEY `fk_Personas_has_Tipo de rol_Personas1_idx` (`Personas_idUsuarios`),
  CONSTRAINT `fk_Personas_has_Tipo de rol_Personas1` FOREIGN KEY (`Personas_idUsuarios`) REFERENCES `personas` (`idUsuarios`),
  CONSTRAINT `fk_Personas_has_Tipo de rol_Tipo de rol1` FOREIGN KEY (`Tipo de rol_idTipo de rol`) REFERENCES `tipo de rol` (`idTipo de rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas_has_tipo de rol`
--

LOCK TABLES `personas_has_tipo de rol` WRITE;
/*!40000 ALTER TABLE `personas_has_tipo de rol` DISABLE KEYS */;
INSERT INTO `personas_has_tipo de rol` VALUES (1,1),(2,1),(3,1),(4,1),(5,1);
/*!40000 ALTER TABLE `personas_has_tipo de rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo de rol`
--

DROP TABLE IF EXISTS `tipo de rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo de rol` (
  `idTipo de rol` int NOT NULL AUTO_INCREMENT,
  `Rol` varchar(45) NOT NULL,
  PRIMARY KEY (`idTipo de rol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo de rol`
--

LOCK TABLES `tipo de rol` WRITE;
/*!40000 ALTER TABLE `tipo de rol` DISABLE KEYS */;
INSERT INTO `tipo de rol` VALUES (1,'Administrador'),(2,'Coordinador'),(3,'Usuario');
/*!40000 ALTER TABLE `tipo de rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipotransporte`
--

DROP TABLE IF EXISTS `tipotransporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipotransporte` (
  `idTipoTransporte` int NOT NULL AUTO_INCREMENT,
  `tipoTransporte` varchar(45) NOT NULL,
  `capacidad` int NOT NULL,
  PRIMARY KEY (`idTipoTransporte`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipotransporte`
--

LOCK TABLES `tipotransporte` WRITE;
/*!40000 ALTER TABLE `tipotransporte` DISABLE KEYS */;
INSERT INTO `tipotransporte` VALUES (1,'Colectivo',60),(2,'Avion',30);
/*!40000 ALTER TABLE `tipotransporte` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-09 21:44:13
