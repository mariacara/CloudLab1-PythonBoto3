#Create an two EC2 instances within each of the AZ specified
import boto3

def create_instance():
    vmcount = 7
    for i in range(3):
        if i == 0:
            subnet = 'subnet-03f95d5380dec04a7' #ID for subnet 172.31.48.0/20; AZ: us-east-1e
        elif i == 1:
            subnet = 'subnet-0af9d66c85cd1abbe' #ID for subnet 172.31.64.0/20; AZ: us-east-1f
        else:
            subnet = 'subnet-003659e241688f15f' #ID for subnet 172.31.80.0/20; AZ: us-east-1b
        for x in range(2):
            ec2_clientami = boto3.client('ec2', region_name='us-east-1', )
            instances = ec2_clientami.run_instances(
                ImageId='ami-0a8b4cd432b1c3063', 
                SubnetId=subnet,
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro',
                KeyName='demo-key',
                SecurityGroupIds=['sg-094c7912f3ac033e6'],
                TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'Name','Value':'VM'+ str(vmcount)}]}]
            )

            vmcount= vmcount +1 #increases the name of VM each time new instance is launched

create_instance()
