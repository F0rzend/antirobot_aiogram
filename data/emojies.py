from dataclasses import dataclass


@dataclass
class Emoji:
    unicode: str
    subject: str
    # имя в винительном падеже используется для переводов и удобного использования в тексте "нажмите на" + name
    name: str


emojies = (
    Emoji(unicode=u'\U0001F48D', subject='ring', name='кольцо'),
    Emoji(unicode=u'\U0001F460', subject='shoe', name='туфлю'),
    Emoji(unicode=u'\U0001F451', subject='crown', name='корону'),
    Emoji(unicode=u'\U00002702', subject='scissors', name='ножницы'),
    Emoji(unicode=u'\U0001F941', subject='drum', name='барабан'),

    Emoji(unicode=u'\U0001F48A', subject='pill', name='пилюлю'),
    Emoji(unicode=u'\U0001F338', subject='blossom', name='цветок'),
    Emoji(unicode=u'\U0001F9C0', subject='cheese', name='сыр'),
    Emoji(unicode=u'\U0001F3A7', subject='headphone', name='наушники'),
    Emoji(unicode=u'\U000023F0', subject='clock', name='часы'),

    Emoji(unicode=u'\U0001F951', subject='avocado', name='авокадо'),
    Emoji(unicode=u'\U0001F334', subject='palm', name='пальму'),
    Emoji(unicode=u'\U0001F45C', subject='handbag', name='сумку'),
    Emoji(unicode=u'\U0001F9E6', subject='socks', name='носки'),
    Emoji(unicode=u'\U0001FA93', subject='axe', name='топор'),

    Emoji(unicode=u'\U0001F308', subject='rainbow', name='радугу'),
    Emoji(unicode=u'\U0001F4A7', subject='droplet', name='каплю'),
    Emoji(unicode=u'\U0001F525', subject='fire', name='огонь'),
    Emoji(unicode=u'\U000026C4', subject='snowman', name='снеговика'),
    Emoji(unicode=u'\U0001F9F2', subject='magnet', name='магнит'),

    Emoji(unicode=u'\U0001F389', subject='popper', name='хлопушку'),
    Emoji(unicode=u'\U0001F339', subject='rose', name='розу'),
    Emoji(unicode=u'\U0000270E', subject='pencil', name='карандаш'),
    Emoji(unicode=u'\U00002709', subject='envelope', name='конверт'),
    Emoji(unicode=u'\U0001F680', subject='rocket', name='ракету'),
)

__all__ = [
    'emojies'
]
