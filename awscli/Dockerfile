FROM alpine
RUN apk add --no-cache aws-cli

VOLUME /root/.aws
VOLUME /project
WORKDIR /project

ENTRYPOINT ["aws"]
CMD [ "s3", "ls" ]
