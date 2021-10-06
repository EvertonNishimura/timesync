# timesync

Sync plc XM time with PR21 [ suppose IP is 192.168.1.1 ] with this snap.

1 - Transfer the snap to PR21:
 sudo scp timesync_0.1_amd64.snap boschrexroth@192.168.1.1:/home/boschrexroth/
 
2 - SSH into PR21:
ssh boschrexroth@192.168.1.1

3 - install snap
sudo snap install timesync_0.1_amd64.snap --devmode

4 - test to see if snap is ok
sudo snap run timesync

results should be: 
Estação 192.168.0.21 -> C-0-0050.0.0.7=ok
or
Estação 192.168.0.21 -> exception

Obs.:
Everything is hardcoded! To modify and snap your modification:
1 - clone this repo
2 - modify
3 - call snapcraft 
snapcraft  (if using a ubuntu machine)
snapcraft --use-lxd  (if using a vm)
