from datetime import datetime
from pony.orm import *
from datetime import datetime
#from django.db import models

# Create your models here.

db = Database("mysql", host="easyvibe.cloudapp.net", user="EASYVIBE_DATA", passwd="123qwe", db="EASYVIBE_DATA")

class Album(db.Entity):
    nodeId = PrimaryKey(int, auto=True)
    author = Required(str)
    title = Required(str)
#    song = Optional("Song")

class Song(db.Entity):
    nodeId = PrimaryKey(int, auto=True)
    author = Required(str)
    genre = Optional(str)
    title = Required(str)
    year = Optional(str)
    album_nodeId = Required(unicode)
    #albums = Set(Album)
    #users_in_songs = Set("UsersInSongs")
    #recommendations = Set("Recommendation")
    #listenings = Set("Listen")

class User(db.Entity):
    nodeId = PrimaryKey(int, auto=True)
    accessToken = Required(str, unique=True)
    birthday = Optional(datetime)
    createdAt = Required(datetime)
    email = Optional(str)
    facebookId = Optional(str)
    fbAccessToken = Optional(str)
    gender = Required(int, default=0)
    name = Required(str, lazy=True)
    age = Optional(int)
    vkAccessToken = Optional(str)
    vkId = Optional(int)
    #users_in_songs = Set("UsersInSongs")
    #devices = Set("Device")
    #notifications = Set("Notification")
    #recommendations = Set("Recommendation")
    #listenings = Set("Listen")

#class UsersInSongs(db.Entity):
#    #id = PrimaryKey(int, auto=True)
#    song_id = Required(int)
#    user_id = Required(int)
#    #song = Required(Song)
#    #user = Required(User)

class Device(db.Entity):
    nodeId = PrimaryKey(int, auto=True)
    deviceToken = Optional(str, unique=True)
    deviceType = Optional(int)
    lastSendDate = Optional(datetime)
    user_nodeId = Required(int)
    #user = Required(User)

class Notification(db.Entity):
    nodeId = PrimaryKey(int, auto=True)
    locArgs = Optional(str)
    lockKey = Optional(str)
    sent = Required(int, default=0)
    user_nodeId = Required(int)
    #user = Required(User)

class Recommendation(db.Entity):
    nodeId = PrimaryKey(int, auto=True)
    createdAt = Required(datetime)
    state = Required(int)
    createdBy_nodeId = Required(int)
    received_nodeId = Required(int)
    song_nodeId = Required(int)
    #user = Required(User)
    #song = Required(Song)

class Listen(db.Entity):
    nodeId = PrimaryKey(int, auto=True)
    createdAt = Required(datetime)
    song_nodeId = Required(int)
    user_nodeId = Required(int)
    #song = Required(Song)
    #user = Required(User)

sql_debug(True)
db.generate_mapping(create_tables=False)
