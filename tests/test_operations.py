import pytest
from pysqlitehelper.helpers import SQLiteHelper


TB_COLUMNS = {
    'title': 'text',
    'description':'text',
    'completed':'boolean',
}


@pytest.fixture
def validator():
    return SQLiteHelper('db')


def test_create_table(validator):
    validator.create_table('test_table',columns=TB_COLUMNS)
    assert validator.table_exists('test_table')



def test_insert_to_table(validator):
    is_inserted = validator.insert('test_table',values={
        'title':'test',
        'description':'test',
        'completed':'True'
    })
    assert is_inserted == True

def test_get_table_column(validator):
    assert isinstance(validator.getColumns('test_table'),list) == True


def test_select_all(validator):
    assert isinstance(validator.selectAll('test_table'),list)



def test_select_where(validator):
    assert isinstance(validator.selectWhereId('test_table',2),dict) == True

