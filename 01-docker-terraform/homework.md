## Module 1 Homework

## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits* 

- `--delete`
- `--rc`
- `--rmc`
- `--rm`

### Answer 1. 
- `--rm`


## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- 0.42.0
- 1.0.0
- 23.0.1
- 58.1.0

### Answer 2.
- 0.42.0


## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767
- 15612
- 15859
- 89009

### Answer 3.
select count(*) from green_taxi_data where lpep_pickup_datetime::date = '2019-09-18'
and lpep_dropoff_datetime::date =  '2019-09-18';
- 15612


## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21

### Answer 4.
SELECT LPEP_PICKUP_DATETIME :: date
FROM GREEN_TAXI_DATA
WHERE TRIP_DISTANCE = (SELECT MAX(TRIP_DISTANCE) FROM GREEN_TAXI_DATA);
- 2019-09-26


## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- "Brooklyn" "Manhattan" "Queens"
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens" 
- "Brooklyn" "Queens" "Staten Island"

### Answer 5.
select "Borough",sum(fare_amount) as total_amount From green_taxi_data join taxi_zone on "PULocationID" = "LocationID" 
where lpep_pickup_datetime::date = '2019-09-18'
and "Borough" !='Unknown'
group by "Borough" 
having sum(fare_amount) > 50000;

- "Brooklyn","Manhattan","Queens"


## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza

### Answer 6.
with pickup_cte as (
select distinct "PULocationID",lpep_pickup_datetime::date as pickup_date,
	lpep_dropoff_datetime::date as dropoff_date,"Zone","DOLocationID",tip_amount from taxi_zone 
	join green_taxi_data on "PULocationID" = "LocationID" 
	where lower("Zone") = 'astoria' and to_char(lpep_pickup_datetime::date,'MM-YYYY') = '09-2019'
	) 
select "Zone" from taxi_zone where "LocationID" =
	(select "DOLocationID" from pickup_cte where tip_amount = 
			(select max(tip_amount) from pickup_cte)
		);

- JFK Airport

## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.

# Answer 7.
$ terraform apply
var.project
  dtc-de-2024

  Enter a value: dtc-de-2024


Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "us-east1"
      + max_time_travel_hours      = (known after apply)
      + project                    = "dtc-de-2024"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US-EAST1"
      + name                        = "dtc_data_lake_dtc-de-2024"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }
          + condition {
              + age                   = 30
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_bigquery_dataset.dataset: Creation complete after 1s [id=projects/dtc-de-2024/datasets/trips_data_all]
google_storage_bucket.data-lake-bucket: Creation complete after 1s [id=dtc_data_lake_dtc-de-2024]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.