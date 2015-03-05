#!/bin/bash

DIR=$( pwd )
CLASSES=$( find -name '*.class' -print )
TEST_INPUT=$DIR/input.txt

for file in $CLASSES; do
    filedir=$( dirname $file )
    filename=$( basename $file | sed s/.class// )
    echo Changing to $filedir
    cd $filedir
    echo Executing $filename
    java $filename < $TEST_INPUT > $DIR/out.txt
    echo Changing back to $DIR
    cd $DIR
done
