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
