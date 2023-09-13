# PP5-Prime-Pulse

![logo](https://res.cloudinary.com/dlulkctls/image/upload/v1689552890/readme-primepulse/banner_image_1_d9cue8.jpg)
# Prime Pulse Application


The Prime Pulse website is an e-commerce website that specializes in selling fitness equipment. The products listed on this website range from weights to cardio and everything in between. It is the one stop online shop for everything fitness related.


[Click here to access live project](https://prime-pulse-d780887a098c.herokuapp.com/)




## Table of Contents
1. [Screenshots](#screenshots)
2. [Design](#design)
    1. [ER Diagram](#er-diagram)
    2. [Design Elements Overview](#design-elements-overview)
3. [Features](#features)
    1. [Features Left to Implement](#features-left-to-implement)
4. [Marketing Strategy](#marketing-strategy)
5. [User Experience (UX)](#user-experience-(ux))
    1. [User stories](#user-stories)
5. [Security Features and Defensive Design](#security-features-and-defensive-design)
    - [User Authentication](#user-authentication)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
4. [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks - Libraries - Programs Used](#frameworks-libraries-programs-used)
5. [Testing](#testing)
    - [Validator Testing](#validator-testing)
6. [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
7. [Credits](#credits)

***

## Screenshots
---
### **Landing Page**

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/home_page_jqlbf4.png" alt="Landing Page" width="800"/>

### **Navigation Bar**
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/home_1_fkkxko.png" alt="Navigation Bar" width="1000"/>


### **Footer Section** 
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689573918/readme-primepulse/footer_e63eaz.png" alt="Navigation Bar" width="1000"/>

### **Sign Up Page** 
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/sign_up_sem3eo.png" alt="Sign Up" width="800"/>



### **Login Page**

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/sign_in_kc0oxs.png" alt="Login Page" width="800"/>


### **Store Page**

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/store_page_sdwpmj.png" alt="Store Page" width="800"/>


### **Product Page**

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/product_details_page_zbvly9.png" alt="Product Page" width="800"/>



### **Cart Page**
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/cart_iyhqbz.png" alt="Cart Page" width="800"/>



### **Billing Page**
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/billing_address_page_hkswlp.png" alt="Billing Address Page" width="800"/>

### **Review Page** 

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/review_page_wjdtoj.png" alt="Review Page" width="800"/>


### **Paypal Transaction Page** 
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/paypal_transaction_vum32d.png" alt="LandiPaypal Transactionng Page" width="800"/>



### **Signout Page** 
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/payment_success_m8nag9.png" alt="Payment successful Page" width="800"/>

### **User Dashboard Page** 

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/dashboard_main_bkealj.png" alt="User Dashboard Page" width="800"/>

### **Orders Page** 

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/dashboard_my_orders_zpgpjy.png" alt="Orders Page" width="800"/>

### **Edit Profile Page** 

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/dashboard_edit_profile_zeeeo1.png" alt="Edit Profile Page" width="800"/>

### **Change Password  Page** 

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/dashboard_change_password_fufnxy.png" alt="Change Password Page" width="800"/>

### **Facebook Page** 

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/facebook_1_b7esip.png" alt="Facebook Page" width="800"/>

[Back to Table of Contents ⇧](#table-of-contents)
## Design
### Wireframes
You can download the wireframes for this website from this link [GoogleDrive](https://drive.google.com/drive/folders/1eaRgxIO0XQZy-wFDHgE63b_CZdl32TG1?usp=drive_link).


<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454066/readme-primepulse/wireframes/Home_Page_rumz3j.png" alt="Home  Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Sign_Up_jf7i3f.png" alt="Sign Up Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Sign_In_pne7lv.png" alt="Sign In Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Item_Page_jnk4sa.png" alt="Item Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Cart_Page_ob4u8b.png" alt="Cart Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454066/readme-primepulse/wireframes/Dashboard_Page_xguatb.png" alt="Dashboard Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Edit_Profile_Page_hmyllb.png" alt="Edit Profile Page" width="500"/>



### ER Diagram

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694597163/readme-primepulse/ER_diagram_bnvttl.png" alt="ER Dagrame" width="1000"/>


This code defines the structure of a relational database using the Database Markup Language (DBML). Each table in the database is defined with its attributes, data types, constraints, and relationships. Here's a brief description of each table and its purpose:
---
**accounts** Table:
- Stores information about user accounts.
- Includes fields for first name, last name, username, email, phone number, and various status flags.
- Used for user authentication and management.

**user_profiles** Table:
- Contains additional user profile information.
- Includes fields for address details, profile picture, and location.

**carts** Table:
- Represents shopping carts used for e-commerce.
- Contains a unique cart identifier and the date it was added.

**cart_items** Table:
- Stores items within user shopping carts.
- Includes information such as user ID, product ID, quantity, and whether the item is active.

**categories** Table:
- Contains product categories.
- Includes fields for category name, slug, description, and an image path.

**payments** Table:
- Records payment transactions.
- Contains details such as user ID, payment ID, payment method, amount paid, and status.

**orders** Table:
- Represents customer orders.
- Includes fields for customer information, order details, and order status.

**order_products** Table:
- Stores individual products within customer orders.
- Contains information such as product ID, quantity, product price, and order status.

**products** Table:
- Contains product listings.
- Includes product name, description, price, stock, availability, and category.

**reviews** Table:
- Stores product reviews submitted by users.
- Contains fields for product ID, user ID, review details, rating, and status.

**Relationships**:
- Various relationships are established between tables using foreign keys, indicating how tables are connected.
- These relationships define how data is related, such as linking user profiles to user accounts, linking cart items to users and products, and connecting orders to users and payments.

Overall, this Database outlines the structure of a comprehensive e-commerce database (e.g PrimePulse), covering user accounts, shopping carts, products, orders, payments, categories, and reviews, along with their relationships and constraints.






### Design Elements Overview
**Colour Scheme**
* A soothing and warm purple and orange to invite the user. Complemented with white background and black and white text with blue buttons. 
**Typography**
* 'Segoe UI'
**Imagery**
* abstract large banner image with company logo in white.


[Back to Table of Contents ⇧](#table-of-contents)


## Features
---
- **Extensive Product Catalog:** Browse through a diverse selection of fitness equipment, including treadmills, dumbbells, exercise bikes, yoga mats, and more.
- **User Accounts:** Create an account and log in to access personalized features such as saving your wishlist, tracking orders, and managing your profile information.
- **Search Functionality:** Easily find specific products using the search feature, saving you time and effort.
- **Shopping Cart and Checkout:** Add desired products to your cart, review your items, and proceed to a secure checkout process for a seamless purchasing experience.
- **Secure Payments:** Enjoy peace of mind with secure online payment options, ensuring the safety and privacy of your financial information.
- **Order Tracking:** Receive email notifications and order confirmation with details about your purchase and delivery status.
- **Customer Support:** Reach out to our friendly customer support team through the contact form for assistance or inquiries about products, orders, or any other concerns.
- **Detailed Product Information:** Access comprehensive product descriptions, images, specifications, and customer reviews to make informed decisions.
- **Responsive Design:** Experience a user-friendly interface that adapts to different devices, providing a seamless shopping experience on desktop, tablet, and mobile.



### **Features Left to Implement**
In the future, we hope to add:
* More payment options 
* Bigger selection of items
* A loyalty Program


[Back to Table of Contents ⇧](#table-of-contents)


## Marketing Strategy
---
A Marking Strategy, is essential for attracting and retaining customers.
1. Define Your Target Audience:
Identify and understand your ideal customers. Consider demographics, interests, behavior, and buying habits. Create buyer personas to guide your marketing efforts effectively.

2. Set Clear Marketing Objectives:
Determine what you want to achieve with your marketing efforts. Common e-commerce objectives include increasing website traffic, boosting sales, expanding your customer base, and enhancing brand awareness.

3. Competitive Analysis:
Research your competitors in the e-commerce space. Identify their strengths and weaknesses, as well as any gaps in their product offerings that you can exploit.

4. Develop Your Unique Selling Proposition (USP):
Define what sets PrimePulse apart from competitors. Your USP should communicate why customers should choose your e-commerce platform over others.

5. Website Optimization:
Ensure your website is user-friendly, mobile-responsive, and easy to navigate. Optimize product pages for SEO, improve page load times, and implement secure payment options.

6. Content Marketing:
Create valuable, engaging content related to your products or industry. This can include blog posts, product guides, videos, and infographics. Content marketing can help drive organic traffic to your site.

7. Social Media Marketing:
Use social media platforms (e.g., Facebook, Instagram, Pinterest) to connect with your audience, showcase products, run targeted ads, and promote special offers.

8. Email Marketing:
Build and nurture an email list. Send personalized, relevant emails to subscribers, including product recommendations, promotions, and updates about your e-commerce platform.

9. Pay-Per-Click (PPC) Advertising:
Run paid advertising campaigns on platforms like Google Ads and Facebook Ads to drive traffic and conversions. Use targeted keywords and ad copy that resonates with your audience.

10. Influencer Marketing:
Partner with influencers in your niche to promote your products. Their recommendations can build trust and credibility with potential customers.

11. Affiliate Marketing:
Create an affiliate program that rewards partners for promoting your products. This can help you reach a wider audience and increase sales.

12. Customer Reviews and Testimonials:
Encourage satisfied customers to leave reviews and testimonials on your website. Positive reviews build trust and credibility.

13. Analytics and Monitoring:
Use tools like Google Analytics to track website performance, user behavior, and conversion rates. Continuously monitor and adjust your marketing strategies based on data insights.

14. Customer Support and Engagement:
Provide excellent customer service and engage with customers through chat, email, or social media. Happy customers are more likely to become repeat buyers and brand advocates.

15. Loyalty Programs:
Implement loyalty programs to reward repeat customers and encourage brand loyalty.

16. Seasonal and Promotional Campaigns:
Plan and execute seasonal promotions, holiday sales, and other special campaigns to boost sales during peak periods.

17. Budget and ROI Analysis:
Allocate your marketing budget wisely and regularly assess the return on investment (ROI) of each marketing channel to optimize spending.

18. Continual Optimization:
Stay agile and adapt your marketing strategy based on changing market conditions, customer feedback, and industry trends.

Remember that consistency and a customer-centric approach are key to the success of your e-commerce marketing strategy. Regularly evaluate and adjust your tactics to ensure you're meeting your objectives and effectively reaching your target audience.


[Back to Table of Contents ⇧](#table-of-contents)

## User Experience (UX)
---
* ### **User stories**

    * **First-Time Visitor Goals**
        1. As a user, I want to be able to browse through a wide range of fitness equipment products, so I can find the items that meet my fitness goals and preferences.

        2. As a user, I want to be able to create an account and log in, so I can access personalized features such as saving my wishlist, tracking my orders, and managing my profile information.

        3. As a user, I want to be able to search for specific fitness equipment products, so I can quickly find what I'm looking for without having to navigate through the entire site.

    * **Returning Visitor Goals**
        1. As a returning visitor, I want to be able to view my order history, so I can track my past purchases and review the details of each order.
        2. As a Returning Visitor, I want to easily access my previously created account, allowing me to log in quickly and access my saved information and preferences.
        3. As a Returning Visitor, I want to be able to make purchases via PayPal.

    * **Frequent User Goals**
        1. As a frequent visitor, I want to be able to reset my password if I forget my password.
        2. As a frequent visitor, I want to be able to change my Profile image.
        3. As a frequent visitor, I want to have the option to subscribe to a newsletter or email updates, allowing me to receive notifications about exclusive discounts, promotions, or upcoming product releases.


[Back to Table of Contents ⇧](#table-of-contents)

## Security Features and Defensive Design
### User Authentication
- Users must provide full name email address when creating an account
- User is verified by email address.
- django default admin page has a path way of admin. We changed this to a different path by using 'honeypot', a dumby admin site is created.
- all sensitive information is stored in a env.py file.

### Form Validation
- CSRF tokens prevent CSRF because without a token, an attacker cannot create valid requests to the backend server. For the Synchronised Token Pattern, CSRF tokens should not be transmitted using cookies. The CSRF token can be transmitted to the client as part of a response payload, such as a HTML or JSON response.

### Database Security

* **Secure Connection (SSL/TLS):** Configure your application to connect to ElephantSQL using a secure SSL/TLS connection. This helps encrypt data transmitted between your application and the database server, protecting it from interception.

* **Strong Authentication:** Use strong and unique credentials (username and password) for accessing your ElephantSQL database.
Avoid using default or easily guessable credentials.
Regularly rotate your database credentials to maintain security.


[Back to Table of Contents ⇧](#table-of-contents)

## Technologies Used
---
### Languages Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)

 ### Frameworks - Libraries - Programs Used
1. [Python](https://www.python.org/):
    * Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. Python is dynamically typed and garbage-collected.
1. [ElephantSQL](https://www.elephantsql.com/):
    * ElephantSQL provides a browser tool for SQL queries where you can create, read, update, and delete data directly from your web browser.
1. [Django](https://www.djangoproject.com/):
    * Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern. 
1. [Bootstrap](https://getbootstrap.com/):
    * Tailwind CSS is an open-source CSS framework. The main feature of this library is that, unlike other CSS frameworks like Bootstrap, it does not provide a series of predefined classes for elements such as buttons or tables.
1. [Node. js](https://nodejs.org/en):
    * Node.js is a cross-platform, open-source server environment that can run on Windows, Linux, Unix, macOS, and more. Node.js is a back-end JavaScript runtime environment, that runs on the V8 JavaScript Engine and executes JavaScript code outside a web browser.
1. [favicon](https://www.flaticon.com/):
    * Used to create icons for web browser tab.
1. [Google Fonts](https://fonts.google.com/):
    * Google fonts were used to choose the fonts for this site. The fonts were declared in the style.css file which is used on all pages throughout the site.
1. [Font Awesome](https://fontawesome.com/):
    * Font Awesome was used on all pages throughout the website to add icons for social media links.
1. [Gitpod](https://www.gitpod.io/):
    * Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub](https://github.com/):
    * GitHub was used to store the site's code after being pushed from Gitpod.
1. [Balsamiq](https://balsamiq.com/):
    * Balsamiq was used to create the wireframes during the design process.
1. [Grammerly](https://app.grammarly.com/):
    * Used to proofread the README.md.
1. [PayPal](https://www.paypal.com/):
    * For Transactions.


[Back to Table of Contents ⇧](#table-of-contents)


## Testing
---
### Validator Testing

The W3C Markup Validator, W3C jigsaw CSS Validator, and PEP8 Code Institute validator Services were used to validate the project to ensure there were no major errors in the project.
* **HTML**
1. Home Page - Document checking completed. No errors or warnings to show.[W3C validator]()
1. Landing Page - Document checking completed. No errors or warnings to show.[W3C validator]()
1. Edit Page - Document checking completed. No errors or warnings to show.[W3C validator]()
1. Login Page - Document checking completed. No errors or warnings to show.[W3C validator]()
1. Sign Up - Document checking completed. No errors or warnings to show.[W3C validator]()
1. Sign Out- Document checking completed. No errors or warnings to show.[W3C validator]()
![HTML Validator ]()
* **CSS**
No errors were found when passing through the official [(Jigsaw) validator]()
![CSS Validator ]()
* **Python**
* [PEP8 Code Institute validator:] (https://pep8ci.herokuapp.com/#)
    * A few minor errors:
        * 

[Back to Table of Contents ⇧](#table-of-contents)

## Deployment
---
### **Heroku**
This site was deployed to Heroku. The steps to deploy are as follows:
1. Ensure in Django settings, DEBUG is False.
1. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
1. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
1. Click View to view the deployed site.


### **Forking the GitHub Repository**
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

- Log in to GitHub and Locate the repository at this link [Prime Pulse]().
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
- A copy of the repository is now created.


### **Making a Local Clone**
1. Log in to GitHub and locate the GitHub repository at this link [Prime Pulse]().
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the preferred cloning option, and then copy the link provided. 
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
7. Press Enter. Your local clone will be created.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> Remote: Counting objects: 10, done.
> Remote: Compressing objects: 100% (8/8), done.
> remote: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

[Back to Table of Contents ⇧](#table-of-contents)


## Credits
---
* [Font Awesome](https://fontawesome.com/) 
* [W3schools](https://www.w3schools.com/)
* [Favicon](https://www.flaticon.com/free-icons/catholic/2) 
* [Unsplash](https://unsplash.com/) 
* [Tailwindcss](https://tailwindcss.com/docs/installation)
* [W3C validator](https://validator.w3.org/)
* [(Jigsaw) validator](https://validator.w3.org/nu/#textarea)
* [Stackoverflow](https://stackoverflow.com/)
* [Slack](https://slack.com/intl/en-ie/)
* [MD Bootstrap](https://mdbootstrap.com) 
[Back to Table of Contents ⇧](#table-of-contents)