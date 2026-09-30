<!-- ================================================================= -->
<!--                   BHOMESH RAZDAN // DEVOPS HUD                  -->
<!--      Enterprise Cloud Architect • DevSecOps • Platform Engineer  -->
<!-- ================================================================= -->

<div align="center">

<!-- Futuristic Cyber Dynamic Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,11,15,30&height=220&section=header&text=BHOMESH%20RAZDAN&fontSize=42&fontAlignY=38&animation=twinkling&fontColor=00F0FF&desc=%E2%88%9E%20DEVSECOPS%20%26%20CLOUD%20PLATFORM%20ENGINEER%20%E2%88%9E&descFontSize=16&descAlignY=62&descAlign=50" width="100%"/>

<!-- Real-Time Typing SVG -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=1000&color=00F0FF&center=true&vCenter=true&width=750&lines=System+Online%3A+Deploying+Zero-Trust+Cloud+Infrastructure;Architecting+Enterprise+Multi-VPC+Bank-Grade+Networks;Operating+8%2B+Production+EKS+Clusters+%7C+ArgoCD+GitOps;Automated+Container+Supply+Chain+%7C+Wiz+%E2%86%92+CIAS+%E2%86%92+Nexus;Immutable+Infrastructure+as+Code+with+Terraform+%26+Terragrunt" alt="Typing SVG" />
</a>

<p align="center">
  <a href="mailto:bhomeshrazdan.work@gmail.com"><img src="https://img.shields.io/badge/TRANSMISSION-bhomeshrazdan.work%40gmail.com-00F0FF?style=for-the-badge&logo=gmail&logoColor=black&labelColor=0a0a0a" alt="Email"/></a>
  <a href="https://www.linkedin.com/in/bhomesh"><img src="https://img.shields.io/badge/NETWORK-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a0a0a" alt="LinkedIn"/></a>
  <a href="https://github.com/bhomesh"><img src="https://img.shields.io/badge/CODE_BASE-GitHub-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0a0a0a" alt="GitHub"/></a>
  <a href="https://medium.com/@BhomeshRazdan"><img src="https://img.shields.io/badge/DISPATCH-Medium-black?style=for-the-badge&logo=medium&logoColor=white&labelColor=0a0a0a" alt="Medium"/></a>
  <img src="https://img.shields.io/badge/LOCATION-India%20%5BIST%5D-FF9933?style=for-the-badge&logo=google-maps&logoColor=white&labelColor=0a0a0a" alt="Location"/>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=bhomesh&color=00F0FF&style=flat-square&label=PROFILE+VIEWS" alt="Profile Views"/>
</p>

</div>

---

### 🛰️ MISSION CONTROL // TELEMETRY & SYSTEM METRICS

```yaml
root@antigravity-core:~# cat /etc/bhomesh/system.telemetry
========================================================================================
ENGINEER_NAME       : Bhomesh Razdan
SYSTEM_CLASS        : DevOps Engineer // Cloud Platform & DevSecOps Specialist
EXPERIENCE_VECTOR   : 3+ Years Operating Production AWS Infrastructure & Kubernetes Fleets
PRODUCTION_FLEET    : 8+ Multi-Tenant AWS EKS Clusters (IRSA, Helm, Istio mTLS, ArgoCD)
SECURITY_PERIMETER  : Zero-Trust Multi-VPC (Transit Gateway, Squid Egress, PrivateLink)
SUPPLY_CHAIN_GATES  : Wiz Platform, CIAS Dynamic Scanning, Sonatype Nexus Intake/Trusted
RELIABILITY_METRIC  : Mean Time to Resolution (MTTR) Cut from 3.8h -> 2.3h (-39.5%)
CORE_DISCIPLINES    : Infrastructure as Code (IaC), GitOps, Cloud Networking & Observability
========================================================================================
```

---

### 📊 OPERATIONAL IMPACT AT A GLANCE

<div align="center">
<table>
  <tr>
    <td align="center" width="25%">
      <h3>📉 -39.5%</h3>
      <p><b>MTTR Reduction</b><br/>Dropped downtime from 3.8h to 2.3h with Datadog APM & automated runbooks</p>
    </td>
    <td align="center" width="25%">
      <h3>☸️ 8+ Clusters</h3>
      <p><b>Production EKS Fleet</b><br/>Zero-downtime upgrades from v1.23 to v1.32 with Istio mTLS</p>
    </td>
    <td align="center" width="25%">
      <h3>⚡ 0.5d ➔ Min</h3>
      <p><b>Supply Chain Cycle</b><br/>Automated Wiz & CIAS image promotion, eliminating Jira wait queues</p>
    </td>
    <td align="center" width="25%">
      <h3>💰 60% Savings</h3>
      <p><b>Compute Optimization</b><br/>Autoscaling Spot runners with pre-baked Packer AMIs (-40% boot time)</p>
    </td>
  </tr>
</table>
</div>

---

### ⚡ ARCHITECTURAL BLUEPRINTS

#### 1. Enterprise Multi-VPC Zero-Trust Network Topology
*Securing core banking workloads with zero direct internet access, strict boundary inspection, and PrivateLink ingress.*

```mermaid
flowchart TD
    subgraph WAN ["Internet Boundary"]
        Internet["External Ingress Traffic"]
    end

    subgraph IDMZ ["IDMZ VPC (Boundary Security)"]
        WAF["AWS WAF & ALB"]
        Squid["Squid Egress Proxies (Whitelisted FQDNs)"]
    end

    subgraph TGW ["AWS Transit Gateway Hub"]
        TGW_Core["TGW Route Tables & Security Segmentation"]
    end

    subgraph BankVPC ["Bank VPC (Isolated Workload Tier)"]
        EKS_Fleet["Production EKS Clusters (Private Subnets)"]
        RDS_Cluster["Multi-AZ RDS Databases"]
        PrivateLink["AWS PrivateLink Endpoints"]
    end

    subgraph SidecarVPC ["Sidecar VPC (Shared Services)"]
        Shared_Services["Observability & Centralized Tooling"]
    end

    Internet --> WAF
    WAF --> TGW_Core
    TGW_Core <--> BankVPC
    TGW_Core <--> SidecarVPC
    BankVPC --> Squid
    Squid --> Internet
```

#### 2. Autonomous Container Image Hydration Supply Chain
*Automated vulnerability gating from developer commit to trusted production deployment.*

```mermaid
flowchart LR
    DevCommit["Developer Commit"] --> GHAction["GitHub Actions Build"]
    GHAction --> Wiz["Wiz Security Scan"]
    Wiz --> NexusIntake["Nexus Intake Registry"]
    NexusIntake --> EC2Bot["Scheduled EC2 Automation Engine"]
    EC2Bot --> CIAS["CIAS Deep Vulnerability Scan"]
    CIAS -->|Passed| NexusTrusted["Nexus Trusted Registry"]
    NexusTrusted --> ArgoCD["ArgoCD GitOps Engine"]
    ArgoCD --> ProdEKS["Production AWS EKS Clusters"]
```

---

### 🛡️ TECHNICAL ARSENAL & TOOLING MATRIX

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>☁️ Cloud Platforms & Core Services</h4>
      <p>
        <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-web-services&logoColor=FF9900" alt="AWS"/>
        <img src="https://img.shields.io/badge/Amazon_EKS-FF9900?style=flat-square&logo=amazon-eks&logoColor=white" alt="EKS"/>
        <img src="https://img.shields.io/badge/AWS_IAM_%26_IRSA-DD344C?style=flat-square&logo=amazon-iam&logoColor=white" alt="IAM"/>
        <img src="https://img.shields.io/badge/VPC_%26_PrivateLink-8C4FFF?style=flat-square&logo=amazon-vpc&logoColor=white" alt="VPC"/>
        <img src="https://img.shields.io/badge/AWS_Transit_Gateway-232F3E?style=flat-square&logo=amazon-aws&logoColor=white" alt="TGW"/>
        <img src="https://img.shields.io/badge/Route_53-232F3E?style=flat-square&logo=amazon-route53&logoColor=white" alt="Route53"/>
        <img src="https://img.shields.io/badge/ALB_%2F_NLB-232F3E?style=flat-square&logo=load-balancer&logoColor=white" alt="ALB"/>
        <img src="https://img.shields.io/badge/AWS_Secrets_Manager-FF9900?style=flat-square&logo=aws-secrets-manager&logoColor=white" alt="SecretsManager"/>
        <img src="https://img.shields.io/badge/Amazon_RDS-527FFF?style=flat-square&logo=amazon-rds&logoColor=white" alt="RDS"/>
        <img src="https://img.shields.io/badge/Lambda_%26_EventBridge-FF9900?style=flat-square&logo=aws-lambda&logoColor=white" alt="Lambda"/>
        <img src="https://img.shields.io/badge/Microsoft_Azure-0089D6?style=flat-square&logo=microsoft-azure&logoColor=white" alt="Azure"/>
        <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=google-cloud&logoColor=white" alt="GCP"/>
      </p>
      <h4>⚙️ Infrastructure as Code & Automation</h4>
      <p>
        <img src="https://img.shields.io/badge/Terraform_Modules-844FBA?style=flat-square&logo=terraform&logoColor=white" alt="Terraform"/>
        <img src="https://img.shields.io/badge/Terragrunt_DRY_IaC-2B3A42?style=flat-square&logo=hashicorp&logoColor=white" alt="Terragrunt"/>
        <img src="https://img.shields.io/badge/AWS_CloudFormation-FF4F8B?style=flat-square&logo=amazon-aws&logoColor=white" alt="CloudFormation"/>
        <img src="https://img.shields.io/badge/Ansible_Automation-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible"/>
        <img src="https://img.shields.io/badge/Helm_v3_Packaging-0F1689?style=flat-square&logo=helm&logoColor=white" alt="Helm"/>
      </p>
      <h4>☸️ Containers, Orchestration & Mesh</h4>
      <p>
        <img src="https://img.shields.io/badge/Kubernetes_v1.23_%E2%86%92_v1.32-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes"/>
        <img src="https://img.shields.io/badge/Docker_Multi--Stage-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
        <img src="https://img.shields.io/badge/Istio_Service_Mesh_mTLS-466BB0?style=flat-square&logo=istio&logoColor=white" alt="Istio"/>
        <img src="https://img.shields.io/badge/Amazon_ECR-232F3E?style=flat-square&logo=amazon-aws&logoColor=white" alt="ECR"/>
        <img src="https://img.shields.io/badge/Nexus_Intake_%26_Trusted-111111?style=flat-square&logo=sonatype&logoColor=white" alt="Nexus"/>
      </p>
    </td>
    <td width="50%" valign="top">
      <h4>🔒 DevSecOps, Vulnerability Scanning & Compliance</h4>
      <p>
        <img src="https://img.shields.io/badge/Wiz_Security_Platform-00D2B4?style=flat-square&logo=wiz&logoColor=black" alt="Wiz"/>
        <img src="https://img.shields.io/badge/CIAS_Vulnerability_Scan-E53935?style=flat-square&logo=security&logoColor=white" alt="CIAS"/>
        <img src="https://img.shields.io/badge/Snyk_Security-4C1E95?style=flat-square&logo=snyk&logoColor=white" alt="Snyk"/>
        <img src="https://img.shields.io/badge/SonarCloud_Code_Quality-F3705A?style=flat-square&logo=sonarcloud&logoColor=white" alt="SonarCloud"/>
        <img src="https://img.shields.io/badge/Trivy_Container_Scan-00A6D6?style=flat-square&logo=aqua&logoColor=white" alt="Trivy"/>
        <img src="https://img.shields.io/badge/OWASP_Dependency_Check-000000?style=flat-square&logo=owasp&logoColor=white" alt="OWASP"/>
        <img src="https://img.shields.io/badge/Squid_Proxy_Egress_Filtering-006400?style=flat-square&logo=linux&logoColor=white" alt="Squid"/>
      </p>
      <h4>🚀 CI/CD Pipelines & GitOps Release Engineering</h4>
      <p>
        <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white" alt="GitHub Actions"/>
        <img src="https://img.shields.io/badge/ArgoCD_GitOps-EF6B48?style=flat-square&logo=argo&logoColor=white" alt="ArgoCD"/>
        <img src="https://img.shields.io/badge/Jenkins_Modernization-D24939?style=flat-square&logo=jenkins&logoColor=white" alt="Jenkins"/>
        <img src="https://img.shields.io/badge/Git_Version_Control-F05032?style=flat-square&logo=git&logoColor=white" alt="Git"/>
      </p>
      <h4>📊 Telemetry, APM & Observability</h4>
      <p>
        <img src="https://img.shields.io/badge/Datadog_APM_%26_Logs-632CA6?style=flat-square&logo=datadog&logoColor=white" alt="Datadog"/>
        <img src="https://img.shields.io/badge/Prometheus_Metrics-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus"/>
        <img src="https://img.shields.io/badge/Grafana_Dashboards-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana"/>
        <img src="https://img.shields.io/badge/AWS_CloudWatch-FF4F8B?style=flat-square&logo=amazon-cloudwatch&logoColor=white" alt="CloudWatch"/>
      </p>
      <h4>💻 Scripting, Systems & Glue Code</h4>
      <p>
        <img src="https://img.shields.io/badge/Python_Automation-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
        <img src="https://img.shields.io/badge/Bash_%2F_Shell-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white" alt="Bash"/>
        <img src="https://img.shields.io/badge/Linux_Administration-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux"/>
        <img src="https://img.shields.io/badge/YAML_Manifests-CB171E?style=flat-square&logo=yaml&logoColor=white" alt="YAML"/>
      </p>
    </td>
  </tr>
</table>

---

### 🛠️ HOW I OPERATE // ENGINEERING PRINCIPLES

- **Zero-Trust by Default:** Enforce least-privilege IAM, VPC endpoint policies, and mTLS between microservices. Never assume trust inside internal networks.
- **Git as the Single Source of Truth:** Deploy everything through declarative GitOps (ArgoCD) and modular Terraform with remote state locking to eliminate drift.
- **Automated Security Gates:** Shift security left by baking Wiz, Snyk, CIAS, and Trivy directly into the deployment stream rather than treating audits as an afterthought.
- **Data-Driven Observability:** Monitor service level indicators with Prometheus and Datadog APM; prioritize actionable alerts backed by verified incident runbooks.

---

### ⏱️ CAREER TIMELINE & COMBAT EXPERIENCE

```
  2023                        2024                        2025                       2026+
  ┌───────────────────────────┬───────────────────────────┬───────────────────────────►
  │ PDEIndia (DevOps Intern)  │ Clouddrove (Assoc. DevOps)│ Zynsera Tech (DevOps Eng) │
  │ • Bash & GH Actions       │ • EKS v1.23 -> v1.32      │ • Bank Multi-VPC Security │
  │ • Terraform AWS Basics    │ • Zero-Downtime Jenkins   │ • Wiz/Nexus/CIAS Pipeline │
  │ • Jenkins Operations      │ • EventBridge & Lambda    │ • 8+ EKS Clusters | Istio │
```

#### 🔹 **Zynsera Technology** | *DevOps Engineer* `[May 2025 – Present]`
> **Domain:** Enterprise Banking Cloud Security, Zero-Trust Multi-VPC & Supply Chain Governance
- 🛡️ **Enterprise Multi-VPC Isolation:** Implemented complete network segmentation (**Bank VPC**, **IDMZ VPC**, **Sidecar VPC**) interconnected via **AWS Transit Gateway** and **AWS PrivateLink**, with **Squid proxy egress filtering**, eliminating flat network access and internet exposure for internal banking microservices.
- 🔄 **Autonomous Image Hydration Supply Chain:** Built an automated EC2-based container promotion engine (`Wiz Security Scan` ➔ `Nexus Intake` ➔ `CIAS Dynamic Testing` ➔ `Trusted Golden Registry`), replacing a manual per-image Jira approval process and eliminating up to **0.5 days of deployment wait time**.
- ☸️ **EKS Fleet Management:** Operate **8+ production AWS EKS clusters** (IRSA, Helm, ArgoCD GitOps, Istio Service Mesh) with Datadog APM and Prometheus/Grafana monitors, driving down **MTTR from 3.8h to 2.3h**.
- 📦 **Standardized IaC Framework:** Authored reusable **Terraform** modules (VPC, Security Groups, IAM, EKS, RDS, Route 53, ALB, ACM) with **remote state locking** across AWS/Azure; integrated Snyk/SonarCloud/Trivy gates into CI/CD to eliminate configuration drift.

#### 🔹 **Clouddrove** | *Associate DevOps Engineer* `[May 2024 – April 2025]`
> **Domain:** Kubernetes Fleet Modernization, Zero-Downtime Migration & Operational Automation
- 🚀 **Zero-Downtime EKS Upgrades:** Upgraded production Kubernetes clusters across **v1.23 ➔ v1.32** throughout Dev, Staging, and Production tiers with automated pre-flight add-on compatibility verification.
- 🏗️ **CI/CD Platform Modernization:** Led a major zero-downtime **Jenkins platform overhaul**, migrating legacy shell automation into containerized declarative **GitHub Actions** workflows and Helm releases secured by **Istio mTLS**.
- ⚡ **Cloud Operations Automation:** Engineered automated operational scripts using **Python** & **Bash** integrated with **AWS EventBridge**, **Lambda**, **SSM Run Command**, and **Parameter Store**.

#### 🔹 **PDEIndia** | *DevOps Intern* `[May 2023 – April 2024]`
> **Domain:** CI/CD Foundations, Infrastructure Provisioning & Build Orchestration
- 🛠️ Scripted custom Bash routines for GitHub Actions workflows, managed Jenkins build nodes, and provisioned immutable AWS cloud resources (EC2, S3, IAM, Security Groups) via Terraform under senior architectural supervision.

---

### 🧩 FLAGSHIP ENGINEERING PROJECTS

<table>
  <tr>
    <td width="50%">
      <h3>⚡ Self-Hosted GitHub Runner Automation</h3>
      <p><b>Stack:</b> Terraform • AWS Auto Scaling • HashiCorp Packer • Spot Instances</p>
      <ul>
        <li>Architected dynamically autoscaling GitHub Actions self-hosted runners on AWS EC2.</li>
        <li>Pre-baked CI runtimes into immutable AMIs with Packer, cutting job boot time by <b>40%</b>.</li>
        <li>Implemented intelligent Spot Instance bidding, slashing compute expenditures by <b>60%</b>.</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🛡️ Automated RDS Disaster Recovery & Validation</h3>
      <p><b>Stack:</b> AWS Lambda • Python / Boto3 • EventBridge • Slack API</p>
      <ul>
        <li>Automated snapshot verification, isolated test instance restore, and integrity checks.</li>
        <li>Cut manual operational disaster recovery drills from <b>2 hours down to 10 minutes</b>.</li>
        <li>Containerized serverless Lambdas with automated reporting pipelines into Slack and Jira.</li>
      </ul>
    </td>
  </tr>
</table>

---

### ✍️ TECHNICAL WRITING & DISPATCHES

<div align="center">
  <a href="https://medium.com/@BhomeshRazdan/supercharge-your-zsh-setup-with-these-essential-plugins-2d3dfbb7cec0">
    <img src="https://img.shields.io/badge/Medium%20Article-Supercharge%20Your%20Zsh%20Setup%20With%20Essential%20Plugins-00F0FF?style=for-the-badge&logo=medium&logoColor=black&labelColor=0d1117" alt="Medium Article"/>
  </a>
</div>

---

### 📈 TELEMETRY METRICS & CODE FREQUENCY

<div align="center">
  <table border="0">
    <tr>
      <td>
        <img height="180em" src="https://github-readme-stats.vercel.app/api?username=Bhomesh&show_icons=true&theme=radical&bg_color=05050e&title_color=00F0FF&icon_color=00F0FF&text_color=B3B8C5&border_color=1F2937&hide_border=false" alt="Bhomesh's GitHub Stats"/>
      </td>
      <td>
        <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Bhomesh&layout=compact&theme=radical&bg_color=05050e&title_color=00F0FF&text_color=B3B8C5&border_color=1F2937&hide_border=false" alt="Top Languages"/>
      </td>
    </tr>
  </table>

  <!-- Streak Stats Card -->
  <p align="center">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=Bhomesh&theme=radical&background=05050e&ring=00F0FF&fire=00F0FF&currStreakNum=00F0FF&sideNums=B3B8C5&sideLabels=B3B8C5&border=1F2937" alt="GitHub Streak" width="85%"/>
  </p>
</div>

---

### 📡 INITIATE SECURE TRANSMISSION

<div align="center">

```
 ╔═══════════════════════════════════════════════════════════════════════════════════╗
 ║           READY TO COLLABORATE ON HIGH-SCALE CLOUD & INFRASTRUCTURE?              ║
 ║      Open for Senior DevOps, Cloud Infrastructure & DevSecOps Opportunities       ║
 ╚═══════════════════════════════════════════════════════════════════════════════════╝
```

<p align="center">
  <a href="mailto:bhomeshrazdan.work@gmail.com">
    <img src="https://img.shields.io/badge/ENCRYPTED_MAIL-bhomeshrazdan.work%40gmail.com-00F0FF?style=for-the-badge&logo=gmail&logoColor=black&labelColor=0d1117" alt="Email"/>
  </a>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/bhomesh">
    <img src="https://img.shields.io/badge/CONNECT-LinkedIn%20Profile-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d1117" alt="LinkedIn"/>
  </a>
  &nbsp;&nbsp;
  <a href="https://medium.com/@BhomeshRazdan">
    <img src="https://img.shields.io/badge/FOLLOW-Medium%20Dispatches-black?style=for-the-badge&logo=medium&logoColor=white&labelColor=0d1117" alt="Medium"/>
  </a>
</p>

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,15,11,2,0&height=100&section=footer" width="100%"/>

</div>
