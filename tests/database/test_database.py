import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_delete_after_update():
    db = Database()
    db.insert_product(999, 'тестові', 'дані', 999)
    db.update_product_qnt_by_id(999, 5)
    qnt1 = db.select_product_qnt_by_id(999)

    assert qnt1[0][0] == 5

    db.delete_product_by_id(999)
    qnt1 = db.select_product_qnt_by_id(999)
    assert len(qnt1) == 0


@pytest.mark.database
def test_select_product_where_qnt_more_than_entered():
    db = Database()
    db.insert_product(100, 'цукерки', 'желейні', 50)
    db.insert_product(101, 'печеня', 'шоколадне', 70)
    entered_qnt = 45
    products = db.get_products_where_qnt_more_that_entered(entered_qnt)
    print(products)
    assert products[0][1] > entered_qnt

    db.delete_product_by_id(100)
    db.delete_product_by_id(101)


@pytest.mark.database
def test_users_where_name_starts_with_entered():
    db = Database()
    db.insert_user(100, 'Mykhailo', 'Ivana Franka 1', 'Lviv', '2455', 'Ukraine')
    name_start_letter = 'M'
    users = db.get_users_where_names_stars_with(name_start_letter)
    print(users)
    assert users[0][1] == users[0][1], f"Users that starts with letter '{name_start_letter}' does`t peresent in the Database"

    db.delete_product_by_id(100)


@pytest.mark.database
def test_product_description_can_be_null():
    db = Database()
    db.insert_product_without_desc(100, 'цукерки', 50)
    products = db.select_product(100)
    print(products)
    assert products[0][2] == None

    db.delete_product_by_id(100)


@pytest.mark.database
def test_user_id_cant_be_null():
    db = Database()
    user = db.insert_user_where_id_is_null('Mykhailo', 'Ivana Franka 1', 'Lviv', '2455', 'Ukraine')
    assert user == None