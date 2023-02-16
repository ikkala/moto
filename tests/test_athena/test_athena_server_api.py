import requests

from moto import mock_athena, settings
from unittest import SkipTest


#boto3.set_stream_logger(name='botocore')

@mock_athena
def test_set_athena_result():
    if not settings.TEST_SERVER_MODE:
        raise SkipTest("We only want to test ServerMode here")

    requests.get(
        "http://localhost:5000/moto-api/seed?a=42",
    )
    exex_id = "bdd640fb-0667-4ad1-9c80-317fa3b1799d"
    athena_result = {
        "region": "eu-west-1",
        "query_execution_id": exex_id,
        "rows": [
            {"Headers": ["first_column"]},
            {"Data": [{"VarCharValue": "1"}]},
        ],
        "column_info": [
            {
                "CatalogName": "string",
                "SchemaName": "string",
                "TableName": "string",
                "Name": "string",
                "Label": "string",
                "Type": "string",
                "Precision": 123,
                "Scale": 123,
                "Nullable": "NOT_NULL",
                "CaseSensitive": True,
            }
        ],
    }
    resp = requests.post(
        "http://localhost:5000/moto-api/static/athena/account/region/query_executions",
        json=athena_result,
    )
    resp.status_code.should.equal(201)

    #client = boto3.client("athena", region_name="eu-west-1")
    #details = client.get_query_execution(QueryExecutionId=exex_id)["QueryExecution"]
    #details.should.equal(athena_result)
