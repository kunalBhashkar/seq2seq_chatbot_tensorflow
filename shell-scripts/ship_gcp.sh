#!/bin/bash

docker tag chat-bot:packaged gcr.io/fir-sandbox-326008/chat-bot:packaged
docker push gcr.io/fir-sandbox-326008/chat-bot:packaged
