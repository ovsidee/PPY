def calculateTotalSalesForEachProduct(data):
    for product, sales in data.items():
        total_sales = sum(sales)
        print(f"Total sales for {product}: {total_sales}")

def findMaxTotalSalesForProduct(data):
    productWithMaxTotalSalesForProduct = ""
    max = 0
    for product, sales in data.items():
        total_sales = sum(sales)
        if total_sales > max:
            max = total_sales
            productWithMaxTotalSalesForProduct = product
    print (f"Max total sales has {productWithMaxTotalSalesForProduct}: {max}")

sales_data = {
    'Product A': [100, 200, 300],
    'Product B': [150, 250, 350],
    'Product C': [50, 70, 90]
}

calculateTotalSalesForEachProduct(sales_data)
findMaxTotalSalesForProduct(sales_data)