# Created by Marcin "Cozoob" Kozub 30.09.2021
from math import inf
from statistics import median, mean

def get_influencer_metrics(blog_posts):
    # return three metrics in the tuple
    # (sum_of_likes, mean_likes_to_comments_ratio, median_of_posted_photos)
    the_likes = sum(post.get("Likes", 0) for post in blog_posts)
    likes_comments_ratios = []

    the_photos = []
    for post in blog_posts:
        try:
            likes_comments_ratios.append(post["Likes"] / post["Comments"])
            the_photos.append(post["Photos"])
        except ZeroDivisionError:
            pass
        except KeyError:
            pass
    the_photos.sort()

    return the_likes, round(mean(likes_comments_ratios), 3), median(the_photos)

if __name__ == '__main__':
    blog_posts = [
        {'Photos': 3, 'Likes': 21, 'Comments': 2},
        {'Likes': 13, 'Shares': 1},
        {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
        {'Comments': 4, 'Shares': 2},
        {'Photos': 8, 'Comments': 1, 'Shares': 1},
        {'Photos': 3, 'Likes': 19, 'Comments': 3}
    ]
    print(get_influencer_metrics(blog_posts))