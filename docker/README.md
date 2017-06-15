# Docker tomcat java
    FROM ubuntu:16.04
    WORKDIR /workspace
    ADD . /workspace
    ENV JAVA_HOME /workspace/jdk1.8.0_121
    ENV CATALINA_HOME /workspace/tomcat9 	
    ENV PATH $PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$CATALINA_HOME/bin
    RUN cp api.war tomcat9/webapps
    
    EXPOSE 8080
    ENTRYPOINT /workspace/tomcat9/bin/startup.sh && tail -F /workspace/tomcat9/logs/catalina.out
    
---

#Dokcer command

> stop all the running docker ps

    sudo docker stop $(sudo docker ps -a -q)

> rm all the bocker images 

    sudo docker rmi $(sudo docker images -q)

> rm all docker containers

    sudo docker rm $(sudo docker ps -a -q)  
