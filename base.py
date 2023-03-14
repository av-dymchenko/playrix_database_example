from Tables import utk_action_promocode
import allure


tables_and_columns_count = {
    'utk_action_promocode': 10
}

@allure.step('Проверяем имена столбцов')
def columns_names_equals_requirement(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 0;")
    column_headers = [desc[0] for desc in cursor.description]
    assert column_headers == list(
        utk_action_promocode.columns_and_types.keys()), "Неверные заголовки столбцов"

@allure.step('Проверяем типы столбцов')
def columns_types_equals_requirement(cursor, table_name):
    for column_header, expected_type in utk_action_promocode.columns_and_types.items():
        cursor.execute(
            f"SELECT data_type "
            f"FROM information_schema.columns "
            f"WHERE table_name='{table_name}' "
            f"AND column_name='{column_header}';")

        data_type = cursor.fetchone()[0]
        assert data_type == expected_type, f"Тип данных столбца {column_header} не является {expected_type}"

@allure.step('Проверяем количество столбцов')
def columns_count_equals_requirement(cursor, table_name):
    columns_count = tables_and_columns_count[table_name]
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    assert len(columns) == columns_count, "Неверное количество столбцов"