from dataclasses import dataclass

@dataclass
class Post:
    id: int
    user_id: int
    content: str
    timestamp: str
    likes: int
    comments: list[str]
    shares: int

    def add_like(self) -> None:
        # Add a like to the post
        pass

    def add_comment(self, comment: str) -> None:
        # Add a comment to the post
        pass

    def add_share(self) -> None:
        # Add a share to the post
        pass
