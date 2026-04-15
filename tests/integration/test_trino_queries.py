def test_trino_client_imports():
    from incentive_fraud.serving.trino_client import get_connection
    assert get_connection is not None
