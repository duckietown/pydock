import pytest

from pydock import docker
from pydock.exceptions import DockerException


def test_exception_attributes():
    with pytest.raises(DockerException) as excinfo:
        docker.image.tag("wrong::image", "wrong::tag")

    exception = excinfo.value
    assert "The docker command executed was" in str(exception)
    assert exception.docker_command[1:5] == [
        "image",
        "tag",
        "wrong::image",
        "wrong::tag",
    ]
    # The exact return code and error string might vary with future docker
    # versions, so following asserts are somewhat relaxed
    assert exception.return_code > 0
    assert not exception.stdout
    assert "wrong::" in exception.stderr
