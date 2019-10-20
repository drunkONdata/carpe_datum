#FROM python:3.8-buster
FROM google/cloud-sdk

ADD . /opt/carpe-datum

ENV PACKAGES="\
        apt-utils \
        apt-transport-https \
        dumb-init \
        wget \
        curl \
        openssh-client \
        python-openssl \
        git \
        ca-certificates \
        tzdata \
        python3 \
        python3-pip \
    " 

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y $PACKAGES && \
    ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && \
    pip3 install pandas \
                 impyute \
                 google-cloud-storage
    #curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz && \
    #mkdir -p /usr/local/gcloud && \
    #tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz && \
    #/usr/local/gcloud/google-cloud-sdk/install.sh && \
    #pip install impyute \
    #            google-cloud-storage

ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

WORKDIR /opt/carpe-datum

ENTRYPOINT ["bash", "run.sh"]