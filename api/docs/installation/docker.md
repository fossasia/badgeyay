# Docker				
		
 ### Prerequisites		
		
 Before you begin this, ensure the following is installed to your system:		
 - Docker, and		
 - A git repository to store your project and track changes.		
		
 ## Create Dockerfile		
		
 Create a file named "Dockerfile" with this content :		
		
 ````	
 FROM ubuntu:16.04		
		
 RUN apt-get update -y && \		
     apt-get install -y python-pip python-dev && \		
     pip install --upgrade pip		
		
 COPY . /app		
		
 WORKDIR /app		
		
 RUN pip install -r requirements.txt		
		
 EXPOSE 5000		
		
 ENTRYPOINT [ "python" ]		
		
 CMD [ "application.py" ]		
 ````		
		
 ## Build Docker image		
		
 ### Build with PATH :		
		
 Make sure you run this command from the same directory as the location of your Dockerfile		
 
 ``$ docker build .``		
		
 Now run this command to see the Docker images you have in your local repository.		
 
 ``docker images``		
		
 ## Debug your build		
		
 If something goes wrong with the build you can fire up a plain ubuntu image and try installing each package from the Dockerfile manually.		
		
 Run this :		
 
 ````		
 docker pull ubuntu:16.04		
 docker run -it -v [full file path to your app files]:/app ubuntu:16.04 /bin/bash		
 ````		
 ## Fire up your Docker container		
 Run this:		
 ``docker run -p 5000:5000 -v [file path to the project files on your computer]:/app fossasia/badgeyay``		
		
 ## Deploy on AWS Elastic Beanstalk				
		
 - Login to AWS and get to the Elastic Beanstalk service.		
 - Create a new environment and select “Docker” as the preconfigured platform.		
 - Upload a zip of your app files, which of course should include the Dockerfile. Create the zip from within the root directory of your app.		
		
 Once you have successfully uploaded your files on the right size instance, Elastic Beanstalk will deploy your app and make it available.		
		
 Cheers
