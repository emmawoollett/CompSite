from django.db import models
from django.db.models import Q


class School(models.Model):
    slug = models.SlugField()
    school_name = models.CharField(max_length=200)
    school_location = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.school_name, self.school_location)


class House(models.Model):
    slug = models.SlugField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='houses')
    house_name = models.CharField(max_length=10)
    house_initial = models.CharField(max_length=1)

    def __str__(self):
        return self.house_name

    def get_student_winners(self, competition=None):
        '''
        For each house output a list of students who have won an event in a specified competition.
        A student has won an event if they have 6 house points from the event.
        :return: a queryset of students
        '''
        if competition:
            return self.students.filter(
                Q(student_track_result__house_points=6,
                  student_track_result__event__competition__competition_name=competition) |
                Q(student_cross_country_result__house_points=6,
                  student_cross_country_result__event__competition__competition_name=competition) |
                Q(student_swim_result__house_points=6,
                  student_swim_result__event__competition__competition_name=competition) |
                Q(student_field_result__house_points=6,
                  student_field_result__event__competition__competition_name=competition)
            ).distinct()
        else:
            return self.students.filter(
                Q(student_track_result__house_points=6) |
                Q(student_cross_country_result__house_points=6) |
                Q(student_swim_result__house_points=6) |
                Q(student_field_result__house_points=6)
            ).distinct()


class Student(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
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

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_winner_events(self, competition=None):
        if competition:
            for result in self.student_swim_result.filter(house_points=6, event__competition__competition_name=competition):
                yield result.event
            for result in self.student_field_result.filter(house_points=6, event__competition__competition_name=competition):
                yield result.event
            for result in self.student_track_result.filter(house_points=6, event__competition__competition_name=competition):
                yield result.event
        else:
            for result in self.student_swim_result.filter(house_points=6):
                yield result.event
            for result in self.student_field_result.filter(house_points=6):
                yield result.event
            for result in self.student_track_result.filter(house_points=6):
                yield result.event

