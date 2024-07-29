import pandas as pd
from app.main import total_revenue_by_month, total_revenue_by_product, total_revenue_by_customer, top_10_customers_by_revenue

def test_total_revenue_by_month():
    data = {
        'order_id': [1, 2],
        'customer_id': [1, 2],
        'order_date': ['2023-01-15', '2023-02-15'],
        'product_id': [1, 2],
        'product_name': ['Product A', 'Product B'],
        'product_price': [100, 200],
        'quantity': [1, 2]
    }
    df = pd.DataFrame(data)
    result = total_revenue_by_month(df)
    assert result['2023-01'] == 100
    assert result['2023-02'] == 400

def test_total_revenue_by_product():
    data = {
        'order_id': [1, 2],
        'customer_id': [1, 2],
        'order_date': ['2023-01-15', '2023-02-15'],
        'product_id': [1, 2],
        'product_name': ['Product A', 'Product B'],
        'product_price': [100, 200],
        'quantity': [1, 2]
    }
    df = pd.DataFrame(data)
    result = total_revenue_by_product(df)
    assert result['Product A'] == 100
    assert result['Product B'] == 400

def test_total_revenue_by_customer():
    data = {
        'order_id': [1, 2],
        'customer_id': [1, 2],
        'order_date': ['2023-01-15', '2023-02-15'],
        'product_id': [1, 2],
        'product_name': ['Product A', 'Product B'],
        'product_price': [100, 200],
        'quantity': [1, 2]
    }
    df = pd.DataFrame(data)
    result = total_revenue_by_customer(df)
    assert result[1] == 100
    assert result[2] == 400

def test_top_10_customers_by_revenue():
    data = {
        'order_id': [1, 2, 3],
        'customer_id': [1, 2, 3],
        'order_date': ['2023-01-15', '2023-02-15', '2023-03-15'],
        'product_id': [1, 2, 3],
        'product_name': ['Product A', 'Product B', 'Product C'],
        'product_price': [100, 200, 300],
        'quantity': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    result = top_10_customers_by_revenue(df)
    assert len(result) == 3
    assert result.iloc[0] == 900
    assert result.iloc[1] == 400
    assert result.iloc[2] == 100
