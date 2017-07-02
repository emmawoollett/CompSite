from StudentApp.models import Student, House
from CompApp.models import *

class ResultModel(models.Model):

    class Meta:
        abstract = True
        ordering = ['-house_points']


class CrossCountryResult(ResultModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_cross_country_result')
    event = models.ForeignKey(CrossCountry, on_delete=models.CASCADE, related_name='cross_country_result')
    position = models.IntegerField()
    house_points = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.event, self.student, self.house_points)


class TrackEventResult(ResultModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_track_result')
    event = models.ForeignKey(TrackEvent, on_delete=models.CASCADE, related_name='track_result')
    time = models.TimeField()
    house_points = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.event, self.student)


class FieldEventResult(ResultModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_field_result')
    event = models.ForeignKey(FieldEvent, on_delete=models.CASCADE, related_name='field_result')
    distance = models.FloatField()
    house_points = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.event, self.student)


class SwimmingResult(ResultModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_swim_result')
    event = models.ForeignKey(Swimming, on_delete=models.CASCADE, related_name='swim_result')
    time = models.TimeField(blank=True, null=True)
    house_points = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.event, self.student)


class TrackRelayResult(ResultModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_track_relay_result')
    event = models.ForeignKey(TrackRelay, on_delete=models.CASCADE, related_name='track_relay_result')
    time = models.TimeField()
    house_points = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.event, self.house)


class SwimmingRelayResult(ResultModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_swim_relay_result')
    event = models.ForeignKey(SwimmingRelay, on_delete=models.CASCADE, related_name='swim_relay_result')
    time = models.TimeField(blank=True, null=True)
    house_points = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.event, self.house)


ResultsModels = [CrossCountryResult, TrackEventResult, FieldEventResult, SwimmingResult]
RelayResultModels = [TrackRelayResult, SwimmingRelayResult]
