__author__ = 'Christian'
import unittest
import json
import urllib2
import time
import random
from datetime import datetime
from dashboard.models import Page, Post, Comment, Like, Reply

class Scraper:

    def __init__(self):
        self.access_token = 'CAACEdEose0cBANEZAPnkCb31sixiusZB90j9X0dDVrKEZCZBQspgc4QpN9sGo16AtqXQXOtZBS4f9F2dNkAL1xeGvpbOvAUns4UU87RWZBRnVieLkKZAFSUcZC67PtfZB4R4cZBXbycPX7RZB0fDqKrrS7l5wM2Jh6ZAeFfz2nEcBpD9jHmUjbmS1XDKqRbo11F8xHuePGGkYUTgw85ZCq7ZCbsVUQZAO0FWduHoBYZD'
        self.wall_posts_url = 'https://graph.facebook.com/{page_id}/feed?access_token={token}'
        self.posts_url = 'https://graph.facebook.com/{page_id}/posts?since={since}&access_token={token}'
        self.comments_url = 'https://graph.facebook.com/{post_id}/comments?access_token={token}&fields=id,comment_count,created_time,from,like_count,message'
        self.likes_url = 'https://graph.facebook.com/{post_id}/likes?access_token={token}'
        self.like_count_url = 'https://graph.facebook.com/{post_id}?access_token={token}&fields=likes.limit(1).summary(true)'

    def scrape(self):

        pages = Page.objects.all().select_related()
        for page in pages:

            if page.page_id in ['11060438851']:
                print('already scraped')
                continue

            print(page.page_id)

            posts = self.get_posts(page.page_id, '2014-12-30')

            for post in posts:

                if not 'message' in post.keys():
                    print("Does not contain 'message' key. Type: " + str(post['status_type']))
                    continue
                if not 'shares' in post.keys():
                    print("Does not contain 'shares' key. Type: " + str(post['status_type']))
                    continue
                if Post.objects.filter(pk=post['id']).count() > 0:
                    print('Already scraped')
                    continue

                try:
                    print('Page: ' + str(page.page_id) + ' - Post date: ' + post['created_time'])
                except:
                    pass

                like_count = self.get_like_count(post['id'])
                create_time = datetime.strptime(str(post['created_time']), "%Y-%m-%dT%H:%M:%S+0000")
                if post['status_type'] == 'shared_story':
                    shares = None
                else:
                    shares = post['shares']['count']

                post_obj = Post(post_id=post['id'],
                                 page_id=page,
                                 message=post['message'],
                                 created_time=create_time,
                                 share_count=shares,
                                 like_count=like_count,
                                 )

                post_obj.save()

                comments = self.get_comments(post['id'])
                for i, comment in enumerate(comments):
                    print('Scraping comment number: {0} - create_time: {1}'.format(str(i), post['created_time']))

                    create_time = datetime.strptime(str(comment['created_time']), "%Y-%m-%dT%H:%M:%S+0000")
                    comment_obj = Comment(post_id=Post.objects.get(pk=post['id']),
                                            comment_id=comment['id'],
                                            comment=comment['message'],
                                            like_count=comment['like_count'],
                                            from_id=comment['from']['id'],
                                            from_name=comment['from']['name'],
                                            created_time=create_time,
                                            comment_count=comment['comment_count'],
                                            )
                    comment_obj.save()

                    if comment['comment_count'] > 0:
                        print('Comment number {0} has comments'.format(str(i)))
                        replies = self.get_comments(comment['id'])
                        for reply in replies:
                            create_time = datetime.strptime(str(reply['created_time']), "%Y-%m-%dT%H:%M:%S+0000")
                            Reply(reply_id=reply['id'],
                                  comment_id=comment_obj,
                                  reply=reply['message'],
                                  like_count=reply['like_count'],
                                  created_time=create_time,
                                  from_id=reply['from']['id'],
                                  from_name=reply['from']['name'],
                                  ).save()

    def get_comments(self, post_id):
        self.delay(from_delay=0.1, to_delay=0.4)
        data = self.get_data(self.comments_url.format(post_id=post_id, token=self.access_token))
        return self.iterate(data)

    def get_wall_posts(self, page_id):
        self.delay()
        data = self.get_data(self.wall_posts_url.format(page_id=page_id, token=self.access_token))
        return self.iterate(data)

    def get_likes(self, post_id):
        self.delay()
        data = self.get_data(self.likes_url.format(post_id=post_id, token=self.access_token))
        return self.iterate(data)

    def get_like_count(self, post_id):
        self.delay(from_delay=0.05, to_delay=0.2)
        data = self.get_data(self.like_count_url.format(post_id=post_id, token=self.access_token))
        return int(data['likes']['summary']['total_count'])

    def get_posts(self, page_id, since, include_comments=False):
        data = self.get_data(self.posts_url.format(page_id=page_id, token=self.access_token, since=since))

        if include_comments:
            posts = self.iterate(data)
            comments = {}
            for post in posts:
                post_id = post['id']
                comments[post_id] = self.get_comments(post_id)
            return posts, comments
        else:

            return self.iterate(data)

    def iterate(self, data, delay=True):
        res = data['data']

        while True:
            if delay:
                self.delay(from_delay=0.4, to_delay=0.8)
            if not 'paging' in data.keys():
                break
            if not 'next' in data['paging'].keys():
                break
            time.sleep(random.randint(1, 2))
            raw = urllib2.urlopen(data['paging']['next']).read()
            data = json.loads(raw)
            res += data['data']
            print len(res)
        return res

    def get_data(self, url):
        try:
            raw = urllib2.urlopen(url).read()
            return json.loads(raw)
        except urllib2.URLError:
            print 'No route to host on URL: ' + url
            self.delay(from_delay=2.5, to_delay=3.5)
            return self.get_data(url)

    def delay(self, from_delay=0.5, to_delay=1.5):
        time.sleep(random.uniform(from_delay, to_delay))


class TestScraper(unittest.TestCase):

    def test_get_comments(self):
        x = Scraper().get_comments('58140803787_10153229105893788')

    def test_get_posts(self):
        x = Scraper().get_posts('58140803787')

    def test_get_wall_posts(self):
        x = Scraper().get_wall_posts('58140803787')

    def test_get_posts_by_party(self):
        self.assertEqual('foo'.upper(), 'FOO')