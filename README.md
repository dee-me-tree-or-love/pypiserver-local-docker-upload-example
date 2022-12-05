# Basics

This is a small replication package for using pypiserver with local docker.

Clone the files in this repo to test it out.

## Getting started

### To start an authentication-protected pypiserver

1. First create a `htpasswd.txt` file with authentication details as described
[here](https://github.com/pypiserver/pypiserver#apache-like-authentication-htpasswd).

2. Next, run the pypiserver in docker

    > Note that `-vvv` parameter sets the verbose output

    ```bash
    # with auth
    docker run --rm -it -p 88:8080 -v $(pwd)/htpasswd.txt:/data/.htpasswd -v $(pwd)/data/packages:/data/packages --name pypiserver pypiserver/pypiserver:latest -vvv -P /data/.htpasswd
    ```

### To start an authentication-free pypiserver

1. Directly, run the pypiserver in docker, overriding the authentication parameters with `-P . -a .`

    ```bash
    # without auth
    docker run --rm -it -p 88:8080 -v $(pwd)/data/packages:/data/packages --name pypiserver pypiserver/pypiserver:latest -vvv -P . -a .
    ```

### Uploading

1. Build and upload the demo package

    ```bash
    # n.b: I am using `poetry` in this example to simplify the build steps
    #   see https://python-poetry.org/docs/cli/#build
    $ cd hello_world
    $ poetry build
    $ twine upload  --repository-url=http://localhost:88/  dist/* --verbose
    ...
    Response from http://localhost:88/:
    200 OK
    ```

2. Check the upload results in the expected folder

    ```bash
    $ ls ../data/packages | grep "hello_world"
    hello_world-... # should show all the uploaded hello_world distributions
    ```
