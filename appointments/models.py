from django.db import models

class Barber(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)  # Optional
    location = models.CharField(max_length=255, blank=True)      # Optional
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Barber: {self.name}, Expertise: {self.expertise if self.expertise else 'Not Specified'}"

class Appointment(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.customer_name} - {self.date} {self.time}"
