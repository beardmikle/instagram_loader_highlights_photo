import instaloader
import self as self

L = instaloader.Instaloader()

USER = input('Введите имя своего аккаунта:')
PASSWORD = input('Введите пароль своего аккаунта:')

L.login(USER, PASSWORD)

account = input('Введите имя аккаунта для скачивания:')

L.download_profile(account, profile_pic=True, profile_pic_only=True, fast_update=True, download_stories=True, download_stories_only=True, download_tagged=True, download_tagged_only=True, post_filter=None, storyitem_filter=None)
# # L.download_highlights(self,
#                             user: Union[int, Profile],
#                             fast_update: bool = False,
#                             filename_target: Optional[str] = None,
#                             storyitem_filter: Optional[Callable[[StoryItem], bool]] = None)
