#### [Back to README](README.md)

## **Testing**
### [**Table of Contents**](#table-of-contents)

- [User Stories](#user-stories)
    - [Anonymous User](#anonymous-user)
        - [General](#general)
        - [Products](#products)
        - [Shopping Bag](#shopping-bag)
        - [Checkout](#checkout)
        - [Profiles](#profiles)
        - [Contact](#contact)
        - [Blog](#blog)
        - [Create Account](#create-account)
    - [Registered User](#registered-user)
    - [Superuser](#superuser)
- [Manual Testing](#manual-testing)
    - [Site Wide](#site-wide)
        - [Header](#header)
        - [Footer](#footer)
    - [Home App](#home-app)
    - [Products App](#products-app)
    - [Bag App](#bag-app)
    - [Checkout App](#checkout-app)
    - [Contact App](#contact-app)
    - [Blog App](#blog-app)
    - [Authentication and Authorization](#authentication-and-authorization)
- [Responsiveness](#responsiveness)
- [Automated Testing](#automated-testing)
- [Bugs and Issues](#bugs-and-issues)
    - [Resolved](#resolved)
    - [Existing](#existing)

## **User Stories**
Each _user story_ was tested to ensure site meets user expectations.

### **Anonymus User**

### **General**   
**_I want to immediately understand the purpose of the site_**
- The imagery, text and navlinks clearly explain the purpose of the site

**_I want to be able to easily navigate through the site_**  
- All links are clearly defined in the navbar with additional options to navigate to different pages throughout the site
- Buttons and icons are easily identifiable
- Consistency across the site is achieved with the navbar and footer remaining fixed across all pages

**_I want a site that appeals to me visually_**
- The combination of imagery, fonts and colours create a visually appealing site.

**_I want to know where I am on the site at any time_**
- Breadcrumbs across the products pages identify where on the site a user is
- Page titles on every page identify what page they are on

**_I want to be informed of actions I make and whether they are successful or not_**
- Toasts messages are triggered for actions performed on the site informing the user of the outcome of that action.

### **Products**   
**_I want to see a list of available products_**
- Clicking the *Shop Now* button on the home page redirects the user to the *All Products* page which displays all products available in the store
- Clicking the *All Products* link in the navbar redirects the user to the *All Products* page which displays all products available in the store
- If a user navigates to a specific category/subcategory of products there is a *Back to All Products* link which will bring the user back to the *All Products* page

**_I want products to be sorted into relevant categories_**
- All Products are sorted into relevant and inituitive categories and subcategories
- Categories and subcategories are accessible through the navbar or the carousel across all product pages

**_I want to be able to search the site for a specific product_**
- The search bar on larger devices and search icon on smaller devices alls users to search for a specific product.
- The search will be performed on the product name and description

**_I want to be able to view the individual product details_**
- Clicking on any product card will redirect the user to the product detail page where they can view a larger image, product name, price and description

**_I want to be able to select the size of a product_**
- The size select box on the product detail page allows users to select a size from the available options

**_I want to be able to adjust the quantity of a product_**
- The quantity box on the product detail page allows users to select their desired quantity of that product

### **Shopping Bag**  
**_I want to easily view my shopping bag_**
- Clicking on the shopping bag icon will direct the user to the shopping bag page
- The icon is in the header and as such is available across the site

**_I want to easily view my bag total_**
- The bag total is visible below the bag icon in the header across the site

**_I want to be able to remove items from my shopping bag_**
- There is a remove item link under the qty box for each item in the shopping bag
- Clicking the remove item link will remove the item from the bag

**_I want to be able to adjust the quantity of items in my shopping bag_**
- There is an update qty link below the qty box for each item in the shopping bag
- Users can adjust the qty using the +/- buttons on the qty box and clicking *update qty* 
- or by simply entering the number of the qty they wish to purchase and clicking *update qty*  

**_I want to see any changes I make to my bag reflected in the bag totals_**  
- Bag/Product totals are automatically updated when item qty is adjusted or an item is removed from the bag  

**_I want to view the details of what is in my bag_**
- All product details including, image, name, price, size (if applicable), qty and subtotal are listed for each item that has been added to the bag

### **Checkout**  
**_I want to be able to checkout securely_**
- I receive clear errors if information has been entered incorrectly
- I credit card form follows common format

**_I want to recieve a confirmation of my order_**
- When an order has been processed successfully the user is redirected to the *Checkout Success* page where all the order details are displayed
- An email is also sent to the email address provided by the user on the *Checkout Page* with the full order details and delivery details

**_I want the confirmation of my order to include the details of my order_**
- When an order has been processed successfully the user is redirected to the *Checkout Success* page where all the order details are displayed
- An email is also sent to the email address provided by the user on the *Checkout Page* with the full order details and delivery details

### **Contact**
**_I want to be able to contact the store_**
- The contact icon in the header redirects the user to the contact page when clicked
- The contact page contains a message form where the user can send a message to the store

**_I want confirmation that my message has been received_**
- Once a message has been sent an email will be sent to the email address entered in the message form informing the user that their message has been received

**_I want the option to sign up for a newsletter_**
- There is a newsletter signup form located in the footer and so is accessible across the site

**_I want confirmation that I have signed up for the newsletter_**
- Toast message confirms they have been added to the mailing list
- When a user signs up for the newsletter an email is sent to the email address entered into the form confirming that they have signed up for the newsletter

**_I want the option to unsubscribe from the newsletter_**
- There is a link in the footer below the newsletter sign up form that redirects the user to the unsubscribe page.
- There is also a link to the unsubscribe page in the newsletter sign up confirmation email
- When the user enters their email address and clicks unsubscribe their email address is removed from the mailing list

**_I want to receive confirmation that I have unsubscribed from the newsletter_**
- Tost message confirms they have been removed from the mailing list
- When a user unsubscribes from the newsletter and email is sent confirming that they have unsubscribed

### **Blog**
**_I want to understand the mission and values of the store_**
- The Intro on the blog page and the blog posts themselves help the user understand the mission and values of the store

### **Create Account** 
**_I want to be able to create an account_**
- If a user wishes to create an account they can click on the user icon and click register
- They will be prompted to fill out the required information and informed of any errors in the form


### **Registered User** 
**_I want to be able to log in and out easily_**
- Clicking on the user icon in the header gives the user the option to log in or out and redirects them to the relevant page when clicked

**_I want to be able to reset my password_**
- The *Forgotten Password* link on the login page redirects users to the password reset page where they can enter their email address and recieve instructions on how to reset password

**_I want to receive confirmation that I have registered for the site_**
- When a users registers for an account an email is sent to the email address entered in the form confirming registration

**_I want to have a personal profile_**
- When a user registers for an account a personal profile page is automatically created for them

**_I want to be able to view my order history_**
- All previous order details can be found in the *Order History* tab on the profile page

**_I want to be able to save my favourite products to my profile_**
- Clicking on the heart icon on the product detail page allows registered users to add that item to their favourites
- These favourites can be viewed or removed in the *Favourites* tab on the profile page

**_I want to be able to remove products from my favourites_**
- Clicking on the solid heart icon either on the product in the *Favourites tab* or on the product detail page will remove that product from the favourites

**_I want to be able to save my default delivery details_**
- Registered users can save default delivery details on during checkout by ensuring the *Save Details* box is checked
- They can also save them on the profile page by filling out the form in the *Default Delivery Tab* and clicking *update info* button

**_I want to be able to easily update my delivery info_**
- Registered users can update their delivery info by completing the form on the *Delivery Info* tab on their profile page

**_I want to be able to deactivate my account_**
- Registered users can deactivate their account using the *Deactivate Acccount* button in the deactivate account tab.

**_I want to receive confirmation my account has been deactivated_**
- When a user deactivates their account they are sent and email confirming the account has been deactivated.

### **Superuser**
**_I want to be able to access the admin panel_**
- Users wih superuser credentials can access the admin panel through the admin link under the *My Account* dropdown in the header.

**_I want to be able to add/edit/delete categories_**
- Superusers can add/edit/delete categories under the *Products* tab in the admin panel

**_I want to ba able to add/edit/delete subcategories_**
- Superusers can add/edit/delete subcategories under the *Products* tab in the admin panel

**_I want to be able to add new products_**
- Superusers can add new products by accessing the *Product Management* page under the *My Account* dropdown in the header
- Or under the *Products* tab in the admin panel

**_I want to be able to edit/delete existing products_**
- Superusers have edit and delete links available to them on each product which can be used to edit or delete products
- Or under the *Products* tab in the admin panel

**_I want to be able to add new blog posts_**
- Superusers can add new products by accessing the *Blog Management* page under the *My Account* dropdown in the header
- Or under the *Blog* tab in the admin panel

**_I want to be able to edit/delete existing blog posts_**
- Superusers have edit and delete links available to them on each blogpost which can be used to edit or delete posts
- Or under the *Blog* tab in the admin panel

**_I want to be able to view/manage users of the site_**
- Superusers can view/manage users of the site in the users section under the *Authentication and Authorization* tab in the admin panel 
    
**_I want to be able to view/manage messages from users_**
- Superusers can view/manage messages to the site in the messages section under the *Contact* tab in the admin panel 

**_I want to be able to view/manage newsletter subscriptions_**
- Superusers can view/manage newsletter subscriptions to the site in the newsletter subscription section under the *Contact* tab in the admin panel 

**_I want to be able to view/manage orders_**
 - Superusers can view/manage orders to the site in the orders section under the *Checkout* tab in the admin panel  


#### [**Table of Contents**](#table-of-contents)
---

## **Manual Testing**
 Each element was tested both locally and on the live site to ensure it was working correctly.  
 Testing on functionality was carried out throughout the build using 
 [DevTools](https://developers.google.com/web/tools/chrome-devtools) to ensure everything worked as it should and to identify
 issues/bugs.

### **Site Wide** 
#### **Header**
 - **_Navbar_** is fixed to top of the viewport when scrolling down
    - Each link was clicked to ensure it directed user to correct page or triggers the dropdown - which ever is applicable
    - Each link changes colour on hover
    - Hovering over a link previews the dropdown of categories/subcategories(if any)
    - Clicking on an item in the dropdown redirects user to the relevant page
    - Hovering over an item in the dropdown highlights that item
 - **_Nav brand logo_** clicked to ensure it returns user to index.html
 - **_Access_**:
    - *Anonymus user* only has access to relevant links:
        - In the main nav:
            - 'All Products', 'Clothing', 'Footwear', 'Swimwear', 'Accessories', 'Blog'
        - In the header: 
            - Under *My Account*: 'Login', 'Register'
            - Shopping Bag
            - Contact
    - *Registered user* only has access to relevant links:
        - In the main nav:
            - As above
        - In the header:
            - Under *My Account*: 'My Profile', 'Logout'
            - Shopping Bag
            - Contact
    - *Superuser* has full access:
        - Under *My Account*: 'Admin', 'Blog Management', 'Product Management, 'My Profile', 'Logout'
- **_Hamburger icon_** is visible on small devices
    - Clicking Hamburger triggers dropdown
    - Links behave as they do in the main navbar
- **_Search box_** (only visible on larger devices):
    - Allows users to filter products by words found in the product name and description, category/subcategory name
    - **_Search icon_** on device size medium and smaller opens the search box that allows users to filter searches.
    - Performing a search with out entering a query triggers a toast error message informing the user they have not entered any search criteria
- **_My Account Icon_** 
    - Previews the dropdown on hover
    - Visible links depend on the type of user
    - Clicking the icon triggers the dropdown
    - Hovering over a link highlights it
    - Each link redirects to the correct page
- **_Shopping Bag Icon_**:
    - Displays the current bag total
    - Redirects user to the *Shopping bag* page
- **_Contact icon_** is only visible on larger devices
    - Redirects user to contact page
    - On smaller devices a link can be found in the sidebar
- **_Delivery Banner_** is visible across the site

#### **Footer**
- Visible across the site at all device sizes
- **_Newsletter Setion_**:
    - A valid email address must be added to the form to submit it
    - If the form is not valid the user is informed
    - If the form is valid: 
        - and the users clicks the *Sign Up* button that email address will be added to the newsletter mailing list if it does not aleady exist in the database
        - If the email address does not exist a toast success message is triggered informing the user they have been added to the mailing list
        - A confirmation email is sent to that email address informing the user they have signed up for the newsletter and includes a link they can follow if they wish to unsubscribe
        - If the email address does exist a toast error message is triggered informing the user that that email address already exists in the database 
    - **_Sign Up Button_**:
        - Changes colour on hover
        - Submits the form if it is valid
        - Refreshes the page 
    - **_Unsubscribe Links_**:
        - The words *unsubsrcibe* and *here* in the text below the *Sign Up* button redirect the user to the *Unsubscribe Page*
- **_Social Media Section_**:
    - Each of the social media icons redirect the user to those sites (sign up pages as pages don't exist for this site)
    - Icons grow when hovered over
    - The envelope icon redirects the user to the contact page  

### **Home App**
- **_Shop Now_** button 
    - Redirects the user to the *All Products* page when clicked
    - Changes colour on hover  

### **Products App**
#### **All Products/Category/Subcategory Pages**:
- **_Category/Subcategory Carousel_**:
    - Set to wraparound and auto rotate
    - Carousel arrows can be used to move the carousel left or right
    - Each cell is a link to that category/subcategory
    - When clicked user is redirected to that page
    - Only visible on medium or larger devices
- **_Page Title_**:
    - Displays the name of the current page
- **_Breadcrumbs_**:
    - Visible when **_not_** on *All Products* page
    - Identifies the current page and any parents of that page
    - Parent links are bold and underlined on hover
    - When clicked returns user to that page
- **_Category Badges_**:
    - A category badge is created for each related child category or subcategory of the current page
    - The category or subcategory of that page is identified by the name of the badge
    - Clicking on a badge will redirect the user to that category/subcategory
    - Category badges change colour on hover
- **_Product Count_**:
    - Displays the product count for that page. 
    - If **_not_** on *All Products* page also displays a *Back to all products* link
    - When clicked this link returns the user to the *All Products* page
    - Link is bold and underlined on hover
- **_Sort By Box_**:
    - Allows users to sort products by defined criteria
    - Clicking the arrows triggers the dropdown displaying available sort criteria
    - Clicking on a sort option will sort the products into that criteria
- **_Product Cards_**:
    - Grows on hover
    - Each card displays the product image, name and price
    - Clicking on a product card image redirects user to the *Product Detail* page for that product
    - If user is **_Superuser_** *Edit* and *Delete* links are visible
    - Clicking the *Edit* link redirects superuser to the *Edit Product* page
    - A toast info message is triggered informing the superuser of what product they are editing
    - Clicking the *Delete* link triggers a *Confirm Delete* modal
        - Identifies the product that will be deleted
        - **_Cancel Button_**
            - Cancels action, closes modal
        - **_Delete Button_**
            - Deletes the product
    - A toast info message is triggered informing the superuser of the product that has been deleted.
- **_Scroll Button_**:
    - Appears when the user scrolls down 100px from the top of the page.
    - When clicked returns the user to the top of the page.
    - Changes colour on hover

#### **Product Detail Page**:
- **_Breadcrumbs_**:
    - Identifies the current product and any parents of that product
    - Parent links are bold and underlined on hover
    - When clicked returns user to that page
- **_Product Image_**:
    - Grows on hover
    - Opens the image url on a new page when clicked
- **_Heart Icon_**:
    - Pulses on hover
    - Triggers tooltip on hover with "Add to Favourites" or "Remove from Favourites" depending on current state.
        - Outline icon - Not a Favourite
        - Solid icon - Is a Favourite
    - Clicking the icon:
        - If the user **_is_** logged in: 
            - Clicking the icon will add that product to their favourites if it is not there already
            - Toast success message is triggered informing the user that that product has been added to their favourites 
            - Includes a link to view their favourites
            - Clicking the link redirects user to their profile page
            - Turns the icon solid
            - If the icon is solid it indicates that the product is already a favourite of the user 
            - Clicking it will remove that product from their favourites
            - Toast success message is triggered informing the user that the product has been removed from their favourites
            - Returns the icon to outline
        - If the user in **_not_** logged in:
            - Clicking on the icon triggers a toast error message informing the user that they must be logged in to save a product and includes links to sign in or sign up
            - Sign in/up links redirects user to relevant page when clicked
- **_Category/Subcategory Tags_**:
    - Identifies which category/subcategory that product belongs to
    - Each tag is a link that when clicked redirects user back to that category/subcategory
    - Each link is bold and underlined on hover
- **_Edit/Delete_** Links:
    - If user is **_Superuser_** *Edit* and *Delete* links are visible
    - Clicking the *Edit* link redirects superuser to the *Edit Product* page
    - A toast info message is triggered informing the superuser of what product they are editing
    - Clicking the *Delete* link triggers a *Confirm Delete* modal
        - Identifies the product that will be deleted
        - **_Cancel Button_**
            - Cancels action, closes modal
        - **_Delete Button_**
            - Deletes the product
    - A toast info message is triggered informing the superuser of the product that has been deleted.
    - Edit/delete links are bold on hover
- **_Size Select Box_**:
    - Only visible on products with sizes
    - Differents size box options for clothing and footwear
    - Allows users to choose a desired size from the options available
    - Clicking the arrow triggers a dropdown of available sizes
- **_Quantity Select Box_**:
    - Allows users to select a quantity for the current product
    - Quantity can be increased or decreased using the plus or minus buttons within the set range (1 -99)
    - Minus button is disabled if quantity is 1
    - Plus button is disabled if quantity is 99
    - Quantity can also be adjusted by entering a numeric value in the box
    - If the quantity selected is outside the set range the user is informed that the qty must be between 1 and 99
- **_Keep Shopping Button_**:
    - Redirects user back to *All Products* page
    - Changes colour on hover
- **_Add to Bag Button_**:
    - Clicking adds the current product along with the size and qty selected to the bag
    - Triggers a toast success message: 
        - informing the user that the product has been added to the bag including the product name, size and quantity.
        - Includes a *Go To Secure Checkout* Button which brings users to the *Checkout* page when clicked
        - If *Delivery Delta* is not reached it informs the user of how much more they need to spend to reach that threshold.
        - If there are additional products in the bag a summary of all bag items is visible
    - Changes colour on hover
- **_Random Product Carousel_**:
    - Set to wraparound and auto rotate
    - Carousel arrows can be used to move the carousel left or right
    - A generated list of 7 random products
    - Each cell contains product image, name and price
    - Each cell is a link to that product
    - Clicking on a cell redirects user to the *Product Detail* Page of that product 
    - Only visible on medium or larger devices 

#### **Add Product Page**:
- Only accessible to superuser through the Product Management Link under the My Account icon in the header
- Contains a form to add a product
- Required inputs are marked with a *
- Box shadow of active input field changes colour - from pink to black
- **_Category Input_** is a dropdown with the list of categories available to choose from
    - Clicking the arrow triggers the dropdown
    - Category names displayed are *friendly names*
- **_Subcategory Input_** is a dropdown with the list of subcategories available to choose from
    - Clicking the arrow triggers the dropdown
    - Subcategory names displayed are *friendly names*
- **_Has Sizes Input_** is a dropdown with options to select if a product has sizes or not
    - Clicking the arrow triggers the drop down
- **_Select Image Button_**:
    - Allows users to select an image to be added
    - When a image is selected the user is informed of what the image will be set to
    - If no image is selected the default image will be added
- **_Cancel Button_**:
    - Cancels the action
    - Returns user to the *All Products* Page
- **_Add Product Button_**:
    - If the form is **_valid_**:
        - Product will be added to the database
        - Product will be displayed on all products and relevant category/subcategory pages
        - Toast success message triggered informing the user that that product has been added
        - Loads that product detail page
    - If the form is **_invalid_**: 
        - It will not be submitted and user will be directed to the incorrect input to correct the form
        - Triggers toast error message informing the user that the form is invalid
- If user tries to access via the url:
    - View is secured by @login required decorator which redirects any user not logged in back to the Sign In page
    - If user is logged in but not superuser 
        - Toast error message is triggered informing the user only store owners can do that 
        - User is redirected to the home page

#### **Edit Product Page**:
- Only accessible to superuser through the *edit* link on the product cards or product detail page
- Toast info message is triggered informing the user what product they are editing
- Contains a form to edit the product on which the link was clicked
- Form is pre populated with the details of that product
- Box shadow of active input field changes colour - from pink to black
- Thumbnail of the current image is visible
- Ticking the remove checkbox will remove that image
- The *Select Image* Button allows the user to select a new image
- It is not necessary to check the remove checkbox if the image is being replaced, only if the image is being removed completely and not being set to a new image
- The image will then be set to the default image
- **_Cancel Button_** cancels the action and returns user to the *All Products* page
- **_Update Button_**:
    - If the form is **_valid_**:
        - Product will be updated
        - Toast success message triggered informing the user that that product has been updated
        - Loads that product detail page
    - If the form is **_invalid_**: 
        - It will not be submitted and user will be directed to the incorrect input to correct the form
- If user tries to access via the url:
    - View is secured by @login required decorator which redirects any user not logged in back to the Sign In page
    - If user is logged in but not superuser 
        - Toast error message is triggered informing the user only store owners can do that 
        - User is redirected to the home page

#### **Delete Product**:
- Only accessible to superuser through the *delete link on the product cards or product detail page
- Clicking the *Delete* link triggers a *Confirm Delete* modal
        - Identifies the product that will be deleted
        - **_Cancel Button_**
            - Cancels action, closes modal
        - **_Delete Button_**
            - Deletes the product
- A toast success message is triggered informing the user of the product that was deleted
- If user tries to access delete via the url:
    - View is secured by @login required decorator which redirects any user not logged in back to the Sign In page
    - If user is logged in but not superuser 
        - Toast error message is triggered informing the user only store owners can do that 
        - User is redirected to the home page

### **Bag App**
- Accessible to all users by clicking the shopping bag icon
- Current bag total is visible below the bag icon across the site
- Total is updated as items are added/removed from the bag
- If bag is empty user is informed that the bag is empty 
- **_Keep Shopping_** Button is visible which redirects users to *All Products* page
- If there are items in the bag the info for each product is displayed including, image, name, sku, price and qty
- **_Quantity box_**: 
    - Allows users to adjust the quantity of that product from the shopping bag page
    - Quantity can be increased or decreased using the plus or minus buttons within the set range (1 -99)
    - Minus button is disabled if quantity is 1
    - Plus button is disabled if quantity is 99
    - Quantity can also be adjusted by entering a numeric value in the box
    - If the quantity selected is outside the set range the user is informed that the qty must be between 1 and 99
    - Clicking the *Update Qty* link below the qty box will:
        - Adjust the qty of that product in the bag 
        - Adjust the product subtotal and bag total automatically
    - Clicking the *Remove* link will:
        - Remove the product from the bag completely - regardless of the qty selected
        - Same products with different sizes will not be affected
        - Adjusts the bag total automatically
- **_Subtotal_**:
    - Subtotal is automatically adjusted as the product qty is adjusted.
- **_Free Delivery Delta_**:
    - If the current bag total is below the *Free Delivery Delta* the amount the user needs to spend to meet the free delivery criteria is displayed below the *Grand Total*
- **_Bag Totals_**:
    - All totals are updated automatically as the bag contents is adjusted.
- **_Keep Shopping Button_**:
    - Redirects user back to *All Products* page
    - Changes colour on hover
- **_Secure Checkout Button_**:
    - Redirects user to the *Checkout* Page
    - Changes colour on hover
- **_Category/Subcategory Carousel_**:
    - Set to wraparound and auto rotate
    - Carousel arrows can be used to move the carousel left or right
    - Each cell is a link to that category/subcategory
    - When clicked user is redirected to that page
    - Only visible on medium or larger devices

### **Checkout App**
#### **Checkout Page**:
- Order summary of the current bag items is displayed including:
    - Bag items count
    - Image, name, size, price, qty and subtotal for each item in the bag
    - Order total, delivery cost and grand total
- **_Details Form_**:
    - Placeholders for each input field inform the user of what information is expected for each field
    - Auto focus is on the first field
    - Box shadow of active input field changes colour - from pink to black
    - Required inputs are marked with a *
    - If it is the first time a registered user is making a purchase or an anonymus user is making a purchase are fields are empty
    - If a logged in user is making a purchase and has previously saved delivery details the form will be populate with those details
    - If the user is anonymous there is a link below the delivery details inviting them to create an account or login if they wish to save their details
        - The *log in* link redirects to the sign in page
        - The *create account* link redirects to the sign up page
        - Both links are bold and underlined on hover
    - If the user is logged in there is a checkbox below the delivery details form that can be checked if they wish to save those details
        - If the box is checked those details are saved and displayed on the users profile page under the *Delivery Info* tab
        - This check box is checked by default
        - If the box is unchecked the details will not be saved
- **_Credit Card Form_**:
    - If the card number entered is invalid user is informed
- **_Adjust Bag Button_**:
    - Redirects user back to the shopping bag page
- **_Complete Order Button_**:
    - If Form is **_valid_**:
        - Loading spinner appears while payment is being processed
        - User is redirect to *Chekout Success* page
        - Toast success message is triggered informing the user that the order was successfully processed
            - It includes the order number - which is unique and automatically generated for each order
            - Also informs the user that a confirmation email will be sent to the email address provided in the form
        - A confirmation email is sent to the email address provided in the form which includes all the details of the order
    - If Form is **_invalid_**:
        - User is directed to the field the needs to be corrected
- Text beneath the buttons informs the user of how much their card will be charged.
- **_Webhooks_**:
    - Ensures that orders are captured and processed if the browser is closed unexpectedly
    - That confirmation email is sent

#### **Checkout Success Page**
- Toast success message is triggered informing the user that the order was successfully processed
    - It includes the order number - which is unique and automatically generated for each order
    - Also informs the user that a confirmation email will be sent to the email address provided in the form
- All the order details are displayed on the page including: 
    - order number, date 
    - item details - name, size, qty, price
    - delivery details
    - totals
- A confirmation email is sent to the email address provided in the form which includes all the details of the order
- **_Find Your Next Love Button_**:
    - Redirects user to the *All Products* page

### **Profiles App**
- A personal profile is automatically created when a user registers and verfies their emaill address
- Is accessible to logged in users via the *My Account* dropdown
- Title displays the users username
- The *Profile Page* consists of 4 tabs
    - My Favourites
    - Order History
    - Delivery Info
    - Deactivate Account
- Each tab can be accessed by using the tab buttons
    - Tab buttons change colour on hover
    - Active button is a different colour 
- **_My Favourites Tab_**
    - If user has no favourites saved:
        - Heading is displayed with the text *You haven't saved anything to your favourites*
        - **_Find Favourites button_**
            - Redirects user to the *All Products* page
            - Changes colour on hover
    - If user has saved products to their favourites:
        - **_Keep Shopping Button_**
            - Redirects user to the *All Products* page
            - Changes colour on hover
        - Each saved product is displayed as it is on the *Product Detail* Page
        - **_Heart Icon_**:
            - Pulses on hover
            - Triggers tooltip on hover with "Remove from Favourites" 
            - Icon is solid denoting that it is a favourite
            - Clicking the icon:
                - Clicking the icon will remove that product to their favourites 
                - Toast success message is triggered informing the user that that product has been removed from their favourites 
        - **_Category/Subcategory Tags_**
            - Identifies which category/subcategory that product belongs to
            - Each tag is a link that when clicked redirects user back to that category/subcategory page
            - Each link is underlined on hover
        - **_Size Select Box_**:
            - Only visible on products with sizes
            - Allows users to choose a desired size from the options available
            - Clicking the arrow triggers a dropdown of available sizes
        - **_Quantity Select Box_**:
            - Allows users to select a quantity for the current product
            - Quantity can be increased or decreased using the plus or minus buttons within the set range (1 -99)
            - Minus button is disabled if quantity is 1
            - Plus button is disabled if quantity is 99
            - Quantity can also be adjusted by entering a numeric value in the box
            - If the quantity selected is outside the set range the user is informed that the qty must be between 1 and 99
        - **_Add to Bag Button_**:
            - Clicking adds the current product along with the size and qty selected to the bag
            - Triggers a toast success message: 
                - informing the user that the product has been added to the bag including the product name, size and quantity.
            - Changes colour on hover
- **_Order History Tab_**
    - If user has no previous orders:
        - Heading is displayed with the text *You haven't placed any orders*
        - **_Go shopping button_**
            - Redirects user to the *All Products* page
            - Changes colour on hover
    - If user has placed orders before the order details are displayed here including:
        - Orders are displayed by the most recent first
        - **_Order Number_**
            - When clicked user is redirected to the checkout success page of that order and the order details are displayed
            - Toast info message is triggered informing the user that this is a past order confirmation and includes the order number for that order
            - **_Back to Profile Button_**
                - Redirects the user back to the *Profile Page*
                - Changes colour on hover
        - Date, items, qty, sizes and the order total
- **_Delivery Info Tab_**
    - Contains the Default Delivery info form
    - Box shadow of active input field changes colour - from pink to black
    - Placeholders for each input field inform the user of what information is expected for each field
    - If user has previously saved delivery info either on the checkout page or by updating the form the form is pre populated with that info
    - If user has not previously saved delivery info the form will be empty
    - User can update/save the info in the form by filling out the details and clicking the *update information* button
    - **_Update Information Button_**
        - Updates the delivery info of the user
        - Triggers a Toast success message informing the user their information has been updated
        - Changes colour on hover
- **_Deactivate Account Tab_**  
    - Contains a button which allows users to deactivate their account
    - Clicking the deactivate account button will trigger a modal asking the user to confirm they want to deactivate their account
        - Close button cancels the action and closes the modal
        - Clicking the deactivate account button will deactivate the account
    - Deactivated users will no longer be able to sign in or view their profile
    - Confirmation email is sent to the user informing them their account has been deactivated
    - Users are redirected to the *All Products Page*
    - **_here link_**
        - Redirects user to the *Contact* page
        - Is bold on hover
- **_Scroll Button_**:
    - Appears when the user scrolls down 100px from the top of the page.
    - When clicked returns the user to the top of the page.
    - Changes colour on hover

### **Contact App**
#### **Contact Page**
- Is accessible to all users
- Contains a message form to contact the store
- Box shadow of active input field changes colour - from pink to black
- Placeholders for each input field inform the user of what information is expected for each field
- All fields are required
- If form is **_valid_**:
    - Message is sent to the store
    - Triggers toast success message informing the user that the message has been sent.
    - Confirmation email is sent to the email address provided confirming that the message has been received
    - Refreshes the Page
- If form is **_invalid_**:
    - User is directed to the invalid field to correct the error
- If form fails to send toast error message is triggered informing the user the message failed.

#### **Newsletter Signup**
- Newsletter sign up was tested as part of the footer. 
- Testing can be found [here](#footer)

#### **Newsletter Unsubscribe Page**
- Can be accessed by all users by clicking the links in the footer
- Can be accessed via the link in the sign up confirmation email
- If an invalid email address format is entered useris informed
- If a vaild email address that exists in the database is entered:
    - Toast success message is triggered informing the user their email address has been removed from the mailing list
    - A confirmation email is sent informing the user they have been unsubscribed from the mailing list and will no longer receive newsletter emails
    - Page is refreshed
- If a valid email address is entered that does not exist in the database:
    - Toast error message is triggered informing the user that that email address does not exist in our database
    - Page is refreshed
- **_Cancel Button_**
    - Cancels the action
    - Refreshes the page
- **_Send Button_**
    - Sends the message if the form is valid
    - Directs the user to the incorrect field if form is invalid
- **_here link_**
    - Redirects user to the *Contact* page  

### **Blog App**
#### **Main Blog Page**
- **_here link_**
    - Redirects user to the *Contact* page  
- **_BlogPost_**
    - Blogposts are ordered by most recent first
- **_layout_** 
    - Depends on whether blogpost has an image or not
- **_Edit/Delete_** Links:
    - If user is **_Superuser_** *Edit* and *Delete* links are visible
    - Clicking the *Edit* link redirects superuser to the *Edit Blog* page
    - A toast info message is triggered informing the superuser of what Blogpost they are editing
    - Clicking the *Delete* link triggers a *Confirm Delete* modal
        - Identifies the Post that will be deleted
        - **_Cancel Button_**
            - Cancels action, closes modal
        - **_Delete Button_**
            - Deletes the post
    - A toast info message is triggered informing the superuser of the blogpost that has been deleted.
    - Edit/delete links are bold on hover
- **_Read More Button_**
    - Redirects user to the Blogpost detail page for that post
- If post is not original content:
    - Orignal Author is credited with a link to the original article
    - **_Original Article Link_**
        - Opens the original article in a new page
    - Origin of the post is credited and when clicked opens the origin site in a new page
- **_Scroll Button_**:
    - Appears when the user scrolls down 100px from the top of the page.
    - When clicked returns the user to the top of the page.
    - Changes colour on hover

#### **Blog Detail Page**
- Displays the full blog post
- **_Edit/Delete_** Links:
    - If user is **_Superuser_** *Edit* and *Delete* links are visible
    - Clicking the *Edit* link redirects superuser to the *Edit Blog* page
    - A toast info message is triggered informing the superuser of what Blogpost they are editing
    - Clicking the *Delete* link triggers a *Confirm Delete* modal
        - Identifies the Post that will be deleted
        - **_Cancel Button_**
            - Cancels action, closes modal
        - **_Delete Button_**
            - Deletes the post
    - A toast info message is triggered informing the superuser of the blogpost that has been deleted.
    - Edit/delete links are bold on hover
- **_Back to Blog Button_**
    - Returns user to the main blog page
    - Changes colour on hover
- If not original content:
    - **_Read Full Article Button_**
        - Opens the original article in a new page
        - Changes colour on hover

#### **Add Blogpost Page**:
- Only accessible to superuser through the Blog Management Link under the My Account icon in the header
- Contains a form to add a blogpost
- Required inputs are marked with a *
- Box shadow of active input field changes colour - from pink to black
- **_Select Image Button_**:
    - Allows users to select an image to be added
    - When a image is selected the user is informed of what the image will be set to
    - There is no default image for blogposts
- **_Cancel Button_**:
    - Cancels the action
    - Returns user to the *Blog* Page
- **_Add Post Button_**:
    - If the form is **_valid_**:
        - Blogpost will be added to the database
        - And displayed on the Blog/Blog details pages
        - Toast success message triggered informing the user that that blogpost has been added
        - Loads that blog detail page
    - If the form is **_invalid_**: 
        - It will not be submitted and user will be directed to the incorrect input to correct the form
        - Triggers toast error message informing the user that the form is invalid
- If user tries to access via the url:
    - View is secured by @login required decorator which redirects any user not logged in back to the Sign In page
    - If user is logged in but not superuser 
        - Toast error message is triggered informing the user only store owners can do that 
        - User is redirected to the home page

#### **Edit Blog Page**
- Only accessible to superuser through the *edit* link on the blog/blogpost pages
- Toast info message is triggered informing the user what blogpost they are editing
- Contains a form to edit the blogpost on which the link was clicked
- Form is pre populated with the details of that blogpost
- Box shadow of active input field changes colour - from pink to black
- Thumbnail of the current image is visible
- Ticking the remove checkbox will remove that image
- The *Select Image* Button allows the user to select a new image
- It is not necessary to check the remove checkbox if the image is being replaced, only if the image is being removed completely and not being set to a new image
- The image will then be set to the default image
- **_Cancel Button_** cancels the action and returns user to the *Blog* page
- **_Update Button_**:
    - If the form is **_valid_**:
        - Blogpost will be updated
        - Toast success message triggered informing the user that the blogpsot has been updated
        - Loads that blogpost detail page
    - If the form is **_invalid_**: 
        - It will not be submitted and user will be directed to the incorrect input to correct the form
- If user tries to access via the url:
    - View is secured by @login required decorator which redirects any user not logged in back to the Sign In page
    - If user is logged in but not superuser 
        - Toast error message is triggered informing the user only store owners can do that 
        - User is redirected to the home page

#### **Delete Blogpost**:
- Only accessible to superuser through the *delete link on the blog or blog detail page
- Clicking the *Delete* link triggers a *Confirm Delete* modal
        - Identifies the Post that will be deleted
        - **_Cancel Button_**
            - Cancels action, closes modal
        - **_Delete Button_**
            - Deletes the post
- A toast success message is triggered informing the user of the blogpost that was deleted
- If user tries to access delete via the url:
    - View is secured by @login required decorator which redirects any user not logged in back to the Sign In page
    - If user is logged in but not superuser 
        - Toast error message is triggered informing the user only store owners can do that 
        - User is redirected to the home page

### **Authentication and Authorization**
#### **Sign In Page**
- Accessisble to all logged out users via the *My Account* dropdown
- **_Sign up here link_**
    - Redirects users to the Register page
    - Is bold on hover
- **_Sign In Form_**
    - Registered users have the option to sign in using their Username and Password
    - If Sign in form is **_invalid_**:
        - User is informed that username and/or password are incorrect
    - If sign in form is **_valid_**:
        - User is redirected to *Home Page*
        - Toast success message is triggered informing the user they have successfully signed in
- **_Remember Me Checkbox_**
    - If checkbox is checked sign in details will be saved
- **_Home Button_**
    - Redirects user to the *Home Page* without signing them in
    - Changes colour on hover
- **_Sign in Button_**
    - If form is valid - signs user into the site
    - Redirects user to *Home Page*
    - Changes colour on hover
- **_Forgot Password Link_**
    - Redirects user to the *Password Reset* page 
    - Is bold on hover
- Users also have the option to sign in using Google or Facebook.
    - **_Log in with Facebook Button_**
        - Redirects user to Facebook Login
        - Changes colour on hover
    - **_Log in with Google Button_**
        - Redirects user to Google login
        - Changes colour on hover 
- **_Random Product Carousel_**:
    - Set to wraparound and auto rotate
    - Carousel arrows can be used to move the carousel left or right
    - A generated list of 7 random products
    - Each cell contains product image, name and price
    - Each cell is a link to that product
    - Clicking on a cell redirects user to the *Product Detail* Page of that product  
    - Only visible on medium or larger devices

#### **Sign Out Page**
- Accessisble to logged users via the *My Account* dropdown
- **_Cancel Button_**
    - Redirects user to *All Products* page without logging them out
    - Changes colour on hover
- **_Sign Out Button_**
    - Signs user out of the site
    - Triggers a toast success message informing the user they have been signed out
    - Redirects user to *Home Page*
    - Changes colour on hover
- **_Random Product Carousel_**:
    - Set to wraparound and auto rotate
    - Carousel arrows can be used to move the carousel left or right
    - A generated list of 7 random products
    - Each cell contains product image, name and price
    - Each cell is a link to that product
    - Clicking on a cell redirects user to the *Product Detail* Page of that product  
    - Only visible on medium or larger devices

#### **Register Page**
- Accessisble to logged out users via the *My Account* dropdown
- **_sign in link_**
    - Redirects user to *Sign In* page
    - Is bold on hover
- **_Register Form_**
    - Box shadow of active input field changes colour - from pink to black 
    - Placeholders for each input field inform the user of what information is expected for each field
- If form is **_invalid_**:
    - User is directed to the incorrect field to correct any errors in the form
- If form is **_valid_**:
    - User is redirected to *Verify Email* page
    - Toast info message is triggered informing the user that a confirmation email has been sent to the email address provided
- Registration is not complete until email address is verified
- Users cannot sign in until they have verified their email address
- **_Sign Up Button_**
    - Submits a valid form
    - Changes colour on hover
- **_Back to login Button_**
    - Redirects user back to Sign in Page
    - Changes colour on hover
- **_Random Product Carousel_**:
    - Set to wraparound and auto rotate
    - Carousel arrows can be used to move the carousel left or right
    - A generated list of 7 random products
    - Each cell contains product image, name and price
    - Each cell is a link to that product
    - Clicking on a cell redirects user to the *Product Detail* Page of that product
    - Only visible on medium or larger devices

## **Responsive Design**
The app was developed using the _Mobile First_ philosophy.

Responsive design was tested throughout the build using [DevTools](https://developers.google.com/web/tools/chrome-devtools)
and [Am I Responsive](http://ami.responsivedesign.is/).

[Bootstrap](https://getbootstrap.com/) grid was used for the structure to ensure responsiveness
at all breakpoints. [Bootstrap](https://getbootstrap.com/) classes, 
including `margin`, `padding`, `text-center`, `display` and `float` were used to adjust HTML structure for various device sizes.
In addition media queries were used to tweak font-sizes, margins, padding and alignment.

#### **Browsers**
- Chrome 
- Edge
- Firefox
- Safari

#### **Screen Sizes**
Using [DevTools](https://developers.google.com/web/tools/chrome-devtools) profiles:
- Moto G4
- Galaxy S5
- Pixel 2/ 2XL
- iPhone 5/SE
- iPhone 6/7/8 
- iPhone 6/7/8 Plus 
- iPhone X 
- iPad / Pro 
- Surface Duo
- Galaxy  Fold

Using [DevTools](https://developers.google.com/web/tools/chrome-devtools) responsive profiles:
- Mobile S - 320px
- Mobile M - 375px
- Mobile L - 425px
- Tablet - 768px
- Laptop - 1024px
- Destop - 1440px

 It was also tested physically on various devices including:
 - Hauwei P20 Pro
 - Galaxy A6
 - HP Pavilion Laptop 

#### [**Table of Contents**](#table-of-contents)
---
## **Automated Testing**
- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) - to validate HTML
    - All errors thrown were related to templating
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) - to vaildate CSS Code
    - no errors found
- [JShint](https://jshint.com/) - to validate Javascript code
    - no errors found
- [PEP8 Online](http://pep8online.com/) 
    - 4 errors relating to file paths that are too long. 
- [Python Checker](https://www.pythonchecker.com/) - no errors found
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) - no overflow detected
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) - generated the below reports:

#### **Home App**
**Home Page**
- **Desktop**
    - Performance: 88
    - Accessiblity: 84
    - Best Practices: 93
    - SEO: 89
- **Mobile**
    - Performance: 63
    - Accessiblity: 86
    - Best Practices: 93
    - SEO: 91

#### **Products App**
**All Products Page**
- **Desktop**
    - Performance: 62
    - Accessiblity: 81
    - Best Practices: 93
    - SEO: 80
- **Mobile**
    - Performance: 45
    - Accessiblity: 83
    - Best Practices: 87
    - SEO: 83

**Product Detail Page**
- **Desktop**
    - Performance: 96
    - Accessiblity: 73
    - Best Practices: 93
    - SEO: 90
- **Mobile**
    - Performance: 56
    - Accessiblity: 78
    - Best Practices: 87
    - SEO: 92

**Edit/Add BlogPost Page**
- There were issues affectin the run of lighthouse on this page as it was redirected to the sign in page

#### **Bag App**
**Shopping Bag Page**
- **Desktop**
    - Performance: 70
    - Accessiblity: 81
    - Best Practices: 93
    - SEO: 80
- **Mobile**
    - Performance: 68
    - Accessiblity: 81
    - Best Practices: 93
    - SEO: 82

#### **Checkout App**
- There were issues affectin the run of lighthouse on this page as it was redirected to the products page

#### **Blog App**
**Blog Page**
- **Desktop**
    - Performance: 97
    - Accessiblity: 83
    - Best Practices: 93
    - SEO: 80
- **Mobile**
    - Performance: 69
    - Accessiblity: 83
    - Best Practices: 93
    - SEO: 83
    
**Blog Detail Page**
- **Desktop**
    - Performance: 85
    - Accessiblity: 83
    - Best Practices: 93
    - SEO: 80
- **Mobile**
    - Performance: 67
    - Accessiblity: 83
    - Best Practices: 93
    - SEO: 83

**Edit/Add BlogPost Page**
- There were issues affectin the run of lighthouse on this page as it was redirected to the sign page

#### **Contact App**
**Contact Page**
- **Desktop**
    - Performance: 97
    - Accessiblity: 79
    - Best Practices: 93
    - SEO: 89
- **Mobile**
    - Performance: 73
    - Accessiblity: 79
    - Best Practices: 93
    - SEO: 91

**Newsletter Unsubscribe Page**
- **Desktop**
    - Performance: 95
    - Accessiblity: 79
    - Best Practices: 93
    - SEO: 89
- **Mobile**
    - Performance: 63
    - Accessiblity: 79
    - Best Practices: 93
    - SEO: 91

#### **Profiles App**
- Lighthouse was unable to generate a report for this page

#### [**Table of Contents**](#table-of-contents)
---

## **Bugs and Issues**

### **Resolved**

**_issue_**:
- Subcategory names not displaying for categories on products pages

**_fix_**:
- Identify the subcategories related to each category
- Attach them to that category
- Needed a bigger query set:
```
       if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            subcategories = Subcategory.objects.filter(category__in=categories)
```

**_issue_**:
- Contact confirmation emails not pulling in template variables/ sender email address

**_fix_**:
- Needed to create an instance of the contact form to pull the relevant info
- Add the instance to the email
```
   instance = form.save()
    sender_email = instance.email
    subject = render_to_string(
        'contact/confirmation_emails/message_confirmation_subject.txt',
        {'instance': instance})
    body = render_to_string(
        'contact/confirmation_emails/message_confirmation_body.txt',
        {'instance': instance,
        'contact_email': settings.DEFAULT_FROM_EMAIL})
```
**_issue_**:
- This was only an issue in deployment
- Newsletter unsubscribe form throwing a ValueError `invalid email address`

**_fix_**: 
- *to_email* in send_mail function was wrapped in brackets.
- Removed the brackets and it worked fine
```
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        to_email,
            )
```
**_issue_**:
- Unable to add favourites to userprofile

**_fix_**:
- Needed to get all products then filter for favourites
```
    products = Product.objects.all()
    fav_products = products.filter(favourites=request.user)
    is_favourite = True
```
- Add fav_products to context

**_issue_**:
- View/function pattern error for favourite product view

**_fix_**:
- I was initially trying to return the product detail page which was throwing the error.
- Changed the return from render to HTTPResponsedirect  
`   return HttpResponseRedirect(request.META['HTTP_REFERER'])`

**_issue_**:
- +/- buttons not being disabled at 1 / 99 on the *Shopping Bag Page*
- After refreactoring the shopping bag there was 2 qty forms on the page and the javascript responsible for disabling the buttons was only picking up the first form

**_fix_**:
- Created a second qty form with unique id's and additional javascript to handle this form seperately.

**_issue_**:
- Although the +/- buttons were being disable outside of the set range the user could manaually enter a numeric value outside of the set range and add it to the bag.

**_fix_**:
- Added some javascript to enforce the 0 - 99 range, preventing the user from manaully entering anything about 99 into the input.
```
    $('.qty_input').keyup(function () {
        let qtyVal = $(this).val();
        if (qtyVal < 0 || qtyVal > 99 || qtyVal.length > 2) {
            $(this).val('');
            swal('Oops! Qty must be between 1-99', 'Please enter a valid quantity', 'error');
        } else {
            $(this).val(qtyVal);
        }
    });

    $('.update-qty').click(function() {
        let form = $(this).siblings('form.update-form');
        let qtyVal = parseInt($(form).find('.qty_input').val());
        if (/^([0-9]|[1-9][0-9])$/.test(qtyVal)) {
            form.submit();
        }
    });
```

#### [**Table of Contents**](#table-of-contents)
---
#### [Back to README.md](README.md)