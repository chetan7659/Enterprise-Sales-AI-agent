CREATE OR REPLACE DATABASE SALES_AI;
CREATE OR REPLACE SCHEMA SALES_AI.CRM;

USE DATABASE SALES_AI;
USE SCHEMA CRM;

CREATE OR REPLACE TABLE customers (
    customer_id INTEGER,
    name STRING,
    industry STRING,
    region STRING
);

CREATE OR REPLACE TABLE leads (
    lead_id INTEGER,
    customer_id INTEGER,
    status STRING,
    score INTEGER
);

CREATE OR REPLACE TABLE opportunities (
    opp_id INTEGER,
    customer_id INTEGER,
    value NUMBER(12,2),
    stage STRING
);

CREATE OR REPLACE TABLE sales_activity (
    activity_id INTEGER,
    opp_id INTEGER,
    notes STRING,
    activity_date DATE
);
