<img src="/media/readme_images/mockup.png">

This project was my final Milestone project for [Code Institute](https://codeinstitute.net/) [Full Stack Diploma in Software Development](https://codeinstitute.net/full-stack-software-development-diploma/) - Full Stack Frameworks with Django Module.

## [**Table of Contents**](#table-of-contents)

- [UX](#ux)
    - [Overview](#overview)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Design Process](#design-process)
        * [Development Process](#development-process)
        * [Design Decisions](#design-decisions)
        * [Colour Scheme](#colour-scheme)
        * [Images](#images)
        * [Typography](#typography)
        * [Wireframes](#wireframes)

- [Database Model](#database-model)

- [Features](#features)
    - [CRUD Functionality](#crud-functionality)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)

- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Project Management](#project-management)
    - [Tools](#tools)
    - [Resources](#resources)

- [Testing](#testing)

- [Deployment](#deployment)
    - [Locally](#locally)
    - [AWS](#aws)
    - [To Heroku](#to-heroku)

- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media) 
    - [Acknowledgements](#acknowledgements)

- [Disclaimer](#disclaimer)

---

## **UX** 
### **Overview**
An e-commerce site selling women's apparel. Users are able to browse and shop anonymously or register for an account to unlock additional features such as saving default delivery info, order history and save favourite products. 

The live site can be viewed [here](https://the-velvet-goldmine.herokuapp.com/)

### **Project Goals**
The aim of this project was to build a fully functioning, visually appealing, e-commerce site. 

- As an owner my goals were:
    - to encourage users to visit the site
    - to encourage users to stay on the site
    - to encourage users to explore the site
    - to encourage users to buy from the site
    - to encourage users to return to the site
    - to encourage users to learn more about Irish Fashion
    - to encourage users to learn more about Sustainable Fashion
    - to help users understand the mission and values of the owner of the site
    - to curate a blog reflecting the views of the owner
    - to add, edit and delete products

### **User Stories**  

#### **As an Anonymous User:**

**General**   
- _I want to immediately understand the purpose of the site_
- _I want to be able to easily navigate through the site_
- _I want a site that appeals to me visually_
- _I want to know where I am on the site at any time_
- _I want to be informed of actions I make and whether they are successful or not_**

**Products**   
- _I want to see a list of available products_
- _I want products to be sorted into relevant categories_
- _I want to be able to search the site for a specific product_
- _I want to be able to view the individual product details_
- _I want to be able to select the size of a product_
- _I want to be able to adjust the quantity of a product_

**Shopping Bag**  
- _I want to easily view my shopping bag_
- _I want to easily view my bag total_
- _I want to be able to remove items from my shopping bag_
- _I want to be able to adjust the quantity of items in my shopping bag_
- _I want to see any changes I make to my bag reflected in the bag totals_
- _I want to view the details of what is in my bag_

**Checkout**  
- _I want to be able to checkout securely_
- _I want to receive a confirmation of my order_
- _I want the confirmation of my order to include the details of my order_

**Contact**
- _I want to be able to contact the store_
- _I want confirmation that my message has been received_
- _I want the option to sign up for a newsletter_
- _I want confirmation that I have signed up for the newsletter_
- _I want the option to unsubscribe from the newsletter_
- _I want to receive confirmation that I have unsubscribed from the newsletter_

**Blog**
-  _I want to understand the mission and values of the store_

**Create Account**   
- _I want to be able to create an account_

#### **As a Registered User:** 
- _I want to be able to log in and out easily_
- _I want to be able to reset my password_
- _I want to receive confirmation that I have registered for the site_
- _I want to have a personal profile_
- _I want to be able to view my order history_
- _I want to be able to save my favourite products to my profile_
- _I want to be able to remove products from my favourites_
- _I want to be able to save my default delivery details_
- _I want to be able to easily update my delivery info_
- _I want to be able to deactivate my account_
- _I want to receive confirmation my account has been deactivated_


### **As a Superuser:**
- _I want to be able to access the admin panel_
- _I want to be able to add/edit/delete categories_
- _I want to ba able to add/edit/delete subcategories_
- _I want to be able to add new products_
- _I want to be able to edit/delete existing products_
- _I want to be able to add new blog posts_
- _I want to be able to edit/delete existing blog posts_
- _I want to be able to view/manage users of the site_
- _I want to be able to view/manage messages from users_
- _I want to be able to view/manage newsletter subscriptions_
- _I want to be able to view/manage orders_



### **Design Process**
- As a dedicated follower of fashion myself, I wanted to design a site that evoked what I feel when I think about fashion. To me fashion is a form of self-expression, creativity and style, not just what is trendy at the moment or the latest look or what celebrities are wearing.  Clothing can help you feel confident, can boost your self-esteem and even cheer you up when your not feeling great. This was what I thought about while designing this site. 
I wanted words like *cool*, *edgy*, *retro*, *stylish*, *creative*, *vibrant* to be what a user thinks of when they visit the site and to associate those words with themselves by extension.
I used imagery, colour and fonts that I felt captured these feelings and emotions.
- I wanted the app to be bright, colourful and visually appealing.
- I wanted the app to be intuitive and easy to navigate
- I wanted to achieve a clean, uncluttered aesthetic
- I used [Bootstrap4](https://getbootstrap.com/) for the layout and structure of the site
- I used various [Bootstrap4](https://getbootstrap.com/) classes and components to enhance and structure different elements.
- I wanted the site to be responsive across all commonly used devices.

#### **Development Process**
 Once I decided to build a clothing store, I broke the development process down into stages to help me manage the project.
 - Figure out what I as a user want/like and expect from an online store.
    - What elements enhance the online shopping experience for me
    - What don't I like when shopping online
    - What is the minimum I expect from an online store
- Decide on a general colour scheme
- Decide on what apps are necessary and what additional apps I would like to include
- Decide on what features in each of those apps are necessary and what additional features I would like to include
- Create wireframes for each page for mobile, tablet and desktop
- Create a dataset for the products app
- Create a minimum viable product
    - Set up Django
    - Set up Allauth
    - Create the base.html and navigation with common elements, links and scripts
    - Create the home app -  basic logic, functionality, structure and style
    - Create the products app - basic logic, functionality, structure and style
    - Create the bag app - basic logic, functionality, structure and style
    - Create the checkout app - basic logic, functionality, structure and style
    - Create the profile app - basic logic, functionality, structure and style
    - Create common elements - footer, toasts, messages
    - Create the contact app - basic logic, functionality, structure and style
    - Create the blog app - basic logic, functionality, structure and style
- Add logic and functionality for additional features
- Adjust layout and styling

#### **Design Decisions**
**From an owners perspective**:
- **_Random Product Carousel_**
    - As an owner I would like to keep visitors on the site for as long as possible and for them to spend money.
    - A lot of the time when a user visits a site they are looking for a particular product or a particular category of products - shoes or dresses or tops etc, and so may limit their search of the site to that particular category.
    - By displaying a random group of products on particular pages it was my intention for visitors to see a selection of products that they might not otherwise have seen and to encourage them to spend more time on the site browsing other categories outside of the original reason for their visit and hopefully purchase something they had not originally intended to buy!

- **_Adding Favourites_**
    - By allowing users to save products to their favourites it will increase the chance of them buying that particular product, if not on this visit then at a later date.
    - It also increases the chances that the user will return to the site, therefore increasing the chances that they will make a purchase.
    - It also helps encourage users to create an account so that they can avail of that feature.

- **_Category/Subcategory Carousel_**
    - Encourages users to search through categories they may not have intended to browse and spend more time on the site.

- **_Blog_**
    - I felt the blog was a chance to convey the values of the store to the users.
    - With people becoming more conscious of their fashion choices, seeking out sustainable fabrics and reducing the impact their buying choices have on the environment I felt it was important for users to understand that those concerns were being addressed by the store. And that we as a business also care about the impact on the environment and being more sustainable.
    - It can also be used as a tool for users who would like to learn more about sustainable fashion practices and hopefully encourage them to adapt some of those practices themselves.
    - It will encourage like minded users to shop in the store.

**From a users perspective**:
- **_Category/Subcategory Carousel_**
    - I was never really a fan of online shopping myself, I found most online stores clunky, and navigation between categories was always a bit of a chore, but obviously, like everyone, I've had to adapt my shopping habits over the last year with retail stores being closed due to the pandemic. 
    - My main problem with online shopping was navigation. A lot of the time you had to navigate back to the start or back to a parent category to get to another subcategory.
    - With that in mind I wanted to make navigation between product categories as easy as possible.
    - Including the carousel at the top of each products page allows the user to easily navigate around the site without ever having to go back to the *All Products* page or even use the navbar
    - It also allowed the user to see exactly what type of products were available in the store easily.

- **_Adding Favourites_**
    - I felt it was important for users to be able to save products they like and have thm available on their profile so they could easily find them again if they wanted to purchase them

- **_Blog_**
    - For users with an interest in fashion outside of just buying clothes, particularly in the Irish fashion industry and sustainable fashion practices it is a resource where they can learn more.

**General design decisions**
- **_Brand Logo_**
    - I placed the Brand Logo in the center of the header as I felt it played an important part in creating the overall aesthetic of the store.
    - I wanted it to be the focal point of the header
- **_Search Bar_**
    - I placed this to the left (on larger devices) as I felt it was important that it was placed in the header and available throughout the store. 
    - I also felt the the header was more balanced with the brand logo in the centre and the search bar and icons on either side.
- **_Box Shadows_**
    - I used box shadows to make elements stand off the page and create more depth.
    - I felt they contributed to the overall aesthetic and really enhanced the product cards and buttons.
    - I felt that using them on the header and footer added a degree of separation to the different sections of the page without being overbearing.
    - I used a pink box shadow on all form inputs to add a little bit of colour to those pages and to enhance the forms themselves and keep them inline with the aesthetic of the rest of the site.
- **_Footer Backgrounds_**
    - I felt that the grey footer on the home page did not fit with the overall aesthetic of the page and cut the page up too much. 
    - I decided on the opaque overlay over the image as the image is an important part of the aesthetic and wanted it to keep the home page as clean as possible with image as the focal point
    - I used the same background colour as the body for the footer across the rest of the site as I wanted the page to flow naturally and not be chopped up by using a different colour
    - I used the box shadow on the top border to give a subtle degree of separation between the content and the footer.
- **_Interchanging title fonts_**
    - I used the Sedgwick Ave Display font for most of the page headings as that font is integral to the overall aesthetic.
    - However on some pages I felt it was a little over bearing and reduced readability so I reverted to the body font - Quicksand - for a cleaner look on those pages.
- **_Carousels_**
    - I hid the carousels on smaller devices as I felt they made the pages a bit cluttered and busy and more a distraction than an enhancement.

#### **Colour Scheme**
- I wanted the colour scheme to be bold, bright and vibrant, feelings which are evoked when I think of fashion, while still being easily readable.  

**Colour Palette**

<img src="/media/readme_images/colour_palette.png">


#### **Primary Colour Palette**

<img src="/media/readme_images/primary_palette.png">

I chose #000, #ee6aa7 and #dee2e6 as my primary colour palette. I felt these colours worked well together and were in keeping with the overall aesthetic of the site.  

<img src="/media/readme_images/black.png">

I chose this colour for the as it enhanced any colour it was paired with, helping to improve readability.  

- **Site Wide**:
    - background for navbar/main header
    - delivery banner text
    - box shadow on delivery banner
    - border/text on buttons
    - background for buttons on hover
    - background for copyright info 


<img src="/media/readme_images/ee6aa7.png">

I chose this colour as it stood out well against #000 and #dee2e6, and was bright and vibrant.   

- **Site Wide**: 
    - brand logo
    - nav header icons
    - navlinks on hover
    - all headings/titles
    - button backgrounds
    - button text on hover
    - footer text (apart from home page)
    - footer icons
    - copyright text
    - toast success border
    - form box shadow
    - scroll button back ground  
    - pink divider

- **Products Pages**:
    - breadcrumb text
    - sort select box text
    - carousel titles
    - edit buttons on product cards
    - category/subcategory button text
    - category/subcategory button background on hover

- **Product Detail Page**:
    - breadcrumb text
    - product name
    - tag icons
    - size select box text/ title
    - quantity title
    - quantity button background
    - random carousel title

- **Shopping Bag**:
    - table titles
    - quantity link/buttons
    - product name

- **Checkout**:
    - placeholder text
    - text

- **Checkout Success**:
    - order info text

- **Blog/Blog Detail**
    - blog titles
    - links

- **Contact**:
    - text  


<img src="/media/readme_images/dee2e6.png">

I chose this colour for the background across the site. I felt that it enhanced the other colours and that they stood out well against it, helping to improve readability.  

- **Site Wide**:
    - background colour (apart from home page)
    - footer background colour (apart from home page)
    - main nav links
    - nav links dropdowns background
    - search box background

- **Home page**:
    - footer text  
  
#### **Secondary Colour Palette**  

<img src="/media/readme_images/secondary_palette.png">

I chose these colours for their similarity to the primary colour palette. I felt they worked well with the primary colour palette and highlighted certain elements without being overbearing, and while still offering enough differentiation for the user to notice the colour change.  


<img src="/media/readme_images/ff077b.png">

I choose this colour for its similarity to #ee6aa7 while being a little bolder and standing out better against the darker grey.  

- **Site Wide**:
    - Navlink dropdown text colour

- **Products Page**:
    - product name/price on cards  

- **Product Detail Page**:
    - product name/price on random carousel  

<img src="/media/readme_images/c7cbcf.png">

I choose this colour for its similarity to #dee2e6 while being a little bolder and standing out better against it.  

- **Site Wide**:
    - footer top border and box shadow (apart from home page)
    - background of scroll button on hover
    - scroll button icon

- **Home Page**:
    - unsubscribe link in home footer

- **Products Page**:
    - background on product card
    - product card border
    - background on category/subcategory badges
    - text colour on category/subcategory badges on hover  

<img src="/media/readme_images/8d9391.png">

I choose this colour for its similarity to #dee2e6 and #c7cbcf, to enhance them and make them standout from the page.  


- **Home Page**:
    - divider in footer
    - scroll button box shadow

- **Products Page**:
    - box shadow on category badges
    - box shadow on product cards

- **Shopping Bag**:
    - remove from bag link  

#### **Images**
- Home page hero image:
    - I chose this image as when I think of street, again I think of self-expression and creativity words I also associate with fashion. 

- Dataset:
    - I created my own dataset as I wanted the product images to fit with the overall aesthetic of the site and the message it is trying to send. 
    - I used images from [Unsplash](https://unsplash.com/), [Pixabay](https://pixabay.com/) and [Pexels](https://www.pexels.com/). Full image credits can be found [here](IMAGE_CREDITS.md).
    - All product info is fictitious.

#### **Typography**
- For the brand logo, page titles and headings I wanted a font that fit with the street art image, that was creative and artistic.
- I chose [Sedgwick Ave Display](https://fonts.google.com/specimen/Sedgwick+Ave+Display?preview.text_type=custom&preview.text=The%20Velvet%20Goldmine&category=Display,Handwriting&sort=date&query=sed) as I felt it was had a graffiti/street art feel to it and a bit of an edge. 
- Which also represented the products the store is selling - edgy, cool, artistic, creative
- For the main home page title I chose [Permanent Marker](https://fonts.google.com/specimen/Permanent+Marker?preview.text=Discover%20Your%20Style&preview.text_type=custom). I chose this font for its readability while also fitting into the overall theme of graffiti/street art.
- I felt that using Sedgwick Ave Display here would be too much for the home page and come across as messy. 
- For the body text I chose [Quicksand](https://fonts.google.com/specimen/Quicksand?preview.text_type=custom&preview.text=The%20Velvet%20Goldmine&sort=date&query=quick). I felt it contrasted well with the artistic nature of Sedgwick Ave Display.
- I felt it was a clean font with good readability and fit the overall aesthetic of the site.  


#### **Wireframes**
- I used [Balsamiq](https://balsamiq.com/wireframes/) to create the wireframes for my project.
- I create 3 sets of wireframes for Desktop, Tablet and Mobile.
- To view the wireframes please click the links below:

**Desktop**  
- Desktop wireframes can be found [here](https://github.com/aineon/velvet-goldmine/tree/master/wireframes/desktop_wireframes)  

**Tablet**  
- Tablet wireframes can be found [here](https://github.com/aineon/velvet-goldmine/tree/master/wireframes/tablet_wireframes) 

**Mobile** 
 - Mobile wireframes an be found [here](https://github.com/aineon/velvet-goldmine/tree/master/wireframes/mobile_wireframes) 

##### [Back to Table of Contents](#table-of-contents)
---


## **Database Model**
- SQLlite was used in Development and PostgresSQL was used for Deployment. 
- I used [Graphviz](https://graphviz.org/) to generate 3 images of the database model  
    1. Image of my custom app models and their relationships
    2. Image of my custom apps models and auth models and their relationships
    3. Image of all models including models automatically generated by Django  

1. Custom Apps
<img src="/media/readme_images/models.png">

2. Custom & Allauth
<img src="/media/readme_images/models_auth.png">

3. All Models
<img src="/media/readme_images/models_all.png">


##### [Back to Table of Contents](#table-of-contents)
---

## **Features**
### **CRUD Functionality**
- While any user of the site can read the data, only admins/superusers can create, update and delete data on the site. 

### **Existing Features**
- The site contains 7 separate custom apps. Each app has its own set of features.
    - Home
    - Products
    - Bag
    - Checkout
    - Contact
    - Blog
    - Profile  
- It also uses [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) to manage authentication, registration, account management and 3rd party account authentication.  
- It uses [Stipe Payments Infrastructure](https://stripe.com/) to manage the payment system.

#### **Site wide Features**
- **_Toast Messages_**
    - There are 4 types of toast messages:
        - Success
        - Info
        - Warning
        - Error
    - They appear site wide when particular actions are performed by the user
    - They provide feedback on the action taken

- **_Automated Emails_**
    - Automated emails are sent to the user when certain actions are performed.
        - Account verification email when a user registers for an account
        - Password reset email
        - Order confirmation email when a user completes an order
        - Confirmation of message received when a user sends a message 
        - Confirmation of newsletter sign up when a user signs up for the newsletter
        - Confirmation of unsubscribe when a user unsubscribes from the newsletter
        - Confirms when a user deactivates their account

- **_Navbar/Sidenav_**:
    - To allow easy navigation across the site
                        
- **_Header_**:
    - Identifies the site name
    - Search bar on larger devices and search icon for dropdown search bar on smaller devices
    - User icon: 
        - With dropdown for login/registration links for logged out users
        - Profile and logout links for logged in users
        - Blog management, product management, profile and log out links for superusers
    - Shopping bag icon:
        - Displays current bag total
        - links to shopping bag page
    - Contact icon:
        - links to contact page  

- **_Delivery Banner_**
    - Informs users of the free delivery threshold

- **_Footer_**:
    - Newsletter signup form to make it available site wide
    - Newsletter unsubscribe links
    - Links to social media pages (links open login pages to these sites as the pages don't exist)
    - Link to contact page
    - Copyright information 

#### **Custom App Features**
#### **Home App**
- Hero text
- Shop Now button which links to the products page

#### **Products App**
**Products Page**:
-  **_Category/Subcategory Carousel_**
    - Rotating carousel that contains images and titles for categories/subcategories
    - Each carousel cell is a link to the category/subcategory it represents
- **_Breadcrumbs_**
    - Allow users to track their file path and easily navigate back to previous pages without having to use the navbar 
- **_Current Category/Subcategory Page title_**
    - Identifies which category/subcategory the user is currently browsing
- **_Category/Subcategory Badges_**
    - Identifies the categories/subcategories linked to the current page
    - Each badge is a link to that category/subcategory
- **_Sort Box_**:
    - Allows users to sort the products based on the defined criteria
- **_Product Count_**:
    - Tells the user how many products are on the current page 
    - If a search has been performed informs user of the product count related to that search including what was searched for
    - If not on *All Products* page contains a link back to *All Products* page
- **_Product Cards_**:
    - Links to the product detail page
    - Displays product image, name and price
    - For superusers contains edit/delete links 
- **_Scroll Button_**:
    - Appears when users scroll down 100px from the top of the page
    - Brings user back to the top of the page when clicked  

**Product Detail Page**:
- **_Breadcrumbs_** 
    - informs user of the category, subcategory and product name of the current page
- **_Product Details_**
    - Larger product image which opens the product image on a new page if clicked
    - Product name
    - Product Price
    - Product description
- **_Add to Favourites Icon_**
    - Heart Icon with tooltip which allows logged in users to add that product to their favourites list
    - If product is not a favourite tooltip appears with *Add to Favourites* text
    - If product is in the users favourite list tooltip appears with *Remove from Favourites* text
    - If user saves product toast success message is triggered informing the user they have saved the product with a link to *View Favourites*
    - If user removes from favourites toast success message is triggered informing them that the product has been removed
- **_Product tags_** 
    - With the subcategory/category of the product where applicable
- **_Edit/delete links_** 
    - Only visible to superuser  
- **_Size select box_** 
    - For products that have sizes
    - Dropdown lists sizes available
- **_Quantity select box_** 
    - Can be increased/decreased within the set range
- **_Keep Shopping button_** 
    - Links back to the *All Products* page
- **_Add to bag button_** 
    - Adds the current product along with the qty selected and size if applicable to the shopping bag.
    - If a product is added to the bag a toast success message appears informing the user of 
        - what has been added to the bag - name, price, size, qty
        - if the bag total is below the free delivery threshold, informs the user how much more they need to spend to reach it
        - button which brings the user to the secure checkout page
- **_Random product carousel_**
    - Generates a carousel of 7 random products 
    - Each cell contains product image, name and price
    - Links to that product detail page

**Product Management**
- Only accessible if superuser
- Form to add a new product

**Edit Product**
- Only accessible if superuser
- Loads selected product details for editing

#### **Bag App**
- **_Product Info_**
    - product image, name, size (if applicable) and sku
- **_Product Price_**
    - price of individual product
- **_Product Qty_**
    - Current qty selected 
    - Option to adjust qty or remove item from bag
- **_Subtotal_**
    - Subtotal for that item
- **_Bag Total_**
    - Total cost of all items in the bag
- **_Delivery Cost_**
    - Cost of delivery if below free delivery threshold
- **_Grand Total_**
    - Total cost of items and delivery
- **_Free Delivery Threshold_**
    - If free delivery threshold hold is not reached informs the user of how much more they need to spend to reach it
- **_Keep Shopping Button_**
    - Brings user back to *All Products* page
- **_Secure Checkout Button_**
    - Brings user to *Secure Checkout* page
-  **_Category/Subcategory Carousel_**
    - Rotating carousel that contains images and titles for categories/subcategories
    - Each carousel cell is a link to the category/subcategory it represents
- **_Scroll Button_**:
    - Appears when users scroll down 100px from the top of the page
    - Brings user back to the top of the page when clicked  

#### **Checkout App**
**Checkout Page**
- **_User Details Form_**
    - Name and email address of the user
- **_Delivery Details Form_**
    - Delivery address for order
    - If user is logged in there is an option to save the info for future use
    - If user is not logged in links to log in or create an account if they would like to save the info for future use. 
    - If info is saved it is display on the users profile page
- **_Credit Card Form_**
    - Prompts user to enter credit card details
    - Informs the user of how much their card will be charged
- If any of the forms are filled out incorrectly user is prompted to correct the errors
- **_Adjust Bag Button_**
    - Brings the user back to the *Shopping bag* page
- **_Complete Order Button_**
    - Processes the order 
    - Redirects to *Checkout Success* page
- **_Order Summary_**
    - Product count
    - Product image, name, qty, size (if applicable) and subtotal
    - Order total
    - Delivery charge
    - Grand total  

**Checkout Success Page**
- Informs the user a confirmation email will be sent
- All order details
- All delivery details
- Totals
- Button brings user back to *All Products* page

#### **Contact App**
**Contact Page**
- **_Message Form_**
    - Sender details
    - Message details
- **_Send Button_**
    - Sends message
- **_Cancel Button_**
    - Cancels the message

**Newsletter Signup**
- The newsletter signup form is located in the footer across the site
- **_Sign Up Button_**
    - Adds user to the newsletter mailing list

**Newsletter Unsubscribe Page**
- Can be accessed by the unsubscribe links in the footer
- When clicked user is redirect to the unsubscribe page which holds the unsubscribe form
- **_Unsubscribe Button_**
    - Removes the user from the mailing list
- **_Cancel Button_**
    - Returns user to the *All Products* page

#### **Blog App**
**Blog Page**
- **_Intro_**
    - Explains the type of posts that users can expect to find in the blog
- **_Contact Link_**
    - Links to the contact page
- **_Blog Posts_**
    - Blog title
    - Edit/delete buttons if superuser
    - Author (if applicable)
    - Image (if applicable)
    - Date Posted
    - Blog intro
    - Credits if not original content
- **_Read More Button_**
    - Links to Blog detail page
- **_Scroll Button_**:
    - Appears when users scroll down 100px from the top of the page
    - Brings user back to the top of the page when clicked  

**Blog Post Detail Page**
- **_Blog Post_**
    - Blog title
    - Edit/delete buttons if superuser
    - Author (if applicable)
    - Image (if applicable)
    - Date Posted
    - Blog intro
    - Credits if not original content
- **_Read Article Button_**
    - Visible if not original content
    - Links to full article page
- **_Back to Blog Button_**
    - Brings user back to Blog page
- **_Scroll Button_**:
    - Appears when users scroll down 100px from the top of the page
    - Brings user back to the top of the page when clicked  

**Blog Management**
- Only accessible if superuser
- Form to add blog post

**Edit BlogPost**
- Only accessible if superuser
- Loads selected blog details for editing

#### **Profiles App**
**Profile Page**
- Only accessible if registered user
- Contains 4 tabs
    - Favourites
    - Order History
    - Default Delivery Info
    - Deactivate Account
- **_Favourites Tab_**
    - Keep Shopping Button - Returns user to the *All Products* page
    - Contains any products that have been added to favourites
    - For each product includes:
        - Product details (same as product detail page)
        - Favourite Icon to remove product from favourites
        - Size select box
        - Qty select box
        - Add to bag button
- **_Order History_**
    - Contains info of previous orders
- **_Default Delivery Info_**
    - Form with delivery info
    - Update button - to update current info
- **_Deactivate Account_**
    - Button to deactivate account
    - Link to contact page

### **Future Features**
- Add logic to manage inventory
- Allow registered users to securely save credit/debit card details for future use
- Allow users to pay using Paypal
- Allow users to comment on blog posts
- Include New Arrivals and Vintage/Preloved section
- Include FAQs section
- Include Shipping and returns policy  

##### [Back to Table of Contents](#table-of-contents)
---


## **Technologies Used**
### **Languages**
- **HTML** - used to create the structure of the application
- **CSS** - used to position and style the application 
- **JavaScript** - used to for interactivity
- **Python** - used to handle backend


### **Libraries and Frameworks**
- [Django](https://www.djangoproject.com/)
- [Bootstrap4](https://getbootstrap.com/)
- [Stripe](https://www.stripe.com/)
- [Google Fonts](https://fonts.google.com/) 
- [Font Awesome](https://fontawesome.com/) 
- [jQuery](https://code.jquery.com/) 
- [Flickity](https://flickity.metafizzy.co/)
- [hover.css](https://ianlunn.github.io/Hover/) 
- [Pillow](https://pypi.org/project/Pillow/2.2.1/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Gunicorn](https://gunicorn.org/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  
- [Sweet Alert](https://sweetalert.js.org/)

### **Project Management**
- [Git](https://git-scm.com/) 
- [Gitpod](https://gitpod.io/) 
- [Github](https://github.com/) 
- [Heroku](https://signup.heroku.com)
- [AWS](https://aws.amazon.com/console/)


### **Tools**
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) 
- [Balsamiq](https://balsamiq.com/wireframes/)
- [Am I Responsive](http://ami.responsivedesign.is/)
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB)
- [Favicon](https://favicon.io/favicon-converter/) 
- [Autoprefixer](https://autoprefixer.github.io/) 
- [Compress PNG](https://compresspng.com/)
- [jpg2png](https://jpg2png.com/)
- [Color-hex](https://www.color-hex.com/)


### **Resources**
- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [cdnjs](https://cdnjs.com/)
- [w3schools](https://www.w3schools.com/) 
- [Stack Overflow](https://stackoverflow.com/)
- Boutique Ado Project - [Code Institute](https://codeinstitute.net/) Full Stack Frameworks Module

##### [Back to Table of Contents](#table-of-contents)
---

## **Testing**
Full testing documentation can be found [here](TESTING.md).

##### [Back to Table of Contents](#table-of-contents)
---

## **Deployment**
This project was developed using Gitpod IDE. The live version of this site is hosted using [Heroku](https://signup.heroku.com/).  

To deploy this project follow the below steps.

The live site can be viewed [here](https://the-velvet-goldmine.herokuapp.com/).  

### **Requirements to run this app**
- **Python3** 
- **Django**
- **Django Allauth**
- **Stripe**
- **PIP** package installation
- The full list of requirements is in the requirements.txt file

### **Locally**
To run this project locally, follow the below steps:
To clone this project from Github:
- Click the [Velvet Goldmine Repository Link](https://github.com/aineon/velvet-goldmine)
- From the repository click the **Code** button
- In the **_Clone with HTTPs_** section, copy the clone URL for the repository
- In your local IDE open **_Git Bash_**
- Change the current working directory to the location where you want the cloned directory to be made
- Type `git clone` and then paste the URL you copied from the repository
```console
git clone https://github.com/aineon/velvet-goldmine.git
```
- Press Enter. Your local clone will be created
- To remove the origin link from your IDE type `git remote rm origin`

- Run the below command to install required packages:  

`pip install -r requirements.txt`

- Alternatively you can download the **ZIP folder** of this project by clicking the **Code** button *(as above)*
and selecting **_Download ZIP_**
- It can then be unpacked into your desired location
- Open the **index.html** file to run the project locally

### **AWS**
[AWS](https://aws.amazon.com/console/) was used to host the static and media files for this project in deployment. To set up AWS please follow the steps below:
- navigate to aws.amazon.com
    - create an account
    - search for S3 and click on it
- **Create a new bucket**   
    - select the region closest to you
    - uncheck block all public access
    - click create bucket
- In the **properties section**:
    - turn on static web hosting
    - fill in some default values for the index and error documents
    - click save
- In the **permissions section**:
    - add the **_cors configuration_**
- Go to the **bucket policy section**
    - select policy generator
    - policy type will be **_s3 bucket policy_**
    - allow all principals by using *
    - the action will be **_get object_**
    - copy the **ARN** and paste it into the **_arn box_**
    - click **_Add Statement_**
    - then **_generate policy_**
    - copy this policy into the **_bucket policy editor_**
    - allow access to all resources in this bucket by adding a /* to the end of the resource key
    - click save
- Go to the **access control list section**
    - set the list objects permission for everyone under the Public Access section 

- **Create a user to access the bucket**
    - from the services menu open **Iam**
    - click groups
    - create a new group
    - **Create the policy used to access the bucket**
    - click policies
    - create policy
    - go to the **_JSON tab_**
    - select **_import managed policy_**
    - search for **_s3_**
    - import the **_s3 full access policy_**
    - get the **_bucket ARN_** from the bucket policy page in s3
    - paste it in
    - click review policy
        - give it a name and description
    - click create policy
- **Attach the policy**
    - go to groups
    - click on the group you just created
    - click attach policy
    - search for the policy you just created and select it
    - click attach policy
- **Create a user**
    - on the users page click **_add user_**
    - give it a name and **_programmatic access_**
    - select next
    - click through to the end and then **_create user_**
    - download the **CSV file** which will contain the **_user access key_** and **_secret access key_** which need to be added to the Heroku config vars  


### **To Heroku**
To deploy the app using [Heroku](https://signup.heroku.com/) from its [GitHub Repository](https://github.com/aineon/velvet-goldmine),
follow the steps below:
- From the IDE terminal create the following files:
    - requirements.txt 
    - Procfile
- Use the below commands to create the files:
````
pip3 freeze > requirements.txt
echo web: python3 manage.py > Procfile
````

- Push these files to Github
- Sign up/login to [Heroku](https://signup.heroku.com/)
- Click the **New** dropdown menu
- Select **Create new app**
- Enter a unique name for the App
- Choose your region
- Click **create app** button
- The **Deploy** tab will open
- Select Github as the **Deployment Method**
- Enter your Github details and the repository name
- Click **search**
- When the correct repository has been found, click connect
- Add PostgresSQL Database:
    - In your **IDE**:
        - Configure your database settings with a call to  
        `dj_database_url.parse(<database url from heroku>)` 
        - Run migrations
        - Load the fixtures in the correct order:
        `python3 manage.py loaddata <fixtures name>`
        - Create a superuser
    - In **Heroku**:
    - Click the **Resources Tab**
    - Under **Add-ons** search for **Heroku Postgres**
    - When found click on it
    - Select Plan name **Hobby Dev - Free**
    - CLick **Submit Order**
- Go to the **Settings** tab
    - Under **Config Vars** select **Reveal Config Vars**
    - Enter the following **key/value** pairs. **_Ensure they match the key/value pairs contained in your settings.py file_**

|**Key**                        |**Value**
|-----------                    |-----------  
| AWS_ACCESS_KEY_ID             | `<AWS_ACCESS_KEY_ID>`
| AWS_SECRET_ACCESS_KEY         | `<AWS_SECRET_ACCESS_KEY>`
| DATABASE_URL                  | `<DATABASE_URL>`
| EMAIL_HOST_PASS               | `<EMAIL_HOST_PASS>`
| EMAIL_HOST_USER               | `<EMAIL CONNECTED TO APP>`
| SECRET_KEY                    | `<DJANGO SECRET KEY>`
| STRIPE_PUBLIC_KEY             | `<STRIPE_PUBLIC_KEY>`
| STRIPE_SECRET_KEY             | `<STRIPE_SECRET_KEY>`
| STRIPE_WH_SECRET              | `<STRIPE_WH_SECRET>`   
| USE_AWS                       | `True`   
      


- Go back to the **Deploy** tab
- Under **Automatic Deploys** select **Enable Automatic Deploys**
- Under **Manual Deploys** select **master** 
- Click **Deploy Branch**
- When the app has finished building, click **Open app** button on the top right of the page.


##### [Back to Table of Contents](#table-of-contents)
---
## **Credits**

### **Code**
- For the newsletter signup view I watched this [tutorial](https://www.youtube.com/watch?v=Hy94jBBgvpk) by [Master Code Online]() on [YouTube](https://www.youtube.com/)
- For the newsletter unsubscribe view I watched this [tutorial]() by [Master Code Online]() on [YouTube](https://www.youtube.com/)
- For the adding favourites view I watched this [tutorial](https://www.youtube.com/watch?v=H4QPHLmsZMU) by [Very Academy](https://www.youtube.com/channel/UC1mxuk7tuQT2D0qTMgKji3w) on [YouTube](https://www.youtube.com/)
- For Gmail login I read this [article](https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5) by [Zoe Chow](https://whizzoe.medium.com/) on [Medium](https://medium.com/)
- For Facebook login I read this [article](https://jinkwon711.medium.com/django-allauth-facebook-login-b536444cbc6b) by [Kwon Jinhwan](https://jinkwon711.medium.com/) on [Medium](https://medium.com/) 
- Tooltips styling - From [Stack Overflow](https://stackoverflow.com/questions/36143382/re-color-tooltip-in-bootstrap-4?noredirect=1&lq=1)
- Tabs functionality on Profile page - [w3schools](https://www.w3schools.com/howto/howto_js_tabs.asp)

### **Content**
- All product names, prices and descriptions are fictional
- BlogPost - [5 homegrown Irish designers you can support during the pandemic](https://www.image.ie/style/fashion/5-homegrown-irish-designers-can-support-pandemic-188728) from [image.ie](https://www.image.ie/)
- BlogPost - [The ugly side of fast fashion: This is the scary impact it’s having on our world](https://www.image.ie/editorial/ugly-fast-fashion-scary-impact-world-environment-142426) from [image.ie](https://www.image.ie/)
- BlogPost - [Fabrics to avoid and embrace if you want to make more sustainable fashion choices](https://www.image.ie/editorial/sustainable-fabrics-146790) from [image.ie](https://www.image.ie/)
- BlogPost - [10 Irish Fashion Brands You Should Know About](https://theculturetrip.com/europe/ireland/articles/10-irish-fashion-brands-you-should-know-about/) from [TheCutluretrip](https://theculturetrip.com/)
- Icons were taken from [FontAwesome](https://fontawesome.com/)

### **Media**
- Hero image on home page -  Image by <a href="https://pixabay.com/photos/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1209761">Free-Photos</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1209761">Pixabay</a>
- Product images were taken from [Unsplash](https://unsplash.com/), [Pixabay](https://pixabay.com/) and [Pexels](https://www.pexels.com/). 
    - Full image credits can be found [here](IMAGE_CREDITS.md).  
- Blogpost images were taken from [Unsplash](https://unsplash.com/), [Pixabay](https://pixabay.com/) and [Pexels](https://www.pexels.com/). 
    - Full image credits can be found [here](IMAGE_CREDITS.md). 
- No Image image and Logo for error pages - created by me 


### **Acknowledgements**
Thank you to my mentor [Adegbenga Adeye](https://github.com/deye9) and CI tutor support for all their time and patience!

---

## **Disclaimer** 
All images and content on this website is for educational purposes only.

##### [Back to Table of Contents](#table-of-contents)

--- 