# Market Basket Analytics – given a purchasing history of products together,recommend additional product to customers making purchases

## Scenario
A new startup company has been selling their products online with several million sales transactions. They have hired you as a data scientist to design a prototype of a market basket analytics system. The system will look at the products the customer has placed in their online shopping cart and recommend another product.
The company has provided us with a training set of 1 million sales of 2 or more products.
For simplicity for this first prototype, they have:
• Limited their training set to a maximum of 4 products per sales transaction
• Limited individual sales to no more than 1 of each product
• Temporal reasoning should not be considered (time and date of the sale should not be considered)
The company only has 10 products. The products are named P01, P02, …, P10. Some products may be new without any sales yet.
The company has provided us with a test set of 100 online shopping carts, and has asked us to recommend 1 additional product for each of the 100 online shopping carts.
When considering the training set, previous purchases of 4 products should be considered most influential, followed by 3 and then 2.

## Download the training set of 1 million sales transactions
Your Python program should download the training set from the following link:
http://kevincrook.com/utd/market_basket_training.txt
You Python program should load and analyze this training set in order to recommend products for the test set.
The training set has no header record.
The training set has 1 million records. Each record should be considered an historical sales transaction. Each record starts with a line number (starting with 0000001 and ending with 1000000), followed by a comma separated products list. There will be 2 or 3 or 4 products per record.

## Download the test set of 100 online shopping carts
Your Python program should download the test set from the following link:
http://kevincrook.com/utd/market_basket_test.txt
You Python program should load this test set, apply the analytics from the training set, and recommend 1 product for each shopping cart.
The test set has no header record.
The test set has 100 records. Each record should be considered an online shopping cart. Each record starts with a line number (starting with 001 and ending with 100), followed by comma separated products in the shopping cart. There will be 1 or 2 or 3 products per shopping cart.

## Create the recommendations file
You Python program will create a file of recommendations in the local directory called market_basket_recommendations.txt
Do not create a header record for this file.
The file must be a proper text file using utf-8 encoding, with each line (including the last line) properly terminated by a machine independent end of line character.
Each line will be 1 recommendation. The line should start with the line number from the test file. Line numbers should all be 3 digits, with leading zeroes if necessary (starting with 001 and ending with 100). Follow the line number with a comma. Follow the comma with the recommended product. Follow the recommended product with an end of line. No spaces anywhere in the file!
Your Python code must be algorithmic in nature
Your Python code must be algorithmic in nature.
Hardcoding output statements that are not algorithmic in nature is considered cheating and is explicitly listed as an act of academic dishonesty in UTD official regulations, with possible referrals for academic dishonesty.
Individual Assignment
This assignment in an individual assignment. You may consult with other student about general approaches to solving the problem and for asking for help to resolve stack traces, but all coding must be your own work. An electronic comparison for similarities in submissions will be made. Any similarities greater than 70% will be investigated by the instructor, with possible referrals for academic dishonesty.

