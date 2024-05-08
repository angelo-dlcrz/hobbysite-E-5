from django.db import models
from django.urls import reverse

from user_management.models import Profile


class Commission(models.Model):
    commission_status_options = (
        ("OPEN", "OPEN"),
        ("FULL", "FULL"),
        ("ECOMPLETED", "COMPLETED"),
        ("DISCONTINUED", "DISCONTINUED")
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    commission_status = models.CharField(
        max_length=15,
        choices=commission_status_options,
        default="OPEN"
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="profile")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.pk])

    def get_first_words(self):
        return self.description[:500]

    def exceeds(self):
        return len(self.description) > 500

    def get_commission_status(self):
        if self.commission_status == "ECOMPLETED":
            return "COMPLETED"
        else:
            return self.commission_status

    class Meta:
        ordering = ['-commission_status', '-created_on']


class Job(models.Model):
    commission = models.ForeignKey(
        'Commission',
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    role = models.CharField(max_length=255)
    manpower = models.PositiveIntegerField()
    job_status_options = (
        ("OPEN", "OPEN"),
        ("FULL", "FULL")
    )
    job_status = models.CharField(
        max_length=10, choices=job_status_options, default="open")

    def __str__(self):
        return self.role

    class Meta:
        ordering = ['-job_status', '-manpower', 'role']


class JobApplication (models.Model):
    job = models.ForeignKey(
        'Job',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    applicant = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="applicants"
    )
    application_status_options = (
        ("APENDING", "PENDING"),
        ("BACCEPTED", "ACCEPTED"),
        ("CREJECTED", "REJECTED")
    )
    application_status = models.CharField(
        max_length=10, choices=application_status_options, default="PENDING")
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(str(self.applicant.display_name), str(self.job.role))

    def get_application_status(self):
        if self.application_status == "APENDING":
            return "PENDING"
        elif self.application_status == "BACCEPTED":
            return "ACCEPTED"
        else:
            return "REJECTED"

    class Meta:
        ordering = ['application_status', '-applied_on']
