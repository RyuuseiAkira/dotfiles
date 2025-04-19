#!/bin/bash

visibility=$(busctl get-property --user sm.puri.OSK0 /sm/puri/OSK0 sm.puri.OSK0 Visible)
toggle=""
  
if [ "$visibility" = "b false" ]; then
	toggle="true"
else
	toggle="false"
fi
  
busctl call --user sm.puri.OSK0 /sm/puri/OSK0 sm.puri.OSK0 SetVisible b $toggle