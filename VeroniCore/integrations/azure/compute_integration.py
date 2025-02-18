import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class ComputeIntegration:
    def __init__(self, aws_access_key, aws_secret_key, region_name='us-west-1'):
        self.ec2 = boto3.client(
            'ec2',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name
        )

    def create_instance(self, image_id, instance_type, key_name, security_group):
        """
        Creates a new EC2 instance.
        """
        try:
            instances = self.ec2.run_instances(
                ImageId=image_id,
                InstanceType=instance_type,
                KeyName=key_name,
                SecurityGroups=[security_group],
                MinCount=1,
                MaxCount=1
            )
            instance_id = instances['Instances'][0]['InstanceId']
            print(f"Instance created with ID: {instance_id}")
            return instance_id
        except NoCredentialsError:
            print("Credentials not available")
            return None
        except ClientError as e:
            print(f"Failed to create instance: {e}")
            return None

    def stop_instance(self, instance_id):
        """
        Stops a running EC2 instance.
        """
        try:
            self.ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Instance stopped: {instance_id}")
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False
        except ClientError as e:
            print(f"Failed to stop instance: {e}")
            return False

    def start_instance(self, instance_id):
        """
        Starts a stopped EC2 instance.
        """
        try:
            self.ec2.start_instances(InstanceIds=[instance_id])
            print(f"Instance started: {instance_id}")
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False
        except ClientError as e:
            print(f"Failed to start instance: {e}")
            return False

    def terminate_instance(self, instance_id):
        """
        Terminates an EC2 instance.
        """
        try:
            self.ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"Instance terminated: {instance_id}")
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False
        except ClientError as e:
            print(f"Failed to terminate instance: {e}")
            return False

    def list_instances(self):
        """
        Lists all EC2 instances with their status.
        """
        try:
            instances = self.ec2.describe_instances()
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    state = instance['State']['Name']
                    print(f"Instance ID: {instance_id}, State: {state}")
            return True
        except NoCredentialsError:
            print("Credentials not available")
            return False
        except ClientError as e:
            print(f"Failed to list instances: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    aws_access_key = "your_aws_access_key"
    aws_secret_key = "your_aws_secret_key"
    compute = ComputeIntegration(aws_access_key, aws_secret_key)

    # Create a new EC2 instance
    instance_id = compute.create_instance(
        image_id="ami-0c55b159cbfafe1f0",  # Example Amazon Linux 2 AMI
        instance_type="t2.micro",
        key_name="your_key_pair_name",
        security_group="your_security_group"
    )

    # List all instances
    compute.list_instances()

    # Stop the instance
    compute.stop_instance(instance_id)

    # Start the instance
    compute.start_instance(instance_id)

    # Terminate the instance
    compute.terminate_instance(instance_id)
