#!/bin/bash

# Ensure we are in the knowledge folder context
echo "Starting file generation in $(pwd)..."

# --- 1. KUBERNETES ---
cd ../local-rag/knowledge/kubernetes
cat << 'EOF' > kube_text.txt
Kubernetes is an open-source container orchestration platform designed to automate deploying, scaling, and operating application containers. It eliminates many of the manual processes involved in deploying and scaling containerized applications by grouping containers into logical units for easy management. Kubernetes provides core capabilities like service discovery, load balancing, and automated rollouts or rollbacks. It is highly extensible and works seamlessly across public, private, and hybrid cloud infrastructures. As a standard for modern cloud-native architecture, Kubernetes ensures high availability and resilient infrastructure management.
EOF
# Convert text to PDF
enscript -p kube_text.ps kube_text.txt && ps2pdf kube_text.ps kubernetes/kubernetes_basics.pdf
enscript -p services_text.ps kube_text.txt && ps2pdf services_text.ps kubernetes/services.pdf
rm kube_text.txt kube_text.ps services_text.ps

# --- 2. RUNBOOKS ---
cd ../local-rag/knowledge/runbooks
cat << 'EOF' > runbooks/CrashLoopBackOff.md
# Runbooks Management
Runbooks are structured, step-by-step guides designed to help engineering teams diagnose, troubleshoot, and resolve system operational issues efficiently. They serve as a critical repository of institutional knowledge, ensuring that repeated infrastructure incidents can be handled consistently by any on-call engineer. Well-maintained runbooks significantly reduce Mean Time to Resolution (MTTR) by eliminating guesswork during high-pressure production outages. They bridge the gap between complex system design and daily operations by providing clear, actionable remediation tracks. Continuous updates and automation of runbooks are essential to keep pace with evolving cloud-native environments.
EOF
cp runbooks/CrashLoopBackOff.md runbooks/OOMKilled.md

# --- 3. INCIDENTS ---
cd ../local-rag/knowledge/incidents
cat << 'EOF' > incidents/INC001.md
# Incidents Management
Incidents represent unexpected disruptions to an organization's IT services or infrastructure quality that require immediate operational intervention. Managing incidents effectively involves structured logging, categorization, prioritization, and swift root-cause analysis to restore normal service operations. Maintaining a comprehensive history of past incidents helps teams identify systemic patterns and vulnerabilities within their deployment pipelines. Post-incident reviews utilize these records to drive architectural improvements and prevent future operational regressions. Ultimately, a disciplined approach to incident tracking directly fortifies a company's overall system reliability and service-level objectives.
EOF
cp incidents/INC001.md incidents/INC002.md

# --- 4. AWS ---
cd ../local-rag/knowledge/aws
mkdir -p aws
cat << 'EOF' > aws_text.txt
Amazon Web Services is a comprehensive and broadly adopted cloud platform offering over two hundred fully featured services from data centers globally. It provides on-demand computing power, database storage, content delivery, and other functionalities to help businesses scale and grow. AWS enables organizations to reduce capital expenditures by replacing upfront infrastructure investment with low variable costs. Security and compliance are core focus areas, providing deeply integrated tools to control, audit, and manage data identities. Millions of customers trust AWS to power a wide variety of workloads from web applications to complex machine learning pipelines.
EOF
# Convert text to PDF
enscript -p aws_text.ps aws_text.txt && ps2pdf aws_text.ps aws/IAM.pdf
enscript -p vpc_text.ps aws_text.txt && ps2pdf vpc_text.ps aws/VPC.pdf
rm aws_text.txt aws_text.ps vpc_text.ps

echo "All files and directories have been successfully created!"