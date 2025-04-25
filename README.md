# full-stack-mlops 🚀 🤖 🧪

## Workflows (The Sacred MLOps Dance Steps)

1. Update config.yaml (Your project's DNA)
2. Update schema.yaml (Because chaos is not our friend)
3. Update params.yaml (Tune those magical numbers)
4. Update the entity (Shape your data destiny)
5. Update the configuration manager in src config (The puppet master)
6. Update the components (Where the real magic happens)
7. Update the pipeline (Connect the dots, like a pro)
8. Update the main.py (The conductor of our ML orchestra)
9. Update the app.py (Making it look pretty for the world)

# How to run? (Don't worry, it's easier than assembling IKEA furniture)
### STEPS:

Clone the repository (Bring the magic to your machine)

```bash
https://github.com/pvrraju/full-stack-mlops
```
**SETUP AND DEPLOYMENT GUIDE**  
*(Your ticket to ML greatness - just follow along!)*

---

**STEP 1: Summon Your Conda Environment** 🐍  
1. **Open** your local repository (your new home away from home).  
2. **Create** a fresh conda env (like making a cozy nest for your code):  
   ```bash
   conda create -n mlops python=3.11 -y
   ```  
3. **Activate** your shiny new environment (wake up, little conda!):  
   ```bash
   conda activate mlops
   ```

---

**STEP 2: Feed Your Project** 🍽️  
1. **Install** all the Python goodies (the breakfast of champions):  
   ```bash
   pip install -r requirements.txt
   ```  
2. **Launch** the app (drumroll, please! 🥁):  
   ```bash
   python app.py
   ```  
3. **Open** your browser and navigate to `http://localhost:5000` (where the magic happens ✨)

---

## MLflow: Your Experiment Butler 🎩  
- **Documentation**: https://mlflow.org/docs/latest/index.html  
- **Quick Start** (As easy as ordering takeout):  
  ```bash
  mlflow ui
  ```

---

## DagsHub Tracking (For the Secret Agent in You) 🕵️‍♂️  
1. **Set** environment variables (your secret handshake):  
   ```bash
    MLFLOW_TRACKING_URI= PASTE_YOUR_OWN_ONE
    MLFLOW_TRACKING_USERNAME= PASTE_YOUR_OWN_ONE
    MLFLOW_TRACKING_PASSWORD= PASTE_YOUR_OWN_ONE
   ```  
2. **Run** your tracking script (like a ninja in the night):  
   ```bash
   python script.py
   ```

---

# AWS CI/CD Deployment with GitHub Actions 🌩️

1. **Log in** to the AWS Console (your cloud command center).  
2. **Create** an IAM user (give them superpowers responsibly):  
   - `AmazonEC2ContainerRegistryFullAccess`  
   - `AmazonEC2FullAccess`  
3. **Create** an ECR repository (your Docker image palace):  
   ```
   566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj
   ```  
4. **Launch** an EC2 instance (Ubuntu flavor - because good taste matters).  
5. **Install** Docker (your container cuisine):  
   ```bash
   # Spring cleaning first
   sudo apt-get update -y
   sudo apt-get upgrade -y

   # Docker installation (easier than installing a kitchen sink)
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```  
6. **Configure** your EC2 as a self-hosted runner (teach it to be your personal assistant):  
   - In GitHub: **Settings → Actions → Runners → New self-hosted runner**  
   - Follow the commands (they're like a recipe, but for computers).  
7. **Add** these secrets (keep them safer than your Netflix password):  
   ```
   AWS_ACCESS_KEY_ID= PASTE_YOUR_OWN_ONE
   AWS_SECRET_ACCESS_KEY= PASTE_YOUR_OWN_ONE
   AWS_REGION= PASTE_YOUR_OWN_ONE
   AWS_ECR_LOGIN_URI=PASTE_YOUR_OWN_ONE.dkr.ecr.us-east-9.amazonaws.com/mlop
   ECR_REPOSITORY_NAME=PASTE_YOUR_OWN_ONE
   ```

---

## Why MLflow Wins (The Not-So-Secret Sauce) 🏆  
- **Production-grade**: Because hobby-grade just won't cut it.
- **Experiment tracking**: Like a GPS for your ML journey.
- **Model logging & tagging**: Marie Kondo would be proud.

---

*Ready to rock the ML world! Let's make some magic happen! 🚀*