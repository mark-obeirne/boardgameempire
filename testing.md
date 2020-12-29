# Testing Details

[Back to readme](https://github.com/mark-obeirne/boardgameempire/blob/master/README.md)

This document includes details of the manual testing process, sites used for code validation and testing, issues faced over the course of this project's completion, and any known outstanding issues.

## Table of Contents
* [Validators and Tools](#validators-and-tools)
* [Manual Testing](#manual-testing)
    * [Devices Used for Testing](#devices-used-for-testing)
    * [Manual Testing Process](#manual-testing-process)


## Validators and Tools
[W3C Markup Validation Service](https://validator.w3.org/)

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

[JSHint](https://jshint.com/)

[ESPrima (JS)](https://esprima.org/demo/validate.html) 

[Pep8 Online](http://pep8online.com/checkresult) 

[Web Accessibility by Level access](https://www.webaccessibility.com/)

[WAVE](https://wave.webaim.org/report#/http://boardgameempire.herokuapp.com/)

## Manual Testing
### Devices Used for Testing
Please note that this project does not support Internet Explorer due to the use of ES6 features and notation. Esports Dictionary was tested on a variety of devices, including:

Dell Laptop
* Google Chrome
* Microsoft Edge
* Mozilla Firefox

Samsung Galaxy S10 Mobile
* Google Chrome
* Firefox

iPhone 8 Mobile
* Google Chrome
* Safari

[Add Mike and Dermot devices]

### Manual Testing Process
This site was tested as a guest customer and as a customer logged into a registered account.

### Navigation Links
1. Click on the site's logo and ensure homepage is loaded
2. Click on dice icon and ensure that random product pages are rendered
3. Click on the user icon
    * If logged out, ensure that menu shows register and login links
    * Click on register and ensure that registration page is loaded
    * Click on login and ensure that sign in page is loaded
    * If logged in, ensure that menu shows my profile and logout links
    * Click on my profile and ensure that profile page loads
    * Click on logout and ensure that customer is brought to page to confirm their desire to logout
4. Click on cart icon
    * If cart is empty, ensure that user is shown that their cart is empty and has a button to bring them to the products page
    * If cart contains items, ensure that user is brought to cart page that shows the items selected
5. If user is logged in, ensure that wishlist icon is visible
    * Click on icon and ensure that user is brought to wishlist page
    * If wishlist is empty, ensure that user is advised that their wishlist is empty and has a button to bring them to products page
6. Click on home link and ensure homepage is loaded
7. Click on all products and ensure that products page is loaded
8. Click on shop by theme and test links in dropdown menu to ensure that products displayed are filtered
9. Click on shop by mechanic and test links in dropdown menu to ensure that products displayed are filtered
10. Click on deals and ensure that all products listed are on sale
11. Click on game of the month and ensure that dedicated GOTM page loads

### Search
1. On mobile, ensure that the search panel unfolds when the magnifying glass is tapped
1. Search without entering a query and ensure user is redirected to products page and shown a message to tell them that they did not enter a query
2. Search for a product and ensure that products page loads with filtered results
3. Search for a publisher or designer and ensure that products page loads with filtered results
4. Search for a product that doesn't exist, and ensure that customer is presented with a message to advise them that there were no matching products and that they can contact the site

### Footer Links
1. Click on About Us and ensure that the correct page loads
2. Click on Returns Policy and ensure that the correct page loads
3. Click on Loyalty Points Program and ensure that the correct page loads
4. Click on Contact Us and ensure that the correct page loads with the contact form
5. Click on Facebook icon and ensure that page opens in new tab
6. Click on Twitter icon and ensure that page opens in new tab
7. Click on Instagram icon and ensure that page opens in new tab

### Contact form
1. Attempt to submit form without all fields filled out and ensure that user is told that the field is required
2. Attempt to submit form without a valid email address supplied and ensure that user is told that this field needs to be corrected
3. Click on send mail button with all fields filled out correctly and ensure that user is redirected to a success page
4. Check Boardgame Empire email address and ensure that message is delivered correctly

### All Products / Search page
1. Click More Details button for a product and ensure correct product detail page is loaded
2. Click Quick Add to Cart button a ensure that page reloads, cart quantity and total increases correctly, and message displays that product is added to cart

### Sort functionality
1. Select Name (A-Z) from dropdown and ensure that products are ordered correctly
2. Select Name (Z-A) from dropdown and ensure that products are ordered correctly
3. Select Price (Low to High) from dropdown and ensure that products are ordered correctly (including sale items)
4. Select Price (High to Low) from dropdown and ensure that products are ordered correctly (including sale items)
5. Select Min Players (Low to High) from dropdown and ensure that products are ordered correctly
6. Select Min Players (High to Low) from dropdown and ensure that products are ordered correctly
7. Select Max Players (Low to High) from dropdown and ensure that products are ordered correctly
8. Select Max Players (High to Low) from dropdown and ensure that products are ordered correctly
9. Select Playtime (Shortest to Longest) from dropdown and ensure that products are ordered correctly
10. Select Playtime (Longest to Shortest) from dropdown and ensure that products are ordered correctly