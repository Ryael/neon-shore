# neon shore

[neon shore - Live Website](https://neon-shore-a156870f9760.herokuapp.com/)

![Stars - Badge](https://badgen.net/github/stars/Ryael/paradise-lost) ![Watchers - Badge](https://badgen.net/github/watchers/Ryael/neon-shore) ![Issues - Badge](https://badgen.net/github/issues/Ryael/neon-shore)

![neon shore](docs/screenshots/paradise-lost.gif)

neon shore is a B2C merchandise store belonging to my dear friend, an artist who goes by [expuella](). As it stands, it's just a prototype and proof of concept but there are plans to get this up and running the future. In the interest of privacy and safety, her real name will be disclosed and she will instead be referred to solely by her alias. I've worked with expuella in the past and currently help her with business inquiries, as well as managing Pixiv and Weibo on her behalf. [Pixiv]() is an imageboard/gallery that's extremely popular in Japan, and [Weibo]() is a micro-blogging alternative to Twitter in China.

This is my fifth and final milestone project as part of Code Institute's Diploma in <strong>Software Development (E-commerce Applications)</strong>.

This project was my idea as opening up a store is something we've spoken about in the past but have never done anything about due to how much time and effort it would require. This is not to mention maintainence and fulfilling orders without a dedicated staff. Having said that, this e-commerce project was the perfect opportunity to take this idea and begin working on it.

Many artists have merchandise stores but they're often created using services like [Shopify]() and full-on storefronts like [etsy]() and these services take a percentage of the profits from the artist. [INPRNT]() is a very popular choice for artists to sell prints of their artwork as INPRNT handles the printing and shipping of the prints once the art is uploaded, however the profit split is a whopping 50:50. Expuella herself also uses INPRNT and has expressed her distaste in staying with them.

Knowing this, I decided to craft an e-commerce website around expuella's vision of "neon-shore", which is a name she chose for the business side of things when she was much younger and it has stuck with her since. neon-shore speaks of expuella's love for tropical settings, beaches in particular, in combination of a neon colour palette. As such, I wanted the design and UI of this website to represent that, hence I asked expuella to work with me as my client and approve my designs and decisions.

For the purpose of this project, expuella will also be referred to as the client It will be my goal to facilitate and actualise her vision of her business.

![neon shore- Responsive](docs/screenshots/responsive.png)

## Table of Contents

1. [neon shore](#neon-shore)
2. [Planning Phase](#planning-phase)
    - [Strategy](#strategy)
      - [Site Aims](#site-aims)
      - [Opportunities ](#opportunities)
    - [Scope](#scope)
3. [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
4. [User Interface](#user-interface)
    - [Design Philosophy](#design-philosophy)
      - [Colours](#colours)
      - [Typography](#typography)
    - [Wireframes](#wireframes)
    - [Database](#database)
5. [Agile Development Process](#agile-development-process)
6. [Features](#features)
    - [Logo](#logo)
    - [Landing Page](#landing-page)
    - [Navigation Menu - New User](#navigation-menu-new-user)
    - [Navigation Menu - Registered User](#navigation-menu-registered-user)
    - [Button](#button)
    - [About](#about)
    - [Register](#register)
    - [Login](#login)
    - [Forgot Your Password](#forgot-your-password)
    - [Logout](#logout)
    - [Dashboard](#dashboard)
    - [Change Your Password](#change-your-password)
    - [Roster List](#roster-list)
    - [Create Roster](#create-roster)
    - [Edit Roster](#edit-roster)
    - [View Roster](#view-roster)
    - [Delete Roster](#delete-roster)
    - [Error 404](#error-404)
    - [Error 505](#error-500)
    - [Favicon](#favicon)
7.  [Code](#code)
    - [Commits](#commits)
8. [Testing]
9. [Future Updates](#future-updates)
10. [Deployment](#deployment)
11. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Tools](#tools)
12. [Credits](#credits)
13. [Acknowledgements](#acknowledgements)

## Planning Phase

### Strategy

#### Site Aims

While a merchandise store may not seem like a good choice for a business, especially with there being so many alternatives between websites like [Redbubble](), [eBay](), and so on, avid fans of art and certain series enjoy to show their support of an artist and their works by purchasing their works. It's my belief that as much as possible of this should go to the sole creator of these works, the original artist. Art is often stolen, used, and printed without permission, and this is an unfortuante truth of the internet. As such, I'd like to bring as much attention and money to the original artists themselves.

Often times, people are more than happy to show their support towards their favourite artist and their works by purchasing prints, which are easy to ship, store, and display. Smaller pieces of merchandise like charms, pins, and stickers are also very popular as they're both cheap and easier to display as they use less room real-estate. Artbooks are also quite popular as they tend to be relatively inexpensive and a very sought-out collector's item, especially for those interested in collecting artbooks.

This site aims to act as a prototype for my client to show her what an e-commerce store would look and function like, while providing a simple, clean, and easy-to-use interface for both clients and admins.

#### Opportunities

The following was an extensive list of features that were brainstormed between expuella and I during the conceptualisation of the website. A feasibility chart was deemed important to prioritise the scope of the intended strategy.

| Opportunity             | Importance  | Feasibility   |
|------------------------ |------------ |-------------  |
| User Account      | 5           | 5             |
| Stripe Payments           | 5           | 5             |
| Landing Page            | 5           | 5             |
| Account Management              | 5           | 5             |
| About Page              | 3           | 5             |
| User Profile            | 5           | 5             |
| Product Management  | 5           | 5             |
| Checkout System          | 5           | 5             |
| Order History   | 5           | 5             |
| Flash Messages             | 5           | 5             |
| Testimonials             | 3           | 4             |
| Contact Page             | 5           | 5             |
| Social Media             | 5           | 5             |
| Different Currencies             | 3           | 1             |
| Promotions             | 3           | 1             |
| Related Products             | 2           | 2             |
| FAQ Page             | 3           | 3             |
| E-mail Confirmation             | 5           | 5             |
| Order Status             | 3           | 1             |
| Trustpilot Reviews             | 4           | 1             |
| Newsletter             | 3           | 3             |
| **Total**               | **87**      | **80**        |

Feasibility is based on time and my current level of ability using languages.

### Scope

As there is an imbalance of 5 points in the above score, (87 vs 80), there will have to be trade-offs made due to the tight schedule of this project.

The above table has been further categorised in order to establish a clear vision of the MVP required while satisfying the above requirements.

UX **Must's**:
  - User can login, logout, and register
  - User can checkout
  - User can use Stripe to carry out payment
  - User can recieve a confirmation email
  - User can view products
  - User can view their order history
  - User can access a store's Social Media
  - User can change and/or reset their passwords
  - User can access their profile
  - User can see feedback for their actions

- UX **Should's**:
  - User can leave and read testimonials
  - User can otherwise reset their password
  - Landing Page
  - About Page
  - Contact Page
  - Error Pages
  - Newsletter
  - Product Management for admin

- UX **Should Not's**:
  - Different Currencies
  - Trustpilot Reviews
  - Order Status
  - Related Products
  - FAQ Page

## User Experience

### Target Audience

  - People who are looking to support artists
  - People who are looking for merchandise of their favourite series
  - People who are fans of original content and merchandise pertaining to it

### User Stories

#### Unregistered Users

  1. As an unregistered user, I want to quickly understand the purpose of this website so that I can determine if I want to continue spending my time on this website and register.

  2. As an unregistered user, I want to easily navigate the menu without getting lost and see the uniformity of each page so that I know this website is worth my time and won't lead to any frustrations.

  3. As an unregistered user, I want to quickly and easily learn more about the website and its purpose if I am unable to infer its purpose from the visuals and text alone, so that I can decide if registering for this website would be beneficial to me.

  4. As an unregistered user, I want to be able to register for an account so that I can view my past orders.

  5. As an unregistered user, I want to be given feedback for my actions so that I know they've been successful or not.

  6. As a site user, I want to be engaged by the user interface, indicating I will enjoy spending time exploring the website as I navigate the same menus repeatedly.

  7. As a site user, I want to experience a unique and uniform design with appealing colours so that every part of the website stimulates a positive response.

  8. As a site user, I want to be able to access the website from any screen size and still have a pleasant viewing experience, so that I'm not restricted to only viewing this website on bigger screens.

#### Registered Users

  9. As a registered user, I want to be able to change my password should I forget so that I have peace of mind in knowing that I won't be locked out of my account.

  10. As a registered user, I want to be able to manage my account by changing my password so that I can avoid any security breaches or implement a stronger password.

  11. As a registered user, I want to be made aware of my account management actions so that I know they have been successful.

  12. As a registered user, I want to be able to access a user dashboard so that I have a base of operations for this website that's readily available.

  13. As a registered user, I want to be able to view a list of products so that I can select some for purchase.

  14. As a registered user, I want to be able to view individual product details so that I can see their price, description, and a larger image to see if it's something I like.

  15. As a registered user, I want to be able to view all my purchases to see how much my order has amounted to.

  16. As a registered user, I want to be able to leave a testimonial to let other people know of my experiences with this store.

  17. As a registered user, I want to be able to contact the store owner easily with any queries I may have.

  18. As a registered user, I want to be able to change my delivery details so that they're correct and saved for future purchases.

  19. As a registered user, I want to be able to recieve a verification email upon registration so that I know my registration was successful.

  20. As a registered user, I want to be able to recieve a confirmation email upon completeing a purchase so that will I have a copy of order.

  21. As a registered user, I want to be able to sort products by their categories so I can quicker identify what I'm interested in.

  22. As a registered user, I want to be able to search the list of products so that I can find anything I'm looking for as quickly as possible.

  23. As a registered user, I want to be able to add a specific amount of a given product to my bag so that I can buy only the amount I'm looking for.

  24. As a registered user, I want to be able to adjust the amount of a given product in my bag so that I can easily make changes to my overall order.

  25. As a registered user, I want to be able to easily enter my payment information so that I can checkout quickly and securely and know that my payment information is safe.

  26. As a registered user, I want to be able to access the order success page after completing a payment to make sure it went through successfully and that I haven't made any mistakes in my shipping details.

  27. As a registered user, I want to be able to access the checkout page so that I review my order whilst entering my payment and shipping details.

#### Admins

  28. As an admin, I want to be able to add a product so that I can add new products to the store via the product management menu

  29. As an admin, I want to be able to edit a product so that I can change the product details via the product management menu.

  30. As an admin, I want to be able to delete the product so that I can remove products that are out of stock or have been discontinued via the product management menu.

  31. As an admin, I want to be able to setup a social media page to promote my business, products, and website.

  32. As an admin, I want to be able to access the users for the website so that I can make any adjustments to their accounts such as changing their password or email, should they request it.

  33. As an admin, I want to be able to view a list of the users so that I know how many active users there are.

#### Dropped

Certain user stories were dropped as part of the agile process. They are as follows:

  - As an unregistered user, I want to be able to view a FAQ page to see what the most popular questions are and if they answer any of my questions.
  - As a unregistered user, I want to quickly navigate to the top from any point on the page so that I don't spend too long scrolling.
  - As a registered user, I want to be able to edit my testimonials in case I make a typo or just want to change it.
  - As a registered user, I want to be able to delete my testimonials in case I want to remove the testimonial altogether.
  - As an admin, I want to add headings to the admin database tables so I can more quickly understand my data.
  - As an admin, I want to filter the admin database tables so that I can more easily find the data I need.

## User Interface

### Design Philosophy

The design of this website began with a simple and clear vision: to encapsulate expuella's vision of a tropical beachfront paradise. Expuella's colour palette has pulled away from the neon palette quite a bit in the past few years so I opted to focus in on the beach aspect. This meant leaving the neon colour palette behind and instead opting for a much softer colour palette.

My goal was first and foremost to replicate the feeling that the user is welcomed by a friendly sandy beach shore.. As such, I began looking for design inspiration all over the internet, including websites like [Dribble](https://dribbble.com/), [Behance](https://www.behance.net/), and [CodePen](https://codepen.io). After about a week of searching, I stumbled upon this [Product UI Showcase](https://codepen.io/TurkAysenur/pen/gORaboY) pen and this is where the idea for my design was born for neon shore. It had that perfect sandy aesthetic that served as the core of this website design going forward.

After consulting my client, we agreed that a less saturated sandy colour would be more effective and less visually overpowering. Montserrat was chosen as the font of choice due to how well it complemented the existing design with its geometric and soft look. Instead of the black, a gray was opted for as it looked a lot more gentle with the less saturated sandy background. Originally, I planned to use EB Garamond for its sleek italic feel and its ability to create a sense of contrast with Montserrat, but unfortunately, expuella was not fond of it so it was removed. After much more searching, no other font type was found that satisified both of us and hence Montserrat was chosen as the sole font for this project. This worked quite well as it is very self-sufficient and looks different enough to the point that different font weights complement each other quite nicely.

One of the biggest takeaways from this was pen the implementation of [SwiperJS](), which allowed me to create a carousel of rotating images, saving a huge deal of space and even allowing me to use a [GSAP]() paintlike mask effect to allow the image be revealed in brushstrokes. Learning to use and customise SwiperJS proved to be quite challenging as it was complex and required a complex HTML structure. However, after much adjustment I was able to find a marriage between a sandy shoreline and an art gallery, which I believe perfectly illustrates the purpose of this website.

The remainder of the website followed the philosophy of this design, so as to create a coherent experience that felt like one thing smoothly led to another without any jarring changes within the user interface.

The design of the UI was mostly made with a desktop approach in mind. The design for the smaller viewports had to come after and while it proved to be a challenge, I'm quite happy with how the website looks and handles at smaller resolutions.

#### Colours

The below image was generated using [coolers.co](https://coolors.co/edeade-4f5356-ffffff). The feint sandy yellow is the colour that was picked from the body of the website, the gray was often used for text content, and the white was used primarily for the navigation menus, the profile interface, and for the footer. The white was used to represent foamy waves and served to create a sense of contrast to prevent the user from only ever seeing sand, which is only about half the point of a beach!

![neon shore - Colours](docs/screenshots/colours.png)

#### Typography

One font was specifically chosen for this website:

- *Montserrat*

Montserrat was chosen for its soft, geometric, and contemorary feeling. Its well rounded corners give it an air of elegance, as if it belongs in an art gallery itself, making it the perfect font for the purpose of neon shore.

All lowercase was my client's preference, as it is part and parcel of both her identity and aesthetic. It proved difficult to work with at first as it was quite difficult to create designs using just fonts that felt different enough, but thankfully after learning to properly manipulate weight, letter spacing, and size, it was still possible to create layouts where the heading and paragraph text looks varied yet consistent.

### Wireframes

The conceptualisation of the layout used in this project began with simple pen and paper sketches, which were then transformed into wireframes via Balsamiq. Everything shown here is a rough beta of the layout, some of which has changed during development.

This is the prototype of the project, which changes over the course of project development.

<details>
  <summary>Home Page</summary>
  <img src="docs/wireframes/home.png" alt="Wireframe of the Home Page">
</details>
<details>
  <summary>Navigation Menu</summary>
  <img src="docs/wireframes/navigation-menu.png" alt="Wireframe of the Navigation Menu">
</details>
<details>
  <summary>General Menu</summary>
  <img src="docs/wireframes/menu.png" alt="Wireframe of the General Menu">
</details>
<details>
  <summary>Roster</summary>
  <img src="docs/wireframes/roster.png" alt="Wireframe of the Roster">
</details>

### Database

![neon shore - Database Schema](docs/schema/database.png)

Above is the database schema as the initial plan for the database tables. Originally, we planned for users to be able to configure their rosters with units, specialisms, abilities, war gear, and weapon profiles. Unfortunately, this fell completely out of scope due to time constraints and unfamiliarity with a method of serialising those models in a way that's customisable to each user.

The user model was not included due to the default user model provided by the ALLAUTH library.

## Agile Development Process

[Jira](https://www.atlassian.com/software/jira) was used to create and track User Stories and issues. Login credentials will be provided for the above project space when the project is submitted. A summary of my agile process and learning outcomes can be found [here](https://github.com/Ryael/paradise-lost/blob/main/AGILE.md).

## Features

### Logo

![logo](docs/screenshots/logo.png)

No suitable icon was found for the logo and hence the Orbitron font was used for it instead. To create a sense of contrast "Paradise" was written in white, whereas "Lost" was written in orange and has lower font weight than "Paradise". This approach to text logo design achieves a sleek and unique look. As expected, interacting with the logo brings the user to the home/landing page.

### Landing Page

![landing-page](docs/screenshots/landing-page.png)

The landing page utilises a hero-video for its background, which loops perfectly every 10 seconds. Upon loading into the page, the user is greeted the video and the dynamically rotating text. The text rotates between synonyms for "army", "fleet", and other similar words every four seconds. Dynamically changing text is very [effective for user conversion](https://www.convertize.io/dynamic-text/) and creates an engaging landing page. This text is accompanied by a call-to-action button with the words "Enlist Now!", urging potential users to sign-up. Lastly, in the top right corner, a hamburger menu is visible which is used to expand a navigation menu.

### Navigation Menu - New User

![navigation-menu-new](docs/screenshots/navigation-menu-new.png)

The navigation menu opens with a smooth fade-in animation and the hamburger icon is replaced with an "X", informing the user that this "X" icon is what they should interact with should they want to close the navigation menu. The user is greeted by a dark gray "carbon-fiber" background with small dots, which consists of a small single dot image that is repeated. This allows the dot to scale to any viewport necessary without any stretching. The links themselves begin as white and when interacted with, all but the active one fade to grey. The social-icons on the bottom also function the same way.

The bottom of the navigation menu features the aforementioned social-icons which also double as the website's footer. This approach was opted for as full screen navigation menus are becoming increasingly popular, given they allow for greater focus on the true page content. Even if a stick navigation bar approach is utilised, it still uses a portion of the viewing space. The footer can also add unnecessary vertical scrolling. As this website aims to utilise the immediately available viewing space, full screen navigation menu was the ideal choice.

### Navigation Menu - Registered User

![navigation-menu-registered](docs/screenshots/navigation-menu-registered.png)

Similarly, to the new user example, the navigation menu changes the links available to the user depending on if they are authenticated or not. If they are not, the above example is what they will see. If they are, however, then they'll instead be shown the Registered User example with the Login and Register links replaced with Dashboard and Logout links.

### Button

![button](docs/screenshots/button.gif)

All the buttons present on the website follow the same design: gray background with orange text and orange decorators on all corners. Upon interaction, the corners expand and float outwards. This effect was made to be reminiscent of an aiming reticle to give the website's buttons a more military-esque feeling, bolstering the site’s sci-fi army feel. The decorators and button text also both flicker upon loading and interaction, as a way of guiding the user.

### About

![about](docs/screenshots/about.png)

The about page is the one of the first pages the user will see should they want to learn more about the purpose of the website. The entirety of the page background is a dark gray with a similar (albeit more widely spaced) dot pattern to the navigation menu. However, this time the dot itself is generated with CSS, which allows it to expand infinitely as required by the viewport. Links are highlighted in orange and turn to white on mouse-over/interaction, providing the user with visual feedback.

### Register

![register](docs/screenshots/register.png)

This is one of the first menus a new user will see, if the landing page user conversion was successful. Upon loading into this page, the user is greeted by a centered menu with a white outline and input text fields outlined in that same orange colour, creating a consistent design throughout. Errors are rendered above their relevant text field and are styled in the same manner as regular paragraph text, meaning that the body text is consistently gray throughout. Additionally, a link to the login page is found at the bottom of the menu and highlighted in orange, instantly standing out to the user who may be looking just to login. The button for the input is same as other buttons showcased earlier. This will be consistent for every other button on this website.

### Login

![login](docs/screenshots/login.png)

Logging in is an important process for any website with features locked behind user registration. As such, login menu itself is simple and short. The user is also provided with a remember-me checkbox, with its opacity reduced ever-so-slightly to make it fit in with the overall colour scheme of the menu. Upon it being checked, it becomes highlighted in the usual orange colour. The user is also presented with two links at the bottom of the menu, one linking them back to the register page and the one below that allowing them to use the "Forgot your password" functionality which allows them to reset their password via email.

### Forgot Your Password

![forgot-your-password](docs/screenshots/forgot-your-password.png)

In terms of design, this section is consistent with the above menus. Upon entering the email the user used for registration, they're able to request a link via email to reset their password. Once that link is used, the user is redirected to the reset password page where they are given a chance to input a new password and then confirm that same password. They are then brought to a new page where they are informed their password has been successfully changed.

### Logout

![logout](docs/screenshots/logout.png)

Should the user want to logout, they are brought to one of the smallest menus across the entire website. It's centered vertically and horizontally, which admittedly does stand out. However, this is intentional as the very small menu box looks out of place when it's placed in the same location as the other menus. Upon logging out, the user is not provided with any text but instead is brought to the landing page as is standard. The links in the navigation menu also revert to "Register" and "Login".

### Dashboard

![dashboard](docs/screenshots/dashboard.png)

Upon successful registration or login, the dashboard page is the first thing the user will see. While there is no message printed to inform the user that their login has been successful, instead they will be greeted by "Welcome, Commander USERNAME!". Between the redirect and the greeting on the dashboard, I feel this is sufficient to let the user know that their login has been successful. The dashboard is available to the user wherever they go via the navigation menu alongside the "Logout" link. On the dashboard itself, the user is given three options on where to go next: "My Rosters", "Change Password", and "Logout".

### Change Your Password

![change-your-password](docs/screenshots/change-your-password.png)

Changing your password on the website is important due to security reasons. Sometimes one may want a more complex password for peace of mind, sometimes one may want to update their password manager, and even sometimes one may want to update their passwords across all websites due to their password being compromised. As such, it is extremely important to provide the user with a way of changing their password. The menu itself is the exact same as before and once the current password, new password, and new password again are submitted, the page is refreshed, and the user is informed via message that their password has been successfully changed.

### Roster List

![roster-list](docs/screenshots/roster-list.png)

Once the user interacts with the "My Rosters" button, they'll be brought to the roster index page, which shows all the available rosters. If this is the user's first time coming to this page, there will be no rosters visible and instead all they'll see is a "Create Roster" button. This button is placed under the created rosters but will be in their immediate viewing space initially. The roster menus are different from the general menus as they are much wider to accommodate the tables. This width is adjusted to around 80% of the viewport on medium-small devices to ensure everything fits nicely and neatly.

Once a roster has been created, it is rendered as a table via HTML and styled using CSS. For wider screens this will be a table with an orange outline as per usual, for medium-small screens this will be a wide card, and for small screens this will be a narrow card. Each of the aforementioned cards are stacked vertically with a small space in between. Each roster has three Font Awesome icons: 1) View (Eye), 2) Edit (Pen), and 3) Delete (Bin). These three icons are common practice for these actions and also fade to white on interaction, indicating that they function as links. The rosters themselves are sorted by their name.

### Create Roster

![create-roster](docs/screenshots/create-roster.png)

The create roster page is fundamentally very similar to the user account management menus, except that it features a number field and drop-down menus for selection. Below the relevant data input is a button that lets the user create a roster with their selected data. Below the button is a link to go back to roster list.

### Edit Roster

![edit-roster](docs/screenshots/edit-roster.png)

Editing a roster is almost identical to creating one as the menu is the same – however, the page title and submit buttons are different. This is a simple and straightforward experience.

### View Roster

![view-roster](docs/screenshots/view-roster.png)

Viewing a roster is more or less identical to the "My Rosters" page, however it shows one select roster in the same fashion as the roster list. Ideally this is what the users would be able to share with other players. Unfortunately, that functionality is currently out of scope. At the bottom of the menu, a "Return" button is available for the user.

### Delete Roster

![delete-roster](docs/screenshots/delete-roster.png)

Opting to delete a roster brings the user to a very simple and short menu where they're asked if this is the correct roster to be deleted. This roster is referenced by name and has a button labelled "Yes" under this text, with a "Cancel" link under that should the user want to return to the roster list.

### Error 404

![error-404](docs/screenshots/error-404.png)

If a user managed to stray off the beaten path, they'll be displayed an error 404 page, which has been styled with the usual orange colour. This design uses an SVG which can be upscaled almost infinitely without sacrificing any quality. This SVG is created entirely using CSS as well. The SVG itself is used to create a round "O" animation that feels at home in any futuristic-themed website and is sandwiched by "4" and "0". The error description is rendered in Exo and in orange, with flashing brackets at both sides that help grab the user's attention.

### Error 500

![error-500](docs/screenshots/error-500.png)

Similarly, to the error 404-page, error 500 is displayed whenever there's an internal server error. Ideally, users will never encounter it. It uses a similar SVG-styled page with the "4" and "4" replaced with "5" and "0" to spell out error 500. The error description reads "Internal Server Error" in the same style as the above error.

### Favicon

![favicon](docs/screenshots/favicon.png)

As with all websites, this one also has a Favicon that is displayed beside the Title of the page. A user can quickly and easily discern if they have neon shore open amongst many different tabs by looking for the capital "P" icon, which is rendered in the same font as the title text, Orbitron.

## Code

Primarily standard practice was followed for creating a Django application, however, due how to `{{forms as p}}` render, `style.css` was split aside from `form.css`, the latter of which targeted any elements on the page post-rendering to style them effectively. `script.js` was also split into two: `hamburger-script.js` and `text-rotator.js` due to the jQuery present on the latter throwing console errors for any page where the dynamic text wasn't present, which was every page except for the home page.

### Commits

- `git status` was used far more frequently to avoid committing anything I didn't intend to, and this helped with keeping the commits down in size.
- If any errors were made in the commit message, `git commit --amend` was used to edit it.
- If a file was unintentionally added, `git restore --staged file` was used to rectify this.
- `git commit -v` was used almost exclusively due to being able a description and see the differences in staged files below.
- The imperative mood was used throughout all messages and descriptions.

All of the above allowed for more precise and correct version control.

## Testing

Extensive testing has been carried out during and post-development and is available in a separate document [here](https://github.com/Ryael/neon-shore/blob/main/TESTING.md).

## Future Updates

1. Expand on the Roster system, allowing users to add units, wargear, weapon profiles, and the like.

2. Include more rulesets including more than just rulesets for Warhammer 40,000, other armies, and so on. Plenty to expand on, but it ultimately requires a lot more time and research.

3. Tighten up and optimise the UI a bit more. I had less time than I would have liked, so certain aspects had to be rushed to get them done to meet the deadline.

4. Properly center the hero video and fix the issue with the dynamically changing text where it stands to lag a bit. There's no easy fix in mind but there are some JavaScript wizards I could ask for advice.

5. Lastly, as this was a project for Simon W., I'd like to convert this from Python and Django to Ruby and Ruby on Rails. I'm already familiar with Ruby as is, but I would love an opportunity to learn on Rails, as well. I look forward to it.

## Deployment

### ElephantSQL

This project uses ElephantSQL as its database. In order to obtain your own Postgres Databse, you should make a new account or just sign-up via your existing GitHub account. After that, follow the next steps:

1. Click "Create New Instance" to create a new database.
2. Give it a name, common practice dictates that this is the name of the project.
3. Select the free plan (Tiny Turtle).
4. Tags can be left blank and instead select the Region and Data center closest to you.
5. After creation, click on the name to be brought to the dashboard for the database where you will be shown the URL and password.

### Cloudinary API

This project also uses the Cloudinary API in order to store its media assests online. To obtain your own API key, after creating an account and logging in, follow these steps:

1. Select Programmable Media for image and video API.
2. On your dashboard, you can copy your API Environment Variable.
3. Make sure to only copy the value, which is the string after the equals sign.

### Heroku Deployment

This project uses Heroku as it's hosting platform of choice, as it runs applications entirely in the cloud.

After account creation, follow the below deployment steps:

1. Select New in the top right corner of your dashboard.
2. Select Create New App.
3. Using a unique app name click create app.
4. Navigate to Settings, where you will configure Config Vars.
5. You will need to add the very minimum of the following:
  - `CLOUDINARY_URL`
  - `DATABASE_URL`
  - `DISABLE_COLLECTSTATIC`
  - `SECRET_KEY`

After all this, you're still not done because Heroku requires two additional files: `requirements.txt` and `Profile`.

You can install your project's requirements using `pip3 install -r requirements.txt`. However, if you have manually added any packages, then you will need to `pip3 freeze --local > requirements.txt`.

The `Procfile` can be created using the following command: `echo web: gunicorn your_app_name.wsgi > Procfile` where "your_app_name" is the name of your application.

Now, lastly, all you need to do is to navigate to the Deploy tab and hit Deploy. Alternatively, you can use the Automatic Deploy functionality to deploy the app every time a push is made.

## Technologies Used

### Languages

- Python
  - The packages installed for this project can be found in the [requirements.txt](https://github.com/Ryael/paradise-lost/blob/main/requirements.txt).
- Django
  - Django was used as the Python web framework.
  - ALLAUTH was used to handle user authentication.
- Heroku
  - Heroku was used to deploy the website.
- ElephantSQL
  - This was used to host the database for the website.
- HTML
  - HTML was responsible for the core structure and layout of all the templates.
- CSS
  - CSS was used to add styling to the HTML to creat a unique design.
- JavaScript
  - JavaScript was used to manipulate the DOM to create the dynamically rotating text.
- jQuery
  - jQuery was used to create the fullscreen navigation menu.
- FontAwesome
  - All the icons present throughout all the pages are from this wonderful package.

### Tools

- [Sublime Text](https://www.sublimetext.com/) - Used as my text editor of choice.
- [Balsamiq](https://balsamiq.com) - Used to create wireframes.
- [Obsidian](https://obsidian.md/) - Used to take notes and create to-do lists.
- [Adope Premiere Pro](https://www.adobe.com/ie/products/premiere.html) - Used to crop, resize, and edit images.
- [W3C HTML Validator](https://validator.w3.org/) - Used to validate HTML code.
- [W3C JigSaw Validator](https://jigsaw.w3.org/css-validator/) - Used to Validate CSS code.
- [JSHint](https://jshint.com/) - Used to validate JS code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate Python code.
- [WAVE WebAIM](https://wave.webaim.org/) - Used to check accessibility.
- [Google Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) - Used to check performance, SEO, accessibility, and best practices.
- [Mozilla Firefox Developer Tools](https://www.mozilla.org/en-US/firefox/new/) - Used to check and test the project.
- [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) - Used to create the Multi Device Website Mockup image.
- [Google Fonts](https://fonts.google.com/) - Fonts were imported from here.
- [Font Awesome](https://fontawesome.com/) - Icons are used from here.
- [Favicon.io](https://favicon.io/) - Used to create a favicon.
- [ShareX](https://getsharex.com/) - Used to take screenshots and gifs.

## Credits

- [GeeksForGeeks](https://www.geeksforgeeks.org/) - Has some of the best Djano and Python tutorials and walkthrough projects, which were an incredible help.
- [Videezy](https://www.videezy.com/abstract/50298-futuristic-globe-world-earth-planet-in-cyberspace-with-binary-code) - Videezy is the go to place for lovely, high quality videos that are free to use even commericially with just good attribution. It's exactly where I found the holographic rotating planet earth.

- [BattleScribe](https://www.battlescribe.net) - This website of course was inspired by none other than BattleScribe. This is what motivated me and have me an inkling of an idea of how to build it, although it still requires a lot more work, I believe my work is cut out for me.

- [Jeremy (CodePen)](https://codepen.io/thefewunshaken/details/BEBYLd) - This was the only example of dynamically changing text I could find handled via vanilla JavaScript, which was what I utilised for this project. Not much was changed, because not much could have been changed whilst keeping the entire functionality. It's a very simple but powerful tool.

- [Rob McFadzean (CodePen)](https://codepen.io/breadz/details/zrMRoo) - It was here that the inspiration for the fullscreen navigation menu was taken from. It's very simple and effective, using only a bit of jQuery. The overall feel and design was changed considerably.

- [Robin Selmer (CodePen)](https://codepen.io/robinselmer/pen/OKwvqE) - This was the general button design that was used throughout the project. It's the corner decorators that give the button such a unique feeling, allowing it to look like a reticle focusing in and out. The design was mostly kept the same but it was changed where possible.

- [Ivan Villamil (CodePen)](https://codepen.io/ivillamil/pen/jWjgzE) - The roster tables present in neon shore were loosely based on these tables in terms of design, but it was the smaller viewport responsiveness that was borrowed and adapted to the my own style and changed quite a bit in the end.

- [Rebai Adnen (CodePen)](https://codepen.io/adnenrebai/pen/KNqQJP) - The very beautiful and sleek 404 page was gotten from here, cleaned up where possible, and adjusted to suit neon shore. Working with this, I've learned quite a bit with regards as to how to manipulate SVGs.

## Acknowledgments

- [Simon Waldron](https://github.com/saikez) - Simon acted as my client, my mentor, my tutor support, and my best friend throughout this entire project. He helped guide me when I was stuck, helped me learn many good practices, how to quickly and efficiently research topics, how to troubleshoot, explained agile methodologies, helped me setup JIRA, and even allowed me to use his pre-configured e-mail server so that users would have the option to reset their passwords. Thank you so much, Simon, it was an absolute pleasure designing this for you and I'm very eager to work not for you but together with you in the near future.

- Rose S. - Rose was instrumental in helping me proofread this readme, testing.md, and agile.mdY ou've saved me so much time and hassle, after looking at it for so long I just can't spot errors any longer... so, thank you so much, Rose! You're wonderful!

- My family and friends, who have been incredibly supportive and have been instrumental in keeping me motivated throughout this project. Thank you all so much! All of you who helped proofread, test, provide feedback on the website, code, and etc... I couldn't have done it without you all!

- The Code Institute community on Slack - Easy, straightforward, and always willing to help and provide advice.
