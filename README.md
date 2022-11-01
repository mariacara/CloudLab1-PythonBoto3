# CloudLab1-PythonBoto3

In this lab, the launchEC2.py script was used to create six EC2 vms, two in each of the three availability zones declared in the “subnet” variable.The EC2s are given a tag/name starting at VM7 and increase numerically as each new instance is deployed. A security group that was created earlier within the lab is assigned to each instance through the security group ID. The instanceinfo.py script was then deployed to retrieve information from each EC2 instance. To deploy the scripts on the cli the following commands were used: 
```
python3 launchEC2.py
```
```
python3 instanceinfo.py
```
