#!/bin/bash

openstack vnf descriptor create --vnfd-file mongo.yaml mongo
openstack vnf descriptor create --vnfd-file upf1.yaml upf1
openstack vnf descriptor create --vnfd-file upf2.yaml upf2
openstack vnf descriptor create --vnfd-file upf3.yaml upf3

openstack vnf descriptor create --vnfd-file nrf.yaml nrf
openstack vnf descriptor create --vnfd-file amf.yaml amf
openstack vnf descriptor create --vnfd-file smf1.yaml smf1
openstack vnf descriptor create --vnfd-file smf2.yaml smf2
openstack vnf descriptor create --vnfd-file smf3.yaml smf3
openstack vnf descriptor create --vnfd-file udr.yaml udr
openstack vnf descriptor create --vnfd-file pcf.yaml pcf
openstack vnf descriptor create --vnfd-file udm.yaml udm
openstack vnf descriptor create --vnfd-file nssf.yaml nssf
openstack vnf descriptor create --vnfd-file ausf.yaml ausf
#openstack vnf descriptor create --vnfd-file basic_setup.yaml basic_setup

