from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    profile_picture: str
    friends: list[int]
    posts: list[int]

    def register(self, name: str, email: str, password: str) -> None:
        # Register a new user
        pass

    def login(self, email: str, password: str) -> bool:
        # Login user and return True if successful
        pass

    def create_post(self, content: str) -> int:
        # Create a new post and return its ID
        pass

    def like_post(self, post_id: int) -> None:
        # Like a post
        pass

    def comment_on_post(self, post_id: int, comment: str) -> None:
        # Add a comment to a post
        pass

    def share_post(self, post_id: int) -> None:
        # Share a post
        pass

    def add_friend(self, friend_id: int) -> None:
        # Send a friend request
        pass
