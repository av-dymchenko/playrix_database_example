import pymysql
import config
import pytest
import base
import allure


@allure.parent_suite('Проверка таблиц БД')
class TestTable():

    # проверяем количество столбцов
    @allure.title('Количество столбцов таблицы {table_name} соответствуют требованиям')
    @pytest.mark.parametrize('table_name',['utk_action_promocode'])
    def test_utk_action_promocode_columns_count_equals_requirement(
            self,
            table_name,
            cursor):
        base.columns_count_equals_requirement(cursor, table_name)

    # проверяем имена столбцов
    @allure.title('Имена столбцов таблицы {table_name} соответствуют требованиям')
    @pytest.mark.parametrize('table_name', ['utk_action_promocode'])
    def test_utk_action_promocode_columns_names_equals_requirement(
            self,
            table_name,
            cursor):
        base.columns_names_equals_requirement(cursor, table_name)

    # проверяем типы данных столбцов
    @allure.title('Типы данных столбцов таблицы {table_name} соответствуют требованиям')
    @pytest.mark.parametrize('table_name', ['utk_action_promocode'])
    def test_utk_action_promocode_columns_types_equals_requirement(
            self,
            table_name,
            cursor):
        base.columns_types_equals_requirement(cursor, table_name)
        
