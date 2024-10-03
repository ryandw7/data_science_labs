#!/bin/bash
COUNT=1
END=$1
while [$COUNT -le $END]
do
    echo "Count = $COUNT"
    ((COUNT++))
done
echo "Loop finished."