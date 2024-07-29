import pandas as pd
from datetime import datetime

def load_data(file_path):
    return pd.read_csv(file_path)

def total_revenue_by_month(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    revenue_by_month = df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_by_month

def total_revenue_by_product(df):
    revenue_by_product = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_by_product

def total_revenue_by_customer(df):
    revenue_by_customer = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_by_customer

def top_10_customers_by_revenue(df):
    revenue_by_customer = total_revenue_by_customer(df)
    top_10_customers = revenue_by_customer.nlargest(10)
    return top_10_customers

def main():
    file_path = 'orders.csv'
    df = load_data(file_path)
    print("Total Revenue by Month:")
    print(total_revenue_by_month(df))
    print("\nTotal Revenue by Product:")
    print(total_revenue_by_product(df))
    print("\nTotal Revenue by Customer:")
    print(total_revenue_by_customer(df))
    print("\nTop 10 Customers by Revenue:")
    print(top_10_customers_by_revenue(df))

if __name__ == "__main__":
    main()
