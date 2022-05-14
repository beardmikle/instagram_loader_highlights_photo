import instaloader
from instaloader import Profile, Post

instance = instaloader.Instaloader()

instance.login(user=input("Введите ваш логин:"),passwd=input("Введите ваш пароль:"))

profile = Profile.from_username(instance.context, username=input("Введите аккаунт для скачивания:"))

for highlight in instance.get_highlights(user=profile):
    for item in highlight.get_items():
        instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))

instance.download_profile(profile_name=profile)

