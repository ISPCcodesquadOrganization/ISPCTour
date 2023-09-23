-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ISPCTour` DEFAULT CHARACTER SET utf8 ;
USE `ISPCTour` ;

-- -----------------------------------------------------
-- Table `ISPCTour`.`Personas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`Personas` (
  `idUsuarios` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `nombreUsuario` VARCHAR(45) NOT NULL,
  `Telefono` INT NOT NULL,
  `direccionUsuario` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idUsuarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ISPCTour`.`Hoteles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`Hoteles` (
  `idHoteles` INT NOT NULL AUTO_INCREMENT,
  `nombreHotel` VARCHAR(45) NOT NULL,
  `direccionHotel` VARCHAR(150) NOT NULL,
  `telefono` INT NOT NULL,
  PRIMARY KEY (`idHoteles`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ISPCTour`.`Destino`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`Destino` (
  `idDestino` INT NOT NULL AUTO_INCREMENT,
  `nombreDestino` VARCHAR(45) NOT NULL,
  `Hoteles_idHoteles` INT NOT NULL,
  PRIMARY KEY (`idDestino`, `Hoteles_idHoteles`),
  INDEX `fk_Destino_Hoteles1_idx` (`Hoteles_idHoteles` ASC) VISIBLE,
  CONSTRAINT `fk_Destino_Hoteles1`
    FOREIGN KEY (`Hoteles_idHoteles`)
    REFERENCES `ISPCTour`.`Hoteles` (`idHoteles`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ISPCTour`.`TipoTransporte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`TipoTransporte` (
  `idTipoTransporte` INT NOT NULL AUTO_INCREMENT,
  `tipoTransporte` VARCHAR(45) NOT NULL,
  `capacidad` INT NOT NULL,
  PRIMARY KEY (`idTipoTransporte`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ISPCTour`.`Tipo de rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`Tipo de rol` (
  `idTipo de rol` INT NOT NULL AUTO_INCREMENT,
  `Rol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTipo de rol`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ISPCTour`.`Paquetes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`Paquetes` (
  `idPaquetes` INT NOT NULL AUTO_INCREMENT,
  `fechaInicio` DATE NOT NULL,
  `fechaFin` DATE NOT NULL,
  `Destino_idDestino` INT NOT NULL,
  `TipoTransporte_idTipoTransporte` INT NOT NULL,
  `cantidadViajantes` INT NOT NULL,
  `Tipo de rol_idTipo de rol` INT NOT NULL,
  PRIMARY KEY (`idPaquetes`, `Destino_idDestino`, `TipoTransporte_idTipoTransporte`, `Tipo de rol_idTipo de rol`),
  INDEX `fk_Paquetes_Destino1_idx` (`Destino_idDestino` ASC) VISIBLE,
  INDEX `fk_Paquetes_TipoTransporte1_idx` (`TipoTransporte_idTipoTransporte` ASC) VISIBLE,
  INDEX `fk_Paquetes_Tipo de rol1_idx` (`Tipo de rol_idTipo de rol` ASC) VISIBLE,
  CONSTRAINT `fk_Paquetes_Destino1`
    FOREIGN KEY (`Destino_idDestino`)
    REFERENCES `ISPCTour`.`Destino` (`idDestino`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Paquetes_TipoTransporte1`
    FOREIGN KEY (`TipoTransporte_idTipoTransporte`)
    REFERENCES `ISPCTour`.`TipoTransporte` (`idTipoTransporte`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Paquetes_Tipo de rol1`
    FOREIGN KEY (`Tipo de rol_idTipo de rol`)
    REFERENCES `ISPCTour`.`Tipo de rol` (`idTipo de rol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ISPCTour`.`Personas_has_Tipo de rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`Personas_has_Tipo de rol` (
  `Personas_idUsuarios` INT NOT NULL,
  `Tipo de rol_idTipo de rol` INT NOT NULL,
  PRIMARY KEY (`Personas_idUsuarios`, `Tipo de rol_idTipo de rol`),
  INDEX `fk_Personas_has_Tipo de rol_Tipo de rol1_idx` (`Tipo de rol_idTipo de rol` ASC) VISIBLE,
  INDEX `fk_Personas_has_Tipo de rol_Personas1_idx` (`Personas_idUsuarios` ASC) VISIBLE,
  CONSTRAINT `fk_Personas_has_Tipo de rol_Personas1`
    FOREIGN KEY (`Personas_idUsuarios`)
    REFERENCES `ISPCTour`.`Personas` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personas_has_Tipo de rol_Tipo de rol1`
    FOREIGN KEY (`Tipo de rol_idTipo de rol`)
    REFERENCES `ISPCTour`.`Tipo de rol` (`idTipo de rol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ISPCTour`.`Personas_has_Paquetes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ISPCTour`.`Personas_has_Paquetes` (
  `Personas_idUsuarios` INT NOT NULL,
  `Paquetes_idPaquetes` INT NOT NULL,
  `Paquetes_Destino_idDestino` INT NOT NULL,
  `Paquetes_TipoTransporte_idTipoTransporte` INT NOT NULL,
  PRIMARY KEY (`Personas_idUsuarios`, `Paquetes_idPaquetes`, `Paquetes_Destino_idDestino`, `Paquetes_TipoTransporte_idTipoTransporte`),
  INDEX `fk_Personas_has_Paquetes_Paquetes1_idx` (`Paquetes_idPaquetes` ASC, `Paquetes_Destino_idDestino` ASC, `Paquetes_TipoTransporte_idTipoTransporte` ASC) VISIBLE,
  INDEX `fk_Personas_has_Paquetes_Personas1_idx` (`Personas_idUsuarios` ASC) VISIBLE,
  CONSTRAINT `fk_Personas_has_Paquetes_Personas1`
    FOREIGN KEY (`Personas_idUsuarios`)
    REFERENCES `ISPCTour`.`Personas` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Personas_has_Paquetes_Paquetes1`
    FOREIGN KEY (`Paquetes_idPaquetes` , `Paquetes_Destino_idDestino` , `Paquetes_TipoTransporte_idTipoTransporte`)
    REFERENCES `ISPCTour`.`Paquetes` (`idPaquetes` , `Destino_idDestino` , `TipoTransporte_idTipoTransporte`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
