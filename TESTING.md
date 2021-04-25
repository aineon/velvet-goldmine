#### [Back to README](README.md)

## **Testing**
### [**Table of Contents**](#table-of-contents)

- [User Stories](#user-stories)
    - [Anonymus User](#anonymus-user)
        - [General](#general)
        - [Products](#products)
        - [Shopping Bag](#shopping-bag)
        - [Checkout](#checkout)
        - [Contact](#contact)
        - [Blog](#blog)
        - [Create Account](#create-account)
    - [Registered User](#registered-user)
    - [Superuser](#superuser)
- [Manual Testing](#manual-testing) 
- [Responsiveness](#responsiveness)
- [Automated Testing](#automated-testing)
- [Bugs and Issues](#bugs-and-issues)
    - [Resolved](#resolved)
    - [Existing](#existing)

## **User Stories**
Each _user story_ was tested to ensure site meets user expectations.

**Anonymus User**: 

**General** :   
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

**Products**:   
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

**Shopping Bag**:  
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

**Checkout**  
**_I want to be able to checkout securely_**
- I receive clear errors if information has been entered incorrectly
- I credit card form follows common format

**_I want to recieve a confirmation of my order_**
- When an order has been processed successfully the user is redirected to the *Checkout Success* page where all the order details are displayed
- An email is also sent to the email address provided by the user on the *Checkout Page* with the full order details and delivery details

**_I want the confirmation of my order to include the details of my order_**
- When an order has been processed successfully the user is redirected to the *Checkout Success* page where all the order details are displayed
- An email is also sent to the email address provided by the user on the *Checkout Page* with the full order details and delivery details

**Contact**
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

**Blog**:
**_I want to understand the mission and values of the store_**
- The Intro on the blog page and the blog posts themselves help the user understand the mission of the store

**Create Account**:
**_I want to be able to create an account_**
- If a user wishes to create an account they can click on the user icon and click register
- They will be prompted to fill out the required information and informed of any errors in the form


**Registered User**:
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
- Registered users can update their delivery info by completing the form on the *Default Delviery Info* tab on their profile page
    - *I want to be able to deactivate my account*

**Superuser**:
    - *I want to be able to access the admin panel*
    - *I want to be able to add/edit/delete categories*
    - *I want to ba able to add/edit/delete subcategories*
    - *I want to be able to add new products*
    - *I want to be able to edit/delete existing products*
    - *I want to be able to add new blog posts*
    - *I want to be able to edit/delete existing blog posts*
    - *I want to be able to view/manage users of the site*
    - *I want to be able to view/manage messages from users*
    - *I want to be able to view/manage newsletter subscriptions*
    - *I want to be able to view/manage orders*  

## **Manual Testing**
 Each element was tested both locally and on the live site to ensure it was working correctly.  
 Testing on functionality was carried out throughout the build using 
 [DevTools](https://developers.google.com/web/tools/chrome-devtools) to ensure everything worked as it should and to identify
 issues/bugs.

## **Responsive Design**
The app was developed using the _Mobile First_ philosophy.

Responsive design was tested throughout the build using [DevTools](https://developers.google.com/web/tools/chrome-devtools)
and [Am I Responsive](http://ami.responsivedesign.is/).

[Bootstrap]() grid was used for the structure to ensure responsiveness
at all breakpoints. [Bootstrap]() classes, 
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
- Galaxy

Using [DevTools](https://developers.google.com/web/tools/chrome-devtools) responsive profiles:
- Mobile S - 320px
- Mobile M - 375px
- Mobile L - 425px
- Tablet - 768px
- Laptop - 1024px

 It was also tested physically on various devices including:
 - Hauwei P20 Pro
 - Galaxy A6
 - HP Pavilion Laptop 

#### [**Table of Contents**](#table-of-contents)
---
## **Automated Testing**
- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) - to validate HTML
    - All errors thrown were related to jinja templating
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) - to vaildate CSS Code
    - no errors found
- [JShint](https://jshint.com/) - to validate Javascript code
    - no errors found
- [PEP8 Online](http://pep8online.com/) 
    - no errors found
- [Python Checker](https://www.pythonchecker.com/) - no errors found
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) - no overflow detected
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) - generated the below reports:






## **Bugs and Issues**

### **Resolved**

**_issue_**:


**_fix_**:



Bugs



subcategory names not displaying for categories
- identify the sub categories related to each category
- attach them to that category
- needed a bigger query set


bug 

contact confirmation emails not pulling in template variables/ sender email address
needed to create an instance of the contact form to pull the relevant info

adding favourites to userprofile
needed to get all products then filter for favourites

view/function pattern error for favourite product view. change return from render to HTTPResponsedirect


#### [**Table of Contents**](#table-of-contents)
---
#### [Back to README.md](README.md)