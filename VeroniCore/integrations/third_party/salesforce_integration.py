from simple_salesforce import Salesforce, SalesforceLogin, SFType
import os

class SalesforceIntegration:
    def __init__(self, username, password, security_token, domain='login'):
        # Login to Salesforce
        self.sf = Salesforce(username=username, password=password, security_token=security_token, domain=domain)

    def query_data(self, soql_query):
        """
        Executes a SOQL query and returns the results.
        """
        try:
            result = self.sf.query(soql_query)
            return result['records']
        except Exception as e:
            print(f"Error querying data: {e}")
            return None

    def create_record(self, object_name, data):
        """
        Creates a new record in Salesforce.
        """
        try:
            obj = self.sf.__getattr__(object_name)
            result = obj.create(data)
            print(f"Record created in {object_name}: {result['id']}")
            return result
        except Exception as e:
            print(f"Error creating record: {e}")
            return None

    def update_record(self, object_name, record_id, data):
        """
        Updates an existing record in Salesforce.
        """
        try:
            obj = self.sf.__getattr__(object_name)
            result = obj.update(record_id, data)
            print(f"Record {record_id} updated in {object_name}.")
            return result
        except Exception as e:
            print(f"Error updating record: {e}")
            return None

    def delete_record(self, object_name, record_id):
        """
        Deletes a record from Salesforce.
        """
        try:
            obj = self.sf.__getattr__(object_name)
            result = obj.delete(record_id)
            print(f"Record {record_id} deleted from {object_name}.")
            return result
        except Exception as e:
            print(f"Error deleting record: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    username = "your_salesforce_username"
    password = "your_salesforce_password"
    security_token = "your_salesforce_security_token"
    salesforce = SalesforceIntegration(username, password, security_token)

    # Query data
    query = "SELECT Id, Name FROM Account LIMIT 10"
    accounts = salesforce.query_data(query)
    print("Queried Accounts:")
    for account in accounts:
        print(account)

    # Create a new Account record
    new_account = {"Name": "New Account Name"}
    created_record = salesforce.create_record("Account", new_account)

    # Update the created Account record
    update_data = {"Name": "Updated Account Name"}
    salesforce.update_record("Account", created_record['id'], update_data)

    # Delete the created Account record
    salesforce.delete_record("Account", created_record['id'])
