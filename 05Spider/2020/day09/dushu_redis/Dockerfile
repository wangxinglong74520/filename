FROM 192.168.17.130:5001
MAINTAINER merlr 1544798456@qq.com
ADD . /usr/src
VOLUME /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/run.sh



