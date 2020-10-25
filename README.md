# Sort Your Paperwork (SYPW)
## Milestone Project 4 by Stan Kaczorkiewicz

The main idea behind this project is the conversation I once had with my
fiancee, where we've been wondering how much paper her employer wastes for
payslips, that they send to all 80 000 emploees every week.
This was over a year ago, but that was a moment when the idea for an app that will sort this problem out appeared.
I know that there is many similar apps, my last company was useing one of them,
but it looks like there is a market demand for more, so why not to make one.

My main assumption was to make it as simple as it's possible, in order to work.
I also wanted to leave some potential for future development and more features.


# UX

I wanted this app to be ineractive, intuitive, responsive and user-friendly. Although now I think, that the name (SYPW = Sort Your PaperWork) might be slightly confusing.

To make use of it intuitive, I used Bootstrap tools, and I chose light-blue and blue colors, as it is my favourite color and it has generally positive reputation.

My first idea for the look of SYPW can be seen [here]() and [here]().

## User
I identified a User as a manager of small to middle-size company and their team. (With the payment system changed from test to real and further database development, it can be more of course.) 
<!-- For now let's call him Haydn, just like in my partner's case, which I described above. -->

To begin with, I assumed, that this app wll only be used by one company, so we don't need to worry about sorting users by company and divide access to some parts of the website just yet.

## User goals and stories
* Manager wants to contact whole team at once
* Team member wants to book holiday, while in the pub with friends (less than six of course)
* Everyone in the company, want to see if they got paid correct amount for their job
* App owner/ creator, that wants to got paid for his job
* Management having a choice of how long they want to use this app for,
* Management having ability to pay for the use of this app
* Management need to have an access to history of their payments for tax purposes
* Every team member can have their say in every conversation, and also can start new topic in Forum

# Features
## Across whole app
User can navigate across whole app by using top navbar. User that is not logged in can only access the extended homepage and payment path, in order to protect the rest of the app content from being exposed to someone external from the company it was intended for. <br>
Via the links in the footer, any user can access my social media, or find some great music.
#

## Home page
For registered users, main page has links to all features of the app, and also some more good music.

Homepage for unregistered user has short description of the reason behind this app and features that my app provides. It has some pictures to be more visually appealing. It also contain two of "User's Opinions", to give it some more credit.

To make it easier for User to pay for the app, there are five links accross the page to get to the payment path. As for now everyone can pay, although the goal is that only manager will pay, the rest of the team will use this app for free. I described that idea in more details in next section.
#

## Payment path
Entering in any one link on the homepage, will bring User to the page with the **illusion of choice**,
where the User needs to declare size of their company.
As for now it does not makes any difference for the price shown on the next page, but leaves great potential for future development.

After choosing that, User is being redirected to **product page**, where has a choice of level of subscription. As one of the requirements for this project was to have valid payment system, instead of creating an actual subscription, there are three products: 
- one month usage,
- six months of access,
- one year of use.

Once User choose the product that meets their needs, the app will redirect them to **bag page**, where they can double check their choice, it's cost and come back to choose different option if they changed their mind. The picture of an old man with the thumb up, that appears on the large screens is meant to be a psychological trick, to make User more confident with their choice.
*At some point I wanted to delete whole bag app, but I realised that it can be moe confusing for user, if they don't feel like they can change their mind (or have to use "back" button to do it) so I decided to leave it the way it is.*

## Checkout
On the Checkout page User needs to fill in the form, where they need to provide their name and email, then "detaild for VAT receipt" ( I don't really know what's needed for that, so it has all the fields for phone and address, like every internet store).
It also contain Order Summary, so our User can see what they pay for. The picture of the drone is unrelated directly with My app functions. Drone is, however, a creation of technology of last few years and as such, still considered advanced technology- just like paperless holiday forms and payslips in many companies.
*To be honest there was a need for some picture there, otherwise an empty space looks inatractive*

On the bottom, User has once again option to change their choice, or to pay if they are happy with it. The reason for difference in a colour of the buttons is to make sure, that they will not click the wrong one.
#

## After payment
While the order is being processed, whole page is covered by animation commonly associated with 'loading page'. Once it's done, User is being redirected to 'Checkout Success' page, where they can 
see all details of their order, including date and order number. This is also the very last page that User can access without an account. From here every User can get some more great classical music, or see their account (or create one).


## Payslips
After starting with Payslip basic database and model, I realised that this part is usually sorted by HR team, not management, so whole this part will need to be changed to only allow User with access to their payslip, and manager/hr_team to upload payslip files, instead of creating them here (although it can be good oportunity for further development if this app will ever be actually used commercially)



# Credit

To beautify my code I used [that program](https://codebeautify.org/)

While making this project I was inspired by the ButiqueAdo app, which is Django project of the Code Institute, that I accomplished few weeks ago.

Almost all of the pictures used on this side, come from [here](www.unsplash.com), which is a great source of open source photos. Those that doesn't come from there, belong to me.

The idea for this form of comunication between users comes from [here](https://data-flair.training/blogs/discussion-forum-python-django/)

<!-- Calendar as for 12/10/2020 comes from [this](https://codepen.io/hind-jai/full/GaxmYP) free library of bootstrap projects and has been found [here](https://colorlib.com/wp/bootstrap-calendars/) -->

Idea for Calendar that only appears after you set the right vale comes from [here](https://codepen.io/tmrDevelops/pen/yHDge), but has been found [on this website](https://uicookies.com/bootstrap-calendar/)

My first idea for contact form to apply for holiday were different, but then I found [this video](https://www.youtube.com/watch?v=rHZwE1AK1h8) and decided that I like it better.

I also would like to say Thank You to the author of [this video](https://www.youtube.com/watch?v=2KqhBkMv7aM) as I found it helpful
