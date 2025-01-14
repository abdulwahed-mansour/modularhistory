#!/bin/bash

wait-for-it.sh redis:6379 --
volume_dirs=( "db/backups" "db/init" "static" "media" "redirects" )
for dir_name in "${volume_dirs[@]}"; do
    dir_path="/modularhistory/_volumes/$dir_name"
    test -w "$dir_path" || {
        echo "Celery lacks permission to write in ${dir_path}."
        [[ "$ENVIRONMENT" = dev ]] && exit 1
    }
done
celery -A core worker --hostname=%h --loglevel=info -E
