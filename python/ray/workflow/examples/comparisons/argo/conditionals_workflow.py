import ray
from ray import workflow
import secrets


@ray.remote
def handle_heads() -> str:
    return "It was heads"


@ray.remote
def handle_tails() -> str:
    return "It was tails"


@ray.remote
def flip_coin() -> str:

    @ray.remote
    def decide(heads: bool) -> str:
        return workflow.continuation(
            handle_heads.bind() if heads else handle_tails.bind()
        )

    return workflow.continuation(decide.bind(secrets.SystemRandom().random() > 0.5))


if __name__ == "__main__":
    print(workflow.run(flip_coin.bind()))
