# Deploying yacy on Google Cloud Platform with Kubernetes
> **Kubernetes** is an open-source system for automating deployment, scaling, and management of containerized applications.

Source: https://kubernetes.io/

Follow these 10 steps to get an instance of yacy running on Google Cloud platform using Kubernetes.

**Note**: The document uses predefined names for various properties like project ID and docker image name to avoid confusion. You may want to change them when needed.

### 1. Create Google Cloud Platform Account
Visit https://cloud.google.com/free/ and follow on-screen instructions to create an account and get the free trial.

### 2. Create a Project
Create a new project with desired name and ID.

![kub1](https://cloud.githubusercontent.com/assets/10860278/26034852/c7ff5cac-38e0-11e7-92fb-1fa711a4c05c.png)

### 3. Create a Container Engine for the Project
Go to https://console.cloud.google.com/kubernetes/list and wait for the container engine to get ready. You may need to select the project from the project section in the top-left corner.

### 4. Open the Google Cloud Shell
In the top-right panel, click the shell button.

![screenshot from 2017-05-14 20-11-27](https://cloud.githubusercontent.com/assets/10860278/26034895/9703f85a-38e1-11e7-8dc1-81e38a5205d0.png)

You'll be greeted by an online console.

![screenshot from 2017-05-14 20-19-07](https://cloud.githubusercontent.com/assets/10860278/26034960/a8147dbc-38e2-11e7-87a1-b9fef076ee6f.png)

### 5. Clone the yacy project
```sh
$ git clone https://github.com/fossasia/badgeyay.git
$ cd badgeyay/
```

### 6. Build the Docker Image and Push to DockerHub Container Registry
```sh
$ docker build -t badgeyay:latest .
$ docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
$ docker push badgeyay
```
This makes our cloud registry ready. Let us create a Kubernetes cluster where we can deploy this.

### 7. Creating a Container Cluster
`gcloud` provides easy to use interface for creating clusters. Let us take a look at the properties that we can configure while creating a cluster.

| Argument | Function | Allowable Values |
|-------------|------------|----------------------|
| `--num-nodes` | Number of nodes in the cluster. | A natural number |
| `--machine-type` | Type of each machine in the cluster. | <li> `f1-micro` <li> `g1-small` <li> `n1-standard-{1,2,4,8}` <li> `n1-highmem-{2,4,8}` <li> `n1-highcpu-{2,4,8}` |
| `--zone` | Zone where nodes would be located. | See [Compute Engine Docs](https://cloud.google.com/compute/docs/regions-zones/regions-zones) |

For this example, let us create a cluster with following command - 
```sh
$ gcloud container clusters create badgeyay-cluster --num-nodes 3 --machine-type n1-standard-1 --zone us-central1-c
```
This will take a few minutes to complete. After done, you can see a new cluster active on your console.

![screenshot from 2017-05-14 21-01-12](https://cloud.githubusercontent.com/assets/10860278/26035369/91ec2912-38e8-11e7-9827-8052896ed842.png)

### 8. Create a Deployment for the Container Registry
```sh
$ kubectl run badgeyay --image=badgeyay:latest --port=8100
deployment "badgeyay" created
```
You can see a list of deployments by running the following commands - 
```sh
$ kubectl get deployments
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
badgeyay    1         1         1            1           2m
```
### 9. Expose the Deployment
With the server now deployed internally on Google Cloud Platform, we need to expose it to the Internet. For this, we use the following command - 
```sh
$ kubectl expose deployment badgeyay --type=LoadBalancer
service "badgeyay" exposed
```
Now, the platform will assign an external IP to the application. This may take some time. Run the following command to see the assigned external IP - 
```sh
$ kubectl get services
NAME         CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
kubernetes   10.79.240.1   <none>          443/TCP        10m
badgeyay       10.79.248.1   104.154.24.48   80:30287/TCP   1m
```

### 10. Visit the Webpage
On a browser, visit the deployment using the external IP (http://104.154.24.48/ in this case).
