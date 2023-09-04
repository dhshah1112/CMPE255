from dataclasses import dataclass

@dataclass
class Message:
    id: int
    sender_id: int
    receiver_id: int
    content: str
    timestamp: str

    def send_message(self, receiver_id: int, content: str) -> None:
        # Send a message to a user
        pass

    def get_messages(self, user_id: int) -> list[str]:
        # Get messages for a user
        pass
