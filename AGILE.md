# Agile Methodology

## Overview

JIRA was chosen for this project due to the great success I had with it during my previous project and the familiarity that came with using this tool during that time.

It felt significantly easier to better utilise this tool, even as a one-person team, which was my main complaint during the previous project.

A similar approach with stand-ups with the client was taken due to how it keeps them informed of progress each day, with sprints lasting between a day to two. All user stories were split into epics, which were then neatly organised and evaulated in terms of story points.

Bugs and additional features were recorded and added to the backlog, however, they were always evaluated so as to ensure they aligned with the MVP.

The biggest takeaway I encounted while working on this project is two-fold:

- Research should be an epic and should have considerable story points assigned to its user stories as this was a very time-consuming process.
- Deployment should also have its own epic and relevant user stories as I had encountered quite a few issues in terms of routing URLs and setting up templates.

For any future projects, I will aim to address these issues by providing them with their own epics as they not to be underestimated in the amount of time they can consume.

Ultimately, it helped me a great deal to stay focused on the task on hand and not to spend too much time on any given issue so as to meet the goal of the MVP.

## Sprint Notes

Below is a summary of learnings from each individual sprint, gotten from screenshots of the sprint prior to completion, and note taken by myself.

### Sprint #1:

https://i.imgur.com/HC51hWw.png

The aim of this sprint was to set-up the project while following along the Boutqiue Ado walkthrough. This involved setting up allauth, the relevant templates, basic UI, and the home page.

- This sprint began on 06/07/23 at 20:00 and ended on 08/07/23 at 00:30. The estimated story point total was 34 but the time taken to complete them all was closer to approximately 14 hours, which made this sprint a total success even with the extension described below.
- The biggest issue I encountered throughout this issue was trouble with templates and URL routing. This was the primary reason I had to extend the sprint by a day.
- UI, which included typography, logo, buttons, colours, and the navigation bar were all decided on with accordance with the client's vision and brand.
- Multiple issues arose with using SwiperJS and learning its intricacies, especially when it came to customising its navigation and pagination. Navigation proved to a big issue as it was difficult to position the navigation arrows and keep them responsive, with a compromise being found in using `position: absolute` and adjusting them with media queries. However, these media queries haven't been fully implemented yet and will be dealt with at a later time.
- Learning how to manipulate GSAP was relatively straight forward due to how expansive and detailed its documentation is, and allowed for a very easy implementation of the desired timing of the painting effect.
- A total of four bugs were encountered during this sprint and two of them were resolved. The remaining two will be attempted to be resolved during future sprints.

### Sprint #2:

https://i.imgur.com/uJqdUva.png

The objective of the second sprint was to finish some basic UI elements and style the majority of the User Management pages.

- This sprint began on 07/09/23 at 21:30 and ended on 11/09/23 at 18:00. The estimated story point total for this sprint was 22.5 but the time taken was closer to 30 hours. While a success overall, the reason for this taking longer than estimated was two-fold: 1) the mobile navigation menu and its transitions, and 2) the plethora of bugs.
- Working with the mobile navigation menu proved to be challenging as it was difficult to manipulate some of the unordered list elements but not all. This was solved by using sibling selectors after some troubleshooting.
- The User Management pages proved to be relatively straight forward thanks to having worked with allauth prior as part of the previous project.
- A total of five bugs were discovered but four were resolved. The remaining one will be solved during future sprints as priority is complete a MVP.

### Sprint #3:

https://i.imgur.com/IUBFeea.png

The main goal of this sprint was to set-up and style the Store page and all its related contents, including the search, sort, categorise functionalities, as well as the detailed product view.

- This sprint began on 11/09/23 at 20:00 and ended on 13/09/23 at 20:00. The estimated story point total for this sprint was 21 points but the only 20 story points were completed. This was due to a bug that I was not able to solve within the time-frame I had set aside for it. Overall, this sprint was a success but it did take longer than estimated due to my not being familiar with Django's workflow for an e-commerce website. The total time taken was close to 20 hours but the sprint went on for longer due to my falling ill.
- The most challenging aspect of this sprint was thinking of designs that would suit the brand of the client and overall aesthetic of the website, but once those were established it wasn't too difficult to work through the rest, especially with the help of Boutique Ado.

### Sprint #4:

https://i.imgur.com/FCk9TSr.png

The aim of this sprint was to set-up and style the Bag page, implement being able to add a select quantity to the bag, and then adjusting the quantity within the bag itself alongside being able to remove items altogether.

- This sprint began on 13/07/23 at 21:31 and ended on 15/07/23 at 1:30. The estimated story point total was 7 at first but bugs were brought into it bringing the total to 20. All of these issues were resolved in time, although it proved to be far longer than anticapted. While still a success, the remove button's bug in the missing or invalid CSRF error caused me a lot of trouble.
- This bug was resolved by finding a solution on Code Institute's Slack from over 3 years ago, which suggested implementing and passing CSRF as a cookie instead. This solution can also be found on Django's official documentation.
- While stuck on the aforementioned issue, time was instead diverted to other bugs, almost all of which were fixed.
- Overall, the time spent was approxtimately 18 hours and matched the assigned story points.

### Sprint #5:

https://i.imgur.com/rlWguhU.png

This sprint was used to find an alternative to Bootstrap's Toasts and use it as flash messages that inform the user that their actions have either have or haven't been successful. As that alone seemed difficult, only one other task was added in the setting-up and styling of the Checkout page.

- This sprint began on 16/07/23 at 8:59 and finished on 17/07/23 at approximately 5:00. The estimated story point total was 6, all of which were completed alongside a bug that had been discovered, bringing the total to 7. It took approximately the estimated time to finish all these tasks, causing this sprint to be a total success.
- The greatest difficulty with this sprint was finding an alternative to Bootstrap's Toast system and finding a way of intregrating it with Django. SweetAlerts were chosen as the flash message method of choice, and it took repreat-read throughs of the documentation to successfully implement it. At first, a center-screen modal pop-up approach was employed but then was later changed to be a much less distracting Toast-like notification.
- The special characters not rendering properly bug was resolved by replacing the `text` field with a `html` field, although this allows for XSS attacks on the website. However, as this website won't be deployed for a commercial purpose until much later, this was was deemed a satisfactory compromise. This, will, however be dealt with in the future with input sanitation.

### Sprint #6:

https://i.imgur.com/ksle5hC.png

This sprint's objective was to setup Stripe and all of its associated functionality, including webhooks. Having known that the Boutique Ado code-along had a very long session for this, the Payment Security (ie. Stripe), was allocated 10 story points and the only other user story to accompany it was chosen to be Order Confirmation, sitting at 2 story points.

- This sprint began on 21/07/23 at 22:00 and finished on 23/07/23 at 5:00. The estimated story point total was 12 and the time taken to complete these user stories took approximately 16 hours but the sprint ran on due to my negligence and being busy with work.
- Setting up Stripe proved to be relatively straightforward and not many issues were encountered, aside from styling the card-details field in order to match the rest of the checkout form. After consulting Stack Overflow and some trial-and-error, this too was resolved.
- Webhooks were set-up but testing will be done after deployment as Stripe no longer supports webhook testing.
- 3 bugs were discovered while working on implenting Stripe functionality, and while not directly related to it, they were still resolved as they proved to be quite simple and Stripe even helped understand why the delivery cost was not being displayed correctly.
