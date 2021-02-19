docker build -t saranraju90/multi-client:latest -t saranraju90/multi-client:$SHA -f ./client/Dockerfile ./client
docker build -t saranraju90/multi-server:latest -t saranraju90/multi-server:$SHA -f ./server/Dockerfile ./server
docker build -t saranraju90/multi-worker:latest -t saranraju90/multi-worker:$SHA -f ./worker/Dockerfile ./worker

docker push saranraju90/multi-client:latest
docker push saranraju90/multi-worker:latest
docker push saranraju90/multi-server:latest

docker push saranraju90/multi-client:$SHA
docker push saranraju90/multi-worker:$SHA
docker push saranraju90/multi-server:$SHA

kubectl apply -f k8s

kubectl set image deployments/server-deployment server=saranraju90/multi-server:$SHA
kubectl set image deployments/client-deployment client=saranraju90/multi-client:$SHA
kubectl set image deployments/worker-deployment worker=saranraju90/multi-worker:$SHA