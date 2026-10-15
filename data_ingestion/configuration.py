
## import os
from snowflake.snowpark import Session


class SnowflakeConnection:

    def __init__(self,account,user,password,role=None,warehouse=None,database=None,schema=None):

        # Define Snowflake connection parameters
        
        self.account = account
        self.user = user
        self.password = password
        self.role = role
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.session = None

        # Environment resolved after connection
        self.env = None

        # Build connection parameters
        self.connection_parameters = {
            "account": self.account,
            "user": self.user,
            "password": self.password,
        }

        # Add optional parameters
        if self.role:
            self.connection_parameters["role"] = self.role

        if self.warehouse:
            self.connection_parameters["warehouse"] = self.warehouse

        if self.database:
            self.connection_parameters["database"] = self.database

        if self.schema:
            self.connection_parameters["schema"] = self.schema

    def connect(self):
        try:
            # Establish Snowpark session
            self.session = Session.builder.configs(self.connection_parameters).create()

            print("Successfully connected to Snowflake!")

            return self.session

        except Exception as e:
            print(f"Failed to connect to Snowflake: {e}")
            raise

    def execute_query(self):
        query = "select * from snowflake_sample_data.information_schema.databases"
        return self.session.sql(query)

    def close(self):
        if self.session is not None:
            self.session.close()
            self.session = None
            print("session is closed.")

    def run(self):
        try:
            self.connect()
            self.execute_query().show()
        finally:
            self.close()




if __name__ == "__main__":

    snowflake_conn = SnowflakeConnection(
        account= " ",
        user= " ",
        password= " ",
        role= " ",
        warehouse= " ",
        database=" ",
        schema = " ",
    )

    snowflake_conn.run()
