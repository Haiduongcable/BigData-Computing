from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName('abc').getOrCreate()
# df=spark.read.csv('/home/haiduong/Documents/Project_2/Data/data_dienthoai/product.csv',header=True)

spark  = SparkSession.builder\
                  .master("local")\
                  .enableHiveSupport()\
                  .getOrCreate()

# spark.conf.set("spark.executor.memory", '8g')
# spark.conf.set('spark.executor.cores', '3')
# spark.conf.set('spark.cores.max', '3')
# spark.conf.set("spark.driver.memory",'8g')
sc = spark.sparkContext
df= spark.read.csv('/home/haiduong/Documents/Project_2/Data/data_dienthoai/product.csv',header=True)