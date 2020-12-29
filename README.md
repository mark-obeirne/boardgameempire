# Boardgame Empire
## Code Institute - Milestone 4 Project
### Live Heroku Link: https://boardgameempire.herokuapp.com/

![Boardgame Empire](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/readme_images/responsive-site-img.png)

## Table of Contents
* [Summary](#summary)
* [Background](#background)
* [Aim of the Site](#aim-of-the-site)
* [Scope](#scope)
    * [User Stories](#user-stories)
* [Site Features](#site-features)
* [Future Features](#future-features)
* [Information Architecture](#information-architecture)
* [Skeleton](#skeleton)
    * [Mobile Wireframes](#mobile-wireframes)
    * [Tablet Wireframes](#tablet-wireframes)
    * [Desktop Wireframes](#desktop-wireframes)
    * [Changes to Wireframes](#changes-to-wireframes)
* [Structure](#structure)
* [Surface](#surface)
    * [Fonts](#fonts)
    * [Colours](#colours)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Meeting User Expectations](#meeting-user-expectations)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Summary
Boardgame Empire is an online boardgame retailer, which specialises in helping customers discover new games easily.

## Background
The boardgame industry is more than just Monopoly, Cluedo, Scrabble, and The Game of Life; games that many people grew up with and, in some cases, ended up hating! 

In 2017, it was estimated that the global market value of boardgames, otherwise known as tabletop games, was $7.2 billion. That is forecast to grow to [approximately $12 billion by 2023](https://www.statista.com/statistics/829285/global-board-games-market-value/). 

That figure is made up of more than sales of old favourites. In 2016, more than 3,900 new boardgames were released! Boardgames are also becoming more diverse, accessible, and inclusive than ever. There is a growing focus on family-friendly and child-friendly games, rulebooks no longer default to male pronouns, and more YouTube channels have popped up to offer rule explanations and video playthoughs. There has been a growth in boardgame conventions over the years, drawing thousands of visitors to exhibition halls around the world who take in new games, play with friends and strangers alike, and hear from those behind the games themselves.

In recent years, boardgame designers have turned to Kickstarter to help get their games produced. Players have embraced this business decision with pledges growing massively in recent years, from $84.6 million in 2015 to $233.8 million this year. Of this substantial figure, almost $13 million was raised by Frosthaven alone with a further $8.8 million being pledged towards the development of a modular gaming table.

## Aim of the Site
Discovering boardgames, and what one might enjoy, can be a tricky endeavour. It often requires cross-site research and time spent digging through rule books, reviews, and forums...

The aim of Boardgame Empire is to make this process a little more streamlined and enjoyable. On each product page, customers are presented with YouTube videos, which show the game in action. One will typically be a playthrough among a group so customers get an impression of how it plays and how enjoyable it is. The other acts as an explanation of the game, its setup, rules, and mechanics, just in case they're going to shoulder the responsibility of explaining it to their group. 

While customers are presented with ways to find specific products - searching, browsing by theme or mechanics of interest, or browsing generally - we make an effort to help customers find games that may be of interest. Each month, Boardgame Empire highlights a game of the month, occasionally features certain publishers or designers, showcases the most popular game on the site, and offers a navigation option to check out a random game. Rather than being a chore, we want to make the experience one of joy and discovery. 

## Scope
Boardgame Empire's primary target market is boardgame enthusiasts. We hope to encourage frequent purchases by offering a loyalty point programme, while the ability to leave reviews may encourage customers to share knowledge and opinions with other customers. However, Boardgame Empire aims to make boardgames more accessible to those looking for gift ideas, or who are open to the idea of playing something fun with a group of friends who wouldn't describe themselves as boardgamers.

### User Stories
#### Customers
* As a newcomer to boardgames, I would like to be able to have easy access to relevant information about a product so that I can easily determine if it is something that would be of interest to me.

* As someone with a growing collection of boardgames, I would like to be able to discover new boardgames without having to do research across a number of websites, so that I can grow my collection further.

* As a boardgame enthusiast, I would like to be able to add boardgames to a wishlist, so that I can plan my purchases and keep an eye out for bargains.

#### Site Owners
* As a business,  we would like to offer a loyalty scheme so that people are more likely to return to make a purchase in the future.

* As the site owner, we would like to make it easy for customers to find a product that interests them, regardless of their familiarity.

* As a business, we would like to showcase boardgames in their best light - being played - so that we can share the joy of tabletop gaming with customers. 

## Site Features
### Slider
Boardgame Empire's homepage features a slider, which can be used to highlight topical games, publishers and designers, ongoing sales, the game of the month, and more. This feature makes it possible to suggest a starting point for a customer who may not be sure what they are looking for.

### Random Game
To aid in a customer's journey of discovery, Boardgame Empire features a random boardgame button as part of the top navbar, which is available at all times. This brings the user to the details page of a random product, which showcases game details, an outline of what the game is, and the YouTube videos to show the game being played and explained.

### Search
For customers who have something particular in mind, Boardgame Empire offers a search mechanic. This can be used to search for a boardgame, a designer or a publisher. 

### Wishlists
If a customer stumbles upon a product of interest, it is possible to add it to their wishlist, provided they are logged into their account. This wishlist feature also highlights if a product is on sale, so a user can add a product and wait until the price is right to purchase it. This wishlist can be managed on a product by product basis or the customer can delete the wishlist in its entirity.  

### Loyalty Points Programme
Customers have a variety of online and brick-and-mortar stores to choose from when purchasing boardgames. In order to encourage customers to return in the future for further purchases, Boardgame Empire offers a Loyalty Point programme. Customers earn points on their purchase, which they can use at checkout on a future purchase for a discount. 

### Order History
Provided a user has made a purchase from a Boardgame Empire account, they will be able to view the order's details and click into it for more information from their profile page.

### Reviews
Once logged in, a user can submit a review of a product and rate it on a scale of 1-5. The most recent reviews are displayed beneath a product on its details page with further reviews available to read on a dedicated page for that product. It has been decided not to limit this to customers who have ordered the product via the store initially in order to build up reviews and ratings, which other customers could find beneficial. 

### Contact Page
The Contact Us page contains a form, which will send an email to the Boardgame Empire email address with the user's query and provided details. Once the email is sent, the user is directed to a success page and can navigate to the store from there.

## Future Features
### Sort By Ratings
Boardgame Empire allows customers to review and rate boardgames. However, there are not enough ratings at this point in time for the ability to sort by rating to be particularly useful. It is planned to enable this functionality in the future, adding another sort option to a fairly extensive list that currently includes: by min or max number of players, by playtime, by age suitability, by price, and alphabetically.  

### Rate Reviews
As reviews are user-generated, they may differ drastically in terms of how helpful they are to others. There is currently no functionality to highlight reviews that a customer found helpful, and this is something that we aim to implement in the future. 

### Multiple Wishlists
For the most part, one wishlist should be sufficient for users. However, there may be cases in which customers would like to organise products into various wishlists. For example, if a customer would like a wishlist for present ideas or unique wishlists for different playgroups, we would like to provide them with this ability.

### Customer Service Chatbot
Customers are invited to email if they have any queries or issues with their orders. In instances where customers have queries that could be dealt with quickly and in real-time, we would like to investigate the practicality of a chatbot. This, we believe, could improve the user experience and save them time as they would not have to partake in a back-and-forth email chain. 

## Information Architecture
### Database Choice

### Data Storage Types

### Database Schema


## Skeleton
### Mobile Wireframes
 
   * [Homepage](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/homepage-mobile.png)
   * [All Products Page / Deals](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/products-mobile.png) 
   * [Product Details Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/product-detail-mobile.png)
   * [All Reviews Page]()
   * [Full Review Page]()
   * [Write Review Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/write-review-mobile.png)
   * [Wishlist Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/wishlist-mobile.png)
   * [User Profile Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/profile-page-mobile.png)
   * [Cart Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/cart-mobile.png)
   * [Checkout Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/checkout-mobile.png)
   * [Checkout Success Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/checkout-success-mobile.png)
   * [About Us Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/about-us-mobile.png)
   * [Returns Policy](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/returns-policy-mobile.png)
   * [Loyalty Points Programme](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/loyalty-points-mobile.png)
   * [Contact Us Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/contact-mobile.png)

### Tablet Wireframes
   * [Homepage](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/homepage-tablet.png)
   * [All Products Page / Deals](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/products-tablet.png) 
   * [Product Details Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/product-detail-tablet.png)
   * [All Reviews Page]()
   * [Full Review Page]()
   * [Write Review Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/write-review-tablet.png)
   * [Wishlist Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/wishlist-tablet.png)
   * [User Profile Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/profile-page-tablet.png)
   * [Cart Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/cart-tablet.png)
   * [Checkout Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/checkout-tablet.png)
   * [Checkout Success Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/checkout-success-tablet.png)
   * [About Us Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/about-us-tablet.png)
   * [Returns Policy](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/returns-policy-tablet.png)
   * [Loyalty Points Programme](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/loyalty-points-tablet.png)
   * [Contact Us Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/contact-tablet.png)

### Desktop Wireframes
   * [Homepage](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/homepage-desktop.png)
   * [All Products Page / Deals](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/products-desktop.png) 
   * [Product Details Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/product-detail-desktop.png)
   * [All Reviews Page]()
   * [Full Review Page]()
   * [Write Review Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/write-review-desktop.png)
   * [Wishlist Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/wishlist-desktop.png)
   * [User Profile Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/profile-page-desktop.png)
   * [Cart Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/cart-desktop.png)
   * [Checkout Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/checkout-desktop.png)
   * [Checkout Success Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/checkout-success-desktop.png)
   * [About Us Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/about-us-desktop.png)
   * [Returns Policy](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/returns-policy-desktop.png)
   * [Loyalty Points Programme](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/loyalty-points-desktop.png)
   * [Contact Us Page](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/wireframes/contact-desktop.png)

### Changes from Wireframes
#### Homepage
The featured best seller card includes the product's description. The wishlist functionality has been moved exclusively within the product detail pages.

#### Product Listings
Rather than displaying box images beside a product's details, it was decided to show them at the top of the product card for flow and for better use of space. 

#### Product Detail
While the product's boxart image is displayed to the side of the product's details on tablets and desktops, this is no longer a slider that cycles through media. The associated YouTube videos are instead displayed beneath the action buttons to give user's added context. These videos sit within a responsive Materialize video container. The flow on desktop works much better in practice than initially laid out.

#### Wishlist
Rather than displaying product details and cart functionality, the wishlist page is now used solely to display the product's image, name, and current price. This enables users to keep an eye on a product's price without having too much information on show, while providing them with an easy way to click through to a product's page for further action.

#### Cart (Mobile)
The mobile page remove's the product's image to use the available space better. The product's name, quantity adjustment buttons, and the item's subtotal are then displayed in a single row.  

## Structure
The navbar is broken into two rows. On the top row, users have access to a search bar (which unfurls on mobile), a button to be brought to the details of a random game, a user menu (which contains links to the user's profile and sign out functionality if logged in or the registration and sign in links if not), a link to the customer's wishlist, and a link to the customer's cart.

The bottom row meanwhile contains the brand's logo, which brings the user back to the homepage, a link to view all products, two dropdown menus that display the themes and mechanics associated with boardgames featured on the site, a link to see current deals, and a link to see the current game of the month.


## Surface
### Fonts
Open Sans is used across the site as the most prominent font. It was chosen as it is very legible, even in paragraphs with lots of text, and because it has been optimised for use across web and mobile.

Meanwhile, Roboto was chosen for headings with the small caps font variant applied. This font, it was felt, looked good whether the bold or regular variant was used. While it helps the text stand out, it doesn't feel out of place, and so acts naturally as a heading of any size.

### Colours
![Boardgame Empire Colours](https://raw.githubusercontent.com/mark-obeirne/boardgameempire/master/static/readme_images/colours-used-coolors.png)

We wanted to emulate the tabletop feel on the site itself too. A dark brown (#392417) is used to tie in with the colour of wood. It also has good legibility against the chosen background colours (or inverted with white text on brown), and is a little more interesting than black on white.

To make it more obvious that an element can be interacted with, the buttons with this background colour lighten to #5D3B26, which is 10% lighter according to [colorbook.io](colorbook.io).

The green (#CDE6D0) chosen as a backdrop is a similar shade to that found on a Monopoly board. It enables the containers and product images to stand out, while ensuring that there isn't too much white space which people may feel could be utilised better. We felt it struck a nice balance. 

Containers have a sheer white shade (#FFFFFF) to them to ensure that the product media and text content stand out. 

Other colours are used more sparingly to add emphasis or to break up elements. A red (#FF0000), orange (#FFA500), and green (#228B22) span indicates the availability of a product. This shade of red is also used to indicate that a product is on sale.


## Technologies Used
### Languages 
HTML & CSS were used for the basic site structure and styling 

JavaScript was used to further enhance the user's experience. For example, it is used to update the customer's grand total in real time if they use loyalty points to discount their purchase, to display a spinner if a page is taking a while to load, and to display modals if a user needs to log in to access a function (such as their wishlist).

Python was used to handle data procured from the database.

### Frameworks
Django was used to develop the project, taking advantage of certain in-built elements such as authentication as well as its templating language to display variables and work with data.

Materialize was used to create interactive and visual elements such as the home page's slider, dropdown elements, and the site's general responsive design.

### Tools
PIP was used to install and manage software packages.

Git was used to track changes in code during development.

GitHub was used to host the project’s repository.

Trello was used to track work that needed to be done from the outset, which enabled a plan of action to be put in place and helped keep on top of any issues or bugs that occurred.

Balsamiq was used to create the wireframes that the site's layout is based upon.

Coolors was used to help find a suitable palette for the site and to check if colours might work together.

Google Fonts was used to find the fonts that would be suitable as headings and general text content.

Font Awesome was used to find icons for use in buttons across the site.

Gimp 2 was used for image manipulation and to create the brand logo.

Birme was used to resize boxart images so that there was consistency across the site.

TinyPNG was used to compress and optimise image files.

Favicon Converter was used to create the favicon based on the brand logo.

HTML Formatter was used to format HTML files and ensure consistency in spacing.

FreeFormatter CSS Beautifier was used to format the CSS stylesheet.

FreeFormatter JS Beautifier was used to format js files from across the project.

## Testing

## Meeting User Expectations

## Deployment


## Credits
### Media
[Spinner - Dice](https://www.animatedimages.org/data/media/710/animated-dice-image-0079.gif)

[About Us - Blood Rage image](https://pixabay.com/photos/blood-rage-tabletop-games-4311101/)

[About Us - Carcassone image](https://pixabay.com/illustrations/board-game-board-game-gaming-2237460/)

[About Us - Settlers of Catan image](https://www.catan.com/files/styles/lightboxy/public/gallery/dye_catan_150618_0650.jpg?itok=9RJRSUjI)

[Loyalty Points - Coin stacks](https://pixabay.com/photos/money-money-tower-coins-euro-2180330/)

[Returns Policy - Boxes](https://pixabay.com/photos/beige-box-brown-cardboard-carton-16875/)

[Slider - Browing games](https://azure.wgp-cdn.co.uk/app-table-top-gaming/posts/DSC_4587-38154.jpg)

[Slider - Sales](https://pixabay.com/illustrations/christmas-christmas-tree-backdrop-2892235/)

[Slider - Fireworks](https://cdn.pixabay.com/photo/2015/04/18/07/41/fireworks-728413_960_720.jpg)

[Logo - Meeple](https://icon-icons.com/icon/meeple/38522)

[Logo - King piece](https://pixabay.com/vectors/chess-king-meeple-black-white-36306/)

[Catan box](https://www.catan.com/files/styles/lightboxy/public/packshots/catan.png?itok=rXKqsgv9)

[Carcassone box](https://images.zmangames.com/filer_public/1c/2a/1c2a5c1e-ddeb-4ab5-abf0-3bef57388498/zm7810_box_front_520px.png)

[Pandemic box](https://images.zmangames.com/filer_public/98/0c/980c04bc-781a-4de7-8034-6ff6f054d7b7/zm7101_box_front_520px.png)

[Dominion box](https://shop.jjcards.com/assets/images/board%20games/rio%20grande/dominion%202nd%20ed%20box.jpg)

[7 Wonders box](https://i5.walmartimages.com/asr/b5434e0e-4a0e-4773-be7b-28ab2950deda_1.506a961d88efb5ed3c0cbc9286719969.jpeg)

[Agricola box](https://www.sheknows.com/wp-content/uploads/2018/08/81wAmibxHxL._SL1500__p7qbt3.jpeg)

[Ticket to Ride box](https://cogsthebrainshop.ie/wp-content/uploads/2013/11/TICKET-TO-RIDE-1.jpg)

[Puerto Rico box](https://i5.walmartimages.com/asr/1d57f65d-549f-47bd-8b27-312305effafb.064321e76fc1716c923d10af3d181b1f.jpeg)

[Small World box](https://i5.walmartimages.com/asr/c449c6ec-cae1-4b3c-8010-f74390d56abd_1.9d0a7645e3cd8d776b8a1396f03b524b.jpeg)

[Power Grid box](https://www.amazon.co.uk/Rio-Grande-Games-RGG559-Power/dp/B07HM7WZT9/ref=asc_df_B07HM7WZT9/?tag=googshopuk-21&linkCode=df0&hvadid=310873739176&hvpos=&hvnetw=g&hvrand=15417965510703906747&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007850&hvtargid=pla-598926208048&psc=1)

[Citadels box](https://images.zmangames.com/filer_public/47/d3/47d3d75c-4520-4e17-963f-a5b31c908e30/wr02_box-front.png)

[King of Tokyo box](https://crystal-cdn3.crystalcommerce.com/photos/685779/KingOfTokyo_3Dbox.jpg)

[Love Letter box](https://cdn.shopify.com/s/files/1/1402/8033/products/llc_boxclam_520px_480x480.jpg?v=1581486768)

[Ticket to Ride Europe box](https://www.thetoyshop.com/medias/537034-Primary-1200Wx1200H?context=bWFzdGVyfGltYWdlc3wxODYyNTEwfGltYWdlL3BuZ3xpbWFnZXMvaDczL2hkNC85MTYzNDQ2MjIyODc4LnBuZ3wxN2MyZmE1ODQzY2VjNjJjMGRkZTliYjAzNGU0MmM3NzViNDRkOTZjODdjOTQ0M2E2MTk1MTgyYzJiMDUwZGRi)

[Race for the Galaxy box](https://images-na.ssl-images-amazon.com/images/I/91yTKe2ES4L._AC_SL1500_.jpg)

[Dixit box](https://cdn.shopify.com/s/files/1/0405/0381/products/916_54d9f2479d31a1.88716786_Dixit_20board_20game_large_3dc6c23d-cea3-4503-9cb3-a2f4fab33c9c_grande.jpg?v=1605264406)

[Stone Age box](https://images.zmangames.com/filer_public/a1/ae/a1ae3e5c-0948-4257-a2f0-c10717613ad6/zm7260_box_front_520px.png)

[Arkham Horror box](https://www.magicmadhouse.co.uk/images/arkham-horror-third-edition-p293489-288714_medium.jpg)

[Codenames box](https://target.scene7.com/is/image/Target/GUEST_b8f62a26-e254-4cc9-bfd7-3c49dbc61561?wid=488&hei=488&fmt=pjpeg)

[Splendor box](https://images-na.ssl-images-amazon.com/images/I/613n3Gky43L._AC_SX425_.jpg)

[Lords of Waterdeep box](https://c1-ebgames.eb-cdn.com.au/merchandising/images/packshots/c0630425331148809ec22cdc0de03c7f_Large.jpg)

[Munchkin box](https://cogsthebrainshop.ie/wp-content/uploads/2017/10/munchkin-card-game.jpg)

[Bohanza box](https://images-na.ssl-images-amazon.com/images/I/81zdBXeGWlL._AC_SL1500_.jpg)

[Forbidden Island box](https://www.gamesworld.com.au/wp-content/uploads/2015/10/FORBIDDEN-ISLAND-1.jpg)

[Lost Cities box](https://www.kosmosgames.co.uk/wp-content/uploads/2018/04/691821_LC_Card_Game_3DBox.jpg)

[The Resistance box](https://cdn.shopify.com/s/files/1/0405/0381/products/3604_560ac185ae59b3.01320100_The_20Resistance_20board_20game_large_9ab15d8c-496e-4b67-922e-6b705422d147_grande.png?v=1605264373)

[Battlestar Galactica box](https://images-na.ssl-images-amazon.com/images/I/71Le6zwW48L._AC_SX425_.jpg)

[Hanabi box](https://i2.wp.com/www.enigmaticevents.com/wp-content/uploads/2018/02/HanabiSdJ_Bild01_Cover3D_sRGB-600x600.jpg?fit=600%2C600&ssl=1)

[Terra Mystica box](https://images.zmangames.com/filer_public/7f/a2/7fa211a0-f16b-4608-acb6-775cc03f0869/zm7244_box_front_520px.png)

[Dominion Intrigue box](https://cdn11.bigcommerce.com/s-9im8f1/images/stencil/1280x1280/products/5632/7048/91UusJQyiML._AC_SL1500___03727.1590441095.jpg?c=2)

[Betrayal at the House on the Hill box](https://www.board-game.co.uk/wp-content/uploads/2019/11/ZBG-HAS266330000_FRONT.jpg)

[Dead of Winter box](https://images-cdn.fantasyflightgames.com/filer_public/5f/6d/5f6db8c3-4f25-45ec-86af-849fc3af723b/ph1000_box_right.png)

[Alhambra box](https://images-na.ssl-images-amazon.com/images/I/814OJBe4jUL._SL1290_.jpg)

[Coup box](https://www.board-game.co.uk/wp-content/uploads/2019/11/ZBG-IBCCOU1_FRONT-1.jpg)

[Galaxy Trucker box](https://cf.geekdo-images.com/gLFt1Kif5Cfag505_COYYw__opengraph/img/_RmgylCHR4AMj7WPBvdXP_tKPzc=/fit-in/1200x630/filters:strip_icc()/pic3926631.jpg)

[Eclipse box](https://cdn.shopify.com/s/files/1/0405/0381/products/553_54da436c225c76.48995041_Eclipse_20board_20game_large_5357113f-c268-4862-9b04-f264c2338edf_1024x1024.jpg?v=1575931863)

[Shadows Over Camelot box](https://m.media-amazon.com/images/I/61CMyHW1O7L._AC_.jpg)

[Robo Rally box](https://images-na.ssl-images-amazon.com/images/I/71gQvFMP%2BLL._AC_SX466_.jpg)

[BANG! box](https://www.google.com/url?sa=i&url=https%3A%2F%2Fboardgamemanuals.fandom.com%2Fwiki%2FBANG!&psig=AOvVaw149i6l7Q0_5OpaYL8L8Zan&ust=1608583203994000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCOj6yeK13e0CFQAAAAAdAAAAABAD)

[Hive box](https://www.boardgamebarrister.com/wp-content/uploads/2015/12/HiveBox.png)

[La Havre box](https://i.pinimg.com/originals/c4/f8/39/c4f839222d62013afe6f37eb10e6101b.jpg)

[Cosmic Encounter box](https://images-cdn.fantasyflightgames.com/filer_public/b8/f5/b8f5cf47-226f-43f4-a8d5-40c09260f1d2/ce01_42ae_box_left.png)

[Star Realms box](https://opinionatedgamers.files.wordpress.com/2015/05/starrealms.png)

[Patchwork box](https://m.media-amazon.com/images/I/91SHanVV2ZL._AC_SS350_.jpg)



## Acknowledgements
I would like to thank my mentor, Antonio Rodriguez for their support and advice over the past year as part of the Code Institute course and for their help with this project.

I would also like to thank my fellow Code Institute students who provided support, advice, and a second opinion on Slack. I would like to thank Igor of Code Institute for their help with one issue faced during deployment.

Finally, I would like to thank all those who took the time to test this website and provide feedback and suggestions.

## Disclaimer
This project is for educational purposes only. 


