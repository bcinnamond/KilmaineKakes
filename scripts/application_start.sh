echo "Running container..."
docker login -u AWS -p $(aws ecr get-login-password --region eu-north-1) 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes
sudo docker run --name kilmainekakes -d -p 5000:5000 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes:latest
