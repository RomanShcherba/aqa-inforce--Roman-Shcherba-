from app.base_api import BaseAPI


class UserAPI(BaseAPI):

    def get_rooms(self):
        response = self.get("/room")
        assert response.status_code == 200
        return response.json()["rooms"]

    def book_room(self, room_id):
        payload = {
            "roomid": room_id,
            "firstname": "Roman",
            "lastname": "Test",
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-10",
                "checkout": "2025-01-12"
            }
        }

        response = self.post("/booking", json=payload)
        assert response.status_code == 200
        return response.json()["bookingid"]
