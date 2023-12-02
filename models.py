from django.db import models

class NoteBooks(models.Model):
    fid = models.AutoField()
    fcreater = models.CharField(max_length=30)
    fnod = models.CharField(max_length=30)
    fparentnod = models.CharField(max_length=30)
    fcreatetime = models.DateField(auto_now_add=True)
    fmodifytime = models.DateField(auto_now=True)
    fnotecontent = models.TextField()
    fdescription = models.TextField()
