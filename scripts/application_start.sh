echo "Running container..."
docker 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes login --username AWS --password-stdin 
docker run --name kilmainekakes -d -p 5000:5000 471112624607.dkr.ecr.eu-north-1.amazonaws.com/kilmainekakes:latest
