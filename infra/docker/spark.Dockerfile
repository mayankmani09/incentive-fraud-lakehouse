FROM bitnami/spark:3.5
USER root
COPY requirements.txt /tmp/requirements.txt
RUN install_packages python3-pip && pip install --no-cache-dir -r /tmp/requirements.txt || true
WORKDIR /opt/project
COPY . /opt/project
ENV PYTHONPATH=/opt/project/src
