# AWS Account Setup & Budget Configuration
## For ML Infrastructure Learning Labs

---

## Step 1: Verify AWS Account Access

**Check your AWS account:**
- [ ] I have an AWS account
- [ ] I can log into AWS Console
- [ ] I have programmatic access (Access Key ID & Secret)

**If you need to create an account:**
1. Go to https://aws.amazon.com
2. Click "Create an AWS Account"
3. Follow the setup process
4. Add payment method (required, but we'll set strict budgets)

---

## Step 2: Set Up Budget Alerts (CRITICAL!)

**⚠️ DO THIS FIRST to avoid unexpected costs!**

### Create Budget Alert:

1. Go to AWS Console → Billing → Budgets
2. Click "Create budget"
3. Choose "Monthly cost budget"
4. Set these values:
   - **Budget name:** ML-Learning-Monthly-Budget
   - **Budgeted amount:** $50 (or your preferred limit)
   - **Budget period:** Monthly
   
5. Set alerts:
   - **Alert 1:** 50% of budgeted amount ($25)
   - **Alert 2:** 80% of budgeted amount ($40)
   - **Alert 3:** 100% of budgeted amount ($50)
   
6. Add your email for notifications

**Confirmation:**
- [ ] Budget created
- [ ] Email alerts configured
- [ ] Received test email

---

## Step 3: Enable Free Tier Usage Tracking

1. Go to Billing Dashboard
2. Enable "AWS Free Tier usage alerts"
3. Add your email

**What's in Free Tier (useful for learning):**
- 750 hours of EC2 t2.micro/t3.micro per month
- 5 GB of S3 storage
- 1 million Lambda requests
- 20 GB of CloudWatch logs
- Some SageMaker Studio lab time

---

## Step 4: Configure AWS CLI

### Install AWS CLI (if not already installed):

```bash
# Check if installed
aws --version

# If not, install (macOS)
brew install awscli
```

### Configure credentials:

```bash
aws configure
```

**Enter:**
- AWS Access Key ID: [your key]
- AWS Secret Access Key: [your secret]
- Default region: us-east-1 (or your preferred region)
- Default output format: json

**Test it:**
```bash
aws sts get-caller-identity
```

**Confirmation:**
- [ ] AWS CLI installed
- [ ] Credentials configured
- [ ] Test command worked

---

## Step 5: Set Up Cost-Saving Practices

### Create a cost_control.sh script:

**This script helps clean up resources after labs**

```bash
#!/bin/bash
# Save this as: ml-infrastructure-learning/scripts/cleanup.sh

echo "🧹 Cleaning up AWS resources to save costs..."

# List running EC2 instances
echo "\n📊 Running EC2 instances:"
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name]' \
  --output table

# List SageMaker endpoints
echo "\n📊 Active SageMaker endpoints:"
aws sagemaker list-endpoints \
  --query 'Endpoints[*].[EndpointName,EndpointStatus]' \
  --output table

# List SageMaker notebook instances
echo "\n📊 SageMaker notebook instances:"
aws sagemaker list-notebook-instances \
  --query 'NotebookInstances[*].[NotebookInstanceName,NotebookInstanceStatus]' \
  --output table

echo "\n⚠️  Remember to delete resources after each lab!"
echo "Use: aws sagemaker delete-endpoint --endpoint-name <name>"
```

**Create the script:**
- [ ] Script created
- [ ] Made executable: `chmod +x cleanup.sh`
- [ ] Tested running it

---

## Step 6: Choose Your AWS Region

**For ML labs, choose regions with good SageMaker support:**

**Recommended regions:**
- `us-east-1` (N. Virginia) - Most services, lowest cost
- `us-west-2` (Oregon) - Good ML support
- `eu-west-1` (Ireland) - If you're in Europe

**My chosen region:** _________________

**Update in AWS CLI config:**
```bash
aws configure set region us-east-1
```

---

## Step 7: Create IAM User for Labs (Optional but Recommended)

**For security, create a separate user for learning:**

1. Go to IAM → Users → Add User
2. Name: `ml-learning-user`
3. Access type: Programmatic + Console
4. Attach policies:
   - AmazonSageMakerFullAccess
   - AmazonS3FullAccess
   - CloudWatchLogsFullAccess
   - IAMReadOnlyAccess
5. Save credentials securely

**Confirmation:**
- [ ] IAM user created
- [ ] Credentials saved
- [ ] Can log in with new user

---

## Step 8: Cost Estimation for Labs

**Expected costs for 30-day plan:**

| Week | Labs | Est. Cost |
|------|------|-----------|
| Week 1 | SageMaker endpoints (2-3 hours) | $5-10 |
| Week 2 | Multiple serving tools testing | $10-15 |
| Week 3 | GPU instances (limited hours) | $15-20 |
| Week 4 | Production setup (then delete) | $5-10 |
| **Total** | | **~$35-55** |

**Cost-saving tips:**
- ✅ Always delete endpoints after labs
- ✅ Use smallest instance types for testing
- ✅ Stop notebook instances when not using
- ✅ Use Spot instances where possible
- ✅ Set up CloudWatch billing alarms
- ✅ Run cleanup script daily

---

## Step 9: GitHub Setup for Your Labs

### Create repo for your lab work:

```bash
cd ~/
mkdir ml-infrastructure-labs
cd ml-infrastructure-labs
git init
```

### Create .gitignore:

```
# AWS credentials
*.pem
*.key
credentials
config

# Python
__pycache__/
*.pyc
venv/
.env

# OS
.DS_Store
```

### Initial commit:

```bash
git add .
git commit -m "Initial commit - ML infrastructure learning labs"
git remote add origin https://github.com/wenichern/ml-infrastructure-labs.git
git push -u origin main
```

**Confirmation:**
- [ ] Local repo created
- [ ] GitHub repo created
- [ ] Connected and pushed

---

## Step 10: Install Required Tools

### Python libraries for labs:

```bash
# Create virtual environment
python3 -m venv ~/ml-learning-env
source ~/ml-learning-env/bin/activate

# Install core libraries
pip install boto3 sagemaker pandas numpy scikit-learn jupyter

# Install for testing/monitoring
pip install requests matplotlib seaborn

# Save requirements
pip freeze > requirements.txt
```

**Confirmation:**
- [ ] Virtual environment created
- [ ] Libraries installed
- [ ] requirements.txt saved

---

## Pre-Lab Checklist ✅

Before starting Day 3 labs, verify:

- [ ] ✅ AWS account active
- [ ] ✅ Budget alerts configured ($50 monthly)
- [ ] ✅ AWS CLI installed and configured
- [ ] ✅ Chosen region set
- [ ] ✅ Cleanup script ready
- [ ] ✅ GitHub repo created
- [ ] ✅ Python environment ready
- [ ] ✅ Understand cost implications
- [ ] ✅ Know how to delete resources

---

## Quick Reference Commands

**Check current costs:**
```bash
aws ce get-cost-and-usage \
  --time-period Start=2026-02-01,End=2026-02-28 \
  --granularity MONTHLY \
  --metrics "UnblendedCost"
```

**List all running SageMaker endpoints:**
```bash
aws sagemaker list-endpoints --query 'Endpoints[?EndpointStatus==`InService`]'
```

**Delete endpoint:**
```bash
aws sagemaker delete-endpoint --endpoint-name <endpoint-name>
aws sagemaker delete-endpoint-config --endpoint-config-name <config-name>
aws sagemaker delete-model --model-name <model-name>
```

**Stop notebook instance:**
```bash
aws sagemaker stop-notebook-instance --notebook-instance-name <name>
```

---

## Emergency Stop - If Costs Get High

**If you exceed budget, immediately:**

1. **Delete all endpoints:**
```bash
# List all endpoints
aws sagemaker list-endpoints --output json | grep EndpointName

# Delete each one
for endpoint in $(aws sagemaker list-endpoints --query 'Endpoints[].EndpointName' --output text); do
    echo "Deleting $endpoint"
    aws sagemaker delete-endpoint --endpoint-name $endpoint
done
```

2. **Stop all EC2 instances:**
```bash
aws ec2 stop-instances --instance-ids $(aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId]' --filters "Name=instance-state-name,Values=running" --output text)
```

3. **Check billing dashboard daily**

---

## You're Ready! 🚀

With this setup complete, you can safely start hands-on labs tomorrow (Day 3).

**Next:** Day 3-5 - Deploy your first model to SageMaker!

