docker build -t churn_prediction/python:3.6 -f Dockerfile . 

docker run -it -p 12000:80 --rm --name=churn_app_train churn_prediction/python:3.6 

docker run -it --rm --name=churn_app_train \
-v /root/datascience/dana_churn_prediction/artifacts/model_joblib:/app/artifacts/model_joblib \
churn_prediction/python:3.6 python3 inference.py -d /app/train_dataset \
-m /app/artifacts/model_joblib \
-out /app/artifacts

# -- Line -- #
docker run -it --rm --name=churn_app -v /root/datascience/dana_churn_prediction/train_dataset:/app/train_dataset -v /root/datascience/dana_churn_prediction/artifacts:/app/artifacts churn_prediction/python:3.6 python3 inference.py -d /app/train_dataset -m /app/artifacts/model_joblib -out /app/artifacts

date +%Y-%m-%d

10 * * * * docker run -it --rm --name=churn_app 
-v /root/datascience/dana_churn_prediction/dataset:/app/churn_project/dataset \
-v /root/datascience/dana_churn_prediction/src/artifacts:/app/churn_project/src/artifacts \
churn_prediction/python:3.6 >> /var/log/cron.log 2>&1

docker run -it --rm --name=churn_app \
-v /Users/richardadiguna/Documents/dana_churn_prediction/train_dataset:/app/train_dataset \
-v /Users/richardadiguna/Documents/dana_churn_prediction/artifacts:/app/artifacts \
churn_prediction/python:3.6 bash

python3 train.py -d /Users/richardadiguna/Documents/dana_churn_prediction/dataset -out /Users/richardadiguna/Documents/dana_churn_prediction/artifacts -v 1

python3 inference.py -d ~/Documents/dana_churn_prediction/train_dataset/ -m ~/Documents/dana_churn_prediction/artifacts/model_joblib

python3 inference.py -d /app/train_dataset \
-m /app/artifacts/model_joblib \
-out /app/artifacts

docker run -it --rm --name=churn_app -v /root/datascience/dana_churn_prediction/train_dataset:/app/train_dataset -v /root/datascience/dana_churn_prediction/artifacts:/app/artifacts churn_prediction/python:3.6 python3 inference.py -d /app/train_dataset -m /app/artifacts/model_joblib -out /app/artifacts >> /var/log/cron.log 2>&1

# Bind volume between host and container for model joblib (inference.py)

python3 train.py -d /Users/richardadiguna/Documents/dana_churn_prediction/dataset -out /Users/richardadiguna/Documents/dana_churn_prediction/artifacts -c /Users/richardadiguna/Documents/dana_churn_prediction/churn_logistic_regression/config/train_config.json -v 1