FROM python:3.6

ARG current_date_var

LABEL maintainer="richard.adiguna@dana.id"

RUN apt-get update && apt-get install -y vim telnet default-libmysqlclient-dev \
    less build-essential git curl openssh-client python3-dev supervisor libssl-dev libffi-dev && \
    apt-get clean && \
    mkdir -p /app/train_dataset /app/artifacts /app/artifacts/model_variable \
    /app/artifacts/model_joblib /app/artifacts/correlation_matrix \
    /app/artifacts/confusion_matrix /app/artifacts/data_composition \
    /app/artifacts/prediction_result

ENV current_date_env=$current_date_var

WORKDIR /app/churn_prediction

COPY . /app/churn_prediction

ENV PYTHON_PACKAGES="\
    scipy \
    numpy \
    pandas \
    scikit-learn \
    paramiko \
    bunch \
    mysqlclient \
    mysql-connector-python \
    sqlalchemy \
    joblib \
"
 
RUN pip3.6 install --upgrade pip \
&& pip3.6 install --no-cache-dir $PYTHON_PACKAGES

CMD python3 train.py -d /app/train_dataset \
    -out /app/artifacts \
    -c /app/churn_prediction/config/train_config.json \
    -v 1
