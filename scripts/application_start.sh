echo "Running container..."
$(aws ecr get-login --no-include-email --region eu-north-1) | docker login --username AWS --password-stdin 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes
sudo docker run --name kilmainekakes -d -p 5000:5000 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes:latest
