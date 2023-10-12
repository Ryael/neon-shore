# Manual Testing

## Bugs

| **Bug**   | **Intended Outcome**  | **Issue**   | **Cause**   | **Solution**  | **Commit**  |
|---  |---  |---  |---  |---  |---  |
| #1  | SwiperJS's slide content (text and image) displayed side by side.   | SwiperJS's slide content (text and image) not displayed side by side.   | Slide content was not being put in a grid as the class name `.hero` was changed to `.hero-section` and only updated for the first slide.  | Change each slide's class from `.hero` to `.hero-section`.  | [732c182](https://github.com/Ryael/neon-shore/commit/732c182a2b0be3a29199a5b63985750f2d710146)  |
| #2  | Custom styles are used over SwiperJS's default styles.  | SwiperJS's default CSS,specifically, `display: block` used instead of custom `display: grid`.   | SwiperJS's styles had more specificity.   | Give custom CSS higher specificity by prefacing it with `.mySwiper`.  | [4c4c7d1](https://github.com/Ryael/neon-shore/commit/4c4c7d14a203250801ae3ca2708942ac70a31264)  |
| #3  | Search box on mobile should not have a `:hover` effect.   | Search box on mobile has a `:hover` effect.   | Mobile search box is a `li` element and all `li` elements have a `:hover` effect.   | Target all the `li` elements but the first, the search box.   | [e657d2b](https://github.com/Ryael/neon-shore/commit/e657d2b2427608a06db006489c3057806eeb21bd)  |
| #4  | When the mobile navigation menu is opened and a wider than expected viewport is achieved, the navigation switches to the wider resolution navigation.   | The mobile navigation menu is opened and then a wider than expected horizontal viewport is achieved. The close button disappears but the menu itself persists.    | `#fullscreen-navigation` isn't being toggled to `display: none` after the viewport is widened.  | Add `display: none` to `#fullscreen-navigation` to ensure the mobile menu doesn't display after viewports higher than specified.  | [2b4d04b](https://github.com/Ryael/neon-shore/commit/2b4d04ba4131721b3216f0453c8a657ea27799c2)  |
| #5  | Logo doesn't flicker upon transition into the mobile navigation menu.   | Logo flickers upon transition into the mobile navigation menu.  | Logo's transition is being covered by one of the other mobile navigation transitions.   | Adjust transition time to account for all transitions.  | [50dbef6](https://github.com/Ryael/neon-shore/commit/50dbef678a6869be2501b399eecdd3b41f99df3d)  |
| #6  | Footers stays at the bottom of the page.  | Footer detaches from the bottom of the page and displays a gap between it and the bottom of the page.   | `.container` sections did not have a viewport assigned in terms of height.  | Assign `height: 100vh` to `.containter` to ensure the footer is pushed to the bottom of the page.   | [ff0ae91](https://github.com/Ryael/neon-shore/commit/ff0ae918affdfcab5a540a835a76d617bde4a873)  |
| #7  | Category names should display as singular names.  | Category names are displaying as plural.  | The names are provided in `categories.json` are all plural.   | Add `singular_name` to `categories.json`.   | [8ef21ea](https://github.com/Ryael/neon-shore/commit/8ef21ea87b424d1510d32abe2db9e39a8ddc46b7)  |
| #8  | Mobile navigation links should only be interactable when the mobile menu is displayed.  | The mobile navigation links are interactable even when the mobile menu is not displayed.  | Mobile navigation links have `pointer-events: auto` by default.   | Toggle `pointer-events` from `auto` to `none` between transitions.  | [623e80a](https://github.com/Ryael/neon-shore/commit/623e80a7176bec539c7790c8f5f9034201d4e4d6)  |
| #9  | Navigation bar menu content should be centered.   | Navigation bar menu content is not centered.  | `padding` is pushing content to the right of center.  | Switch from `display: flex` to `display: grid` and use `grid-template-columns: 1fr 0fr 1fr` to completely center everything.  | [9245fc3](https://github.com/Ryael/neon-shore/commit/9245fc33a33f73d478a088dbf07f6ac65b6fd942)  |
| #10   | Upon item being removed from the bag, the page should automatically reload without any errors.  | Upon attempting to remove an item from the bag, the page reloads but a csrf error occurs.   | The csrf error prevents the item from being removed from the bag.   | Use `getCookie` code from Django documentation.   | [3021fa1](https://github.com/Ryael/neon-shore/commit/3021fa1be8afb7b874e30467a6b43d330712d7b6)  |
| #11   | Pagination for the home page should fit into the vertical viewport.   | Pagination for the home page doesn't fit into the vertical viewport.  | Container padding and margins are pushing the pagination out of view.   | Update container padding and margins to account for the pagination.   | [a0023a4](https://github.com/Ryael/neon-shore/commit/a0023a4b108d064d7e4d5848074bdab3f5b4800e)  |
| #12   | Flash messages should display special characters correctly.   | Flash messages are not rendering special characters properly.   | SweetAlert `text` field doesn't render special characters.  | Change SweetAlert `text` field to `html` field.   | [d7dc57d](https://github.com/Ryael/neon-shore/commit/d7dc57db9bcd44c734500fd708c46ebabc7a0fc1)  |
| #13   | Delivery cost should be calculated.   | Delivery cost is not being calculated.  | Delivery cost logic was not implemented.  | Import `Decimal` and add `delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / 100)` as the delivery logic.  | [fc99213](https://github.com/Ryael/neon-shore/commit/fc9921341d465e9f262d71e1309763ea6c1fc547)  |
| #14   | Page title for product details should be all lowercase.   | Page title for product details should be capitalised.   | `{{ product.name }}` is capitalised by default.   | Add `\| lower` to `{{ product.name }}` to ensure it's rendered as all lowercase.  | [6d53619](https://github.com/Ryael/neon-shore/commit/6d53619f3b63e41540c68694b8120603684f3733)  |
| #15   | Toast modal should not cover the navigation bar.  | Toast modal is covering the navigation bar, preventing the user from accessing their bag.   | Default SweetAlert style places the alert in the top right, which is where the navigation bar bag sits.   | Overwrite default style with custom by adding relative positioning for the modal.   | [9f6cb75](https://github.com/Ryael/neon-shore/commit/9f6cb75d95b0e9df3fc147fe8ce105768625aa52)  |
| #16   | Registered user can access their profile.   | Registered user was unable to access their profile.   | Error 500 was displayed, as migrations were not being run upon deployment to Heroku.  | Add a release phase command to procfile.  | [26c329b](https://github.com/Ryael/neon-shore/commit/26c329b4857e4a8a3eb35a4bee5c942fafb67467)  |
| #17   | Successful deployment to Heroku.  | Deployment was failing.   | `django-country` was missing a db-relation.   | Upgrade `django-countries`.   | [18498c8](https://github.com/Ryael/neon-shore/commit/18498c8355649aeb9c556c78ab03d374cd90a8d8)  |
| #18   | Heroku should use Python 3.11.6.  | Heroku was using 3.11.4.  | Heroku was using a previously built release.  | Add `runtime.txt` with Python 3.11.6.   | [e55b877](https://github.com/Ryael/neon-shore/commit/e55b877e852c3134e68277fc74926d2a350aa36b)  |
| #19   | Admin user can log into the website.  | Admin user was unable to log into the website.  | Admin had no user profile.  | Recreate admin user.  | N/A   |
| #20   | User can input payment details when checking out.   | User was unable to input payment details when checking out.   | jQuery CDN wasn't being loaded due to a security issue.   | Change `http` to `https` for the jQuery CDN, which is much more secure.   | [c2fa42e](https://github.com/Ryael/neon-shore/commit/c2fa42e5cf7f0d0584cc63e5cdeb4cb1ea3135f2)  |
| #21   | No horizontal scrollbar should be present across all content.   | Horizontal scrollbar is present across all content.   | `width: 100vw` on body and containers, in combination with the vertical scrollbar is what causes this.  | Remove `width: 100vw` from body and all containers.   | [0e1a7d4](https://github.com/Ryael/neon-shore/commit/0e1a7d417ac431155fdb8e9bb129273c0272e32a)  |
| #22   | Stripe webhook should deliver events successfully.  | Stripe webhook was not delivering events successfully.  | Stripe endpoint configured incorrectly.   | Add `/checkout/wh` to the end of the endpoint.  | N/A   |
| #23   | Stripe should send confirmation emails upon successful checkout.  | Stripe was not sending confirmation emails.   | Error 500, there was an extra newline in the subject confirmation email template.   | Remove the newline from the subject template.   | [dee11b4](https://github.com/Ryael/neon-shore/commit/dee11b40446f320ad7eabaeebe89785e4c2d7b7e)  |

## Responsiveness

Mozilla Firefox's built-in Responsive Design Mode was to extensively test all aspects of Paradise Lost. It works on viewports as small as 350px.

## Accessibility

[WAVE WebAIM](https://wave.webaim.org/) was used to test the accessibility. A handful of label and aria-label errors were returned, as well as one constrast error but those were quickly fixed.

## Performance

Google Lighthouse was used to assess the performance of this website. All tests were performed in incognito mode to avoid interference from any other sources. Tests were carried out on each section but the same result was returned every time. This was the same case for mobile, and as such, only one result will be provided.

![Lighthouse](docs/testing/lighthouse.png)

## Validation

### HTML

[W3C Markup Validation Service](https://validator.w3.org/nu/) was used to validate all the HTML. Each file was checked by text input first and then by address afterwards. No errors were found, aside from errors pertaining to templating. A few warnings were flagged but this was assumed to be because of Django as well.

![HTML](docs/testing/html.png)

### CSS

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate both CSS stylesheets. No errors were found for `form.css` but `style.css` showed errors for "Property r doesn't exist". However, after extensive research, this may just be that the validation tool is out of date. Property `r` refers to the radius of a circle and is often used in SVG designs. There's even a [CSS-Tricks page](https://css-tricks.com/svg-properties-and-css/) that covers the use of it. Additionally, it seems like the [VSCode linter](https://github.com/microsoft/vscode/issues/85828) also picks up on it incorrectly and has since 2019. The latest post was last month and it still seems to be an issue.

![Form CSS](docs/testing/form-css.png)

![Style CSS](docs/testing/style-css.png)

### JS

[JSHint](https://jshint.com/) was used to validate JavaScript code. It detected one unused variable, but that variable is indeed used and was hence left alone.

![JavaScript](docs/testing/jshint.png)

### PEP8

[PEP8 Code Institute Linter](https://pep8ci.herokuapp.com/#) was used to validate Python code. The only errors found were to do with lines being too long and those were all fixed. `settings.py` had a handful of line too long errors but as they were provided that same way by the base template and for fear of tampering with important configurations, these errors were left untouched.

## Device Testing

The website was tested on many different devices, such as:

- Samsung Galaxy S10
- Samsung Galaxy S21
- Samsung Galaxy Note 8
- MSI GE72 6QF Apache Pro
- iPhone 8
- iPhone 10
- iPhone 11
- iPhone 11 Pro
- iPhone 12
- iPhone 14 Pro Max
- iPad Mini (Landscape and Portrait)
- iPad (Landscape and Portrait)
- Vivo S1 Pro
- LG v60
- Huawei P40 Pro
- Google Pixel 6

## Browser Compatibility

- Mozilla Firefox
- Google Chrome
- Opera
- Safari
- Microsoft Edge

I tested the website extensively on Mozilla Firefox, Google Chrome, and Microsoft Edge. For the remaining two, I asked friends and family to test the website on my behalf while overlooking it to ensure cross-compatibility. No issues or bugs were reported.

### User Story Testing

1. As an unregistered user, I want to quickly understand the purpose of this website so that I can determine if I want to continue spending my time on this website and register.

  - Upon arriving at the landing page, the user is greeted by the hero video and dynamically changing text that informs the user of the purpose of the website.
  - The typography help to convey the feeling that this is a very futuristic, sci-fi, and army-focused website which should help the user infer its purpose.

2. As an unregistered user, I want to easily navigate the menu without getting lost and see the uniformity of each page so that I know this website is worth my time and won't lead to any frustrations.

  - The colour scheme is consistent throughout all pages, as are the menus which emulate an application-like approach that help familiarise the user with the website.
  - The navigation menu is sleek, clean, and simple. Everything is well laid-out and easy to understand.

3. As an unregistered user, I want to quickly and easily learn more about the website and its purpose if I am unable to infer its purpose from the visuals and text alone, so that I can decide if registering for this website would be beneficial to me.

  - After this point, the user is able to open the navigation menu if the visuals were engaging enough to open the "About" page, where they can find more detailed information about the purpose of this website in great detail.

4. As an unregistered user, I want to be able to register for an account so that I can start building my army rosters.

  - The home page has an "Enlist Now!" button that re-directs the user to the "Register" page, where they're able to easily and quickly make an account for the website.
  - The user is also able to access this page by opening the fullscreen navigation menu and navigating to the "Register" link in the middle of the screen.

5. As a registered user, I want to be able to change my password should I forget so that I have peace of mind in knowing that I won't be locked out of my account.

  - Upon opening the dashboard, the user is prompted to change their password. However, this assumes that they know what it was prior to this. If not, there's a highlighted link at the bottom of the page that re-direct them towards the "Forgot Your Password" page, where the user can reset their password via e-mail.
  - If the user registered without providing an e-mail, then they have the option of contacting the admin and asking them to help them change their password.
  - Alternatively, if the user was logged out, once they navigate to the "Login" page there'll be a link to "Reset" their password in case they forgot at the bottom of the menu, which brings them to the same place as above.

6. As a registered user, I want to be able to manage my account by changing my password so that I can avoid any security breaches or implement a stronger password.

  - Registered users are able to open their dashboard, which acts as their base of operations. Here they can find a "Change Your Password" button which re-directs them to the page of the same name. The user is able to change their password by first inputting their current password and their new, desired password twice.

7. As a registered user, I want to be made aware of my account management actions so that I know they have been successful.

  - Upon changing or updating their password, if the "Forgot Your Password" functionality was used then a page is displayed to inform the user's action was successful. If the "Change Your Password" functionality was used then a message is printed above the form to inform them that their password has been changed successfully.

8. As a registered user, I want to be able to access a user dashboard so that I have a base of operations for this website that's readily available.

  - Upon logging in or registering, the user is provided feedback that their action was successful by being brought to the "Dashboard" page.
  - They are greeted here with a "Welcome, Commander %USERNAME%!" to further inform that they're at the right place.
  - There are three buttons here which allow them to navigate to a) "My Rosters", b) "Change Your Password", c) "Logout" pages.
  - The "Dashboard" page is accessible from all parts of the website via the navigation menu once the user is logged in.

9. As a registered user, I want to be able to create my roster so that I can view it later.

  - From the "Dashboard" page, a user is able to navigate to the "My Rosters" page where they are greeted by a "Create Roster" button.
  - Upon interaction with this button, they are brought to another page where they're able to create a roster.
  - On this "Create Roster" page, once all the details are input and the button is interacted with, the user is brought back to the "My Rosters" page where a message is printed to let them a roster has been successfully created.

10. As a registered user, I want to be able to view my roster so that I can decide if it needs to have any changes made to it.

  - Users are able to view their current rosters via the "My Roster" page, which is available via the easily accessible "Dashboard".
  - Here a table is displayed of all the available rosters.
  - A user can interact with the "eye" icon to see a roster on its own.
  - Nothing else is possible here and the user is provided with a button to return back to their list of rosters.

11. As a registered user, I want to be able to update my roster so that I can make sure it's always up to date.

  - From the "My Roster" page where all the current rosters are displayed, beside each roster is three icons: an "eye", a "pen", and a "bin". The second is often used as an icon for the edit function, which is precisely what this icon does.
  - It re-directs the user to the "Edit Roster" page, where they can make changes to their roster of choice.
  - Upon confirmation of the changes, they're returned back to the roster list where a message is printed to inform them that their edit has been successful.

12. As a registered user, I want to be able to delete my roster so that any old or unnecessary rosters don't use any unnecessary space.

  - In the same way as above, a registered user is able to make all management actions on their rosters via the "My Rosters" page.
  - In this case, the focus is on the "bin" icon, which is commonly used as a delete button.
  - Interacting with it will re-direct the user to the "Delete Roster" page where the user is asked if they are sure that this is the roster they want to delete. The name of the roster will be bold and a button asking for their confirmed will be found below that.
  - Should they confirm, they'll be brought back to the "My Roster" page where there'll be one roster less and a message printed informing that roster has been deleted.

13. As an admin, I want to be able to log into an admin interface so that I can view, add, update, or delete information pertaining to the army rosters.

  - Django's provided admin interface makes it very quick and simple to login, manage data however you may wish to.
  - This, however, is limited to how your models are set-up.

14. As an admin, I want to be able to access the users for the website so that I can make any adjustments to their accounts such as changing their password or email, should they request it.

  - The built-in admin interface is very powerful and offers powerful user management tools.
  - Admins are able to change a user's username, first name, last name, email address, permissions, groups, password, as well as their latest login and date of registration.

15. As an admin, I want to be able to view a list of the users so that I know how many active users there are.

  - Simply by navigating to the "User" portion of the admin panel, an admin is quickly and easily able to see exactly how many users have registered on their website and how many of them are active.

16. As a site user, I want to be engaged by the user interface, indicating I will enjoy spending time building my rosters as I navigate the same menus repeatedly.

  - The menus were all built in such a way that it feels cohesive and everything leads to another. Buttons are snappy and quick, with animations playing very quickly.
  - When one has to navigate lots of menus quickly, it's equally important that said menus are well-designed and responsive.
  - The designs are also consistent throughout, with each part of the website complementing each other.

17. As a site user, I want to be shown responses from the website upon interaction with it so that I know the creation, deletion, or update of my roster has been successful.

  - Upon any of the successful edit, create, and delete roster actions, the user is brought back to the "My Rosters" page, where the relevant message is printed just below the title of the page so as to inform them their action has been carried out.

18. As a site user, I want to experience a unique and uniform design with appealing colours so that every part of the website stimulates a positive response.

  - The user interface was built with a very sleek and futuristic theme in mind that's supposed to evoke feelings of sci-fi war-games with its buttons, hero-video, and dot-like backgrounds. Design was put on the forefront to engage the user as much as possible and maximise user conversion.

19. As a site user, I want to be able to access the website from any screen size and still have a pleasant viewing experience, so that I'm not restricted to only viewing this website on bigger screens.

  - This website has been optimised for all viewports, even for mobiles with widths as small as 350px.
  - Generally speaking, these sort of websites tend to lend themselves well to bigger screens due to the amount of data they display, but this data has been styled in such a way that the data displays nicely even at smaller viewports.

20. As a site user, I want to be able to contact the admin via e-mail, find their GitHub project repository, or even find them on other socials like LinkedIn.

  - Any user is able to find the admin's socials via the navigation menu, which is always available to them.
  - There they can find the admin's LinkedIn, GitHub, and their e-mail.

[Back to Readme](https://github.com/Ryael/paradise-lost)
