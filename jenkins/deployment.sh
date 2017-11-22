#!/bin/bash

profile=$1
workSpace=$HOME/dc-workspace
projectName=DcClouds
gitUrl=git@gitlab.digitalchina.com:shipy/DcCloud.git
projectPath=$workSpace/$projectName
deployPath=/root/.jenkins/jobs/DcCloud_online1/workspace/

function compile() {
	cd $projectPath
	
	if  [ ! -n "$profile" ] ;then
		mvn clean package
	else
		mvn clean package -P $profile
	fi
}

function cpWar() {
	if  [ ! -n "$profile" ] ;then
		warName=DcCloud_dev.war
	elif [[ "$profile"x = "Online"x ]]; then
		#statements
		warName=DcCloud_online.war
	else
		warName=DcCloud_dev.war
	fi

	cp ${projectPath}/target/$warName $deployPath

}

function getCode() {
	if [ ! -d "$workSpace" ]; then
		mkdir -p $workSpace
	fi


	if [ -d "$projectPath" ]; then
		cd $projectPath
		git pull
	else
		git clone $gitUrl $projectPath
	fi
}

getCode

compile

cpWar
