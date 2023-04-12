FROM <base-image>
WORKDIR /app
COPY . /app
RUN <commands-to-build-and-run-the-project>
