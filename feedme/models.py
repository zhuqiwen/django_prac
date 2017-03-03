from django.db import models
from django.contrib.auth.models import User


# Create your models here.


    # id INT NOT NULL,
    # user_id INT NOT NULL,
    # is_public tinyint,
    # file_path VARCHAR(255) NOT NULL,
    # title VARCHAR(255),
    # duration INT,
    # insctruction LONGTEXT,
    # price INT,
    # view_count BIGINT,
    # rating tinyint,
    # suspended tinyint,
    # suspended_date DATE,
    # created DATE,
    # modified DATE,
    # deleted DATE,
    # PRIMARY KEY(id)


class video(models.Model):
    user_id = models.ForeignKey(User)
    is_public = models.BooleanField(null=False, default=False)
    file_path = models.FilePathField()
    title = models.CharField(max_length=255, null=False)
    duration = models.BigIntegerField()
    instruction = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    view_count = models.IntegerField()
    rating = models.SmallIntegerField()
    is_suspended = models.BooleanField()
    suspended_date = models.DateTimeField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)



    # id INT NOT NULL,
    # user_id INT NOT NULL,
    # video_id INT NOT NULL,
    # comment LONGTEXT,
    # suspended tinyint,
    # suspended_date DATE,
    # created DATE,
    # modified DATE,
    # deleted DATE,
    # PRIMARY KEY(id)

class comment(models.Model):
    user_id = models.ForeignKey(User)
    video_id = models.ForeignKey(video)
    comment = models.TextField()
    is_suspended = models.BooleanField()
    suspended_date = models.DateTimeField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)


    # id INT NOT NULL,
    # content VARCHAR(255),
    # PRIMARY KEY(id)

class tag(models.Model):
    content = models.CharField(max_length=255)


    # id INT NOT NULL,
    # video_id INT ,
    # time_point INT,
    # time_marker_id INT,
    # deleted DATE,
    # PRIMARY KEY(id)

class video_tag_mapping(models.Model):
    video_id = models.ForeignKey(video)
    tag_id = models.ForeignKey(tag)
    deleted = models.DateTimeField(auto_now=True)


class ingredient(models.Model):
    ingredient = models.CharField(max_length=255)


class video_ingredient_mapping(models.Model):
    video_id = models.ForeignKey(video)
    ingredient_id = models.ForeignKey(ingredient)
    deleted = models.DateTimeField(auto_now=True)


class taste(models.Model):
    taste = models.CharField(max_length=255)


class video_taste_mapping(models.Model):
    video_id = models.ForeignKey(video)
    taste_id = models.ForeignKey(taste)
    deleted = models.DateTimeField(auto_now=True)

