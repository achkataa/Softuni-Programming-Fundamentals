class Comment():
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes
    def zdr(self):
        print(self.username)
        print(self.content)
        print(self.likes)

comment = Comment("user1", "I like this book")

comment.zdr()