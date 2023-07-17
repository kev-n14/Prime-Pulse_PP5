# PP5-Prime-Pulse

![logo](https://res.cloudinary.com/dlulkctls/image/upload/v1689552890/readme-primepulse/banner_image_1_d9cue8.jpg)
# Prime Pulse Application


The Prime Pulse website is an e-commerce website that specializes in selling fitness equipment. The products listed on this website is from weights to cardio and everything in between.It is the one stop online shop for everything fitness related.

## Features
---
### **Landing Page**

![Landing Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572938/readme-primepulse/home_page_jqlbf4.png)

### **Navigation Bar**

![Navigation Bar](https://res.cloudinary.com/dlulkctls/image/upload/v1689573129/readme-primepulse/home_1_fkkxko.png)


### **Footer Section** 


![Footer Section](https://res.cloudinary.com/dlulkctls/image/upload/v1689573918/readme-primepulse/footer_e63eaz.png)


### **Sign Up Page** 


![Sign Up Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689573916/readme-primepulse/sign_up_sem3eo.png)


### **Login Page**


![Login Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572929/readme-primepulse/sign_in_kc0oxs.png)


### **Signout Page** 


![Signout Page]()
### **Store Page**


![Store Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572933/readme-primepulse/store_page_sdwpmj.png)



### **Product Page**


![Product Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572940/readme-primepulse/product_details_page_zbvly9.png)


### **Cart Page**

![Cart Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572930/readme-primepulse/cart_iyhqbz.png)


### **Billing Page**

![Billing Address](https://res.cloudinary.com/dlulkctls/image/upload/v1689572930/readme-primepulse/billing_address_page_hkswlp.png)

### **Review Page** 


![Review Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572932/readme-primepulse/review_page_wjdtoj.png)
### **Paypal Transaction Page** 

![Paypal Transaction Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689573949/readme-primepulse/paypal_transaction_vum32d.png)
### **Signout Page** 

![Payment successful Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572931/readme-primepulse/payment_success_m8nag9.png)
### **User Dashboard Page** 


![User Dashboard Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572930/readme-primepulse/dashboard_main_bkealj.png)
### **Orders Page** 


![Orders Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572930/readme-primepulse/dashboard_my_orders_zpgpjy.png)
### **Edit Profile Page** 


![Edit Profile Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572929/readme-primepulse/dashboard_edit_profile_zeeeo1.png)
### **Change Password  Page** 


![Change Password Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572930/readme-primepulse/dashboard_change_password_fufnxy.png)
### **Facebook Page** 


![Facebook Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572934/readme-primepulse/facebook_1_b7esip.png)

### **Facebook Second Page** 


![Facebook Second Page](https://res.cloudinary.com/dlulkctls/image/upload/v1689572934/readme-primepulse/facebook_1_b7esip.png)







### **Features Left to Implement**
In the future, we hope to add:
* More payment options 
* Bigger selction of items


## User Experience (UX)
---
* ### **User stories**

    * **First-Time Visitor Goals**
        1. As a First Time Visitor, 

        2. As a First Time Visitor, 

        3. As a First Time Visitor, 

    * **Returning Visitor Goals**
        1. As a Returning Visitor,

        2. As a Returning Visitor, 

        3. As a Returning Visitor, 
    * **Frequent User Goals**
        1. As a Frequent User, 
        2. As a Frequent User, 
        3. As a Frequent User, 

* ### **Design**
    * **Colour Scheme**
        * A soothing and warm purple and orange to invite the user. Complemented with white background and black and white text with blue buttons. 
    * **Typography**
        * 'Segoe UI'
    * **Imagery**
         * abstract large banner image with company logo in white.
 

* ### **Wireframes**
    * Edit Page - [View]()
    * Login - [View]()
    * Sign Up - [View]()
    * Landing Page - [View]()




## Security Features and Defensive Design
### User Authentication
- Users must provide full name email address.
- User is verified by email address.
- django default admin page is has a path way of admin/. we changed this to a different path. By use honey a dumby admin site is created.
- all sensitive imformation is stored in a env.py file.

### Form Validation
- CSRF tokens prevent CSRF because without a token, an attacker cannot create valid requests to the backend server. For the Synchronised Token Pattern, CSRF tokens should not be transmitted using cookies. The CSRF token can be transmitted to the client as part of a response payload, such as a HTML or JSON response.

### Database Security


## Technologies Used
---
### Languages Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)

 ### Frameworks - Libraries - Programs Used
1. [Python](https://www.python.org/):
    * Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. Python is dynamically typed and garbage-collected
1. [ElephantSQL](https://www.elephantsql.com/):
    * ElephantSQL provides a browser tool for SQL queries where you can create, read, update, and delete data directly from your web browser.
1. [Django](https://www.djangoproject.com/):
    * Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern. 
1. [Bootstrap](https://getbootstrap.com/):
    * Tailwind CSS is an open-source CSS framework. The main feature of this library is that, unlike other CSS frameworks like Bootstrap, it does not provide a series of predefined classes for elements such as buttons or tables.
1. [Node. js](https://nodejs.org/en):
    * Node.js is a cross-platform, open-source server environment that can run on Windows, Linux, Unix, macOS, and more. Node.js is a back-end JavaScript runtime environment, that runs on the V8 JavaScript Engine and executes JavaScript code outside a web browser
1. [favicon](https://www.flaticon.com/):
    * Used to create icons for web browser tab.
1. [Google Fonts](https://fonts.google.com/):
    * Google fonts were used to choose the fonts for this site. the fonts were declared in the style.css file which is used on all pages throughout the site.
1. [Font Awesome](https://fontawesome.com/):
    * Font Awesome was used on all pages throughout the website to add icons for social media links.
1. [Gitpod](https://www.gitpod.io/):
    * Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub](https://github.com/):
    * GitHub was used to store the site's code after being pushed from Gitpod.
1. [Balsamiq](https://balsamiq.com/):
    * Balsamiq was used to create the wireframes during the design process.
1. [Grammerly](https://app.grammarly.com/):
    * Used to proofread the README.md

## Testing
---

## Validator Testing

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

### Testing User Stories from the User Experience (UX) Section
#### **First Time Visitor Goals**
1. As a First Time Visitor, 
1. As a First Time Visitor, 
1. As a First Time Visitor,  
    
#### **Returning Visitor Goals**
1. As a Returning Visitor, 

1. As a Returning Visitor, 


1. As a Returning Visitor, 

#### **Frequent User Goals**
1. As a Frequent User, 

2. As a Frequent User, 

3. As a Frequent User, 
 
## Performance
---
### **Lighthouse Test**
* Landing Page
![Landing Page]()

* Edit Page
![Gallery Page]()

* Sign Up Page 
![Sign Up Page ]()

* Sign Out Page 
![Sign Out Page  ]()

* Sign In Page 
![Sign In Page  ]()


## Deployment
---
### **Heroku**
This site was deployed to Heroku. The steps to deploy are as follows:
1. Ensure in Django settings, DEBUG is False
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
1. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the preferred cloning option, and then copy the link provided. 
1. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
1. Open Git Bash
1. Change the current working directory to the location where you want the cloned directory to be made.
1. Type git clone, and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
Press Enter. Your local clone will be created.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> Remote: Counting objects: 10, done.
> Remote: Compressing objects: 100% (8/8), done.
> remote: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
1. Type **'Enter'** to create the local clone.


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
* [slack](https://slack.com/intl/en-ie/)
* [MD Bootstrap](https://mdbootstrap.com) 
