gcloud compute zones describe us-west1-b
gcloud compute disks create stagingdisk --image-project ubuntu-os-cloud
--image-family ubuntu-minimal-2004-lts --zone us-west1-b
gcloud compute disks create stagingdisk --image-project ubuntu-os-cloud --image-family ubuntu-minimal-2004-lts --zone us-west1-b
gcloud compute images create nested-vm-image --source-disk=stagingdisk --source-disk-zone=us-west1-b --licenses=https://www.googleapis.com/compute/v1/projects/vm-options/global/licenses/enable-vmx
gcloud compute instances create nested-vm-image1 --zone us-west1-b --min-cpu-platform "Intel Haswell" --machine-type n1-standard-4 --image nested-vm-image
ls
$ gcloud container clusters create kubia --num-nodes=1 --machine-type=e2-micro --region=us-west1
kubectl get nodes
vim kubia_rc.yaml
kubectl create -f kubia-rc.yaml
vim kubia_rc.yaml
ls
kubectl create -f kubia-rc.yaml
kubectl create -f kubia_rc.yaml
vim kubia_rc.yaml
kubectl create -f kubia_rc.yaml
kubectl get pods
kubectl run kubia --image=your-docker-image --port=8080
kubectl expose rc kubia --type=LoadBalancer --name kubia-http
kubectl get services
curl http://35.203.130.136:3000/api/score?studnt_id=11111
curl http://34.118.237.252:8080/api/score?studnt_id=11111
gcloud compute disks create --size=10GiB --zone=us-west1-a mongodb
gcloud compute disks create --size=2GiB --zone=us-west1-a mongodb
start minikube
gcloud auth logi
gcloud auth login
sudu su
minikube start
kubectl get pods
kubectl get pod kubia-rc-ghldb -o yaml
ls
kubectl get pods
vim kubia_rc.yaml 
kubectl get pods
kubectl describe nodes
sudo systemctl status kube-apiserver
kubectl config view
kubectl cluster-info
kubectl config use-context gke_gke-demo-426300_us-west1_kubia
kubectl proxy --port=8080 &
gcloud auth login
gcloud config set gke-demo-426300
kubectl proxy --port=8080 &
curl -k http://localhost:8080/
kubectl get pods
kubectl get pod kubia-r69m6 -o yaml
kubectl get pod kubia-r69m6 -o json
vim kubia-rc-with-labels.yaml
kubectl create -f kubia-rc-with-labels.yaml
vim kubia-rc-with-labels.yaml
kubectl create -f kubia-rc-with-labels.yaml
vim kubia-rc-with-labels.yaml
kubectl create -f kubia-rc-with-labels.yaml
kubectl get po --show-labels
kubectl get po -L env
kubectl get po -l env=python3.8
kubectl get po -l creation_method=manual
kubectl label node minikube type=new
start minibuke
sudo wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo cp minikube-linux-amd64 /usr/local/bin/minikube
sudo chmod 755 /usr/local/bin/minikube
minikube version
kubectl label node minikube type=new
start minkube
start minikube
kubectl annotate pod kubia-r69m6 myannotation="this pod is created to test"
kubectl describe pod kubia-rc
kubectl get ns
kubectl get po --namespace kube-system
kubectl delete po kubia-rc-with-labels
kubctl delete po -l env=python3.8
