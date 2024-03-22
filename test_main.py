import pytest

# Import the functions to be tested
from src.main import createNode, updateNode, deleteNode, getNode, lambda_handler

# Define test cases
@pytest.mark.parametrize("http_method, path_parameters, body_data, expected_result", [
    ('POST', None, {'node_data': 'data'}, {'statusCode': 201})
])

def test_lambda_handler(http_method, path_parameters, body_data, expected_result):
    # Create event dictionary for the lambda_handler
    event = {
        'httpMethod': http_method,
        'pathParameters': path_parameters,
        'body': body_data
    }
    # Call lambda_handler with the event
    result = lambda_handler(event)
    # Assert the result
    assert result == expected_result

# Run the tests
if __name__ == "__main__":
    pytest.main()
