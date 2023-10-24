import argparse
import logging
import sys

from api_client import APIClient

log = logging.getLogger(__name__)


def sort_to_order(url, token):
    log.info("Creating api client")
    api = APIClient(url, token)

    log.info("Deleting parts marked as reprint")
    api.part.delete(id="airplane,knight")

    log.info("Updating parts to the next step")
    parts = [
        {
            "id": "widget",
            "title": "Widget",
            "copies": 1,
            "model": "bracket",
            "material": "MJF_PA12-BLACK",
            "attributes": {
                "prev_step": "dye_black",
                "next_step": "shipping",
                "technology": "MJF",
                "order_id": 443,
                "tray": "240",
                "target_date": "2022-03-18",
            },
        },
        {
            "id": "coupling",
            "title": "Coupling",
            "copies": 1,
            "model": "coupling",
            "material": "SLS_PA11-BLACK",
            "attributes": {
                "prev_step": "dye_black",
                "next_step": "shipping",
                "technology": "SLS",
                "order_id": 302,
                "tray": "240",
                "target_date": "2022-03-18",
            },
        },
        {
            "id": "flange",
            "title": "Flange",
            "copies": 1,
            "model": "flange",
            "material": "SLS_PA11-RED",
            "attributes": {
                "prev_step": "dye_red",
                "next_step": "shipping",
                "technology": "SLS",
                "order_id": 201,
                "tray": "240",
                "target_date": "2022-03-10",
            },
        },
        {
            "id": "vase",
            "title": "Vase",
            "copies": 3,
            "model": "vase",
            "material": "MJF_PA12-RED",
            "attributes": {
                "prev_step": "dye_red",
                "next_step": "shipping",
                "technology": "MJF",
                "order_id": 168,
                "tray": "240",
                "target_date": "2022-07-23",
            },
        },
    ]
    api.part.put(parts)

    log.info("Creating sub-batches")
    sub_batches = [
        {
            "id": "240_no_post_process",
            "title": "Tray 240: no post process",
            "query": "tray=240&prev_step=printing",
        },
        {
            "id": "240_dye_black",
            "title": "Tray 240: Dye black",
            "query": "tray=240&prev_step=dye_black",
        },
        {
            "id": "240_dye_red",
            "title": "Tray 240: Dye red",
            "query": "tray=240&prev_step=dye_red",
        },
    ]
    api.batch.put(sub_batches)

    log.info("Deleteing original batch")
    api.batch(240).delete()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AM-Vision API sorting to order")
    parser.add_argument("url", type=str, help="API URL")
    parser.add_argument("token", type=str, help="API token")
    args = parser.parse_args()
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="[%(asctime)s: %(levelname)s] %(message)s",
    )

    sort_to_order(args.url, args.token)
