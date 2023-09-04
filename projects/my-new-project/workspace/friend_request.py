from dataclasses import dataclass

@dataclass
class FriendRequest:
    sender_id: int
    receiver_id: int
    status: str

    def send_request(self) -> None:
        # Send a friend request
        pass

    def accept_request(self) -> None:
        # Accept a friend request
        pass

    def reject_request(self) -> None:
        # Reject a friend request
        pass
