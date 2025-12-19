# Automation Tests – UI & API for Booking System

This project contains both **UI** and **API** automation tests for the demo application:  
👉 [https://automationintesting.online/]

- **UI tests**: Validate booking flow in the frontend using **Playwright + Pytest (async)**  
- **API tests**: Validate room management and bookings via **REST API** using **Python + Requests + Pytest**

---

## 📌 Tested Flows

### UI Automation

1. Open Booking page
2. Fill booking form with valid and invalid data
3. Verify errors for invalid input
4. Book rooms (Single, Double, Suite)
5. Verify reserved dates are unavailable
6. Check success messages and disabled buttons

### API Automation

1. **Create a Room** via Admin API → Verify room visible via User API
2. **Book a Room** via User API → Verify booking created successfully
3. **Edit Room** via Admin API → Verify updated data via User API
4. **Delete Room** via Admin API → Verify room no longer visible via User API

> ⚠️ Note: The demo API is unstable and may not strictly follow REST conventions. Tests are written to handle real behavior.

---

## 🧰 Tech Stack

- Python 3.10+
- Pytest
- Requests (API tests)
- Playwright (UI tests)
- Virtualenv (optional but recommended)

Create and activate virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

Install Playwright browsers (for UI tests)
playwright install

Running Tests
UI Tests (Playwright)
pytest -v tests/ui
# To see the browser
pytest -v tests/ui --headed

API Tests (Requests)
pytest -v tests/api
