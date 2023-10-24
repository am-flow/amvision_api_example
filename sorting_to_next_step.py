import argparse
import logging
import sys

from api_client import APIClient

log = logging.getLogger(__name__)


def sort_to_next_step(url, token):
    log.info("Creating api client")
    api = APIClient(url, token)

    log.info("Uploading STL files")
    stls = {
        "airplane": "stls/airplane.stl",
        "bus": "stls/bus.stl",
        "flange": "stls/flange.stl",
        "vase": "stls/vase.stl",
        "bracket": "stls/bracket.stl",
        "coupling": "stls/coupling.stl",
        "knight": "stls/knight.stl",
    }
    ids = {"id": ",".join(stls.keys())}
    response = api.model.search.post(ids, page_size=len(stls))
    for model in response["results"]:
        del stls[model["id"]]
    for id, filename in stls.items():
        with open(filename, "rb") as stl:
            api.model.post({"id": id}, files={"geometry": stl})

    log.info("Uploading parts")
    parts = [
        {
            "id": "airplane",
            "title": "Airplane",
            "copies": 1,
            "model": "airplane",
            "material": "SLS_PA11",
            "attributes": {
                "prev_step": "printing",
                "next_step": "shipping",
                "technology": "SLS",
                "order_id": 168,
                "tray": "240",
                "target_date": "2022-07-23",
            },
        },
        {
            "id": "bus",
            "title": "Bus",
            "copies": 5,
            "model": "bus",
            "material": "SLS_PA11",
            "attributes": {
                "prev_step": "Printing",
                "next_step": "shipping",
                "technology": "SLS",
                "order_id": 201,
                "tray": "240",
                "target_date": "2022-03-10",
            },
        },
        {
            "id": "bracket",
            "title": "Bracket",
            "copies": 1,
            "model": "bracket",
            "material": "MJF_PA12",
            "attributes": {
                "prev_step": "Printing",
                "next_step": "shipping",
                "technology": "MJF",
                "order_id": 201,
                "tray": "240",
                "target_date": "2022-03-10",
            },
        },
        {
            "id": "widget",
            "title": "Widget",
            "copies": 1,
            "model": "bracket",
            "material": "MJF_PA12",
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_black",
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
            "material": "SLS_PA11",
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_black",
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
            "material": "SLS_PA11",
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_red",
                "technology": "SLS",
                "order_id": 201,
                "tray": "240",
                "target_date": "2022-03-10",
            },
        },
        {
            "id": "knight",
            "title": "Knight",
            "copies": 1,
            "model": "knight",
            "material": "MJF_PA12",
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_red",
                "technology": "MJF",
                "order_id": 302,
                "tray": "240",
                "target_date": "2022-03-18",
            },
        },
        {
            "id": "vase",
            "title": "Vase",
            "copies": 3,
            "model": "vase",
            "material": "MJF_PA12",
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_red",
                "technology": "MJF",
                "order_id": 168,
                "tray": "240",
                "target_date": "2022-07-23",
            },
        },
    ]
    api.part.put(parts)

    log.info("Creating a batch")
    batch = {
        "id": "240",
        "title": "Tray 240",
        "query": "tray=240",
    }
    # using PUT here instead of POST unlike the tutorial to prevent already-exists-error
    api.batch.put([batch])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AM-Vision API sorting by next step")
    parser.add_argument("url", type=str, help="API URL")
    parser.add_argument("token", type=str, help="API token")
    args = parser.parse_args()
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="[%(asctime)s: %(levelname)s] %(message)s",
    )

    sort_to_next_step(args.url, args.token)
