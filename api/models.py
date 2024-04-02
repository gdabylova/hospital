from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField(default = None)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    type_insurance = models.CharField(max_length=10, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')])

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Doctor(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=150)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True)
    experience = models.CharField(max_length=100)
    date_start_job = models.DateField()
    date_end_job = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    doctor = models.ManyToManyField(Doctor, related_name='services')

    def __str__(self):
        return self.name

class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = (
        (PLANNED, PLANNED),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED),
    )


    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PLANNED)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.doctor.full_name} - {self.patient.full_name} - {self.visit_date}"