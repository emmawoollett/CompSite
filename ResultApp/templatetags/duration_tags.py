from django import template

register = template.Library()


@register.filter
def duration(timedelta):
    if timedelta in (None, ''):
        return ''
    total_seconds = int(timedelta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds % 60)
    if hours:
        return '%s:%02.d:%02.d.%.1s' % (hours, minutes, seconds, timedelta.microseconds)
    elif minutes:
        return '%02.d:%02.d.%.1s' % (minutes, seconds, timedelta.microseconds)
    else:
        return '%02.d.%.1s' % (seconds, timedelta.microseconds)