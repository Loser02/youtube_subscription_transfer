# YouTube Data Transfer

This script allows you to transfer your YouTube subscriptions.

## Prerequisites

To use this script, you need to have Python installed on your system, along with the following packages:

- `google-auth`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `google-api-python-client`

You can install the required packages using pip: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client


YOU NEED THE .JSON FILE TO RUN THIS AND ADD TEST USERS SO API ISNT BLOCKED SO PLEASE DO THAT BY= 

1. MAKE THE client_secrets.json FILE:
STEP 1=Go to the https://console.cloud.google.com/
STEP 2=Sign in with your Google account if you haven't already.
STEP 3=Click the "Select a project" dropdown at the top, then click "New Project" in the top-right corner of the dialog (dont need to edit name or organization) and click create.
<img width="1920" alt="image" src="https://user-images.githubusercontent.com/127698874/235308735-974d034a-4ad0-40d7-8e55-83032d7e7963.png">
STEP 4=In the left-hand menu, navigate to "APIs & Services" > "Library."
<img width="1920" alt="image" src="https://user-images.githubusercontent.com/127698874/235308874-ee86157d-53de-47a0-aae8-ef713df5b397.png">
<img width="1919" alt="image" src="https://user-images.githubusercontent.com/127698874/235308910-9bc01c9b-870c-4a2f-a016-13333629c4e8.png">
STEP 7:In the search bar, type "YouTube Data API v3" and select it from the results.
<img width="1920" alt="image" src="https://user-images.githubusercontent.com/127698874/235308959-78951754-4874-47bb-8107-449197a37c9e.png">
STEP 8=Click "Enable" to enable the YouTube Data API v3 for your project. that will take you to this screen=<img width="1920" alt="image" src="https://user-images.githubusercontent.com/127698874/235309005-017c12cd-6eef-4908-8d1a-5ecd9b7f6426.png">
STEP 9=After the API is enabled, click "Create Credentials" in the top-right corner.
<img width="1920" alt="image" src="https://user-images.githubusercontent.com/127698874/235309038-77499e94-e5d4-4440-93c5-e039c6e5b1a5.png">
STEP 10=In the "Add credentials to your project" page, select "YouTube Data API v3" for "Which API are you using?" and check user data and click next.
<img width="441" alt="image" src="https://user-images.githubusercontent.com/127698874/235309251-0b211b90-8895-4212-9f93-98956b3ff2cb.png">
STEP 11=fill in any app name and your email address= <img width="464" alt="image" src="https://user-images.githubusercontent.com/127698874/235309363-8ac81f56-5bdb-4a89-88c8-0c3a937d18a4.png">
STEP 12=click add or remove scopes and type https://www.googleapis.com/auth/youtube.force-ssl into search bar. check it and then update and then save and countinue. <img width="1920" alt="image" src="https://user-images.githubusercontent.com/127698874/235309494-867a3cd7-2ba2-4ed2-8e86-c1c2f7f29399.png">
STEP 13=select desktop app and click create <img width="450" alt="image" src="https://user-images.githubusercontent.com/127698874/235309570-d53fa4ca-81de-495a-a8d4-df59b20a2f3f.png">
STEP 14=download and save the file as client_secrets.json in the same directory as the python script. <img width="889" alt="image" src="https://user-images.githubusercontent.com/127698874/235309691-0b031879-3ba0-488e-8bf7-22f211529c5d.png">

2. ADDING ACCOUNTS TO TESTERS:
STEP 1=Go to the https://console.cloud.google.com/
STEP 2=In the left-hand menu, navigate to "APIs & Services" > "OAuth consent screen." <img width="1923" alt="image" src="https://user-images.githubusercontent.com/127698874/235309806-c691e2c1-b26c-4bdb-8ac6-4647940e0ea7.png">
STEP 3=Scroll down to the "Test users" section.
Click "Add Users" to add test users.
Enter the email addresses of the Google accounts you'd like to grant access to your app. These should be the email addresses of the source and target accounts you want to transfer data between. Click "SAVE" to save the test users. <img width="1920" alt="image" src="https://user-images.githubusercontent.com/127698874/235309879-8652d891-6ff9-40c4-b9aa-52a7d4ac148a.png">

## Usage

1. Open a terminal or command prompt and navigate to the directory containing the `transfer_youtube_data.py` script and the `client_secrets.json` file.

2. Run the script: python transfer_youtube_data.py

3. The script will prompt you to authorize access to your Google accounts. First, authorize the source account (the account you want to transfer data from) and then the target account (the account you want to transfer data to).

4. The script will transfer your YouTube subscriptions and playlists. Watch history cannot be transferred due to API limitations.

5. Once the transfer is complete, the script will display a confirmation message.

(dont forget to copy the python script)

## Note

Please keep your `client_secrets.json` file private and secure. It contains sensitive information about your Google API project, and sharing it could expose your project to unauthorized access or potential abuse.

also the script might say it has finished transferring but if it didnt transfer all of them then that means you have reached the daily quota and have to do it again in 24 hours 

