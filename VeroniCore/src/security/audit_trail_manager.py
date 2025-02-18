# audit_trail_manager.py
# This script keeps a detailed log of all data transactions, changes, and accesses for auditing and compliance purposes.

import datetime
import json

class AuditTrailManager:
    def __init__(self, log_file='audit_log.json'):
        self.log_file = log_file
        self.logs = self.load_logs()

    def load_logs(self):
        try:
            with open(self.log_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_logs(self):
        with open(self.log_file, 'w') as file:
            json.dump(self.logs, file, indent=4)

    def log_transaction(self, transaction_type, details):
        log_entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'transaction_type': transaction_type,
            'details': details
        }
        self.logs.append(log_entry)
        self.save_logs()
        print(f"Transaction logged: {transaction_type} - {details}")

    def get_logs(self, transaction_type=None):
        if transaction_type:
            return [log for log in self.logs if log['transaction_type'] == transaction_type]
        return self.logs

    def generate_audit_report(self):
        return json.dumps(self.logs, indent=4)

if __name__ == "__main__":
    # Example usage of AuditTrailManager
    audit_manager = AuditTrailManager()

    # Example transactions to log
    audit_manager.log_transaction('Data Access', 'User X accessed sensitive data.')
    audit_manager.log_transaction('Data Modification', 'User Y modified user records.')

    # Retrieve and print all logs
    logs = audit_manager.get_logs()
    print("All Audit Logs:")
    print(audit_manager.generate_audit_report())
    