import os
import sys
os.system(" sudo mkdir /root/jfrog ")
os.system(" sudo apt-get update -y ")
os.system(" sudo apt-get install default-jdk -y ")
os.system(" sudo apt-get install wget -y ")
os.system(' echo JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java" >> /etc/environment ')
os.system("sudo wget url: https://bintray.com/artifact/download/jfrog/artifactory-debs/pool/main/j/jfrog-artifactory-oss-deb/jfrog-artifactory-oss-6.10.1.deb -P /root/jfrog/ ")
os.system("sudo apt-get update -y")
os.system("sudo dpkg -i  /root/jfrog/jfrog-artifactory-oss-6.10.1.deb")
os.system("systemctl start artifactory")
