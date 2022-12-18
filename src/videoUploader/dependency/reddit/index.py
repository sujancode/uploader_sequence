import praw
import json
from requests import Session, session

from dependency.database.index import getDatabaseWrapperInstance

from dependency.reddit.reddit import RedditWrapper

REDDIT_WRAPPER_INSTANCE=None


def getRedditWrapperInstance(username="",password="",client_id="",client_secret="",proxy="",create_new_instance=False):
    global REDDIT_WRAPPER_INSTANCE
    db=getDatabaseWrapperInstance()
    RedditClient=""
    try:
        session=Session()
        session.proxies['https']=proxy

        RedditClient=praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent=username.strip(),
            requestor_kwargs={'session': session},  # pass Session
        )
    except Exception as e:
        print(e)
    if create_new_instance:
        return RedditWrapper(reddit=RedditClient,json=json,db=db)
        
    if not REDDIT_WRAPPER_INSTANCE:
        REDDIT_WRAPPER_INSTANCE = RedditWrapper(reddit=RedditClient,json=json,db=db) 
    return REDDIT_WRAPPER_INSTANCE

    