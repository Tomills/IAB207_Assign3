from sqlalchemy import select
from . import db
from .models import Bid

# Reflect census table via engine: census
bid_table = Table('bids', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([bid_table])


# Execute the statement on connection and fetch 10 records: result
results = connection.execute(stmt).fetchmany(size=10)

# Execute the statement and print the results
print(results)