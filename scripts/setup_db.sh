#!/bin/bash
psql -h localhost -U postgres -c "CREATE USER shop WITH PASSWORD 'shop123';"
psql -h localhost -U postgres -c "GRANT ALL ON DATABASE shoplite TO shop;"
