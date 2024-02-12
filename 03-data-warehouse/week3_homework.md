## Week 3 Data Warehouse Homework Queries

-- Answer 1
SELECT count(*) as trips
FROM dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitioned;
-- 840,402

-- Answer 2
-- create materialized table 
CREATE OR REPLACE TABLE dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata 
AS SELECT * FROM dtc-de-zoomcamp-410523.ny_taxi.external_green_tripdata;

SELECT COUNT(DISTINCT PULocationID) as distinctPickup FROM dtc-de-zoomcamp-410523.ny_taxi.external_green_tripdata;
-- 0 B processed 
SELECT COUNT(DISTINCT PULocationID) as distinctPickup FROM dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata;
-- 6.41 MB processed 

-- Answer 3
SELECT COUNT(*) FROM dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitioned
WHERE fare_amount = 0;
-- 1622

-- Answer 4
-- Creating a partition and cluster table
CREATE OR REPLACE TABLE `dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitoned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM `dtc-de-zoomcamp-410523.ny_taxi.external_green_tripdata`;
-- Partition by lpep_pickup_datetime and cluster on PULocationID

-- Answer 5
SELECT DISTINCT(PULocationID) as distinctPickup FROM dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
-- 12.82 MB processed

SELECT DISTINCT(PULocationID) as distinctPickup FROM dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitoned_clustered
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
-- 1.12 MB processed

-- Answer 6
-- GCP Bucket 

-- Answer 7
-- FALSE

-- Answer 8
SELECT count(*) as query FROM dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata;
-- 0 bytes due to the query being cached