Pydapter is in development. 

You will find most stream functionality in RedisAdapter.py


To run a test environment, you can use the docker-compose which will start redis, redis insight and a jupyter science notebook.
Modify docker-compose-yml to name your network and conainers accordingly

A mirror of the images has been pushed to adregistry, it is advised you use those images.
However, if you do not have access, simply change the image to use the cloud variant
You will need to change the port mapping as well to something that is not currently used.

 redis:
    image: "redis:latest"                                <-------------- Use if local
    #image: "adregistry.fnal.gov/redislabs/redis:latest" <-------------- Use if on bidaqt
    container_name: bobby_redis
    ports:
      - "6380:6379"                                      <-------------- Change this to 63XX:6379            
    networks:
      - bobby_pydapter                                   <-------------- Change this with your name

Do this for all services and networks




To start everything, navigate to this repos root directory when the docker-compose.yml lives run:
   
   docker compose up -d

Jupyter will print a unique token / url which you will need. You can view the logs to obtain it.
It looks like this:   http://127.0.0.1:8888/lab?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

   docker compose logs

Jupyter will also mount the root directory to the jupter working directory so files will persist 




From your local machine you can then port forward via ssh or putty the ports will be the same as in your compose file

ssh -L 6380:bidaqt:6380 -L 5541:bidaqt:5541 -L 8889:bidaqt:8889 bidaqt

