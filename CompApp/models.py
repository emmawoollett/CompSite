from django.db import models
from django_extensions.db.fields import AutoSlugField


class Competition(models.Model):
    slug = models.SlugField(default='competition_name')
    competition_name = models.CharField(max_length=200)
    competition_date = models.DateField()

    def __str__(self):
        return self.competition_name

    def get_all_events(self):
        event_list = \
            list(self.cross_country_events.all()) + \
            list(self.track_events.all()) + \
            list(self.track_relay_events.all()) + \
            list(self.field_events.all()) + \
            list(self.swimming_events.all()) + \
            list(self.swimming_relay_events.all())
        return event_list

    class Meta:
        ordering = ['-competition_date']


class Event(models.Model):
    slug = AutoSlugField(populate_from=['competition', 'year_group', 'gender'])
    BOYS = 'M'
    GIRLS = 'F'
    GENDER_CHOICES = ((BOYS, 'Boys'), (GIRLS, 'Girls'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    YEAR_7 = '07'
    YEAR_8 = '08'
    YEAR_9 = '09'
    YEAR_10 = '10'
    YEAR_11 = '11'
    YEAR_CHOICES = (
        (YEAR_7, 'Year 7'),
        (YEAR_8, 'Year 8'),
        (YEAR_9, 'Year 9'),
        (YEAR_10, 'Year 10'),
        (YEAR_11, 'Year 11'),
    )
    year_group = models.CharField(max_length=2, choices=YEAR_CHOICES, default=None)

    class Meta:
        abstract = True

    def get_event_type(self):
        return self.__class__.__name__


class CrossCountry(Event):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='cross_country_events')

    def __str__(self):
        return '%s %s' % (self.get_year_group_display(), self.get_gender_display())


class TrackEvent(Event):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='track_events')
    distance_in_meters = models.IntegerField()
    HEATS = 'Heats'
    FINAL = 'Final'
    TRACK_CHOICES = ((HEATS, 'Heats'), (FINAL, 'Final'))
    track_choice = models.CharField(max_length=5, choices=TRACK_CHOICES, default=FINAL)

    def __str__(self):
        return '%s %s %sm %s' % (self.get_year_group_display(), self.get_gender_display(), self.distance_in_meters,
                                 self.track_choice)


class TrackRelay(Event):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='track_relay_events')
    number_of_students = models.IntegerField()
    distance_per_student = models.IntegerField()

    def __str__(self):
        return '%s %s %s by %sm' % (
            self.get_year_group_display(), self.get_gender_display(), self.number_of_students, self.distance_per_student)


class FieldEvent(Event):
    HIGH_JUMP = 'HJ'
    LONG_JUMP = 'LJ'
    TRIPLE_JUMP = 'TJ'
    CRICKET_BALL = 'CB'
    ROUNDERS_BALL = 'RB'
    SHOT_PUT = 'SP'
    DISCUS = 'DI'
    JAVELIN = 'JA'
    POLE_VAULT = 'PV'
    FIELD_NAME = (
        (HIGH_JUMP, 'High Jump'),
        (LONG_JUMP, 'Long Jump'),
        (TRIPLE_JUMP, 'Triple Jump'),
        (CRICKET_BALL, 'Cricket Ball'),
        (ROUNDERS_BALL, 'Rounders Ball'),
        (SHOT_PUT, 'Shot Put'),
        (DISCUS, 'Discus'),
        (JAVELIN, 'Javelin'),
        (POLE_VAULT, 'Pole Vault'),
    )
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='field_events')
    field_name = models.CharField(max_length=2, choices=FIELD_NAME, default=None)

    def __str__(self):
        return '%s %s %s' % (self.get_year_group_display(), self.get_gender_display(), self.get_field_name_display())


class Swimming(Event):
    BREAST_STROKE = 'BS'
    BACKSTROKE = 'BA'
    FREESTYLE = 'FR'
    OPEN = 'OP'
    STROKE_CHOICES = (
        (BREAST_STROKE, 'Breaststroke'),
        (BACKSTROKE, 'Backstroke'),
        (FREESTYLE, 'Freestyle'),
        (OPEN, 'Open'),
    )
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='swimming_events')
    stroke = models.CharField(max_length=2, choices=STROKE_CHOICES, default=FREESTYLE)
    distance_in_meters = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.get_year_group_display(), self.get_gender_display(), self.get_stroke_display())


class SwimmingRelay(Event):
    FREESTYLE = 'FR'
    MEDLEY = 'ME'
    STROKE_CHOICES = (
        (FREESTYLE, 'Freestyle'),
        (MEDLEY, 'Medley'),
    )
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='swimming_relay_events')
    number_of_students = models.IntegerField()
    distance_per_student = models.IntegerField()
    stroke = models.CharField(max_length=2, choices=STROKE_CHOICES, default=FREESTYLE)

    def __str__(self):
        return '%s %s %s by %sm %s' % (
            self.get_year_group_display(), self.get_gender_display(), self.number_of_students,
            self.distance_per_student, self.get_stroke_display())
