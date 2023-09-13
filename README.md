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
    2. [Development Methodology](#development-methodology)
    
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

<details>
<summary>Screenshots Dropdown</summary>

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

</details>

[Back to Table of Contents ⇧](#table-of-contents)

## Design
---
### Wireframes
You can download the wireframes for this website from this link [GoogleDrive](https://drive.google.com/drive/folders/1eaRgxIO0XQZy-wFDHgE63b_CZdl32TG1?usp=drive_link).
<details>
<summary>Wireframes Board</summary>

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454066/readme-primepulse/wireframes/Home_Page_rumz3j.png" alt="Home  Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Sign_Up_jf7i3f.png" alt="Sign Up Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Sign_In_pne7lv.png" alt="Sign In Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Item_Page_jnk4sa.png" alt="Item Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Cart_Page_ob4u8b.png" alt="Cart Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454066/readme-primepulse/wireframes/Dashboard_Page_xguatb.png" alt="Dashboard Page" width="500"/>
<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694454065/readme-primepulse/wireframes/Edit_Profile_Page_hmyllb.png" alt="Edit Profile Page" width="500"/>

</details> 

---
### ER Diagram
<details>
<summary>ER Diagram</summary>

![ER Diagram](https://res.cloudinary.com/dlulkctls/image/upload/v1694597163/readme-primepulse/ER_diagram_bnvttl.png)
</details> 

---


This code defines the structure of a relational database using the Database Markup Language (DBML). Each table in the database is defined with its attributes, data types, constraints, and relationships. Here's a brief description of each table and its purpose:

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
---
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
---
In the future, we hope to add:
* More payment options 
* Bigger selection of items
* A loyalty Program


[Back to Table of Contents ⇧](#table-of-contents)


## Marketing Strategy
---
A Marking Strategy, is essential for attracting and retaining customers.
1. Target Audience:
    * Fitness Enthusiasts: Individuals who are passionate about fitness, whether they are beginners or seasoned athletes, looking for high-quality fitness equipment to support their workouts.
    * Home Gym Owners: People who have dedicated spaces for home gyms and need equipment like treadmills, dumbbells, resistance bands, and more to maintain their fitness routines at home.
    * Health-Conscious Consumers: Individuals focused on improving their overall health and well-being by investing in fitness equipment for cardiovascular workouts, strength training, or flexibility exercises.
    * Professional Athletes: Professional athletes, trainers, and coaches who require specialized equipment for sports training and conditioning.
    * Gym Owners: Owners of fitness centers and commercial gyms seeking to purchase equipment to furnish their facilities and cater to their clients' needs.
    * Physical Therapy Patients: Individuals undergoing physical therapy or rehabilitation, requiring specific fitness equipment to aid in their recovery and exercise routines.
    * Weight Loss Seekers: People on weight loss journeys looking for fitness equipment to support their fitness and exercise plans.
    * Budget-Conscious Shoppers: Those looking for affordable yet reliable fitness equipment options to fit their budget constraints.
    * Gift Shoppers: Shoppers searching for fitness-related gifts for friends and family members who prioritize health and fitness.
    * Online Shoppers: People who prefer the convenience of online shopping and access to a wide range of fitness equipment options from the comfort of their homes.


2. Set Clear Marketing Objectives:
    * Increase Website Traffic: Aim to grow organic and referral website traffic by a certain percentage each month through search engine optimization (SEO), content marketing, and social media promotion.
    * Boost Sales Revenue: Set monthly, quarterly, and annual revenue targets. Track sales growth and monitor the average order value to ensure steady revenue increase.
    * Expand Customer Base: Focus on acquiring new customers and increasing the customer database. Measure the growth in the number of registered users.
    * Enhance Brand Awareness: Measure brand visibility and recognition through social media mentions, brand searches, and engagement metrics.
    * Increase Customer Retention: Develop loyalty programs and retention tactics to encourage repeat purchases and long-term customer relationships.
    * Track Customer Feedback: Monitor customer reviews and feedback to make improvements and address concerns.


3. Content Marketing:
    * Blog Posts:

        * Fitness Tips: Share workout routines, nutrition advice, and fitness tips to help customers achieve their fitness goals.
        * Product Reviews: Write in-depth reviews of gym equipment and accessories available on the website, highlighting features, benefits, and user experiences.
        * How-To Guides: Create step-by-step guides on assembling and using specific gym equipment.
        * Buying Guides: Offer guidance on choosing the right equipment based on fitness goals, available space, and budget.
        * Health and Wellness Articles: Publish articles on topics like healthy eating, stress management, and mental well-being, emphasizing their connection to fitness.

    * Email Newsletter:

        * Send regular newsletters featuring blog highlights, product promotions, and fitness tips.
        * Include personalized product recommendations based on user behavior and interests.

    * Social Media Content:

        * Share engaging visuals, videos, and short fitness tips on social media platforms.
        * Run social media contests, challenges, and giveaways to encourage user engagement.
        
    * SEO-Optimized Content:

        * Optimize all content for search engines to improve organic visibility.
        * Use relevant keywords related to fitness equipment and accessories.



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

* ### **Test Cases: User stories**
---
* ### **First-Time Test Cases**
1. As a user, I want to be able to browse through a wide range of fitness equipment products, so I can find the items that meet my fitness goals and preferences.
<details>
    <summary>Click Here for User Test Case</summary>
    
1. Step 1: go to https://prime-pulse-d780887a098c.herokuapp.com/.
    user will be greeted by an inviting landing page

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694617820/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.05.59_ej0glv.png" alt="landing page" width="500"/>

2. Step 2: scroll down to see more products.

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694617828/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.06.03_kv6atb.png" alt="landing page" width="500"/>

</details>

---


2. As a user, I want to be able to create an account and log in, so I can access personalized features such as saving my wishlist, tracking my orders, and managing my profile information.

<details>

<summary>Click Here for User Test Case</summary>


1. Step 1: Naviagte to the sign up page via the naviagtion bar. Click on Sign Up button


<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694618255/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.16.18_lf8ik6.png" alt="nav bar" width="500"/>

2. Step 2: The user is then invited to fill out the form. An email is then

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694618257/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.16.34_zq7ttk.png" alt="sign up page" width="500"/>

3. Step 3: The user will be greeted by a message and asked to check their emails to verify account.


<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694619405/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.35.12_ozah59.png" alt="activation message" width="500"/>

4. Step 4: Once the email is verified the user is asked to sign in.

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694619404/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.36.00_cdywaz.png" alt="sign in page" width="500"/>

5. Step 5: The user will then have access to their own personnal dashboard

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694619403/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.36.12_ewat1a.png" alt="dashboard page" width="500"/>

</details>

---

3. As a user, I want to be able to search for specific fitness equipment products, so I can quickly find what I'm looking for without having to navigate through the entire site.

<details>

<summary>Click Here for User Test Case</summary>


1. Step 1: Naviagte to the search bar located on the navbar at the top of the page


<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694620341/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.51.39_pvtt29.png" alt="search bar" width="500"/>

2. Step 2: If the user searches for 'dumbbells' only related items will be shown.

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694620344/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.51.57_fvi9ab.png" alt="result page" width="500"/>


</details>

---



* ### **Returning Visitor Test Cases**

1. As a returning visitor, I want to be able to view my order history, so I can track my past purchases and review the details of each order.
<details>
    <summary>Click Here for User Test Case</summary>
    
1. Step 1: from the dashboard users can access their order history by click on the 'My Orders' button

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694620836/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.00.09_pbikao.png" alt="dashboard page" width="500"/>

2. Step 2: from here users can see order history.

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694620835/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.00.15_zdm0lr.png" alt="orders page" width="500"/>

</details>

---


2. As a Returning Visitor, I want to easily access my previously created account, allowing me to log in quickly and access my saved information and preferences.

<details>

<summary>Click Here for User Test Case</summary>


1. Step 1: Users can do this by navigating to the sign in page via thye navigation bar. Once here they will be propted to enter their creditenials to login


<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694619404/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_16.36.00_cdywaz.png" alt="search bar" width="500"/>

2. Step 2: The user is logged in

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694621240/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.07.04_fabug9.png" alt="search bar" width="500"/>


</details>

---

3. As a Returning Visitor, I want to be able to make purchases via PayPal.

<details>

<summary>Click Here for User Test Case</summary>


1. Step 1: Once the user has logged in and added items to their car. If they click on the cart button froim here they can review the cart.


<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694621383/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.08.41_i6mdna.png" alt="cart review" width="500"/>

2. Step 2: By clicking on the checkout button the useer is brought to the "Place Order" page. Here they are prompted to fill out the 'Billing Address' form.

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694621384/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.08.50_xilpsb.png" alt="Place order" width="500"/>

3. Step 3: When the user clicks on the "place Order' button they are then transferred to the 'Payment Page'.

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694621385/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.09.06_kis9ox.png" alt="make payment " width="500"/>


</details>

---

* ### **Frequent Visitor Test Cases**

1. As a frequent visitor, I want to be able to reset my password if I forget my password.
<details>
    <summary>Click Here for User Test Case</summary>
    
1. Step 1: From the Dashboard Page the user can click on the 'reset password' button.

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694622277/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.22.13_qishla.png" alt=" dashboard page" width="500"/>

2. Step 2: from here users can fill out the two required fields to reset password.

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694622273/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.22.23_cstyjr.png" alt=" reset password page " width="500"/>

</details>

---


2. As a frequent visitor, I want to be able to change my Profile image.

<details>

<summary>Click Here for User Test Case</summary>


1. Step 1: From the Dashboard Page the user can click on the 'edit profile' button.

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694622277/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.22.13_qishla.png" alt=" dashboard page" width="500"/>

2. Step 2: from here, the user can click on profile picture field and 'choose file' button

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694622380/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.26.11_txj1qq.png" alt="profile picture" width="500"/>


</details>

---

3. As a frequent visitor, I want to have the option to subscribe to a newsletter or email updates, allowing me to receive notifications about exclusive discounts, promotions, or upcoming product releases.

<details>

<summary>Click Here for User Test Case</summary>


1. Step 1: From the Dashboard Page the user can click on the 'Sign Up To Our News Letter' button.

    <img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694622277/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.22.13_qishla.png" alt=" dashboard page" width="500"/>

2. Step 2: from here, the user ccan provide an email to sign up for the newsletter

<img src="https://res.cloudinary.com/dlulkctls/image/upload/v1694622549/readme-primepulse/User%20Stories/first%20time%20users/Screenshot_2023-09-13_at_17.28.52_tx9cbi.png" alt="newsletter form page " width="500"/>




</details>

---


### Development Methodology
---
* The development followed an Agile methodology on the [PrimePulse github Project] (https://github.com/users/kev-n14/projects/9)

<details>
<summary>Agile board</summary>

![Github project](https://res.cloudinary.com/dlulkctls/image/upload/v1694613232/readme-primepulse/User%20Stories/agile_board_kqmmql.png)
</details> 

[Back to Table of Contents ⇧](#table-of-contents)

## Security Features and Defensive Design
---
### User Authentication
- Users must provide full name email address when creating an account
- User is verified by email address.
- django default admin page has a path way of admin. We changed this to a different path by using 'honeypot', a dumby admin site is created.
- all sensitive information is stored in a env.py file.

### Form Validation
---
- CSRF tokens prevent CSRF because without a token, an attacker cannot create valid requests to the backend server. For the Synchronised Token Pattern, CSRF tokens should not be transmitted using cookies. The CSRF token can be transmitted to the client as part of a response payload, such as a HTML or JSON response.

### Database Security
---
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

 ### Frameworks - Programs Used
 ---
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


### Libraries

* cloudinary_storage
* django.contrib.admin
* django.contrib.auth
* django.contrib.contenttypes
* django.contrib.sessions
* django.contrib.messages
* django.contrib.staticfiles
* django.contrib.sites
* cloudinary
* category
* accounts
* store
* carts
* orders
* admin_honeypot

[Back to Table of Contents ⇧](#table-of-contents)


## Testing
---
### Validator Testing

The W3C Markup Validator, W3C jigsaw CSS Validator, and PEP8 Code Institute validator Services were used to validate the project to ensure there were no major errors in the project.
* **HTML**
[HTML Validator](https://validator.w3.org/)

1. Home Page - Document checking completed. No errors or warnings to show.
1. Edit Page - Document checking completed. No errors or warnings to show.
1. Login Page - Document checking completed. No errors or warnings to show.
1. Sign Up - Document checking completed. No errors or warnings to show.
1. Landing Page - Document checking completed. No errors or warnings to show.

* **CSS**
No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
* **Python**
* [PEP8 Code Institute validator:] (https://pep8ci.herokuapp.com/#)
    * A few minor errors:
        * E501 line too long
        * W293 blank line contains whitespace

* **Lighthouse**
1. Home Page - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636392/readme-primepulse/User%20Stories/Test%20result/light-house-home_zvxqxa.png)
1. Cart Page - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636390/readme-primepulse/User%20Stories/Test%20result/light-house-cart_ph040s.png)
1. Login Page - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636384/readme-primepulse/User%20Stories/Test%20result/light-house-sign-in_cs8w5b.png)
1. Sign Up - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636389/readme-primepulse/User%20Stories/Test%20result/light-house-sign-up_fgi0ru.png)
1. Order Page - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636387/readme-primepulse/User%20Stories/Test%20result/light-house-orders_lqqfhc.png)
1. Newsletter Page - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636385/readme-primepulse/User%20Stories/Test%20result/light-house-newsletter_ldswkc.png)
1. Edit Profile Page - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636382/readme-primepulse/User%20Stories/Test%20result/light-house-edit-profile_tmjdzn.png)
1. Product Page - Document checking completed. No errors or warnings to show.[Lighthouse](https://res.cloudinary.com/dlulkctls/image/upload/v1694636381/readme-primepulse/User%20Stories/Test%20result/light-house-product-page_pdt25g.png)



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
---
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

- Log in to GitHub and Locate the repository at this link [Prime Pulse]().
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
- A copy of the repository is now created.


### **Making a Local Clone**
---
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