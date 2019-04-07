from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    # action_by
    # nominator
    event_url = models.CharField(max_length=100)
    
    # location
    # country code & region/region code, determined by location
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    start_date = models.DateField()
    end_date = models.DateField()
    # rating
    # primary_goals
    # CFP_url
    # conference_contact
    # internal_contact
    # comments/history/actions
    # fiscal year/half/quarter
    # month
    # duplicates/votes
    # github issue
    # reports
    # sponsorships
    # tags

class Report(models.Model):
    # foreign key to Event...
    report_title = models.CharField(max_length=100)
    # action_by
    # sponsored
    # followup_w_nominee
    # execution_date
    # notes/comments/history
    # audience_reach
    # expected_attendance_num
    # attendee_type
    # suggested_elastic_attendees
    # event_brief_url
    # report_url
    # region
    # sponsorship
    # tags

class Sponsorship(models.Model):
    # foreign key to Event...?
    # action_by
    # status (proposed/accept/done)
    start_date = models.DateField()
    end_date = models.DateField()
    # rec'd sponsorship level
    # sponsored before
    # proposed sponsor amt
    # actual sponsor amt
    # payment currency
    # amt in local currency
    # tags