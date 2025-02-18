import boto3
from botocore.exceptions import NoCredentialsError

class StorageIntegration:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key, region_name='us-west-1'):
        self.bucket_name = bucket_name
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name
        )

    def upload_file(self, file_path, s3_file_name):
        """
        Uploads a file to the specified S3 bucket.
        """
        try:
            self.s3.upload_file(file_path, self.bucket_name, s3_file_name)
            print(f"Upload Successful: {s3_file_name}")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_file(self, s3_file_name, local_file_path):
        """
        Downloads a file from the specified S3 bucket to a local path.
        """
        try:
            self.s3.download_file(self.bucket_name, s3_file_name, local_file_path)
            print(f"Download Successful: {local_file_path}")
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def list_files(self):
        """
        Lists all files in the specified S3 bucket.
        """
        try:
            response = self.s3.list_objects_v2(Bucket=self.bucket_name)
            for obj in response.get('Contents', []):
                print(f"File: {obj['Key']}")
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def delete_file(self, s3_file_name):
        """
        Deletes a file from the specified S3 bucket.
        """
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=s3_file_name)
            print(f"Deleted File: {s3_file_name}")
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False

if __name__ == "__main__":
    # Example usage
    bucket_name = "your_bucket_name"
    aws_access_key = "your_aws_access_key"
    aws_secret_key = "your_aws_secret_key"
    storage = StorageIntegration(bucket_name, aws_access_key, aws_secret_key)

    # Upload a file
    storage.upload_file("local_file.txt", "uploaded_file.txt")

    # List files in the bucket
    storage.list_files()

    # Download a file
    storage.download_file("uploaded_file.txt", "downloaded_file.txt")

    # Delete a file
    storage.delete_file("uploaded_file.txt")
