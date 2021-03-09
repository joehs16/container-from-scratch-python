# container-from-scratch-python
This is building a container from scratch

## Build the Container Yourself and Push to Docker Hub

### Build image
*(If you want to develop yourself)* 
docker build --tag=duke-nba-wiki:latest .

### List docker images
docker image ls

### Run my newly built container

docker run -it joechs/duke-nba-wiki:firsttry python app.py --userinfo "<joseph.hsieh@duke.edu> NBA Popularity Analysis"  --granularity 'monthly' --start '20150701' --end '20160401' --names "Lebron James,Kevin Durant"  

### Push to Docker Hub

*Note:  You will need to change for your Docker Hub Repo*
 docker push joechs/duke-nba-wiki:firsttry

