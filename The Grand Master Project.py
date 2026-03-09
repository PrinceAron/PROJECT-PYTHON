posts = [
    {"id": 1, "content": "Learning Python!", "likes": 120, "public": True},
    {"id": 2, "content": "Bad day...", "likes": 15, "public": True},
    {"id": 3, "content": "Check this out!", "likes": 300, "public": False},
    {"id": 4, "content": "Lambda functions are cool", "likes": 450, "public": True},
    {"id": 5, "content": "Dinner time", "likes": 50, "public": True}
]

public_posts = list(filter(lambda x: x['public'], posts))
public_posts.sort(key=lambda x: x['likes'])
print(public_posts)
print( )

likes_only = list(map(lambda x: x['likes'], public_posts))
print(likes_only)
print( )

from functools import reduce

total_likes = reduce(lambda x,y: x + y, likes_only, 0)
print(total_likes)
print( )

def create_feedback_msg(threshold):
    x = lambda score: "Viral Success!" if score > threshold  else "Niche Content"
    return x

feedback_checker = create_feedback_msg(500) 
result_msg = feedback_checker(total_likes)  

print(f"Total Likes: {total_likes}")
print(f"Feedback: {result_msg}")