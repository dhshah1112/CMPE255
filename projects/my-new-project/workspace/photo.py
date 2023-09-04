from dataclasses import dataclass

@dataclass
class Photo:
    id: int
    user_id: int
    caption: str
    image_url: str
    timestamp: str

    def upload_photo(self, user_id: int, caption: str, image_url: str) -> int:
        # Upload a photo and return its ID
        pass

    def get_photos(self, user_id: int) -> list[int]:
        # Get photos for a user
        pass
