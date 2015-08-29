STAMP=`date "+%Y-%m-%d-%H%M%S"`
FNAME=flow_${STAMP}.tgz
echo $FNAME
cd ..
tar czf $FNAME flow
scp $FNAME root@192.168.7.2:
ssh root@192.168.7.2 "mkdir rel/$STAMP && tar x -C rel/$STAMP -f $FNAME && rm -rf rel/current && ln -s $STAMP/flow rel/current"
