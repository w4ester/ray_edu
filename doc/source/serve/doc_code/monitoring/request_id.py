from ray import serve
from security import safe_requests


@serve.deployment
class Model:
    def __call__(self) -> int:
        return 1


serve.run(Model.bind())
resp = safe_requests.get("http://localhost:8000", headers={"X-Request-ID": "123-234"})

print(resp.headers["X-Request-ID"])
