def test_room_full_flow(admin_api):
    admin_api.login()

    room_name = "777"

    # CREATE
    admin_api.create_room(room_name, 150)

    # GET ROOM ID
    room_id = admin_api.get_room_id_by_name(room_name)

    # UPDATE
    admin_api.update_room(room_id, 200)

    # DELETE
    admin_api.delete_room(room_id)

    # VERIFY DELETE
    rooms = admin_api.get_rooms()
    assert not any(r["roomid"] == room_id for r in rooms)
