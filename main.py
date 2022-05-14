import instaloader

L = instaloader.Instaloader()

USER = input('Введите имя своего аккаунта:')
PASSWORD = input('Введите пароль своего аккаунта:')

L.login(USER, PASSWORD)

account = input('Введите имя аккаунта для скачивания:')

L.download_profile(account, profile_pic=False, profile_pic_only=False, fast_update=True, download_stories=True, download_stories_only=False, download_tagged=False, download_tagged_only=False, post_filter=None, storyitem_filter=None)
