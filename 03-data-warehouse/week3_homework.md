
## Week 3 Data Warehouse Homework Queries

Question 1: What is count of records for the 2022 Green Taxi Data?
-   65,623,481
-   840,402
-   1,936,423
-   253,647
```sql
SELECT count(*) as trips
FROM dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitioned;
```
> Output: __840,402__
---
Question 2: Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.  What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?
-   0 MB for the External Table and 6.41MB for the Materialized Table
-   18.82 MB for the External Table and 47.60 MB for the Materialized Table
-   0 MB for the External Table and 0MB for the Materialized Table
-   2.14 MB for the External Table and 0MB for the Materialized Table

```sql
-- create materialized table

CREATE OR REPLACE TABLE dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata 

AS SELECT * FROM dtc-de-zoomcamp-410523.ny_taxi.external_green_tripdata;

SELECT COUNT(DISTINCT PULocationID) as distinctPickup FROM dtc-de-zoomcamp-410523.ny_taxi.external_green_tripdata;
```
> 0 B processed
```sql
SELECT COUNT(DISTINCT PULocationID) as distinctPickup FROM dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata;
```
>6.41 MB processed
---
Question 3: How many records have a fare_amount of 0?
-   12,488
-   128,219
-   112
-   1,622
```sql
SELECT COUNT(*) FROM dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitioned
WHERE fare_amount = 0;
```
> 1622
---
Question 4: What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)
-   Cluster on lpep_pickup_datetime Partition by PUlocationID
-   Partition by lpep_pickup_datetime Cluster on PUlocationID
-   Partition by lpep_pickup_datetime and Partition by PUlocationID
-   Cluster on by lpep_pickup_datetime and Cluster on PUlocationID
- Creating a partition and cluster table
```sql
CREATE OR REPLACE TABLE `dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitoned_clustered`

PARTITION BY DATE(lpep_pickup_datetime)

CLUSTER BY PULocationID AS

SELECT * FROM `dtc-de-zoomcamp-410523.ny_taxi.external_green_tripdata`;
```
> Partition by lpep_pickup_datetime and cluster on PULocationID
---
Question 5: Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)  
Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?  
Choose the answer which most closely matches.
-   22.82 MB for non-partitioned table and 647.87 MB for the partitioned table
-   12.82 MB for non-partitioned table and 1.12 MB for the partitioned table
-   5.63 MB for non-partitioned table and 0 MB for the partitioned table
-   10.31 MB for non-partitioned table and 10.31 MB for the partitioned table
```sql
SELECT DISTINCT(PULocationID) as distinctPickup 
FROM dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
```
> 12.82 MB processed
```sql
SELECT DISTINCT(PULocationID) as distinctPickup 
FROM dtc-de-zoomcamp-410523.ny_taxi.green_tripdata_partitoned_clustered
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
```
> 1.12 MB processed
---
Question 6: Where is the data stored in the External Table you created?
-   Big Query
-   GCP Bucket
-   Big Table
-   Container Registry
> GCP Bucket
---
Question 7: It is best practice in Big Query to always cluster your data:
-   True
-   False
> FALSE
---
(Bonus: Not worth points) Question 8: No Points: Write a  `SELECT count(*)`  query FROM the materialized table you created. How many bytes does it estimate will be read? Why? 
```sql
SELECT count(*) as query FROM dtc-de-zoomcamp-410523.ny_taxi.materialized_green_tripdata;
```
> 0 bytes because query cached.