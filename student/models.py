from django.db import models






class Student(models.Model):
    name=models.CharField( max_length=100 , null=False  )
    description=models.TextField(default="this is a student")

    def __str__(self) -> str:
        return self.name




class Lesson(models.Model):
    name=models.CharField(max_length=100 , null=False )
    description=models.TextField(default="this is a Lesson")

    def __str__(self) -> str:
        return self.name    



class Package(models.Model):
    class Meta:
        ordering=['-name']
    name=models.CharField(max_length=100 , null=False  )
    description=models.TextField(default="this is a Package")

    def __str__(self) -> str:
        return self.name   



class Course(models.Model):
    package=models.ForeignKey(Package , on_delete=models.CASCADE)
    lesson=models.ForeignKey( Lesson , on_delete=models.CASCADE)
    student=models.ManyToManyField( Student )  
    name=models.CharField(max_length=100 , null=False  )
    description=models.TextField(default="this is a Course")               

    def __str__(self) -> str:
        return self.name  