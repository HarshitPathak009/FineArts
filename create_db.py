from app import db, User, Post
from pic_db import database as d 

db.drop_all()
db.create_all()
print(User.query.all())

for i in d:
    user = User(artist_name=i, instagram=d[i]["instagram"], branch=d[i]["branch"], image=d[i]["profile_url"])
    db.session.add(user)
    db.session.commit()

print(User.query.all())
print(Post.query.all())

for i in User.query.all():
    for j in d[i.artist_name]["images_url"]:
        work = Post(art=j["url"],artist_id=i.id)
        db.session.add(work)
        db.session.commit()

print(Post.query.all())
