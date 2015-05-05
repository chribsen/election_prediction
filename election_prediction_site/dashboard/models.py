from django.db import models


class Party(models.Model):
    party_name = models.CharField(max_length=191)

    def __unicode__(self):
        return self.party_name


class Page(models.Model):
    page_id = models.CharField(max_length=191, primary_key=True)
    page_name = models.CharField(max_length=191)
    party = models.ForeignKey(Party)
    is_politician = models.BooleanField()

    def __unicode__(self):
        return self.page_name


class Post(models.Model):
    post_id = models.CharField(max_length=191, primary_key=True)
    page_id = models.ForeignKey(Page)
    message = models.TextField()
    created_time = models.DateTimeField()
    like_count = models.IntegerField(null=True)
    share_count = models.IntegerField(null=True)
    sentiment_score = models.FloatField(null=True)
    is_negative = models.NullBooleanField(null=True)


class Like(models.Model):
    post_id = models.ForeignKey(Post)
    from_name = models.CharField(max_length=191)
    from_id = models.CharField(max_length=191)


class Comment(models.Model):
    comment_id = models.CharField(max_length=191, primary_key=True)
    comment = models.TextField()
    comment_clean = models.TextField()
    post_id = models.ForeignKey(Post)
    from_id = models.CharField(max_length=191, default=None)
    from_name = models.CharField(max_length=191, default=None)
    created_time = models.DateTimeField()
    like_count = models.IntegerField(null=True)
    sentiment_score = models.FloatField(null=True)
    is_negative = models.NullBooleanField(null=True)
    comment_count = models.IntegerField()


class Reply(models.Model):
    reply_id = models.CharField(max_length=191, primary_key=True)
    comment_id = models.ForeignKey(Comment)
    reply = models.TextField()
    reply_clean = models.TextField()
    from_id = models.CharField(max_length=191)
    from_name = models.CharField(max_length=191)
    like_count = models.IntegerField(null=True)
    created_time = models.DateTimeField()
    sentiment_score = models.FloatField(null=True)
    is_negative = models.NullBooleanField(null=True)




