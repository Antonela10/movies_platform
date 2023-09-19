#!/bin/sh

RUN_DIR=$(dirname "$(realpath "$0")")

TASK="$1"
[ $# -gt 0 ] && shift

# Map task to scripts here
if [ -f "$RUN_DIR/scripts/$TASK" ]; then
  "$RUN_DIR/scripts/$TASK" "$@"
else
  echo "Task not found: $TASK" >&2
  exit 2
fi