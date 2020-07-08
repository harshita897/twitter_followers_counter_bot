# twitter_followers_counter_bot
This bot will automatically update your profile name with the amount of followers
Twitter API Authentication
Step 1: Apply for a Twitter dev account

Next step is to create the Twitter API credentials from the Twitter Developer site. Here, you have to select the Twitter user responsible for this account. It should probably be you or your organization.

Step 2: Create an Application

Twitter grants authentication credentials to apps, not accounts. An app can be any tool or bot that uses the Twitter API. So you need to register your an app to be able to make API calls.

To register your app, go to your Twitter apps page and select the Create an app option.

You need to provide the following information about your app and its purpose:

App name: a name to identify your application (such as examplebot) Application description: the purpose of your application Your or your application’s website URL: required, but can be your personal site’s URL since bots don’t need a URL to work Use of the app: how users will use your app

Step 3: Create the Authentication Credentials

To create the authentication credentials, go to your Twitter apps page again. Here you’ll find the Details button of your app. Clicking this button takes you to the next page, where you can generate the credentials.

By selecting the Keys and tokens tab, you can generate and copy the key, token, and secrets to use them in your code

Step 4: Install tweepy
Running the bot
If you exported the API credentials succesfully you can run the bot by:

python update_profile_follow_counter.py


Author
Harshita Agarwal
