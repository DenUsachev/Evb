# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.db import models

class Albums(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=300,null=False)
    title = models.CharField(max_length=300,null=False)
    class Meta:
        managed = False
        db_table = 'Albums'

class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    access_token = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True, null=True)
    age = models.IntegerField(blank=True,null=False, default=0)
    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True)
    fb_id = models.CharField(max_length=255, blank=True)
    fb_token = models.CharField(max_length=255, blank=True)
    gender = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    vk_id = models.BigIntegerField(blank=True, null=True)
    vk_token = models.CharField(max_length=255, blank=True)
    picture = models.CharField(max_length=1000, blank=True)
    lang = models.CharField(max_length=6, blank=True)
    mutex = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'Clients'

class Devices(models.Model):
    id = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=255, blank=True)
    type = models.IntegerField(blank=True, null=True)
    last_send_date = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Clients)
    class Meta:
        managed = False
        db_table = 'Devices'

class Grants(models.Model):
    # id = models.CharField(prymary_key=True)
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(Clients,related_name='fk_owner')
    guest = models.ForeignKey(Clients,related_name='fk_guest')
    created = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'Grants'

class Songs(models.Model):
    author = models.CharField(max_length=200,null=False, blank=True)
    genre = models.CharField(max_length=200,null=True, blank=True)
    title = models.CharField(max_length=200,null=False, blank=True)
    year = models.SmallIntegerField(null=True)
    album = models.CharField(max_length=200,null=True, blank=True)
    artwork = models.CharField(max_length=500,null=True, blank=True)
    url = models.CharField(max_length=1000,null=True, blank=True)
    itunes_url = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'Songs'

class Listen(models.Model):
    created = models.DateTimeField(auto_now=True)
    song_id = models.CharField(max_length=64)
    client_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'Listen'

# class Notifications(models.Model):
#     id = models.IntegerField(primary_key=True)
#     sent = models.IntegerField()
#     client_id = models.IntegerField(blank=True, null=True)
#     delivered = models.DateTimeField()
#     class Meta:
#         managed = False
#         db_table = 'Notifications'
#
# class Recommendations(models.Model):
#     id = models.IntegerField(db_column='Id', primary_key=True) # Field name made lowercase.
#     created = models.DateTimeField()
#     updated = models.DateTimeField(blank=True, null=True)
#     state = models.IntegerField(blank=True, null=True)
#     creator_id = models.IntegerField()
#     recepient_id = models.IntegerField()
#     song_id = models.CharField(unique=True, max_length=64)
#     is_read = models.IntegerField()
#     class Meta:
#         managed = False
#         db_table = 'Recommendations'

#
# class Usersinsongs(models.Model):
#     id = models.CharField(primary_key=True, max_length=64)
#     client_id = models.IntegerField()
#     song_id = models.CharField(max_length=64)
#     hash = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'UsersInSongs'

