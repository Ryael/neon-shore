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

- This sprint began on 06/07/22 at 20:00 and ended at 08/07/22 at 00:30. The estimated story point total was 34 but the time taken to complete them all was closer to approximately 14 hours, which made this sprint a total success even with the extension described below.
- The biggest issue I encountered throughout this issue was trouble with templates and URL routing. This was the primary reason I had to extend the sprint by a day.
- UI, which included typography, logo, buttons, colours, and the navigation bar were all decided on with accordance with the client's vision and brand.
- Multiple issues arose with using SwiperJS and learning its intricacies, especially when it came to customising its navigation and pagination. Navigation proved to a big issue as it was difficult to position the navigation arrows and keep them responsive, with a compromise being found in using `position: absolute` and adjusting them with media queries. However, these media queries haven't been fully implemented yet and will be dealt with at a later time.
- Learning how to manipulate GSAP was relatively straight forward due to how expansive and detailed its documentation is, and allowed for a very easy implementation of the desired timing of the painting effect.
- A total of four bugs were encountered during this sprint and two of them were resolved. The remaining two will be attempted to be resolved during future sprints.
