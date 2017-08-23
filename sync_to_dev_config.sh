#!/bin/bash -x

# rt4 repo for temp testing
#rsync -arv rt4repo/ root@192.168.50.3:/mnt/qnap/yum/rt4repo/
#ssh root@192.168.50.3 'createrepo /mnt/qnap/yum/rt4repo/'

# Final repo location
rsync -arv rt4repo/7/x86_64/perl-*rpm root@192.168.50.3:/mnt/qnap/yum/thecloud/7/perl/
rsync -arv rt4repo/7/x86_64/rt4-*rpm root@192.168.50.3:/mnt/qnap/yum/thecloud/7/rt/
rsync -arv rt4repo/7/x86_64/google*font*rpm root@192.168.50.3:/mnt/qnap/yum/thecloud/7/fonts/
ssh root@192.168.50.3 'createrepo /mnt/qnap/yum/thecloud/7/'
