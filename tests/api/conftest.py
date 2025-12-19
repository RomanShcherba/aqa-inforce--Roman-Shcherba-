import pytest
from app.admin_api import AdminAPI
from app.user_api import UserAPI

@pytest.fixture
def admin_api():
    api = AdminAPI()
    api.login()
    return api

@pytest.fixture
def user_api():
    return UserAPI()