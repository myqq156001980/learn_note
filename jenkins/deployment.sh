#!/bin/bash

profile=$1
workSpace=dc-workspace
projectName=DcClouds
gitUrl=
projectPath=HOME/$workSpace/$projectName
deployPath=

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
		warName=
	else
		warName=
	fi

	cp ${projectPath}/target/$warName $deployPath

}

function getCode() {
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
