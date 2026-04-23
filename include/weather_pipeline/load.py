from datetime import datetime, timezone
from io import StringIO
import os

import boto3
import pandas as pd


def save_weather_to_s3(
    transformed_data: dict,
    city_name: str,
    bucket_name: str = "apiairflow",
) -> None:
    df = pd.DataFrame([transformed_data])

    safe_city_name = city_name.lower().replace(" ", "_")
    timestamp = datetime.now(timezone.utc).strftime("%d%m%Y%H%M%S")
    object_key = (
        f"current_weather_data/{safe_city_name}/"
        f"current_weather_data_{safe_city_name}_{timestamp}.csv"
    )

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3_client = boto3.client("s3")
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=csv_buffer.getvalue(),
        ContentType="text/csv",
    )

    print(f"Uploaded file to s3://{bucket_name}/{object_key}")
