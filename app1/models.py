from django.db import models

# Create your models here.

class Film(models.Model):
    title = models.CharField(("Titel"), max_length=250)
    runtime = models.IntegerField(("Laufzeit"))
    language = models.CharField(("Sprache"), max_length=50)
    fsk = models.IntegerField(("Fsk"), default = 16)
    year = models.IntegerField(("Jahr"), default = 1980)
    dolby = models.BooleanField(("Dolby 5.1 (j/n)"), default=True)
    description = models.TextField(("Beschreibung"))

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filme"

    def __str__(self):
        return f"{self.title} ({str(self.year)})"

    #def get_absolute_url(self):
    #    return reverse("Film_detail", kwargs={"pk": self.pk})
