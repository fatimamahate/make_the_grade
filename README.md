<h1 align="center">Make The Grade</h1>

* [Live project link](https://make-the-grade.herokuapp.com/)

* [Repository Link](https://github.com/fatimamahate/make_the_grade)

Make The Grade is an application useful for students and teachers. Students (or users as in the code) can input their target grade and scores for the latest assessment. Make The Grade is designed so that students input their scores as soon as they recieve them. The application can (if needed for user) work out the average score needed on each remaining exam to meet their target score. This is especially useful for students working below their average grade. 

Teachers receive a School ID which is unique to that particular school. The School ID can be shared with students along with their own unique User ID. Both the School ID and User ID are meant to be kept secret so only those who schools who have 'subscribed' to the Make The Grade service can access it. Furthermore, this ensures data cannot be mixed about and people who are not 'subscribers' of the service cannot access the service with random numbers. 

All of the data regarding each student- as well as each school is stored in Google Sheets. 

## Contents

 * User Experience
* Features
* Design
 * Technologies Used
* Testing
 * Deployment
 * Credits
 * Acknowledgements

## User Experience
Users of the application should be able to:

* Input correct, valid ID's
* Input target (if user hasn't already done so)
* Check what data is already in the database
* Input assessment data in a consecutive manner
* Find out how much they need iin each of the remaining exams to reach target. 
* Find out if they have reached/exceeded target.

## Features
1. A welcome message to user.
    1. Asks user for School ID - A thank you message pops up for correct id
    2. Asks user for User ID - A thank you message pops up for correct id
2. 
## Design

## Technologies Used
* [Python](https://www.python.org/)

## Testing

## Deployment
### Clone a repository
* To clone a repository, go to the GitHub repository.
* Click on Code
* Copy the link
* Open GitBash
* Type in git clone, copy your URL and press enter.

### Deploy to Heroku
* Create login with Heroku
* Click on 'Create New App'
* Name your file- name must be unique
* Select the region that you are in
* Navigate to and click on the settings tab
* Navigate to the Config vars section of page.
* In the 'Key' Field, type CREDS
* Then copy requirments.txt file contents into Value field.
* Then click 'Add'
* Add another, with 'Key' field as PORT and the 'value' as 8000
* Click on 'Add buildpack"
* Select 'Python' and then save changes.
* Repeat last two steps but this time select node.js and then save changes
* Navigate to deply section at the top
* Select Github (if it is your first time using heroku you may need to verify your account by typing in your password.)
* Look for the github repository with the code
* Select automatic deploy

### Use the Google Sheets API
#### Creating a Google Sheet
* Visit [the Google Sheets](https://docs.google.com/spreadsheets/u/0/) website and if needed create an account
* Navigate and click on blank to create a blank worksheet
* Insert your data into the cells on the sheet

#### Google Drive API - to generate credentials
* Visit [the Google Cloud Platform](https://console.cloud.google.com/getting-started) website.
* If not already, create an account.
* Select 'Select a project'
* Select new project
* Name your porject
* Click 'Select Project'
* On the side, click on 'APIs and services' and then click on 'Library'
* Search for Google Drive in the search bar 
* Click on Google Drive API
* Click on 'Enable'
* Click on 'Create Credentials'
* For the following questions choose the answers that follow the question
1. Which API are you using?
Google Drive API
2. What data will you be accessing?
Application Data
3. Are you planning to use this API with Compute Engline, Kubernetes Engine, App Engine or Cloud Functions?
No, I am not using them
* Then click on 'Next'
* Type in a service account name - try the name of the project
* Click on 'create'
* In the role dropdown, select 'Basic' then 'Editor'
* Click 'continue'
* Then click 'done'
* In the 'Credentials' tab, navigate to the Service Account that is created
* Then click on 'Keys'
* Navigate and click on 'Add Key'
* Choose 'Create New Key'
* Select 'JSON' (recommended)
* Credentials are downloaded on your device.
* Copy file into your GitPod editor for this particular project
* Rename to creds.json
* In .gitignore add this file name

#### Google Sheets API
* On the same website as above
    * In the search bar, search for 'Google Sheets'
    * Select 'Google Sheets API'
    * Click on 'Enable'

## Credits
* In order to amend data for a specific student, I temporarily [deleted](https://itecnote.com/tecnote/python-how-to-delete-remove-row-from-the-google-spreadsheet-using-gspread-lib-in-python/) the row and rejoined at the end of the table with the new data.
* Love Sandwiches was also important to the understanding of this project.


## Acknowledgements
Thank you to my mentor, Brian Macharia, who provided invaluable, constructive feedback on this PP3 project. 
