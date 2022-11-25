from google.cloud import bigquery
from google.oauth2 import service_account
import json

credentials = service_account.Credentials.from_service_account_file(
    'key.json')
client = bigquery.Client(credentials=credentials)


def prediction(request):
    nbrecos = request.args.get("nbrecos", 1)
    headers = {"Content-Type": "application/json"}
    query = """
      SELECT
      *
      FROM
      ML.FORECAST(MODEL `sood-365307.parkings_eu.PARKING_ENCAN`,
             STRUCT({} AS horizon, 0.8 AS confidence_level))
    """.format(nbrecos)
    query_job = client.query(query)  # Make an API request.
    prediction_df = query_job.to_dataframe()
    prediction_json = prediction_df[prediction_df["id"] == "17300-P-003"][["forecast_timestamp","forecast_value"]].to_json(date_format='iso')
    prediction_json = json.loads(prediction_json)
    return (prediction_json, 200, headers)
