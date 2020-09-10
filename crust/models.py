from datetime import datetime
from django.contrib.gis.db import models



class Cuisine(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Admin(models.Model):
    store_id = models.IntegerField()
    created_at =models.DateTimeField(default = datetime.now) 
    hash = models.CharField(max_length = 255)
    def __str__(self):
        return self.store_id


class  Address(models.Model):
    store_id = models.IntegerField()
    address_first_line = models.CharField(max_length = 100)
    address_second_line = models.CharField(max_length =100)
    address_street_number = models.CharField(max_length = 20)
    address_street_name = models.CharField(max_length = 50)
    google_url = models.CharField(max_length = 255)

    def __str__(self):
        return self.store_id


class City(models.Model):
    name = models.CharField(max_length = 255)
    district_id  = models.IntegerField()

    def __str__(self):
         return self.name

class Country(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length = 255)
    country_id = models.IntegerField()


    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length = 255)
    suburb_id = models.IntegerField()

    def __str__(self):
        return self.name


'''class Suburb(models.Model):
    name = models.CharField(max_length = 255)
    post_code = models.IntegerField()
    city_id = models.IntegerField()
   # coords = models.MultiPolygonField()

    def __str__(self):
        return self.name'''


class Comment(models.Model):
    post_id = models.IntegerField()
    body = models.CharField(max_length = 100)
    commented_by = models.IntegerField()
    commented_by_store = models.IntegerField()
    commented_at = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.post_id


class CommentLike(models.Model):
    user_id = models.IntegerField()
    store_id = models.IntegerField()
    comment_id =models.IntegerField()


    def __str__(self):
        return self.user_id

class  Post(models.Model):
    #type(enum 'review', 'photo')
    store_id = models.IntegerField()
    posted_by = models.IntegerField()
    like_count= models.IntegerField()
    comment_count = models.IntegerField()
    hidden = models.BooleanField()
    official = models.BooleanField()
    posted_at = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.store_id


class PostPhoto(models.Model):
    post_id =models.IntegerField()
    url =models.TextField()

    def __str__(self):
        return self.post_id

class PostReview(models.Model):
    post_id = models.IntegerField()
    #overall_score =
    #taste_score
    # service_score
    # value_score
    # ambience_score
    body = models.TextField()


    def __str__(self):
        return self.post_id

class Reply(models.Model):
    comment_id =models.IntegerField()
    body =models.CharField(max_length = 100)
    replied_by = models.IntegerField()
    replied_by_store = models.IntegerField()
    replied_at = models.DateTimeField(default = datetime.now)
    reply_to = models.IntegerField() 

    def __str__(self):
        return self.body


class ReplyLike(models.Model):
    user_id = models.IntegerField()
    store_id = models.IntegerField()
    reply_id = models.IntegerField()

    def __str__(self):
        return self.user_id



class Reward(models.Model):
    code = models.CharField(max_length = 12)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    #type ('one_time')
    store_id = models.IntegerField()
    store_group_id = models.IntegerField()
    valid_from = models.DateField()
    valid_until =models.DateField()
    promo_image = models.CharField( max_length = 100)
    terms_and_condition = models.CharField(max_length = 100)
    active = models.BooleanField()
    redeem_limit = models.IntegerField()

    def __str__(self):
        return self.code


class Rating(models.Model):
    store_id = models.IntegerField()
    heart_ratings =models.IntegerField()
    okay_ratings = models.IntegerField()
    burnt_ratings =models.IntegerField()

    def __str__(self):
        return self.store_id

class Store(models.Model):
    name = models.CharField(max_length = 100)
    phone_country =models.CharField( max_length = 100)
    phone_number = models.CharField( max_length = 100)
    location_id =models.IntegerField()
    suburb_id = models.IntegerField()
    city_id = models.IntegerField()
    cover_image =models.TextField()
    order =models.IntegerField()
    rank = models.IntegerField()
    followercount =models.IntegerField()
    review_count = models.IntegerField()
    z_id = models.TextField()
    z_url = models.TextField()
    more_info = models.TextField()
    avg_cost =models.IntegerField()
    coords = models.MultiPolygonField()

  


    def __str__(self):
        return self.name

class StoreAddress(models.Model):
    store_id = models.IntegerField()
    address_first_line =models.TextField()
    address_second_line = models.TextField()
    address_street_number = models.TextField()
    address_street_name = models.TextField()
    google_url = models.TextField()

    def __str__(self):
        return self.store_id



class StoreCuisine(models.Model):
    store_id = models.IntegerField()
    cuisine_id = models.IntegerField()

    def __str__(self):
        return self.store_id

class StoreFollow(models.Model):
    store_id = models.IntegerField()
    follower_id = models.IntegerField()

    def __str__(self):
        return self.store_id


class StoreGroup(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class StoreHour(models.Model):
    store_id = models.IntegerField()
    order = models.IntegerField()
    dotw = models.TextField()
    hours = models.TextField()

    def __str__(self):
        return self.store_id


class Tag(models.Model):
    name = models.CharField( max_length = 100)   

    def __str__(self):
        return self.name


class SystemError(models.Model):
    error_type = models.CharField(max_length = 64)
    description = models.CharField(max_length = 255)
    occurred_at = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.error_type



class UserAccount(models.Model):
    email = models.CharField(max_length = 255)

    def __str__(self):
        return self.email


class UserClaim(models.Model):
    user_id = models.IntegerField()
    
    #type str 
    #value type str
    def __str__(self):
        return user_id
       

class UserFollow(models.Model):
    user_id = models.IntegerField()
    follower_id = models.IntegerField()

    def __str__(self):
        return user_id

class UserLogin(models.Model):
    social_type = models.CharField(max_length = 100)
    social_id =models.CharField(max_length = 100)  
    user_id = models.IntegerField()

    def __str__(self):
        return self.user_id


class UserProfile(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length = 64)
    preferred_name = models.CharField(max_length = 64) 
    profile_picture = models.TextField()
    gender = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    tagline = models.CharField(max_length = 64)
    follower_count = models.IntegerField() 
    store_count = models.IntegerField()
    fcm_token = models.CharField(max_length = 255)
    admin_id = models.IntegerField()  

    def __str__(self):
        return username


class UserReward(models.Model):
    user_id = models.IntegerField()
    reward_id = models.IntegerField()
    unique_code = models.CharField(max_length = 100)
    last_redeemed_at = models.DateField()
    redeemed_count = models.IntegerField()

    def __str__(self):
        return self.user_id

    










































    








