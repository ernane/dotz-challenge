import sys
from awsglue.transforms import ApplyMapping, ResolveChoice, DropNullFields
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)
## @type: DataSource
## @args: [database = "dotz_challenge_raw", table_name = "price_quote_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="dotz_challenge_raw",
    table_name="price_quote_csv",
    transformation_ctx="datasource0",
)
## @type: ApplyMapping
## @args: [mapping = [("tube_assembly_id", "string", "tube_assembly_id", "string"), ("supplier", "string", "supplier", "string"), ("quote_date", "string", "quote_date", "string"), ("annual_usage", "long", "annual_usage", "long"), ("min_order_quantity", "long", "min_order_quantity", "long"), ("bracket_pricing", "string", "bracket_pricing", "string"), ("quantity", "long", "quantity", "long"), ("cost", "double", "cost", "double")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        ("tube_assembly_id", "string", "tube_assembly_id", "string"),
        ("supplier", "string", "supplier", "string"),
        ("quote_date", "string", "quote_date", "string"),
        ("annual_usage", "long", "annual_usage", "long"),
        ("min_order_quantity", "long", "min_order_quantity", "long"),
        ("bracket_pricing", "string", "bracket_pricing", "string"),
        ("quantity", "long", "quantity", "long"),
        ("cost", "double", "cost", "double"),
    ],
    transformation_ctx="applymapping1",
)
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice2"]
## @return: resolvechoice2
## @inputs: [frame = applymapping1]
resolvechoice2 = ResolveChoice.apply(
    frame=applymapping1, choice="make_cols", transformation_ctx="resolvechoice2"
)
## @type: DropNullFields
## @args: [transformation_ctx = "dropnullfields3"]
## @return: dropnullfields3
## @inputs: [frame = resolvechoice2]
dropnullfields3 = DropNullFields.apply(
    frame=resolvechoice2, transformation_ctx="dropnullfields3"
)
## @type: DataSink
## @args: [catalog_connection = "dotz_connection", connection_options = {"dbtable": "price_quote_csv", "database": "dotz_challenge"}, transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = dropnullfields3]
datasink4 = glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=dropnullfields3,
    catalog_connection="dotz_connection",
    connection_options={"dbtable": "price_quote", "database": "dotz_challenge"},
    transformation_ctx="datasink4",
)
job.commit()
