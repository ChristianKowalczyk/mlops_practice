python3 save_model.py

## Creating cluster
gcloud container clusters create tf-serving-cluster --num-nodes=2 --machine-type=e2-medium --zone us-central1-a

## Getting credential
gcloud container clusters get-credentials tf-serving-cluster --zone us-central1-a --project <YOUR_GCP_PROJECT_ID>

## Build docker image
docker login <br/>
docker build --platform linux/amd64 -t username/tf-serving-model:v1.0 . <br/>
docker push username/tf-serving-model:v1.0

## Deploy helm chart
helm install tf-serving-release ./tf-serving-chart

## test_model.py 
kubectl get services tf-serving-release-tf-serving-chart -o jsonpath='{.status.loadBalancer.ingress[0].ip}' to output the external IP <br/>




