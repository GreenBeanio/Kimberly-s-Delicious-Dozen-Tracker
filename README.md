# Kimberly's Delicious Dozen Tracker

___
___

## What Does It Do?

___

This program is used for tracking the sales and activity log for Kimberly's Delicious Dozen.

It consists of the following sections

___

### Log

This section is used to track the work done. Each entry consists of the following elements:

- Date:
  - This is the date of the activity.
- Start:
  - This is the start time of the activity.
- End:
  - This is the end time of the activity.
- Activity:
  - This is one of the activities from the activity section.
- Order:
  - This is one of the orders from the order section.
- Note:
  - This is an optional note about the activity.

___

### Activities

This section is used to record the activities worked on. It only consists of one element:

- Activity:
  - The name of the activity worked on.

___

### Items

This section is used to record the items produced and sold. It consists of two elements:

- Item Name:
  - This is the name of the item.
- Item Price:
  - This is the suggested price of the item.

___

### Customers

This section is used to track each customer. It consists of the following elements:

- Company Name:
  - This is the name of the company the contact works at.
- Contact Name:
  - This is the name of the contact.
- Email:
  - This is the email of the contact.
- Phone Number:
  - This is the phone number of the contact.
- Social Media:
  - This is the social media of the contact.
- Address:
  - This is the address of the contact.
- Status:
  - This is the status of the contact.
- Note:
  - This is an optional note about the contact.

___

### Orders

This section is used to track orders. Each entry consists of the following elements:

- Order Name:
  - This is the name of the order.
- Customer:
  - This is used to record the customer of the order. It is an id value that is generated for each customer.
- Order Date:
  - This is the date that the order was placed on.
- Planned Date:
  - This is the date that the order is planned to be sold on.
- Final Date:
  - This is the date that the order was finished and money was collected.
- Price:
  - This is the price the order was sold at.
    - The price can be manually specified or calculated later form the items in the order.
- Status:
  - This is the current status of the order.
- Payment Type:
  - This is how the order was paid for.
- Note:
  - This is an optional note about the order.

___

### Order Items

This section is used to track the individual items in an order. Each entry consists of the following elements:

- Order Name:
  - This is the name of the order.
- Item:
  - This is the specific item in the order.
- Quantity:
  - This is the quantity of the item.
- Price:
  - This is the price of the item.
    - This can be manually specified or calculated from the quantity and the item suggested price.
- Note:
  - This is a note about the item.

___
___

## Reason For Creation

___

This program was created to hopefully organize my Mother's tracking of her cookie business.

I doubt she will even use this as she claims to be, and is, very computer illiterate. However, I can't sit idle by as she creates the most unorganized mess of a spreadsheet that ahs ever existed.
___
___

## Running The Python Script

___

1. Move all the entire contents from inside either the MySQL or the SQLite folder into the root directory.

    - If you're using MySQL you will need to setup a MYSQL server and run the SQL script to set up the database.
      - You will also need to rename "blank_config.json" to "config.json" and put in your MySQL information.
    - If you're using SQLite no extra set up is required.
2. Run the following code:

___

### Windows

- Initial Run
  - cd /your/folder
  - python3 -m venv env
  - call env/Scripts/activate.bat
    - If using powershell instead of cmd do
      - ./env/Scripts/Activate.ps1
  - python3 -m pip install -r requirements.txt
  - python3 KDD.py
- Running After
  - cd /your/folder
  - call env/Scripts/activate.bat && python3 KDD.py
    - If using powershell instead of cmd do
      - ./env/Scripts/Activate.ps1 && python3 KDD.py
- Running Without Terminal Staying Around
  - Change the file type from py to pyw
  - You should just be able to click the file to launch it
  - May need to also change python3 to just python if it doesn't work after the change
    - In the first line of the code change python3 to python

___

### Linux

- Initial Run
  - cd /your/folder
  - python3 -m venv env
  - source env/bin/activate
  - python3 -m pip install -r requirements.txt
  - python3 KDD.py
- Running After
  - cd /your/folder
  - source env/bin/activate && python3 KDD.py
- Running Without Terminal Staying Around
  - Run the file with nohup
  - May have to set executable if it's not already
    - chmod +x KDD.py

___
___
