class Posts:
    def __init__(self, id, title, content, views, user_account_id, comments = []):
        self.id = id
        self.title = title
        self.content = content
        self.views = views
        self.user_account_id = user_account_id
        self.comments = comments
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.views}, {self.user_account_id})"