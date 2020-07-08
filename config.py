# twitterbot/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv('eY9qQrIZaDuzkmg49NoXVThFX')
    consumer_secret = os.getenv('hKO2UOmHJ68d00UF3YLU84bYV5f82aKPk8krpfxex7lp7jXJFo')
    access_token = os.getenv('1256632516397731841-nhHPnZD8nJHxyRwZrch3Mk0WCDMg5s')
    access_token_secret = os.getenv('7vzEMP7eYTZVaznhTTnfPcmydk5DXO0Gebexbz3UD0jKW')

    auth = tweepy.OAuthHandler('eY9qQrIZaDuzkmg49NoXVThFX','hKO2UOmHJ68d00UF3YLU84bYV5f82aKPk8krpfxex7lp7jXJFo')
    auth.set_access_token('1256632516397731841-nhHPnZD8nJHxyRwZrch3Mk0WCDMg5s','7vzEMP7eYTZVaznhTTnfPcmydk5DXO0Gebexbz3UD0jKW')
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error creating API', exc_info=True)
        raise e
    logger.info('API created')
    return api
