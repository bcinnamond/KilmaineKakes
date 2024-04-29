echo "Logging in to Amazon ECR..."
docker login --username AWS --password $(aws ecr get-login-password --region eu-north-1) 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes
echo "Logged in to Amazon ECR successfully."

echo "Pulling image from Amazon ECR"
docker pull 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes:latest
echo "Pulled image from Amazon ECR successfully."
