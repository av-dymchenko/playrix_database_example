import pytest
import pymysql
import config

@pytest.fixture
def cursor():
    connection = pymysql.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        port=config.port,
        db=config.db_name
    )
    cursor = connection.cursor()
    return cursor