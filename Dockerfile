FROM python:3.10-alpine
RUN /bin/sh -c apk update
RUN /bin/sh -c apk add coreutils bash build-base bzip2-dev curl figlet gcc g++ git sudo util-linux libevent jpeg-dev libffi-dev libpq libwebp-dev libxml2 libxml2-dev libxslt-dev linux-headers musl neofetch openssl-dev wget sudo libc-devzlib-dev jpeg py3-wheel py3-numpy py3-pillow python3-dev readline-dev
RUN git clone https://github.com/ApolloDevsTR/ApolloUserBot /root/ApolloUserBot
WORKDIR /root/ApolloUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "apollo"]
