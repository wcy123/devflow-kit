```
debug()
{
    sudo dmesg -n8
    sudo bash -c "echo 0xfffffff > /sys/module/drm/parameters/debug"
    #cat /sys/bus/pci/devices/0000:08:00.0/*
    #cat /sys/bus/pci/devices/0000:08:00.1/*
}

```