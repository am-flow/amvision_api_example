import argparse
import logging
import sys

from api_client import APIClient

log = logging.getLogger(__name__)


def perform_configuration(url, token):
    log.info("Creating api client")
    api = APIClient(url, token)

    log.info("Uploading part attributes")
    attributes = [
        {
            "id": "next_step",
            "title": "Next step",
            "field": "next_step",
            "datatype": "STRING",
            "filtering": True,
            "sorting": True,
            "detail": True,
            "summary": True,
            "order": 0,
        },
        {
            "id": "prev_step",
            "title": "Previous step",
            "field": "prev_step",
            "datatype": "STRING",
            "filtering": True,
            "sorting": True,
            "detail": True,
            "summary": False,
            "order": 1,
        },
        {
            "id": "technology",
            "title": "Technology",
            "field": "technology",
            "datatype": "STRING",
            "filtering": True,
            "sorting": False,
            "detail": True,
            "summary": False,
        },
        {
            "id": "order",
            "title": "Order #",
            "field": "order_id",
            "datatype": "NUMBER",
            "filtering": True,
            "sorting": False,
            "detail": True,
            "summary": True,
        },
        {
            "id": "tray",
            "title": "Print tray",
            "field": "tray",
            "datatype": "STRING",
            "filtering": True,
            "sorting": False,
            "detail": True,
            "summary": False,
        },
        {
            "id": "target_date",
            "title": "Target date",
            "field": "target_date",
            "datatype": "STRING",
            "filtering": True,
            "sorting": True,
            "detail": True,
            "summary": True,
        },
    ]
    api.part_attribute.put(attributes)

    log.info("Uploading query categories")
    categories = [
        {"id": "next_step", "title": "Next step"},
        {"id": "order", "title": "Order #"},
        {"id": "date", "title": "Target date"},
    ]
    api.query_category.put(categories)

    log.info("Uploading sorting queries")
    sorting_queries = [
        {
            "id": "next_step",
            "title": "Next step",
            "query": "",
            "category": "next_step",
            "dynamic_attribute": "next_step",
        },
        {
            "id": "target_date",
            "title": "Target date",
            "query": "",
            "category": "date",
            "dynamic_attribute": "target_date",
        },
        {
            "id": "order",
            "title": "Order #",
            "query": "",
            "category": "order",
            "dynamic_attribute": "order",
        },
    ]
    api.query.put(sorting_queries)

    log.info("Subscribing to the webhook")
    api.webhook.post(
        {"event": "batch.finalize", "target": "http://example.com/on_batch_sorted/"}
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="AM-Vision API one-time configuration example"
    )
    parser.add_argument("url", type=str, help="API URL")
    parser.add_argument("token", type=str, help="API token")
    args = parser.parse_args()
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="[%(asctime)s: %(levelname)s] %(message)s",
    )

    perform_configuration(args.url, args.token)
