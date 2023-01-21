#!/usr/bin/env bash

# Stop on errors, print commands
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail
# set -x

for file in "$@"; do
   raco fmt -i $file # format the file using racket fmt
   sed -i '' -e 's/\[/\(/g' -e 's/\]/\)/g' $file # replace [ with ( and ] with )
done