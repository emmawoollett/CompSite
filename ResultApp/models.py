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
    house_points = models.FloatField()

    def __str__(self):
        return '%s %s %s' % (self.event, self.student, self.house_points)


class TrackEventResult(ResultModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_track_result')
    event = models.ForeignKey(TrackEvent, on_delete=models.CASCADE, related_name='track_result')
    time = models.DurationField()
    house_points = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.event, self.student)

    def record_check(self):
        record = TrackEventRecord.objects.get(event=self.event)
        return record.record_breaker(self)

    class Meta:
        ordering = ['time']


class FieldEventResult(ResultModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_field_result')
    event = models.ForeignKey(FieldEvent, on_delete=models.CASCADE, related_name='field_result')
    distance = models.FloatField()
    house_points = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.event, self.student)

    def record_check(self):
        record = FieldEventRecord.objects.get(event=self.event)
        return record.record_breaker(self)


class SwimmingResult(ResultModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_swim_result')
    event = models.ForeignKey(Swimming, on_delete=models.CASCADE, related_name='swim_result')
    time = models.DurationField(blank=True, null=True)
    house_points = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.event, self.student)


class TrackRelayResult(ResultModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_track_relay_result')
    event = models.ForeignKey(TrackRelay, on_delete=models.CASCADE, related_name='track_relay_result')
    time = models.DurationField()
    house_points = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.event, self.house)

    def record_check(self):
        record = TrackRelayRecord.objects.get(event=self.event)
        return record.record_breaker(self)

    class Meta:
        ordering = ['time']


class SwimmingRelayResult(ResultModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_swim_relay_result')
    event = models.ForeignKey(SwimmingRelay, on_delete=models.CASCADE, related_name='swim_relay_result')
    time = models.DurationField(blank=True, null=True)
    house_points = models.FloatField()

    def __str__(self):
        return '%s %s' % (self.event, self.house)


class RecordModel(models.Model):
    date = models.DateField()

    class Meta:
        abstract = True


class TrackEventRecord(RecordModel):
    event = models.ForeignKey(TrackEvent, on_delete=models.CASCADE, related_name='track_record')
    time = models.DurationField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s %s' % (self.event, self.first_name, self.last_name)

    def record_breaker(self, result):
        if self.event != result.event:
            return False
        if self.time > result.time:
            return True
        else:
            return False


class FieldEventRecord(RecordModel):
    event = models.ForeignKey(FieldEvent, on_delete=models.CASCADE, related_name='field_record')
    distance = models.FloatField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s %s' % (self.event, self.first_name, self.last_name)

    def record_breaker(self, result):
        if self.event != result.event:
            return False
        if self.distance < result.distance:
            return True
        else:
            return False


class TrackRelayRecord(RecordModel):
    event = models.ForeignKey(TrackRelay, on_delete=models.CASCADE, related_name='track_relay_record')
    time = models.DurationField()
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_track_relay_record')

    def __str__(self):
        return '%s - %s' % (self.event, self.house)

    def record_breaker(self, result):
        if self.event != result.event:
            return False
        if self.time > result.time:
            return True
        else:
            return False


ResultsModels = [CrossCountryResult, TrackEventResult, FieldEventResult, SwimmingResult]
RelayResultModels = [TrackRelayResult, SwimmingRelayResult]
RecordModels = [TrackEventRecord, FieldEventRecord, TrackRelayRecord]
