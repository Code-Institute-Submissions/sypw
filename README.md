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
#

## Profile app
Once User created an account, they can see and update all personal details. 
This is also a place where they can find all their order history.
Right now changing Company's name and number of team members is disabled, as all default users for first (current) version of this app
are supposed to belong to one team in the same company.
In the future version, only manager will be able to see and edit "company" fields. Another option for the future is manager's ability to add or remove
their team member's account, that will be placed here as well.
#

## Holiday 
In the holiday app, user has ability to apply (paperless) for holiday at any time. Until the manager_user will be introduced, all holiday requests will be sent to company email, that comes from settings.
Holiday Form has DateTimePicker from Bootstrap, to be able to see an actual calendar and to ensure all dates will be written in the same format.
Firstly, my idea for holiday form was different, but then I found [this video](https://www.youtube.com/watch?v=rHZwE1AK1h8) and decided that I like it better.

Once the contact form is submitted, User is redirected to 'see_holiday' template. I didn't wanted it to be blank (or to simply redirect User to homepage), so there is a calendar (source in 'Credit' section),
where User can see their desired dates, count when there will be a weekend etc.

#
## Payslips
My first Idea for payslips app was simple- manager will place each of his colleagues salary in the right place and then magic will happen. 
Then I looked at my own paper payslip and I understood how wrong I was.
There are whole complicated programms to enable whole HR teams to sort out all those Tax-Insurance-Pension-Other_Contributions-Salary dependencies. 
I am now drastically aware about my lack of knowledge in this matter.
As such, whole this app will need to be changed to only allow User with access to their payslip, and hr_team to upload ready payslip files, instead of creating them here (although it could be good oportunity for further development if this app will ever be actually used commercially).

#

## Forum (Comunicado)
I was going to call that app 'messages' but in Django that name is reserved for Django's messages (I didn't know that before I tried). 
*The actual name of it came to me by accident as I currently learn Spanish and it sounds Spanish. I didn't know that it's actual Spanish word for notice or release, that actualy matches it's function. Even more surprised me fact, that this word also exist in English and means **a brief report for immediate publication** that is also quite adequate.*

While starting with this app, I thought about direct messages between users, but that would be just a copy of emails, that are nightmare of all 
office workes around the world.
The idea for this form of comunication between users comes from [here](https://data-flair.training/blogs/discussion-forum-python-django/).
It is probably most complex app of this project and creation of it took me a lot of time.

The main problem I had with it was to save user's name automatically to their posts and messages, also to match discussion with Forum and to add right email. 
For a little while 'name' and 'email' in Forum part and also 'nick' and 'forum' in Discussion was enabling User to add any name of any user registered in database.
That would leave a lot of room for corruption or spam messages.
After trying to figure it out by myself for nearly 4 days (I almost did that once, but then another error occured and I didn't realise that it has other reason), I asked Code Institute's Tutors for help.
It took three tutor's to find what's wrong (what implies that some of them are not most competent for this job), but finally Scott was able to find the bug and explain me what am I doing wrong.
Once he showed me one example of right approach to that task, I quickly fixed all of the other issues I had there.
The latest idea was to block users from deleting or editing posts that was created by someone else. I achived that by creating new variable called 'author' and checking if it match current user. I was even able to share that idea with another CI student on our Slack, as he was struggling with the same matter.

Here I also need to explain, that I left quite a lot of commented code
in comunicado/views.py in order to have quick access to ability of editing and deleting other's posts and messages in the 'old' way.
Once the profile levels will be created, I'm going to allow users to edit their own posts, and managers to edit or delete all posts (as censorship it might be neccessary for all bunch of reasons).

Also it's worth to be mentioned, that I personally like the layout of messages on the small screen, with name leaning towards the left and buttons leaning towords the right side of the screen, creating stairs-like shape on the screen.
I found it sort of funny and I belive it matches whole SYPW theme.

# Features left to implement

As mentioned couple times above, main thing this website needs is leveling of the user profiles. 

Also in holiday app I want user to be able to see their holidays on the calendar that will be displayed there.

Payslips functionality will also need a lot of work done.

And finally view of whole app will be different for user, manager_user and hr_team.





# Credit

To beautify my code I used [that program](https://codebeautify.org/)

First of all I would like to say Thank You to Scott, Tutor from Code Institute, that helped me to understand Many_to_one dependencies and fix my Forum app.

While making this project I was inspired by the ButiqueAdo app, which is Django project of the Code Institute, that I accomplished few weeks ago.

Almost all of the pictures used on this side, come from [here](www.unsplash.com), which is a great source of open source photos. Those that doesn't come from there, belong to me.


Idea for Calendar that only appears after you set the right vale comes from [here](https://codepen.io/tmrDevelops/pen/yHDge), but has been found [on this website](https://uicookies.com/bootstrap-calendar/)

I also would like to say Thank You to the author of [this video](https://www.youtube.com/watch?v=2KqhBkMv7aM) as I found it helpful
