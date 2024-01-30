"""
An example of using a Pydantic model and custom validate user input in an
interactive workflow. 

Included in our Guide to Creating Interactive Workflows:
    https://docs.prefect.io/latest/guides/creating-interactive-workflows/
"""
from typing import Literal

import pydantic
from prefect import flow, get_run_logger, pause_flow_run


class ShirtOrder(pydantic.BaseModel):
    size: Literal["small", "medium", "large", "xlarge"]
    color: Literal["red", "green", "black"]

    @pydantic.validator("color")
    def validate_age(cls, value, values, **kwargs):
        if value == "green" and values["size"] == "small":
            raise ValueError("Green is only in-stock for medium, large, and XL sizes.")

        return value


@flow
def get_shirt_order():
    logger = get_run_logger()
    shirt_order = None

    while shirt_order is None:
        try:
            shirt_order = pause_flow_run(wait_for_input=ShirtOrder)
        except pydantic.ValidationError as exc:
            logger.error(f"Invalid size and color combination: {exc}")

    logger.info(f"Shirt order: {shirt_order.size}, {shirt_order.color}")


if __name__ == "__main__":
    get_shirt_order.serve("get-shirt-order")
