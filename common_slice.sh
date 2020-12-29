#!/bin/bash

openstack vnf create --vnfd-name nrf nrf --vim-name chris_vim --description "nrf"
sleep 10
openstack vnf create --vnfd-name amf amf --vim-name chris_vim --description "amf"
sleep 10
#openstack vnf create --vnfd-name smf1 smf1 --vim-name chris_vim --description "smf"
#sleep 10
openstack vnf create --vnfd-name udr udr --vim-name chris_vim --description "udr"
sleep 10
openstack vnf create --vnfd-name pcf pcf --vim-name chris_vim --description "pcf"
sleep 10
openstack vnf create --vnfd-name udm udm --vim-name chris_vim --description "udm"
sleep 10
openstack vnf create --vnfd-name nssf nssf --vim-name chris_vim --description "nssf"
sleep 10
openstack vnf create --vnfd-name ausf ausf --vim-name chris_vim --description "ausf"