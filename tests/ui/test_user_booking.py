import pytest
from pages.user_page import UserPage

@pytest.mark.asyncio
async def test_tc_ui_01_booking_valid(page):
    user_page = UserPage(page)
    await user_page.open("https://automationintesting.online/")
    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-18", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data(
        firstname="Andrew",
        lastname="Satory",
        email="qwerty@gmail.com",
        phone="+380952553232"
    )
    await user_page.submit_reservation()

    success_message = await user_page.get_success_message()
    assert "Booking Confirmed" in success_message

@pytest.mark.asyncio
async def test_tc_ui_02_blank_fields(page):
    """
    TC_UI_02: Book room with blank fields
    """
    user_page = UserPage(page)
    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-18", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data()
    await user_page.submit_reservation()

    assert "Firstname should not be blank"
    assert "Lastname should not be blank"
    assert "must not be empty"
    assert "must not be empty"

@pytest.mark.asyncio
async def test_tc_ui_03_short_firstname_lastname(page):
    """
    TC_UI_03: Fields less than 3 characters
    """
    user_page = UserPage(page)
    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-18", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data(
        firstname="Jo",
        lastname="Jo",
        email="qwerty@gmail.com",
        phone="+380952553232"
    )
    await user_page.submit_reservation()
    assert "size must be between 3 and 18"
    assert "size must be between 11 and 21"

@pytest.mark.asyncio
async def test_tc_ui_04_long_firstname_lastname(page):
    """
    TC_UI_04: Name and Lastname more than valid range
    """
    user_page = UserPage(page)

    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-18", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data(
        firstname="w" * 19,
        lastname="w" * 31,
        email="qwerty@gmail.com",
        phone="+380952553232"
    )
    await user_page.submit_reservation()
    assert "size must be between 3 and 18"
    assert "size must be between 11 and 21"

@pytest.mark.asyncio
async def test_tc_ui_05_bad_email(page):
    """
    TC_UI_05: Bad-formed email
    """
    user_page = UserPage(page)

    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-18", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data(
        firstname="Joe",
        lastname="Joe",
        email="qwerty",
        phone="+380952553232"
    )
    await user_page.submit_reservation()

    assert "must be a well-formed email address"

@pytest.mark.asyncio
async def test_tc_ui_06_short_phone(page):
    """
    TC_UI_06: Phone number with 10 characters
    """
    user_page = UserPage(page)

    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-18", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data(
        firstname="Joe",
        lastname="Joe",
        email="qwerty@gmail.com",
        phone="1234567890"
    )
    await user_page.submit_reservation()

    assert "size must be between 11 and 21"

@pytest.mark.asyncio
async def test_tc_ui_07_long_phone(page):
    """
    TC_UI_07: Phone number with 22 characters
    """
    user_page = UserPage(page)

    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-18", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data(
        firstname="Joe",
        lastname="Joe",
        email="qwerty@gmail.com",
        phone="11234567890123456789012"
    )
    await user_page.submit_reservation()
    assert "size must be between 11 and 21"

@pytest.mark.asyncio
async def test_tc_ui_08_unavailable_dates(page):
    """
    TC_UI_08: Booked dates are unavailable
    """
    user_page = UserPage(page)

    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-19", "2025-12-20")
    await user_page.check_availability()
    await user_page.book_single_room()
    await user_page.click_reserve_now()
    await user_page.fill_customer_data(
        firstname="Andrew",
        lastname="Satory",
        email="qwerty@gmail.com",
        phone="+380952553232"
    )
    await user_page.submit_reservation()
    await user_page.open_booking_page()
    await user_page.set_dates("2025-12-19", "2025-12-19")
    await user_page.check_availability()
    await user_page.book_single_room()

    assert "Booked dates should be marked as Unavailable"