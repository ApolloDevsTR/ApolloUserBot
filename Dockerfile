#TODO: make a special image and publish it to docker hub 
FROM python:3.10-alpine
RUN apk add --no-cache --update coreutils bash build-base bzip2-dev curl figlet gcc g++ git sudo util-linux libevent jpeg-dev libffi-dev libpq libwebp-dev libxml2 libxml2-dev libxslt-dev linux-headers musl neofetch openssl-dev wget sudo libc-dev zlib-dev jpeg py3-wheel py3-numpy py3-pillow python3-dev readline-dev
ADD https://api.github.com/repos/ApolloDevsTR/$ApolloUserBot/git/refs/heads/main version.json
# dont cache if there is a new commit
RUN git clone https://github.com/ApolloDevsTR/ApolloUserBot /root/ApolloUserBot
WORKDIR /root/ApolloUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "apollo"]