from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Story(models.Model):
    name = models.CharField(max_length=200)
    content=models.TextField()
    class Genre(models.TextChoices):
        AUTO="AU", "Auto"
        FANTASY="FA", "Fantasy"
        SCIFI="SF", "Science Fiction"
        MYSTERY="MY", "Mystery"
        ROMANCE="RO", "Romance"
        HORROR="HO", "Horror"
        FAIRYTALE= "FT","Fairy Tale"

    genre = models.CharField(
        max_length=2,
        choices=Genre.choices,
        default=Genre.AUTO
    )

    class Format(models.TextChoices):
        AUTO="AU", "Auto"
        PROSE = "PR", "Prose"
        DIARY = "DI", "Diary"
        POEM = "PO", "Poem"
        LETTER="LT","Letter"
        SCREENPLAY="SP","Screenplay"

    format_type = models.CharField(
        max_length=2,
        choices=Format.choices,
        default=Format.AUTO
    )

    class Perspective(models.TextChoices):
        AUTO="AU", "Auto"
        FIRST = "1P", "First Person"
        SECOND = "2P", "Second Person"
        THIRD = "3P", "Third Person"

    perspective = models.CharField(
        max_length=2,
        choices=Perspective.choices,
        default=Perspective.AUTO
    )

    class Audience(models.TextChoices):
        AUTO="AU", "Auto"
        CHILD = "CH", "Children"
        TEEN = "TE", "Teenagers"
        ADULT = "AD", "Adults"

    audience = models.CharField(
        max_length=2,
        choices=Audience.choices,
        default=Audience.AUTO
    )
    class Status(models.TextChoices):
        PENDING = "PE", "Pending"
        APPROVED = "AP", "Approved"
        REJECTED = "RE", "Rejected"

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING
    )


    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name