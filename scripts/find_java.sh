#!/bin/bash

DIR=$( pwd )
CLASSES=$( find -name '*.class' -print )
# you can change these
TEST_INPUT=$DIR/input.txt
OUT_FILE=$DIR/"out.txt"

for file in $CLASSES; do
    filedir=$( dirname $file )
    filename=$( basename $file | sed s/.class// )
    echo Changing to $filedir
    cd $filedir
    echo Executing $filename
    java $filename < $TEST_INPUT > $OUT_FILE
    echo Changing back to $DIR
    cd $DIR
done
