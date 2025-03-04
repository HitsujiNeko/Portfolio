from django import template

register = template.Library()

# Skills のスキルレベルを星に変換するフィルタ
@register.filter(name='skill_level_to_stars')
def skill_level_to_stars(level):
    stars = '★' * level
    empty_stars = '☆' * (5 - level)
    return stars + empty_stars