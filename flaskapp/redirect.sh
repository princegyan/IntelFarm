#!/bin/bash

while true;do

	python temp.py > reading
	echo "Read from stdin: ${REPLY}"
	reading > kofi
		echo "Redirection Done"
done
