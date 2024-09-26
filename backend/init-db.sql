-- Connect to the 'navina_db' database
\c navina_db

-- Create extensions if they don't exist
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- You can add other initialization steps here, such as:
-- - Creating schemas
-- - Setting up roles
-- - Creating initial tables (if not handled by your ORM)

-- For example:
-- CREATE SCHEMA IF NOT EXISTS my_schema;

-- CREATE TABLE IF NOT EXISTS my_table (
--     id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
--     name TEXT NOT NULL,
--     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
-- );

-- Remember to add any other setup steps your application needs