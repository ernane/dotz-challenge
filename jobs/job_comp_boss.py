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
## @args: [database = "dotz_challenge_raw", table_name = "comp_boss_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="dotz_challenge_raw", table_name="comp_boss_csv", transformation_ctx="datasource0"
)
## @type: ApplyMapping
## @args: [mapping = [("component_id", "string", "component_id", "string"), ("component_type_id", "string", "component_type_id", "string"), ("type", "string", "type", "string"), ("connection_type_id", "string", "connection_type_id", "string"), ("outside_shape", "string", "outside_shape", "string"), ("base_type", "string", "base_type", "string"), ("height_over_tube", "double", "height_over_tube", "double"), ("bolt_pattern_long", "string", "bolt_pattern_long", "string"), ("bolt_pattern_wide", "string", "bolt_pattern_wide", "string"), ("groove", "string", "groove", "string"), ("base_diameter", "string", "base_diameter", "string"), ("shoulder_diameter", "string", "shoulder_diameter", "string"), ("unique_feature", "string", "unique_feature", "string"), ("orientation", "string", "orientation", "string"), ("weight", "string", "weight", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        ("component_id", "string", "component_id", "string"),
        ("component_type_id", "string", "component_type_id", "string"),
        ("type", "string", "type", "string"),
        ("connection_type_id", "string", "connection_type_id", "string"),
        ("outside_shape", "string", "outside_shape", "string"),
        ("base_type", "string", "base_type", "string"),
        ("height_over_tube", "double", "height_over_tube", "double"),
        ("bolt_pattern_long", "string", "bolt_pattern_long", "string"),
        ("bolt_pattern_wide", "string", "bolt_pattern_wide", "string"),
        ("groove", "string", "groove", "string"),
        ("base_diameter", "string", "base_diameter", "string"),
        ("shoulder_diameter", "string", "shoulder_diameter", "string"),
        ("unique_feature", "string", "unique_feature", "string"),
        ("orientation", "string", "orientation", "string"),
        ("weight", "string", "weight", "string"),
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
## @args: [catalog_connection = "dotz_connection", connection_options = {"dbtable": "comp_boss_csv", "database": "dotz_challenge"}, transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = dropnullfields3]
datasink4 = glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=dropnullfields3,
    catalog_connection="dotz_connection",
    connection_options={"dbtable": "comp_boss", "database": "dotz_challenge"},
    transformation_ctx="datasink4",
)
job.commit()
