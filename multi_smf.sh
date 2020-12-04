#!/bin/bash

openstack vnf create --vnfd-name mongo mongo --vim-name chris_vim --description "mongodb"
openstack vnf create --vnfd-name upf1 upf1 --vim-name chris_vim --description "upf1"
sleep 5
openstack vnf create --vnfd-name upf2 upf2 --vim-name chris_vim --description "upf2"
sleep 5
openstack vnf create --vnfd-name upf3 upf3 --vim-name chris_vim --description "upf3"


sleep 10

openstack vnf create --vnfd-name nrf nrf --vim-name chris_vim --description "nrf"
sleep 10
openstack vnf create --vnfd-name amf amf --vim-name chris_vim --description "amf"
sleep 10
openstack vnf create --vnfd-name smf1 smf1 --vim-name chris_vim --description "smf"
sleep 10
openstack vnf create --vnfd-name smf2 smf2 --vim-name chris_vim --description "smf2"
sleep 10
openstack vnf create --vnfd-name smf3 smf3 --vim-name chris_vim --description "smf3"
sleep 10
openstack vnf create --vnfd-name udr udr --vim-name chris_vim --description "udr"
sleep 10
openstack vnf create --vnfd-name pcf pcf --vim-name chris_vim --description "pcf"
sleep 10
openstack vnf create --vnfd-name udm udm --vim-name chris_vim --description "udm"
sleep 10
openstack vnf create --vnfd-name nssf nssf --vim-name chris_vim --description "nssf"
sleep 10
openstack vnf create --vnfd-name ausf ausf --vim-name chris_vim --description "ausf"

