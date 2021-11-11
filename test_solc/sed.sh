echo {$#}123
if [[ $# -ne 1 ]];then
    echo "usage $0 filename";
    exit 0;
fi
sed -i 's/^/"var simpleContract = eth.contract(/"';
echo "done"
