from typing import Any
from unittest.mock import MagicMock, patch
import boto3
import yaml
from io import StringIO


def get_accounts() -> dict:
    s3 = boto3.client("s3")
    s3_response_object = s3.get_object(Bucket="bucketName", Key="fileName")

    return yaml.safe_load(s3_response_object["Body"].read())


def get_accounts_2() -> dict:
    s3 = boto3.client("s3")
    s3_response_object = s3.get_object(Bucket="bucketName", Key="fileName")
    s3_response_object2 = s3.get_object(Bucket="bucketName", Key="fileName")

    d1 = yaml.safe_load(s3_response_object["Body"].read())
    d2 = yaml.safe_load(s3_response_object2["Body"].read())
    return (d1, d2)


@patch("boto3.client")
def test_foo__mock_reading_of_s3_file(boto_client_mock):
    mock_s3_client = MagicMock()
    body = """
    accounts:
      - name: 'test account 1'
        number: '1231231231'
      - name: 'test account 2'
        number: '4564564545'
      - name: 'test account 3'
        number: '7898797897'
    """
    mock_response = {"Body": StringIO(body)}
    mock_s3_client.get_object = MagicMock(return_value=mock_response)
    boto_client_mock.return_value = mock_s3_client

    result = get_accounts()

    assert result == {
        "accounts": [
            {"name": "test account 1", "number": "1231231231"},
            {"name": "test account 2", "number": "4564564545"},
            {"name": "test account 3", "number": "7898797897"},
        ]
    }
    mock_s3_client.get_object.assert_called_once()


@patch("boto3.client")
def test_foo2__mock_reading_of_s3_file(boto_client_mock):
    mock_s3_client = MagicMock()
    body1 = """
    accounts:
      - name: 'test account 1'
        number: '1231231231'
      - name: 'test account 2'
        number: '4564564545'
      - name: 'test account 3'
        number: '7898797897'
    """
    body2 = """
    accounts:
      - name: 'test account 4'
        number: '1231231231'
      - name: 'test account 5'
        number: '4564564545'
      - name: 'test account 6'
        number: '7898797897'
    """
    mock_response1 = {"Body": StringIO(body1)}
    mock_response2 = {"Body": StringIO(body2)}
    mock_s3_client.get_object = MagicMock(side_effect=[mock_response1, mock_response2])
    boto_client_mock.return_value = mock_s3_client

    result1, result2 = get_accounts_2()

    assert result1 == {
        "accounts": [
            {"name": "test account 1", "number": "1231231231"},
            {"name": "test account 2", "number": "4564564545"},
            {"name": "test account 3", "number": "7898797897"},
        ]
    }
    assert result2 == {
        "accounts": [
            {"name": "test account 4", "number": "1231231231"},
            {"name": "test account 5", "number": "4564564545"},
            {"name": "test account 6", "number": "7898797897"},
        ]
    }
