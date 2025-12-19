from app.base_api import BaseAPI


class AdminAPI(BaseAPI):

    def login(self):
        response = self.post(
            "/auth/login",
            json={
                "username": "admin",
                "password": "password"
            }
        )

        assert response.status_code == 200, "Admin login failed"

        token = response.json().get("token")
        assert token, "Auth token not returned"

        self.session.headers.update({
            "Cookie": f"token={token}"
        })

    def create_room(self, name: str, price: int):
        payload = {
            "roomName": name,
            "type": "Suite",
            "accessible": True,
            "image": "https://example.com/room.png",
            "description": f"Room {name} created via API",
            "roomPrice": price,
            "features": ["WiFi", "Safe"]
        }

        response = self.post("/room", json=payload)

        assert response.status_code == 200, (
            f"Create room failed: {response.status_code}, {response.text}"
        )

    def get_rooms(self):
        response = self.get("/room")
        assert response.status_code == 200
        return response.json()["rooms"]

    def get_room_id_by_name(self, room_name: str) -> int:
        rooms = self.get_rooms()
        room = next((r for r in rooms if r["roomName"] == room_name), None)
        assert room, f"Room '{room_name}' not found"
        return room["roomid"]

    def update_room(self, room_id: int, new_price: int):
        payload = {
            "roomName": "Updated Room",
            "type": "Double",
            "accessible": False,
            "image": "https://example.com/updated.png",
            "description": "Updated via API",
            "roomPrice": new_price,
            "features": ["TV", "Refreshments"]
        }

        response = self.put(f"/room/{room_id}", json=payload)
        assert response.status_code == 200, (
            f"Update room failed: {response.status_code}"
        )

    def delete_room(self, room_id: int):
        response = self.delete(f"/room/{room_id}")
        assert response.status_code == 200, (
            f"Delete room failed: {response.status_code}"
        )
