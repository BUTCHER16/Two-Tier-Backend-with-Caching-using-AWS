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
