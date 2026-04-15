def test_feature_engineering_module_imports():
    from incentive_fraud.silver.feature_engineering import build_features
    assert build_features is not None
