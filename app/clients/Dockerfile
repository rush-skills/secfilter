FROM ruby:2.1.5
ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY clients.rb clients.rb
CMD ruby clients.rb
