from requests.auth import HTTPBasicAuth, HTTPDigestAuth 
from pathlib import Path
import json
import requests

s = requests.Session()

def get_clusters():
  url_vcenter = 'https://vcsa-01.haas-451.pez.vmware.com/rest/com/vmware/cis/session'
  username_vcenter = 'administrator@vsphere.local'
  password_vcenter = 'rsKNMG4sw5R8mcvDpu!'

  url_get_clusters = 'https://vcsa-01.haas-451.pez.vmware.com/api/vcenter/namespace-management/clusters'

  resp_login = s.post(url_vcenter, auth=(username_vcenter,password_vcenter), verify=False)

  resp_clusters = s.get(url_get_clusters, verify=False)

  clusters_json = resp_clusters.json()

  cluster_ids = list()
  
  for cluster_json in clusters_json:
    cluster_ids.append(cluster_json['cluster'])

  return cluster_ids

#number_SC = len(cluster_ids)

#i = 0

#print("Here are existing supervisor clusters:")

#while i < number_SC:
#  i = i+1
#  print(str(i) + ": " + clusters_json[i-1]['cluster_name']) 

#sc_selected = input("Please input the number of the supervisor cluster:")

#while not str.isdigit(sc_selected):
#    sc_selected = input("This is not a number. Please input the number of the supervisor cluster:")

#while int(sc_selected) > i:
#    sc_selected = input("This number does not exist. Please input the number of the supervisor cluster:")


def create_namespace():
  print("Creating namespace: ")

  url_create_namespace = 'https://vcsa-01.haas-451.pez.vmware.com/api/vcenter/namespaces/instances'

  json_create_namespace = '/Users/pyang/Downloads/v7k8s-tc-templates-master/sc06/ns-create_api-payload.json'

  with open(json_create_namespace) as f:
    payload = json.load(f)
    resp_create_namespace = s.post(url_create_namespace, json=payload, verify=False)

#  url_get_namespace = 'https://vcsa-01.haas-451.pez.vmware.com/api/vcenter/namespaces/instances/ns06'

#  resp_get_namespace = s.get(url_get_namespace, verify=False)

  return (resp_create_namespace)