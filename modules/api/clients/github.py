import requests


class GitHub:
    
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            " https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    def get_emoji(self):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()

        return body
    
    def list_public_events(self, id):
        r = requests.get(f'https://api.github.com/events/{id}')
        body = r.json()

        return body
    
    def list_of_following_users(self, username):
        r = requests.get(f'https://api.github.com/users/{username}/following')
        body = r.json()

        return body