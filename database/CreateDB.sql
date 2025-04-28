-- 1. Schema
CREATE SCHEMA IF NOT EXISTS WhatToEat
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_general_ci;

USE WhatToEat; 

-- 2. tables
CREATE TABLE `Ingredient` (
  `IngrdID` INT AUTO_INCREMENT PRIMARY KEY,
  `IngrdName` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Option` (
  `OptID` INT AUTO_INCREMENT PRIMARY KEY,
  `MealName` VARCHAR(255) NOT NULL,
  `EatOut` BOOLEAN NOT NULL,
  `CuisineType` VARCHAR(100),
  `Mood` VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Fridge` (
  `IngredID` INT NOT NULL,
  `Qty` INT NOT NULL,
  PRIMARY KEY (`IngredID`),
  CONSTRAINT `fk_fridge_ingredient` FOREIGN KEY (`IngredID`) 
    REFERENCES `Ingredient`(`IngrdID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Recipe` (
  `OptID` INT NOT NULL,
  `IngrdID` INT NOT NULL,
  `Qty` INT NOT NULL,
  `Optional` BOOLEAN NOT NULL,
  PRIMARY KEY (`OptID`, `IngrdID`),
  CONSTRAINT `fk_recipe_option` FOREIGN KEY (`OptID`) 
    REFERENCES `Option`(`OptID`),
  CONSTRAINT `fk_recipe_ingredient` FOREIGN KEY (`IngrdID`) 
    REFERENCES `Ingredient`(`IngrdID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Restaurant` (
  `RstrntID` INT AUTO_INCREMENT PRIMARY KEY,
  `RstrntName` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Menu` (
  `RstrntID` INT NOT NULL,
  `OptID` INT NOT NULL,
  `Price` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`RstrntID`, `OptID`),
  CONSTRAINT `fk_menu_restaurant` FOREIGN KEY (`RstrntID`) 
    REFERENCES `Restaurant`(`RstrntID`),
  CONSTRAINT `fk_menu_option` FOREIGN KEY (`OptID`) 
    REFERENCES `Option`(`OptID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
