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

Desktop PC with 3440*1440 Monitor
* Google Chrome

Samsung Galaxy S10 Mobile
* Google Chrome
* Firefox

iPhone XR Mobile
* Google Chrome
* Safari

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

### Product Details
1. If logged in, click Add to Wishlist / Remove from Wishlist and ensure relevant action is taken
2. If logged out, click on login and register links and ensure appropriate pages are displayed
3. Click on +/- buttons and ensure that quantity field updates accordingly
4. Manually enter a negative value into quantity field and ensure that it resets to 1
5. Manually enter a value higher than the max available and ensure that it resets to the max available
6. Click add to cart button and ensure appropriate quantity and total is added to cart, and message displayed on page refresh to indicate how many items are in user's cart
7. Add the maximum quantity to cart and, when page reloads, attempt to add more to cart. Ensure that page reloads with an error message informing user that they're trying to add too many products to their cart. 
8. Click on details and reviews tab headings
9. If logged in, click Write Review button in reviews tab and ensure that correct page loads

### Wishlist
1. Add multiple products to wishlist
2. Navigate to wishlist page
3. Click Details button and ensure relevant page loads
4. Click Remove From Wishlist and ensure page refreshes with product removed
5. Click Delete Wishlist button and ensure modal pops up to confirm deletion
6. Cancel request by clicking x in top right of modal
7. Confirm request by clicking delete wishlist button and ensure that page reloads with a blank wishlist

### Profile
1. Add/change details in user details section and click Update Information
    * Page should reload and save details regardless of what fields were filled out as they are optional
2. If there are items in wishlist, click Manage Wishlist button and ensure correct page loads
3. If customer has completed orders, click on order number and ensure relevant page appears with correct order details

### Cart
1. Click on +/- buttons and ensure that quantity field updates accordingly
2. Manually enter a negative value into quantity field and ensure that it resets to 1
3. Manually enter a value higher than the max available and ensure that it resets to the max available
4. Adjust quantity and click Update Quantity link and ensure page refreshes, updates cart quantity and displays a success message
5. Click Remove Item and ensure page refreshes with product removed
6. Click Proceed to Checkout button and ensure Checkout page displays

### Checkout
#### Unregistered Users
1. Ensure that login or register text is displayed beneath pay securely button to tell user about loyalty points and links to correct pages

#### Registered Users
1. If user has filled out profile details, ensure that relevant fields are prefilled
2. Click up and down arrow next to use points field and ensure that user can't get past min or max values
3. Manually enter negative value and ensure points value gets reset to 0
4. Manually enter more points than currently available and ensure that field gets reset to max valid value (i.e. divisible by 50)
5. Manually enter a number that is not divisible by 50 and ensure that field updates to a value that is divisible by 50
6. Ensure that grand total value in Loyalty Points and Charges section and beneath pay securely button updates to reflect points used (with every 50 points worth €0.10)

#### Common testing
1. Attempt to checkout without filling in fields and ensure that validation kicks in
2. Uncheck billing details same as delivery details box and ensure billing details section appears with blank fields
3. Check box again and ensure billing details section is hidden
4. With checkbox ticked, checkout and ensure that billing and delivery details match in order summary
5. Enter an invalid card number and ensure error message appears to prompt user
6. Enter an expiry date in the past and ensure error message is shown
7. Enter too short a CCV and ensure error message is displayed
8. Click Back to Cart button and ensure cart page is displayed
9. Click Pay Securely and check that spinner is shown and, once order is processed, that customer is redirected to order summary screen
10. Uncheck billing details same as delivery details box and enter different details. Upon checkout, ensure that these details are saved correctly.

### Review
1. Click on Write Review button in product details tab and ensure that page loads with form rendered
2. Attempt to submit review without filling out all fields and ensure that field required is highlighted
3. Fill out form and submit review to check that success message is displayed and user is redirected to product page
4. Attempt to write another review for the same product and ensure that product detail page loads with an error message

## Issues Encountered and Resolutions
### iOS Dropdown issues
Materialize's dropdown menus have caused some issues when navigating the site on iOS devices. The sort menu and navigation menus would select the wrong option, resulting in products not appearing as the user had selected or the incorrect theme or mechanic being selected.

To rectify this, the browser-default class is applied to select dropdown menus. In addition, closeOnClick was set to false within the Materialize initialisation options, as [recommended by cwar082](https://stackoverflow.com/questions/61985187/materialize-css-side-nav-dropdown-wrong-links-on-ios-safari).

### Sorting By Price
Initially, both the regular price and sale price fields were filled out for products. However, when sorting by price, only the product's regular price was taken into account. 

The ordering of the sale price and regular price fields were subsequently reordered so that Coalesce could be used to sort by price (and take sale price into account when sorting), as the null fields (i.e. sale price if product is not on sale) are ignored. This was an approach that was [suggested by PatrikAkerstrand](https://stackoverflow.com/questions/8120953/order-by-with-columns-that-are-sometimes-empty) with tweaking required to ensure it fit the needs of the site.

While this approach worked for sorting price from lowest to highest and ensured that sale and regularly priced products intertwined, sorting from highest to lowest required an additional step. An if statement was written to check if sortkey is Coalesce("sale_price", "price") and direction is descending, and the products queryset is reversed if so.

### Materialize Tabs
Product details were originally displayed using a card format on mobile and a stacked card layout on larger devices. However, this resulted in issues with the details and reviews tab. 

In the end, a custom layout using divs was designed to display product images above its details on mobile and alongside details on larger devices. 

### Checkout - Gift Purchase
The checkout page features a checkbox that allows users to specify that the product is a gift. However, the value of the checkbox was being posted to the view as "on" rather than "True", so this had to be manually converted. In addition, gift_purchase had to be included in the form's fields in forms.py as it was ommitted originally.

### Billing Details Same As Delivery Details
Custom JavaScript was written to handle autofilling the user's billing details if the user indicated that they matched delivery details. As the function targeted all input fields, it overwrote the different billing information when the user tried to fill these fields out.

In order to fix this, the OrderForm class was updated to specify which fields related to delivery fields. This list was then used to check fields and apply a class of "delivery-input-field" to those that applied, which were subsequently targetted by the function.

### Loyalty Points
The first attempt at giving the customer the ability to use loyalty points earned as a discount against a purchase checked the value of the grand total and updated the value as points were used. However, it was noticed that this resulted in a cumulative effect where the discount would jump from €0.10 to €0.30 and keep this trend up as more points were applied.

A cart total was added beneath the order summary to both give the user more information and to act as a base value, which ensured that a global variable did not have to be set and used to check if the points being used were increasing or decreasing, as suggested [here](https://stackoverflow.com/questions/49971457/input-type-number-how-to-detect-if-value-was-incremented-or-decremented).

The loyalty points functionality also had to be updated to handle manual user input. 50 loyalty points are worth €0.10, so for convenience, the input selector is set to increment by 50. We had to ensure that users could not set negative loyalty points, more loyalty points than they currently have, and that the value entered is divisible by 50. 

## Any known issues
### Mobile sidenav menu
The 'Shop by Theme' and 'Shop by Mechanic' menus show and hide by tapping the menu header. However, it requires a slightly longer press to close rather than a simple tap as you would to open. Holding the menu option for too long results in a user menu opening to ask if the user would like to open in a new tab. This is something that we would like to explore further, as the slightly longer press isn't the most intuitive.

### Crispy forms
On some pages (listed below), Crispy Forms has not rendered the form correctly and ommitted a closing div for a row. This resulted in the footer being displayed inside the container. A closing div has been manually added to the affected pages and noted in a comment. These pages have passed validation, but the extra div has been highlighted by Gitpod. 

#### Affected Pages:
* contact.html
