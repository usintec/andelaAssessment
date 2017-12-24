import sys
import os
import docker 
from threading import Thread
from queue import Queue

class andela():
  
  def __init__(self, client, nodeImageName, mongodbImageName, networkName):
    self.client = client
    self.nodeImageName = nodeImageName
    self.mongodbImageName = mongodbImageName
    self.networkName = networkName
    self.network = ''
    self.usintecNodeImage = ''
    self.usintecMongodbImage = ''

  #create a network
  def createNetwork():
    network = self.client.networks.create(self.networkName, driver="bridge")
    return network

  #get network details
  def networkDetails(networkId):
    network = self.client.network.get(networkId)
    return network  

  #pull image
  def pullImage(self, imageName=''):
    #the image name should not be empty
    if(imageName != ''):
      image = client.images.pull(imageName)	
    return image
 
  #start container and attach it to the created network
  def startContainer(imageName='', networkName = ''):
    if(imageName != ''):
      for container in self.client.containers.list():
        #if(container.image['name'] == imageName):
          #print(container.image['name'] + ' is already existing. I will proceed to check if part of our created Network')
        #else:
          container = self.client.container.run(imageName, detach=True, network=networkName)
          return container

  def nodeConfigurationFile(nodeServerContainerId,mongodbServerIp,mongodbServerPort = 27017):
    cofigFile = open(".env","w")
    info = "PORT=3000\nDB_URL=mongodb://" + mongodbServerIp + ":" + mongodbServerPort +"/andela"
    configFile.write(info)
    configFile.close()
    os.system("docker cp .env " + nodeServerContainerId + "/app .")
    os.system("node server.js")

    if(nodeServerContainerId):
      self.client
  def run(self,data):
    try:
      os.system('systemctl start docker')
      thread = Thread(target = notification, args=(data,))
      thread.start()
      self.usintecMongodbImage = self.pullImage(self.mongodbImageName)
      progress = "." 
      nodeImage = False

      while(data != 'none'):

        #if self.usintecMongodbImage != '' and nodeImage == False:
          #self.usintecNodeImage = self.pullImage(self.nodeImageName)
          #nodeImage = True
    
        #if self.network == '' and self.usintecNodeImage != '':
          #self.createNetwork()

        print(data.get())

      print("thread finished")
    except Exception as ex:
      print(ex.message);


#client = docker.DockerClient(base_url='unix://var/run/docker.sock')
client = docker.from_env()
events = client.events(decode=True)
ThisModule = sys.modules[__name__]
nodeImageName = 'usintec/node'
mongodbImageName = 'usintec/mongodb'
networkName = 'andela_network'

  #events
def start(client, event):
  return event['Action']
def stop(client, event):
  return event['Action']
def pull(client, event):
  return event['Action']
def copy(client, event):
  return event['Action']
def create(client, event):
  #if only a network is created i.e not volume 
  if(event['Type'] == 'network'):
    return event

#this function is stated in a thread that monitors docker's event
def notification(data):
  try:
    for event in events:
      if(hasattr(ThisModule,event['Action'])):
        data.put(getattr(ThisModule,event['Action'])(client,event))
  except Exception as ex:
    print(ex.message);

if __name__ == "__main__":
  try:
    data = Queue()
    program = andela(client, nodeImageName, mongodbImageName, networkName)
    program.run(data)
  except Exception as ex:
    print(ex.message);
