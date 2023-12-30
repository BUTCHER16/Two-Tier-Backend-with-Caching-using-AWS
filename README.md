# Two-Tier-Backend-with-Caching-using-AWS
Implement a Two-Tier Backend with API Gateway, Fargate, Lambda, RDS, DynamoDB, and IAM. Enhance performance with integrated caching. Scalable, efficient, and cost-effective AWS architecture for optimized data retrieval.

Team Members:
  - Albert Ravidoss R
  - Karthi
  - Sriram

This project idea consists of building Create, Read, Update, and Delete APIs that integrate
with a scalable database, and optionally, a caching layer to improve performance. You’ll use
the API Gateway service to set up a resource and routes that map to your compute tier.
For computing, you can use many options, but I suggest using either AWS Lambda or AWS
Fargate. AWS Lambda is a very popular serverless computing service that integrates easily
with API Gateway. AWS Fargate uses AWS-managed infrastructure to host your computing,
but you won’t need to worry about maintaining it. Typically, folks use Docker containers
with Fargate to define their environments.

If you go with Lambda, you’ll need to create a Lambda Function and implement the
necessary logic for your CRUD apis. If you go with Fargate, you’ll need to set up a cluster
and similarly implement the logic.

For the database layer, you also have many options. I suggest going with either Amazon RDS
for a relational database or Amazon DynamoDB if you prefer NoSQL. If you go with RDS,
you’ll need to create a database (I suggest trying Aurora Serverless) and the necessary
tables. You may also need to configure your Database’s security groups to allow access
from your home machine. Going with DynamoDB is much more straightforward. You just
need to create a table and start adding your items. You’ll be able to view and interact with
your DynamoDB tables directly in the AWS console.

If you want to improve performance and get some experience with caching, you can go one
step further and add an ElastiCache Redis cluster. You can integrate it into your Lambda or
Fargate application during the reading flow by first checking if an item exists in the cache
before retrieving it from your RDS or DynamoDB table. Make sure to populate the record
into your cache if you don’t find it!

Project -> Procedure

Step-by-Step Guide for the Project:

1. Define API Gateway:
  Use AWS API Gateway to set up a new API, define resources, and create routes for CRUD operations (Create, Read, Update, Delete).
  Establish the necessary methods (GET, POST, PUT, DELETE) for each route.

2. Choose Compute Tier:
  Option 1: AWS Lambda
  Create Lambda functions for each CRUD operation.
  Implement logic within each function to handle data processing.
  Integrate Lambda functions with API Gateway.

  Option 2: AWS Fargate
  Set up an AWS Fargate cluster.
  Create Docker containers defining your computing environments.
  Implement CRUD logic within the containers.
  Configure Fargate to host your containers.

3. Select Database:
  Option 1: Amazon RDS (Relational Database Service)
  Choose a relational database engine (e.g., MySQL, PostgreSQL) or try Aurora Serverless.
  Create a database instance and define necessary tables for your data.
  Configure security groups to allow access from your development machine.

  Option 2: Amazon DynamoDB
  Create a DynamoDB table with the required attributes.

4. Implement CRUD Logic:
  Depending on your chosen compute tier (Lambda or Fargate), implement logic for Create, Read, Update, and Delete operations.

5. Optional: Integrate ElastiCache Redis Cluster:
  Set up an ElastiCache Redis cluster for caching.
  Modify your Read operation logic to check the cache first before querying RDS or DynamoDB.
  If data is not in the cache, retrieve it from the database and store it in the cache for subsequent requests.

6. Testing:
  Test each API endpoint to ensure proper functionality.
  Verify that caching improves performance during read operations.

7. Monitoring and Optimization:
  Implement logging and monitoring for your APIs using AWS services like CloudWatch.
  Optimize your architecture based on performance metrics.
  Consider adjusting cache expiration policies and size based on usage patterns.

8. Documentation:
  Document your architecture, including API specifications, database schema, and caching strategy.
  Provide clear instructions on how to deploy and scale the application.

9. Security Considerations:
  Implement security best practices, such as encrypting data in transit and at rest.
  Apply appropriate IAM roles and policies for your Lambda functions or Fargate containers.

10. Deployment:
  Deploy your APIs, compute tier (Lambda or Fargate), and database.
  Monitor for any deployment issues and troubleshoot if necessary.
