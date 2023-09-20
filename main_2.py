from pyspark.sql import SparkSession
from pyspark.sql.functions import explode_outer

# Создаем SparkSession
spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

# Создаем датафреймы с продуктами и категориями
products_data = [("Product1", ["Category1", "Category2"]),
                 ("Product2", ["Category2"]),
                 ("Product3", ["Category1", "Category3"]),
                 ("Product4", [])]

categories_data = [("Category1", "CategoryName1"),
                   ("Category2", "CategoryName2"),
                   ("Category3", "CategoryName3")]

products_df = spark.createDataFrame(products_data, ["Product", "Categories"])
categories_df = spark.createDataFrame(categories_data, ["CategoryId", "CategoryName"])

# Развертываем списки категорий с использованием explode_outer
products_expanded_df = products_df.select("Product", explode_outer("Categories").alias("CategoryId"))

# Выполняем объединение с таблицей категорий с использованием left_outer
result_df = products_expanded_df.join(categories_df, products_expanded_df["CategoryId"] == categories_df["CategoryId"], "left_outer") \
    .select("Product", "CategoryName")

# Заменяем пустые значения в столбце "CategoryName" на "No Category"
result_df = result_df.na.fill("No Category", ["CategoryName"])

# Отображаем результат
result_df.show()


# Второе решение с помощью pandas
import pandas as pd

# Создаем датафреймы с продуктами и категориями
products_data = {
    'Product': ['Product1', 'Product2', 'Product3', 'Product4'],
    'Categories': [['Category1', 'Category2'], ['Category2'], ['Category1', 'Category3'], []]
}

categories_data = {
    'CategoryId': ['Category1', 'Category2', 'Category3'],
    'CategoryName': ['CategoryName1', 'CategoryName2', 'CategoryName3']
}

products_df = pd.DataFrame(products_data)
categories_df = pd.DataFrame(categories_data)

# Развертываем списки категорий и объединяем датафреймы
result_df = products_df.explode('Categories', ignore_index=True) \
    .merge(categories_df, left_on='Categories', right_on='CategoryId', how='left') \
    .drop(columns='CategoryId')

# Заполняем пустые значения в столбце 'CategoryName' строкой 'No Category'
result_df['CategoryName'].fillna('No Category', inplace=True)

# Отображаем результат
print(result_df)
