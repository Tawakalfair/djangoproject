from django.db import models

# Create your models here.
'''
LEVEL=[
    ("T", "Tinggi"),
    ("S", "Sedang"),
    ("R", "Rendah"),
]

class Pertanyaan(models.Model):
    judul           = models.CharField(max_length=60)
    Pertanyaan      = models.TextField()
    level           = models.CharField(max_length=1, choices=LEVEL)

    def __str__(self):
        return self.judul
'''