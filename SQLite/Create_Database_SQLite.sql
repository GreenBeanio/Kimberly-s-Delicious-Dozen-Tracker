# Create database
CREATE DATABASE KDD;
# Use Database
USE KDD;
# Create Tables
CREATE TABLE Customers (
	customerId INTEGER,
    companyName VARCHAR(128),
    contactName VARCHAR(32),
    email VARCHAR(48),
    phoneNumber VARCHAR (15),
    socialMedia VARCHAR(64),
    address VARCHAR(128),
    lastOrder DATE,
    lastFinishedOrder DATE,
    status TEXT,
    note TEXT,
    PRIMARY KEY (customerId),
    CONSTRAINT valid_status CHECK ((status) IN ("Good Standing","On The Fence","Blacklisted"))
);
CREATE TABLE Orders (
	orderId INTEGER,
    orderName VARCHAR(64) UNIQUE NOT NULL,
	customer INT NOT NULL,
    note TEXT,
    orderDate DATE NOT NULL,
    plannedDate DATE NOT NULL,
    finalDate DATE,
    price DECIMAL(6,2),
    paymentType VARCHAR(32),
    status TEXT,
    PRIMARY KEY (orderId),
    FOREIGN KEY (customer) REFERENCES Customers(customerId),
    CONSTRAINT planned_after_order CHECK (plannedDate >= orderDate),
    CONSTRAINT final_after_order CHECK (finalDate >= orderDate),
    CONSTRAINT valid_status CHECK ((status) IN ("Production", "Sold", "Cancelled", "Preorder","No Payment","Late"))
);
CREATE TABLE Items (
	itemId INTEGER,
    itemName VARCHAR(64) UNIQUE NOT NULL,
    price DECIMAL(6,2) NOT NULL,
    PRIMARY KEY (itemId)
);
CREATE TABLE Activity (
	activityId INTEGER,
    activityName VARCHAR(64) UNIQUE NOT NULL,
    PRIMARY KEY (activityId)
);
CREATE TABLE OrderItems (
	id INTEGER,
    orderName VARCHAR(64) NOT NULL,
    itemName VARCHAR(64) NOT NULL,
    quantity DECIMAL(5,3) NOT NULL,
    price DECIMAL(6,2),
    note VARCHAR(64),
	PRIMARY KEY (id),
    FOREIGN KEY (orderName) REFERENCES Orders(orderName),
    FOREIGN KEY (itemName) REFERENCES Items(itemName),
    UNIQUE (orderName, itemName, note)
);
CREATE TABLE Log (
	logId INTEGER,
    date DATE GENERATED ALWAYS AS (DATE(startTime)) STORED NOT NULL,
    startTime DATETIME NOT NULL,
    endTime DATETIME NOT NULL,
    duration TIME GENERATED ALWAYS AS (ROUND((JULIANDAY(endTime) - JULIANDAY(startTime)) * 24 * 60 * 60)) STORED NOT NULL,
    note Text,
    activity VARCHAR(64) NOT NULL,
    orderName VARCHAR(64) NOT NULL,
    PRIMARY KEY (logId),
    FOREIGN KEY (activity) REFERENCES Activity(activityName),
    FOREIGN KEY (orderName) REFERENCES Orders(orderName),
    CONSTRAINT same_day CHECK (DATE(startTime) = DATE(endTime)),
    CONSTRAINT positive_duration CHECK (duration > 0)
);
