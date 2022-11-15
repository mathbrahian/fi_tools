from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64,  null=False, blank=False)
    direction = models.CharField(max_length=128,  null=False, blank=False)
    phone_number = models.CharField(max_length=16, null=False, blank=False)
    
    def __str__(self):
        return f"Client: {self.name}"
    
    def save(self, *args, **kwargs):
        # # if not CompanyCountry.objects.filter(company=self.company, country=self.country).exists():
        # #     raise ValueError("The company does not operate in the country")
        # else:
        super().save(*args, **kwargs)
