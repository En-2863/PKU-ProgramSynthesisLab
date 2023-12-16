#!/bin/bash
BASE_DIR=$(dirname $(realpath $0))

# For my local windows machine
# docker run --rm -it \
#    -v C:\\Users\\En.Avenue\\Desktop\\lab2-handout\\judge\\global:/mnt/global_space \
#    -v C:\\Users\\En.Avenue\\Desktop\\lab2-handout\\judge\\user:/mnt/user_space \
#    --cpus 4 --pids-limit 512 --memory 8g --network none --memory-swap -1 \
#    --hostname container --add-host="container:127.0.0.1" \
#    -e TOKEN=1:submission \
#    lab2_submitter_local

# For Linux
docker run --rm -it \
    -v $BASE_DIR/global:/mnt/global_space \
    -v $BASE_DIR/user:/mnt/user_space \
    --cpus 4 --pids-limit 512 --memory 8g --network none --memory-swap -1 \
    --hostname container --add-host="container:127.0.0.1" \
    -e TOKEN=1:submission \
    lab2_submitter_local