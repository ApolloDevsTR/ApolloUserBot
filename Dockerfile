FROM python:3.10-alpine
RUN git clone https://github.com/ApolloDevsTR/ApolloUserBot /root/ApolloUserBot
WORKDIR /root/ApolloUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "apollo"]
