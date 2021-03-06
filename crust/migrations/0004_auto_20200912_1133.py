# Generated by Django 3.1.1 on 2020-09-12 08:33

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crust', '0003_auto_20200911_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('address_first_line', models.CharField(max_length=100)),
                ('address_second_line', models.CharField(max_length=100)),
                ('address_street_number', models.CharField(max_length=20)),
                ('address_street_name', models.CharField(max_length=50)),
                ('google_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('body', models.CharField(max_length=100)),
                ('commented_by', models.IntegerField()),
                ('commented_by_store', models.IntegerField()),
                ('commented_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('store_id', models.IntegerField()),
                ('comment_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('suburb_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('posted_by', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('comment_count', models.IntegerField()),
                ('hidden', models.BooleanField()),
                ('official', models.BooleanField()),
                ('posted_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('heart_ratings', models.IntegerField()),
                ('okay_ratings', models.IntegerField()),
                ('burnt_ratings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('body', models.CharField(max_length=100)),
                ('replied_by', models.IntegerField()),
                ('replied_by_store', models.IntegerField()),
                ('replied_at', models.DateTimeField(default=datetime.datetime.now)),
                ('reply_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReplyLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('store_id', models.IntegerField()),
                ('reply_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('store_id', models.IntegerField()),
                ('store_group_id', models.IntegerField()),
                ('valid_from', models.DateField()),
                ('valid_until', models.DateField()),
                ('promo_image', models.CharField(max_length=100)),
                ('terms_and_condition', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('redeem_limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('location_id', models.IntegerField()),
                ('suburb_id', models.IntegerField()),
                ('city_id', models.IntegerField()),
                ('cover_image', models.TextField()),
                ('order', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('followercount', models.IntegerField()),
                ('review_count', models.IntegerField()),
                ('z_id', models.TextField()),
                ('z_url', models.TextField()),
                ('more_info', models.TextField()),
                ('avg_cost', models.IntegerField()),
                ('coords', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='StoreAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('address_first_line', models.TextField()),
                ('address_second_line', models.TextField()),
                ('address_street_number', models.TextField()),
                ('address_street_name', models.TextField()),
                ('google_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreCuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('cuisine_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('follower_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StoreHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('order', models.IntegerField()),
                ('dotw', models.TextField()),
                ('hours', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SystemError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_type', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255)),
                ('occurred_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('follower_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_type', models.CharField(max_length=100)),
                ('social_id', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('username', models.CharField(max_length=64)),
                ('preferred_name', models.CharField(max_length=64)),
                ('profile_picture', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('tagline', models.CharField(max_length=64)),
                ('follower_count', models.IntegerField()),
                ('store_count', models.IntegerField()),
                ('fcm_token', models.CharField(max_length=255)),
                ('admin_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserReward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('reward_id', models.IntegerField()),
                ('unique_code', models.CharField(max_length=100)),
                ('last_redeemed_at', models.DateField()),
                ('redeemed_count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='WorldBorder',
        ),
    ]
