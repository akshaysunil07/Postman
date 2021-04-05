## Build Docker Image
run the files in docker using:
docker build -t ImageName .


## Table, Schemas
Schema = 'test_schema'
Table = 'products'

## Points Achieved
- Support for updating existing products in the table based on `sku` as the primary key
- All details ingested into a single table
- Create aggregated table for name and number of products

## Points not Achieved
- Support for regular non-blocking parallel ingestion of the given file into a table.

## What can be improved upon
- non-blocking parallel ingestion can be introduced.
