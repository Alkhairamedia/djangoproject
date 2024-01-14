from django.db import models

# Create your models here.



class Staffs(models.Model):
   CATEGORY = (
      ('classteacher', 'classteacher'),
      ('subject_teacher', 'subject_teacher'),
      ('helper', 'helper'),
      ('cleaner', 'cleaner'),
      ('driver', 'driver'),
      ('security', 'security')
   )
   first_name = models.CharField(max_length=200, null=True)
   middle_name = models.CharField(max_length=200, null=True)
   suname = models.CharField(max_length=200, null=True)
   username = models.CharField(max_length=200, null=True)
   email = models.CharField(max_length=200, null=True)
   phone = models.CharField(max_length=200, null=True)
   category = models.CharField(max_length=200, null=True, choices=CATEGORY)
   description =  models.CharField(max_length=200, null=True)
   dateEmployed = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self):
      return self.suname 
   
class teachers(models.Model):
   first_name = models.CharField(max_length=200, null=True)
   middle_name = models.CharField(max_length=200, null=True)
   suname = models.CharField(max_length=200, null=True)
   username = models.CharField(max_length=200, null=True)
   email = models.CharField(max_length=200, null=True)
   phone = models.CharField(max_length=200, null=True)
   category = models.CharField(max_length=200, null=True, blank=True)
   classInCharge =  models.CharField(max_length=200, null=True, blank=True)
   dateEmployed = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self):
      return self.suname

class Students(models.Model):
   departmental = (
      ('science', 'science'),
      ('commercial', 'commercial'),
      ('art', 'art')
   )
   
   classCat = (
      ('sss1', 'sss1'),
      ('sss2', 'sss2'),
      ('sss3', 'sss3'),
      ('jss1', 'jss1'),
      ('jss2', 'jss2'),
      ('jss3', 'jss3')
   )
   first_name = models.CharField(max_length=200, null=True)
   middle_name = models.CharField(max_length=200, null=True)
   suname = models.CharField(max_length=200, null=True)
   username = models.CharField(max_length=200, null=True)
   studentId = models.CharField(max_length=200, null=True)
   email = models.EmailField(max_length=200, null=True)
   phone = models.CharField(max_length=200, null=True)
   classAdmitted= models.CharField(max_length=200, null=True, choices=classCat)
   department_name = models.CharField(max_length=200, null=True, blank=True,  choices= departmental)
   classtecher = models.ForeignKey(teachers, null=True, on_delete= models.SET_NULL)
   currentClass= models.CharField(max_length=200, null=True, choices=classCat)
   dateAdmitted = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self):
      return self.studentId



class Classes(models.Model):
   name = models.CharField(max_length=200, null=True)
   student = models.ManyToManyField(Students)
   teacher = models.ForeignKey(teachers, null=True, on_delete= models.SET_NULL)
   academic_Session = models.CharField(max_length=200, null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   
   def full_name(self):
      return self.name
   


class Assignments(models.Model):
   classe = models.CharField(max_length=200, null=True)
   teacher = models.ForeignKey(teachers, null=True, on_delete= models.SET_NULL)
   question = models.CharField(max_length=200, null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   
   def full_name(self):
      return self.name
   
   
class subjects(models.Model):
   Subject = (
      ('english', 'english'),
      ('mathematic', 'mathematic'),
      ('physics', 'physics'),
      ('chemistry', 'chemistry'),
      ('biology', 'biology'),
      ('geograpyh', 'geograpyh'),
      ('furthermath', 'furthermath'),
      ('economics', 'economics'),
      ('agric science', 'agric science'),
      ('commerce', 'commerce'),
      ('literature', 'literature')
   )
   
   deptCategory = (
      ('science', 'science'),
      ('commercial', 'commercial'),
      ('art', 'art')
   )
   subjects_name = models.CharField(max_length=200, null=True, unique=True, choices=Subject )
   deptCategory = models.CharField(max_length=200, null=True, choices= deptCategory)
   book = models.CharField(max_length=200, null=True)
   teacher =  models.ForeignKey(teachers, null=True, on_delete= models.SET_NULL)
   
   def __str__(self):
      return self.subjects_name

   
class scheme_of_work(models.Model):
   subject = models.ForeignKey(subjects, null=True, on_delete= models.SET_NULL)
   classes = models.ForeignKey(Classes, null=True, on_delete= models.SET_NULL)
   topic = models.CharField(max_length=200, null=True)
   content = models.CharField(max_length=200, null=True)
   lesson_guid = models.CharField(max_length=200, null=True)
   academic_Session = models.CharField(max_length=200, null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   
   def full_name(self):
      return self.subject.subjects_name


class department(models.Model):
   dept = (
      ('science', 'science'),
      ('commercial', 'commercial'),
      ('art', 'art')
   )
   
   name = models.CharField(max_length=200, null=True, choices= dept)
   teachers = models.ManyToManyField(teachers)
   subjects = models.ManyToManyField(subjects)
   students = models.ManyToManyField(Students)
   
   def __str__(self):
      return self.name
   
   
class attendance(models.Model):
   name = models.CharField(max_length=200, null=True) 
   academicSession = models.CharField(max_length=200, null=True)
   class_name = models.CharField(max_length=200, null=True)
   studentId = models.CharField(max_length=200, null=True)
   terms = models.CharField(max_length=200, null=True)
   Status = models.CharField(max_length=200, null=True)
   days= models.DateField(auto_now_add=True, null=True)
   
   def __str__(self):
      return self.name


class Parents(models.Model):
   name = models.CharField(max_length=200, null=True)
   username = models.CharField(max_length=200, null=True)
   child = models.ManyToManyField(Students)
   email = models.EmailField(max_length=200, null=True)
   phone = models.CharField(max_length=200, null=True)
   classAdmitted= models.CharField(max_length=200, null=True)
   childAdmitedDate = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self):
      return self.name