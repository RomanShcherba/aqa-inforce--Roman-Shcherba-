from pages.base_page import BasePage


class UserPage(BasePage):

    # ===== Navigation =====
    BOOKING_BUTTON = "//nav//a[normalize-space()='Booking']"

    # ===== Booking form =====
    CHECKIN_INPUT = "//label[normalize-space()='Check In']/following::input[1]"
    CHECKOUT_INPUT = "//label[normalize-space()='Check Out']/following::input[1]"
    CHECK_AVAILABILITY_BUTTON = "//button[normalize-space()='Check Availability']"

    # ===== Rooms =====
    SINGLE_BOOK_NOW = "(//a[@class='btn btn-primary'])[1]"
    DOUBLE_BOOK_NOW = "(//a[@class='btn btn-primary'])[2]"
    SUITE_BOOK_NOW = "(//a[@class='btn btn-primary'])[3]"

    # ===== Reservation form =====
    FIRSTNAME_INPUT = "//input[@placeholder='Firstname']"
    LASTNAME_INPUT = "//input[@placeholder='Lastname']"
    EMAIL_INPUT = "//input[@placeholder='Email']"
    PHONE_INPUT = "//input[@placeholder='Phone']"
    RESERVE_NOW_BUTTON = "//button[normalize-space(text())='Reserve Now']"
    SELECTED_ROOM = "//div[@title='Selected']"

    # ===== Errors =====
    FIRSTNAME_ERROR = "//li[contains(text(),'First name')]"
    LASTNAME_ERROR = "//li[contains(text(),'Last name')]"
    EMAIL_ERROR = "//li[contains(text(),'Email')]"
    PHONE_ERROR = "//li[contains(text(),'Phone')]"
    CHECKIN_ERROR = "//li[contains(text(),'Check in')]"
    CHECKOUT_ERROR = "//li[contains(text(),'Check out')]"

    # ===== Success =====
    SUCCESS_MESSAGE = "//h2[normalize-space()='Booking Confirmed']"
    UNAVAILABLE_LABEL = "//div[@title='Unavailable']"
    # ================= ACTIONS =================
    
    async def open(self, url: str):
        await self.page.goto(url)

    async def open_booking_page(self):
        await self.click(self.BOOKING_BUTTON)

    async def set_dates(self, checkin: str, checkout: str):
        await self.fill(self.CHECKIN_INPUT, checkin)
        await self.fill(self.CHECKOUT_INPUT, checkout)

    async def check_availability(self):
        await self.click(self.CHECK_AVAILABILITY_BUTTON)
        await self.page.wait_for_selector(self.SINGLE_BOOK_NOW)

    async def book_single_room(self):
        await self.click(self.SINGLE_BOOK_NOW)

    async def book_double_room(self):
        await self.click(self.DOUBLE_BOOK_NOW)

    async def book_suite_room(self):
        await self.click(self.SUITE_BOOK_NOW)

    async def get_selected_room(self):
        await self.click(self.SELECTED_ROOM)
    
    async def click_reserve_now(self): 
        await self.click(self.RESERVE_NOW_BUTTON)

    async def fill_customer_data(
        self,
        firstname: str = "",
        lastname: str = "",
        email: str = "",
        phone: str = ""
    ):
        await self.fill(self.FIRSTNAME_INPUT, firstname)
        await self.fill(self.LASTNAME_INPUT, lastname)
        await self.fill(self.EMAIL_INPUT, email)
        await self.fill(self.PHONE_INPUT, phone)

    async def submit_reservation(self):
        await self.click(self.RESERVE_NOW_BUTTON)

    # ================= ASSERTIONS =================

    async def get_success_message(self) -> str:
        return await self.get_text(self.SUCCESS_MESSAGE)

    async def get_firstname_error(self) -> str:
        return await self.get_text(self.FIRSTNAME_ERROR)

    async def get_lastname_error(self) -> str:
        return await self.get_text(self.LASTNAME_ERROR)

    async def get_email_error(self) -> str:
        return await self.get_text(self.EMAIL_ERROR)

    async def get_phone_error(self) -> str:
        return await self.get_text(self.PHONE_ERROR)
    
    async def is_room_unavailable(self) -> bool:
        return await self.page.locator(self.UNAVAILABLE_LABEL).is_visible()
