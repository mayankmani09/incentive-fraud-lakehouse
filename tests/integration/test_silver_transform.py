def test_silver_job_module_imports():
    import jobs.spark.silver_claims_job as job
    assert job is not None
