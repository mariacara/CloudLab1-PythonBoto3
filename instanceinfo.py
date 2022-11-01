# Collect information of each EC2 instance.
import boto3
ec2 = boto3.resource('ec2')
ec2details = ec2.instances.all()
for instance in ec2details:
    for ec2int in instance.network_interfaces:
        print('Instance name is', instance.tags[0]['Value']) # returns the value (name) within the tags list
        print('Instance id is',instance.id)
        print('Private IPv4 is',instance.private_ip_address)
        print('Public IPv4 is',instance.public_ip_address)
        print('Subnet ID is',ec2int.subnet_id)
        print('Availability zone is',ec2int.subnet.availability_zone)
        print('#'*60)