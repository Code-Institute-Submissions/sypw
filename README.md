# Sort Your Paperwork (SYPW)
## Milestone Project 4 by Stan Kaczorkiewicz

The main idea behind this project is the conversation I once had with my
fiancee, where we've been wondering how much paper her employer wastes for
payslips, that they send to all 80 000 emploees every week.
This was over a year ago, but that was the moment when the idea for an app that will sort this problem out appeared.
I know that there are many similar apps, my last company was using one of them,
but it looks like there is a market demand for more, so why not make one.

My main assumption was to make it as simple as it's possible, in order to work.
I also wanted to leave some potential for future development and more features.


# UX

I wanted this app to be ineractive, intuitive, responsive and user-friendly. Although now I think, that the name (SYPW = Sort Your PaperWork) might be slightly confusing.

To make it intuitive, I used Bootstrap tools, and I chose light-blue and blue colors, as it is my favourite color and it has generally positive associations.

My first idea for the look of SYPW was: ![alt text](https://github.com/MrColorado35/sypw/blob/master/media/plan_1.jpg) and [here](https://github.com/MrColorado35/sypw/blob/master/media/plan_2.jpg). It did not really change a lot, except for homepage look and payslips functionality.

## User
I identified a User as a manager of small to middle-size company and their team. (With the payment system changed from test to real and further database development, it can be more, of course.) 


To begin with, I assumed, that this app will only be used by one company, so we don't need to worry about sorting users by company and divide access to some parts of the website just yet.

## User goals and stories
* Manager wants to contact whole team at once
* Team member wants to book holiday, while in the pub with friends (less than six of course)
* Everyone in the company wants to see if they got paid the correct amount for their job
* App owner/ creator, that wants to get paid for his job
* Management having a choice of how long they want to use this app for,
* Management having ability to pay for the use of this app
* Management need to have an access to history of their payments for tax purposes
* Every team member can have their say in every conversation, and also can start new topic in Forum

# Features
## Across whole app
User can navigate across the whole app by using top navbar. User that is not logged in can only access the extended homepage and payment path, in order to protect the rest of the app content from being exposed to someone external from the company it was intended for. <br>
Via the links in the footer, any user can access my social media, or find some great music.
#

## Home page
For registered users, main page has links to all features of the app, and also some more good music.

Homepage for unregistered user has short description of the reason behind this app and features that my app provides. It has some pictures to be more visually appealing. It also contain two of "User's Opinions", to give it some more credibility.

To make it easier for User to pay for the app, there are five links accross the page to get to the payment path. As for now everyone can pay, although the goal is that only manager will pay, the rest of the team will use this app for free. I described that idea in more details in next section.
#

## Payment path
Entering in any one link on the homepage, will bring User to the page with the **illusion of choice**,
where the User needs to declare size of their company.
As for now it does not makes any difference for the price shown on the next page, but leaves great potential for future development.

After choosing that, User is being redirected to **product page**, wherethey have a choice of a level of subscription. As one of the requirements for this project was to have valid payment system, instead of creating an actual subscription, there are three products: 
- one month usage,
- six months of access,
- one year of use.

Once User chooses the product that meets their needs, the app will redirect them to **bag page**, where they can double check their choice, it's cost and come back to choose different option if they changed their mind. The picture of an old man with the thumb up, that appears on the large screens is meant to be a psychological trick, to make User more confident with their choice.
*At some point I wanted to delete the whole bag app, but I realised that it can be more confusing for user, if they don't feel like they can change their mind (or have to use "back" button to do it) so I decided to leave it the way it is.*

## Checkout
On the Checkout page User needs to fill in the form, where they need to provide their name and e-mail, then "details for VAT receipt" ( I don't really know what's needed for that, so it has all the fields for phone and address, like every internet store).
It also contains Order Summary, so our User can see what they pay for. The picture of the drone is unrelated directly with My app functions. Drone is, however, a creation of technology of last few years and as such, still considered advanced technology- just like paperless holiday forms and payslips in many companies.
*To be honest there was a need for some picture there, otherwise an empty space looks unatractive*

On the bottom, User has once again an option to change their choice, or to pay if they are happy with it. The reason for difference in a colour of the buttons is to make sure, that they will not click the wrong one.
#

## After payment
While the order is being processed, whole page is covered by animation commonly associated with 'loading page'. Once it's done, User is being redirected to 'Checkout Success' page, where they can 
see all details of their order, including date and order number. This is also the very last page that User can access without an account. From here every User can get some more great classical music, or see their account (or create one).
#

## Profile app
Once User created an account, they can see and update all personal details. 
This is also a place where they can view their order history.
Right now changing Company's name and number of team members is disabled, as all default users for first (current) version of this app
are supposed to belong to one team in the same company.
In the future version, only manager will be able to see and edit "company" fields. Another option for the future is manager's ability to add or remove
their team member's account, that will be placed here as well.
#

## Holiday 
In the holiday app, user has an ability to apply (paperless) for annual leave at any time. Until the manager_user will be introduced, all holiday requests will be sent to company email, that comes from settings.
Holiday Form has DateTimePicker from Bootstrap, to be able to see an actual calendar and to ensure all dates will be written in the same format.
Firstly, my idea for holiday form was different, but then I found [this video](https://www.youtube.com/watch?v=rHZwE1AK1h8) and decided that I like it better.

Once the contact form is submitted, User is redirected to 'see_holiday' template. I didn't want it to be blank (or to simply redirect User to homepage), so there is a calendar (source in 'Credit' section),
where User can see their desired dates, count when there will be a weekend etc.

#
## Payslips
My first Idea for payslips app was simple- manager will place each of his colleagues salary in the right place and then magic will happen. 
Then I looked at my own paper payslip and I understood how wrong I was.
There are whole complicated programmes to enable whole HR teams to sort out all those Tax-Insurance-Pension-Other_Contributions-Salary dependencies. 
I am now drastically aware about my lack of knowledge in this matter.
As such, this whole app will need to be changed to only allow User with access to their payslip, and hr_team to upload ready payslip files, instead of creating them here (although it could be a good oportunity for further development if this app will ever be actually used commercially).

#

## Forum (Comunicado)
I was going to call that app 'messages' but in Django that name is reserved for Django's messages (I didn't know that before I tried). 
*The actual name of it came to me by accident as I'm currently learnning Spanish and it sounds Spanish. I didn't know that it's an actual Spanish word for notice or release, that actualy matches it's function. Even more surprising to me was the fact, that this word also exist in English and means **a brief report for immediate publication** that is also quite adequate.*

While starting with this app, I thought about direct messages between users, but that would be just a copy of emails, that are a nightmare of all 
office workes around the world.
The idea for this form of comunication between users comes from [here](https://data-flair.training/blogs/discussion-forum-python-django/).
It is probably most complex app of this project and creation of it took me a lot of time.

The main problem I had with it was to save user's name automatically to their posts and messages, also to match discussion with Forum and to add right email. 
For a little while 'name' and 'email' in Forum part and also 'nick' and 'forum' in Discussion was enabling User to add any name of any user registered in database.
That would leave a lot of room for corruption or spam messages.
After trying to figure it out by myself for nearly 4 days (I almost did that once, but then another error occured and I didn't realise that it has other reason), I asked Code Institute's Tutors for help.
It took three tutor's to find what's wrong (what implies that some of them are not the most competent for this job), but finally Scott was able to find the bug and explain to me what am I doing wrong.
Once he showed me one example of right approach to that task, I quickly fixed all of the other issues I had there.
The latest idea was to block users from deleting or editing posts that were created by someone else. I achived that by creating new variable called 'author' and checking if it matches current user. I was even able to share that idea with another CI student on our Slack, as he was struggling with the same matter.

Here I also need to explain, that I left quite a lot of commented code
in comunicado/views.py in order to have a quick access to ability of editing and deleting other's posts and messages in the 'old' way.
Once the profile levels will be created, I'm going to allow users to edit their own posts, and managers to edit or delete all posts (as censorship might be neccessary for all bunch of reasons).

Also it's worth to be mentioned, that I personally like the layout of messages on the small screen, with name leaning towards the left and buttons leaning towords the right side of the screen, creating stairs-like shape on the screen.
I found it sort of funny and I believe it matches the whole SYPW theme.

# Features left to implement

* As I mentioned couple of times above, main feature this website needs to be competitive on the market is leveling system for the user profiles. As for now, admins/managers abilities are available only to superusers, using standard django levels. The goal is to implement at least three different levels of User- manager_user, ht_team and user (team member)/

* Holiday app works fine for now, but my idea for developing it in the future is to change the calendar for one, where user will be able to see not only all his/her holiday but also holiday of other members of their team.

* Payslips, as described above, will only provide ability to paste ready payslip file for hr_team members. Except that, every user will only have an access to their own paylips.

* Possibility to adjust app content depending on Company- so I could earn real money on this projet at some point.

# Technologies

In this project, I used following technologies:
* HTML5 to structure the page;
* CSS3 for adding the style;
* Bootstrap 4 for intuitive navigation and easy styling;
* JavaScript to add functionality and logic;
* Django as main core for whole projec;
* jQuery for finding elements in the DOM tree;
* GitPod as an enviroment for my workspace;
* GitHub for version control and to store all files;
* FontAwesome to get some fancy icons;
* Google Fonts for the fonts I'm using accross the pages;
* Gmail to send real messages in Production;
* Developer Tools (build-in feature of Google Chrome), that allowed me to apply all the changes I intened to make and to see their effects (or lack of effect in many cases) immediately;
* [jshint](https://jshint.com/) for final, automatic tests of my JavaScript (although it does not recognise the jQuery);
* To beautify my code I used [that program](https://codebeautify.org/)
* [Stripe](https://stripe.com/gb) to enable payment system


# Testing 

During the process of creation of SYPW, I was constantly testing all new functionalities using both, GitPod and Google Chrome Dev Tools.
Some of those tests effects I already described in Forum section.
Sometimes painful process of constant manual tests, was rewarded with all intended functionality to work in harmony, and (hopefully) giving nice and smooth User Experience.

I've also done some automatic tests form my static files and all HTML. It's worth to mention, that because of use of the Jinja language, most of HTML validators recognize it as an error and don't want to cooperate any more.

Another interesting issue that I encountered while testing, was that all Forum Topics stopped working, once I introduced automatic user adding function.
It happened because previous version allowed User to Write any name as an author, so they did not match the ones in database.
To fix that I had to turn back all the changes, delete all Topics and then start again.
Luckily I did not push changes to Heroku yet, so I had time to clear the Forum in Production, before error occured.

# Deployment
I used Heroku to store my app in production and AWS to store all media and static files. As it was my third project using S3 in AWS was less painful than previously, but still required me to rely on Code Institute example. 

In order to make migrations to Heroku easier, I decided to leave commented database part in settings file, 
as now it only requires 3 clicks and paste of my database URL, instead of changing whole function, as I did before.

In this project I did not push all of my changes to Heroku every day, like I did in my previous projects.
Quite a few times when at the end of the day I encountered a bug or an issue, I refrained from sending it to Heroku, so my live app could still work, even if dev version crashed. 
Then I pushed it to Heroku once everything (or at least most critical parts) were fixed.
I really liked it more that way.
Also couple of times I encountered an issue in heroku app, even if it worked in Production.
To fix that I had to set DEBUG to True in Heroku Config Vars, so I could see where the problem was.



# Credit
First of all I would like to say Thank You to **Scott**, Tutor from Code Institute, that helped me to understand Many_to_one dependencies and fix my Forum app.

I'm also grateful to my mentor, **Reuben Ferrante** for his patience and valuable feedback, that I received quite a few times during development of SYPW.

While making this project I was inspired by the ButiqueAdo app, which is a Django project of the Code Institute, that I accomplished in August.

Almost all of the pictures used on this side, come from [here](www.unsplash.com), which is a great source of free photos. Those that don't come from there, have been taken by myself.

Idea for Calendar that only appears after you set the right vale comes from [here](https://codepen.io/tmrDevelops/pen/yHDge), but has been found [on this website](https://uicookies.com/bootstrap-calendar/)

I also would like to say Thank You to the author of [this video](https://www.youtube.com/watch?v=2KqhBkMv7aM) as I found it helpful during the process of creation of this app.
