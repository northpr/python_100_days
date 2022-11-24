facebook_posts = [
    {"Post_no":0, "Likes": 21, "Comments":2},
    {"Post_no":1, "Likes": 13, "Comments":2, "Shares":1},
    {"Post_no":2, "Likes": 33, "Comments":8, "Shares":3},
    {"Post_no":3, "Comments":4, "Shares":2},
    {"Post_no":4, "Comments":1, "Shares":1},
    {"Post_no":5, "Likes":19, "Comments":3}
]

total_likes = 0
missing_like = 0
missing_like_postnum = []
for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        missing_like += 1
        missing_like_postnum.append(post["Post_no"])
        
print(f"Total likes: {total_likes}")
print(f"Missing: {missing_like}")
print(f"Post without like: {missing_like_postnum}")