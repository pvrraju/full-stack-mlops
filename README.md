# full-stack-mlops

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/pvrraju/full-stack-mlops
```
**SETUP AND DEPLOYMENT GUIDE**  
*(Copy, paste & conquer!)*

---

**STEP 1: Summon Your Conda Environment**  
1. **Open** your local repository (the gateway to greatness).  
2. **Create** a fresh conda env (think of it as a clean lab coat):  
   ```bash
   conda create -n mlops python=3.11 -y
   ```  
3. **Activate** your pristine new environment:  
   ```bash
   conda activate mlops
   ```

---

**STEP 2: Install the Brain Food**  
1. **Install** all required Python goodies:  
   ```bash
   pip install -r requirements.txt
   ```  
2. **Launch** the app (cue the drumroll):  
   ```bash
   python app.py
   ```  
3. **Open** your browser and go to `http://localhost:5000` (or whichever port your app uses). ✨

---

## MLflow: Your Experiment Butler  
- **Documentation**: https://mlflow.org/docs/latest/index.html  
- **Quick Start**:  
  ```bash
  mlflow ui
  ```

---

## DagsHub Tracking (Secret-Agent Edition)  
1. **Set** environment variables (shhh, top secret):  
   ```bash
    MLFLOW_TRACKING_URI= PASTE_YOUR_OWN_ONE
    MLFLOW_TRACKING_USERNAME= PASTE_YOUR_OWN_ONE
    MLFLOW_TRACKING_PASSWORD= PASTE_YOUR_OWN_ONE

   ```  
2. **Run** your tracking script undercover:  
   ```bash
   python script.py
   ```

---

# AWS CI/CD Deployment with GitHub Actions

1. **Log in** to the AWS Console.  
2. **Create** an IAM user for deployment with these policies:  
   - `AmazonEC2ContainerRegistryFullAccess`  
   - `AmazonEC2FullAccess`  
3. **Create** an ECR repository and note its URI:  
   ```
   566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj
   ```  
4. **Launch** an EC2 instance (Ubuntu flavor recommended).  
5. **Install** Docker on your EC2:  
   ```bash
   # Optional housekeeping
   sudo apt-get update -y
   sudo apt-get upgrade -y

   # Docker installation
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```  
6. **Configure** your EC2 as a self-hosted GitHub Actions runner:  
   - In GitHub: **Settings → Actions → Runners → New self-hosted runner**  
   - Follow the on-screen commands one by one.  
7. **Add** these secrets under your repo’s Settings → Secrets:  
   ```
   AWS_ACCESS_KEY_ID= PASTE_YOUR_OWN_ONE
   AWS_SECRET_ACCESS_KEY= PASTE_YOUR_OWN_ONE
   AWS_REGION= PASTE_YOUR_OWN_ONE
   AWS_ECR_LOGIN_URI=PASTE_YOUR_OWN_ONE.dkr.ecr.us-east-9.amazonaws.com/mlop
   ECR_REPOSITORY_NAME=PASTE_YOUR_OWN_ONE
   ```

---

## Why MLflow Wins  
- **Production-grade**: Built for the real world.  
- **Experiment tracking**: Never lose an experiment in the couch cushions.  
- **Model logging & tagging**: Like labeling your Tupperware—no mystery leftovers here.  

---

*Ready, set, deploy! 🚀*