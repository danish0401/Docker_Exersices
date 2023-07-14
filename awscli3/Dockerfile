FROM alpine
RUN apk add --no-cache aws-cli

ENTRYPOINT ["aws"]
CMD [ "s3", "ls" ]
