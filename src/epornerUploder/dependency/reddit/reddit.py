from selenium.webdriver.common.by import By

class RedditWrapper:
    def __init__(self,reddit,json,db) -> None:
        self.reddit=reddit
        self.json=json
        self.db=db

    def get_ip(self):
        return self.reddit._core._requestor._http.proxies

    def get_account_banned_status(self):
        return self.reddit.user.me().subreddit.user_is_banned
    
    def get_random_name(self,browser):
        random_name_url="https://old.reddit.com/api/v1/generate_username.json"
        browser.get(random_name_url)
        body=browser.find_element(By.CSS_SELECTOR,"body").text
        body=self.json.loads(body)
        return body["usernames"][0]

    def scrape_top_posts_from_subreddit(self,subreddit):
        subreddit=self.reddit.subreddit(subreddit).top("month",limit=25)
        return [item for item in subreddit]
            

    def get_subreddits_by_type(self,type):
        collection="subreddits"
        collections=self.db.find_one(collection,{'type':type})
        return [item for item in collections["subreddits"]]
    
    def get_posts(self):
        collection="posts"
        return self.db.find_all(collection)
    
    def post_with_title_url(self,subreddit,title,url):
        account=self.reddit.user.me() 
        banned= any(account.subreddit.banned())

        if not banned:
            subreddit=self.reddit.subreddit(subreddit)
            subreddit.submit(title=title,url=url)
        else:
            raise Exception(f"Banned on {subreddit}")
    
    def pin_to_post(self,subreddit,title,url):
        subreddit=self.reddit.subreddit(f"u_{subreddit}")
        submisson=subreddit.submit(title=title,url=url)
        submisson.mod.sticky()
    
    def get_top_post_of_account(self,author):
        subreddit=self.reddit.subreddit(f"u_{author}").top("month",limit=25)
        return [item for item in subreddit]
        
    def get_top_subreddit_comments(self,subreddit):
        comments=self.reddit.subreddit(subreddit).comments(limit=50)
        return [ comment for comment in comments ]
    
    def reply_to_comment(self,comment,text):
        return comment.reply(text)
    
    def get_current_user(self):
        return self.reddit.user.me()
    
    def delete_all_submission(self,username):
        user=self.reddit.redditor(username)
        submission=user.submissions.new(limit=None)
        for sub in submission:
            sub.delete()
