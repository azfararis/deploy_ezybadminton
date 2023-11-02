from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=128)
    address = models.TextField(max_length=50)
    phoneNo = models.TextField(max_length=11)


class Court(models.Model):
    courtId = models.CharField(primary_key=True, max_length=10, default="")
    description = models.TextField(max_length=50)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

class Booking(models.Model):
    userId = models.CharField(primary_key=True, max_length=10)
    courtId = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    hours = models.IntegerField(default=1)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate the total price based on price_per_hour and hours
        if self.courtId and self.hours:
            self.totalPrice = self.courtId.price_per_hour * self.hours
        super().save(*args, **kwargs)


class Feedback(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    courtId = models.ForeignKey(Court, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=100)
    rate = models.IntegerField()