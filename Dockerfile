FROM debian:latest

# Create the bot's directory
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY . /usr/src/bot

# install dependencies
RUN apt-get update
RUN apt-get install -y python3 python3-pip git

# Install bot reqs
RUN pip3 install -r ./src/requirements.txt

# Start the bot.
CMD ["python3", "nov.py"]