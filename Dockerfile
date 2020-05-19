FROM python:3.7


ENV BUILD_DIR="/app/build"
ENV RUNTIME_DIR="/app/runtime"
ENV APP_USER="lml"

# Suppose server have 10 cpu cores. The recommended number of gunicorn worker is ((2 x $num_cores) + 1) = 21
ENV WORKER_NUM=21
ENV SERVICE_PORT=8080

# ENV variables used by server
ENV model_storage=${RUNTIME_DIR}/storage
# set EML_RETRAIN_MODELS to retrain all models
# ENV EML_RETRAIN_MODELS=1


# Install dependences
WORKDIR ${BUILD_DIR}
COPY requirements.txt requirements-ml.txt ${BUILD_DIR}/
RUN python3 -m pip install --quiet --upgrade pip && \
    python3 -m pip install --quiet -r requirements-ml.txt && \
    python3 -m pip install --quiet -r requirements.txt


# Install this project
COPY . ${BUILD_DIR}
RUN adduser --system --no-create-home --group ${APP_USER} && \
    python3 setup.py install --quiet && \
    # prepare example for runtime
    echo "Preparing examples. This may take up to 5 minutes" && \
    python3 runtime/init.py && cp -r runtime ${RUNTIME_DIR}


# Prepare runtime
WORKDIR ${RUNTIME_DIR}
RUN chown --recursive ${APP_USER}:${APP_USER} ${RUNTIME_DIR}/*


USER ${APP_USER}
EXPOSE ${SERVICE_PORT}

# Default parameters:
#   Uvicorn worker class is required by Fastapi
#   Container schedulers typically expect logs to come out on stdout/stderr, thus gunicorn is configured to do so
#   Gunicorn needs to store its temporary file in memory (e.g. /dev/shm)
ENTRYPOINT gunicorn --worker-class=uvicorn.workers.UvicornWorker \
                    --log-file=- \
                    --worker-tmp-dir=/dev/shm \
                    --chdir=${RUNTIME_DIR} \
                    --bind=:${SERVICE_PORT} \
                    --workers=${WORKER_NUM} asgi:app
