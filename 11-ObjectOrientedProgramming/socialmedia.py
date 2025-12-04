class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts+=content
        print(self.posts)
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        print(f'{self.username} has these posts: ')
        for i in range(len(self.posts)):
            print(f'{i+1}. {self.posts[i]}')
def main():
    user1=SocialMediaProfile('Paravojik')
    user1.add_post('hello')
    user1.add_post('bye')
    user1.display_timeline()
    user2=SocialMediaProfile('johndoe')
    user2.add_post('Hello, world!')
    user2.add_post('Had a great day at the park!')
    user2.add_post("What's up, Natalie? How are you?")
    user2.display_timeline()

if __name__=="__main__":
    main()