#!/bin/bash

cd ..
cd main
make
cd ..
cd bin
./glomosim config.in
