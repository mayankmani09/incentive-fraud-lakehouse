def test_bronze_job_module_imports():
    import jobs.spark.bronze_claims_job as job
    assert job is not None
