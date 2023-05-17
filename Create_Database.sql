# Create database
CREATE DATABASE KDD;
# Use Database
USE KDD;
# Create Tables
CREATE TABLE Customers (
	customerId INT AUTO_INCREMENT NOT NULL,
    companyName VARCHAR(128),
    contactName VARCHAR(32),
    email VARCHAR(48),
    phoneNumber VARCHAR (15),
    socialMedia VARCHAR(64),
    address VARCHAR(128),
    lastOrder DATE,
    lastFinishedOrder DATE,
    status ENUM("Good Standing","On The Fence","Blacklisted"),
    note TEXT,
    PRIMARY KEY (customerId)
);
CREATE TABLE Orders (
	orderId INT AUTO_INCREMENT NOT NULL,
    orderName VARCHAR(64) UNIQUE NOT NULL,
	customer INT NOT NULL,
    note TEXT,
    orderDate DATE NOT NULL,
    plannedDate DATE NOT NULL,
    finalDate DATE,
    price DECIMAL(6,2),
    paymentType VARCHAR(32),
    status ENUM("Production", "Sold", "Cancelled", "Preorder","No Payment","Late"),
    PRIMARY KEY (orderId),
    FOREIGN KEY (customer) REFERENCES Customers(customerId),
    CONSTRAINT planned_after_order CHECK (plannedDate >= orderDate),
    CONSTRAINT final_after_order CHECK (finalDate >= orderDate)
);
CREATE TABLE Items (
	itemId INT AUTO_INCREMENT NOT NULL,
    itemName VARCHAR(64) UNIQUE NOT NULL,
    price DECIMAL(6,2) NOT NULL,
    PRIMARY KEY (itemId)
);
CREATE TABLE Activity (
	activityId INT AUTO_INCREMENT NOT NULL,
    activityName VARCHAR(64) UNIQUE NOT NULL,
    PRIMARY KEY (activityId)
);
CREATE TABLE OrderItems (
	id INT AUTO_INCREMENT NOT NULL,
    orderName VARCHAR(64) NOT NULL,
    itemName VARCHAR(64) NOT NULL,
    quantity DECIMAL(5,3) NOT NULL,
    price DECIMAL(6,2),
    note VARCHAR(64),
	PRIMARY KEY (id),
    FOREIGN KEY (orderName) REFERENCES Orders(orderName),
    FOREIGN KEY (itemName) REFERENCES Items(itemName),
    UNIQUE KEY (orderName, itemName, note)
);
CREATE TABLE Log (
	logId INT AUTO_INCREMENT NOT NULL,
    date DATE GENERATED ALWAYS AS (DATE(startTime)) STORED NOT NULL,
    startTime DATETIME NOT NULL,
    endTime DATETIME NOT NULL,
    duration TIME GENERATED ALWAYS AS (TIMEDIFF(endTime, startTime)) STORED NOT NULL,
    note Text,
    activity VARCHAR(64) NOT NULL,
    orderName VARCHAR(64) NOT NULL,
    PRIMARY KEY (logId),
    FOREIGN KEY (activity) REFERENCES Activity(activityName),
    FOREIGN KEY (orderName) REFERENCES Orders(orderName),
    CONSTRAINT same_day CHECK (DAY(startTime) = DAY(endTime)),
    CONSTRAINT positive_duration CHECK (duration > 0)
);
