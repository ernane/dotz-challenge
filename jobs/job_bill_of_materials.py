import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import ApplyMapping, DropNullFields, ResolveChoice
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)
## @type: DataSource
## @args: [database = "dotz_challenge_raw", table_name = "bill_of_materials_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="dotz_challenge_raw",
    table_name="bill_of_materials_csv",
    transformation_ctx="datasource0",
)
## @type: ApplyMapping
## @args: [mapping = [("col0", "string", "col0", "string"), ("col1", "string", "col1", "string"), ("col2", "string", "col2", "string"), ("col3", "string", "col3", "string"), ("col4", "string", "col4", "string"), ("col5", "string", "col5", "string"), ("col6", "string", "col6", "string"), ("col7", "string", "col7", "string"), ("col8", "string", "col8", "string"), ("col9", "string", "col9", "string"), ("col10", "string", "col10", "string"), ("col11", "string", "col11", "string"), ("col12", "string", "col12", "string"), ("col13", "string", "col13", "string"), ("col14", "string", "col14", "string"), ("col15", "string", "col15", "string"), ("col16", "string", "col16", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        ("col0", "string", "col0", "string"),
        ("col1", "string", "col1", "string"),
        ("col2", "string", "col2", "string"),
        ("col3", "string", "col3", "string"),
        ("col4", "string", "col4", "string"),
        ("col5", "string", "col5", "string"),
        ("col6", "string", "col6", "string"),
        ("col7", "string", "col7", "string"),
        ("col8", "string", "col8", "string"),
        ("col9", "string", "col9", "string"),
        ("col10", "string", "col10", "string"),
        ("col11", "string", "col11", "string"),
        ("col12", "string", "col12", "string"),
        ("col13", "string", "col13", "string"),
        ("col14", "string", "col14", "string"),
        ("col15", "string", "col15", "string"),
        ("col16", "string", "col16", "string"),
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
## @args: [catalog_connection = "dotz_connection", connection_options = {"dbtable": "bill_of_materials_csv", "database": "dotz_challenge"}, transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = dropnullfields3]
datasink4 = glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=dropnullfields3,
    catalog_connection="dotz_connection",
    connection_options={
        "dbtable": "bill_of_materials",
        "database": "dotz_challenge",
    },
    transformation_ctx="datasink4",
)
job.commit()
