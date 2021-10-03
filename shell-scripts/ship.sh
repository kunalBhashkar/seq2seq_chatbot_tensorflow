#!/bin/bash

docker tag hello-world:latest gcr.io/fir-sandbox-326008/hello-world:latest
docker push  gcr.io/fir-sandbox-326008/hello-world:latest
