FROM alpine


# Install AWSCLI
RUN apk add --no-cache aws-cli

ARG ACCESS_KEY_ID x
ARG SECRET_ACCESS_KEY x
ARG DEFAULT_REGION x
WORKDIR /home
ADD script.sh /home
RUN chmod 777 script.sh
# RUN aws configure set aws_access_key_id $ACCESS_KEY_ID; aws configure set aws_secret_access_key $SECRET_ACCESS_KEY; aws configure set default.region $DEFAULT_REGION;

# ENTRYPOINT [ "aws", "--version" ]
# ENTRYPOINT [ "aws","configure" ]
ENTRYPOINT [ "./script.sh" ]
CMD [ "aws","s3", "ls" ]