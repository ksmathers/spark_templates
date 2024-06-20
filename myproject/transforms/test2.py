from sparkle import transform, Input, Output
from pyspark.sql import DataFrame
import pyspark.sql.functions as F
from datetime import datetime

def pyspark_fn(df : DataFrame) -> DataFrame:
    now = datetime.now().strftime("%Y-%m-%d")
    return df.withColumn('version', F.lit(now))

@transform(
    i = Input("/myproject/data/raw/main/Master"),
    o = Output("/myproject/data/raw/clean/Master_clean")
)
def compute(i, o):
    df = i.dataframe()
    result = pyspark_fn(df)
    o.write_dataframe(i.dataframe())
