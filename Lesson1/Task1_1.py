while (True):
    duration = int(input('duration = '))
    if duration < 60:
        print(duration, 'сек')
    elif 60 <= duration < 3600:
        minutes = duration // 60
        seconds = duration % 60
        print(minutes, 'мин', seconds, 'сек')
    elif 3600 <= duration < 86400:
        hours = duration // 3600
        minutes = (duration - (hours * 3600)) // 60
        seconds = (duration - (hours * 3600) - (minutes * 60))
        print(hours, 'час', minutes, 'мин', seconds, 'сек')
    elif duration >= 86400:
        days = duration // 86400
        hours = (duration - (days * 86400)) // 3600
        minutes = (duration - (days * 86400) - (hours * 3600)) // 60
        seconds = (duration - (days * 86400) - (hours * 3600) - (minutes * 60))
        print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')