export PATH=/bin:/drives/c/Users/chunywan/DOCUME~1/MobaXterm/slash/bin:/drives/h/WINDOWS:/drives/c/Windows/system32
$id=$1
declare -a args
function connection {
    args=();
    args+=(-L0.0.0.0:102$id:xbjlabdpsvr$id:22);
    args+=(-R0.0.0.0:10074:xcdl190074:22);
    args+=(-R0.0.0.0:10152:xsjsda153:22);
    args+=(-R0.0.0.0:10142:xcosda142:22);
    args+=(-R0.0.0.0:10261:gitenterprise.xilinx.com:22);
    ssh "${args[@]}"   xbjlabdpsvr$id 'while sleep 1; do echo ======; date; hostname; done'
}

connection;
while sleep 15; do
        connection;
done
