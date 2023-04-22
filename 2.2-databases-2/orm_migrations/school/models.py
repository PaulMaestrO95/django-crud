from django.db import models


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    teachers = models.ManyToManyField(
        Teacher,
        related_name='students',
        through='TeacherStudent',
    )
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name


class TeacherStudent(models.Model):
    class Meta:
        unique_together = (('student', 'teacher'),)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Студенты'
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Учителя'
    )
