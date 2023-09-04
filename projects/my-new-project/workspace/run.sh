   sudo apt-get update
   sudo apt-get install python3
   
   sudo apt-get install python3-pip
   
   pip3 install dataclasses
   
   from user import User
   from post import Post
   from friend_request import FriendRequest
   from message import Message
   from photo import Photo

   # Create instances of the classes and perform actions
   user = User(1, "John Doe", "john@example.com", "password", "profile.jpg", [], [])
   user.register("John Doe", "john@example.com", "password")
   user.login("john@example.com", "password")
   post_id = user.create_post("Hello, world!")
   user.like_post(post_id)
   user.comment_on_post(post_id, "Nice post!")
   user.share_post(post_id)
   user.add_friend(2)

   post = Post(1, 1, "Hello, world!", "2022-01-01 12:00:00", 1, ["Nice post!"], 1)
   post.add_like()
   post.add_comment("Great post!")
   post.add_share()

   friend_request = FriendRequest(1, 2, "pending")
   friend_request.send_request()
   friend_request.accept_request()
   friend_request.reject_request()

   message = Message(1, 1, 2, "Hello!", "2022-01-01 12:00:00")
   message.send_message(2, "How are you?")
   messages = message.get_messages(1)

   photo = Photo(1, 1, "My photo", "photo.jpg", "2022-01-01 12:00:00")
   photo_id = photo.upload_photo(1, "My photo", "photo.jpg")
   photos = photo.get_photos(1)
   
   python3 main.py
   