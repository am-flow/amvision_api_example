import argparse
import logging
import json
import sys

from api_client import APIClient


log = logging.getLogger(__name__)


def upload_all(address, port, token):
    # instantiate API client
    api = APIClient(address, port, token)

    # load design references
    with open('data/design_references.json') as in_file:
        refs = json.load(in_file)

    # filter out previously uploaded designs
    ids = {'id': ','.join(refs.keys())}
    response = api.design_reference.search.post(ids, page_size=len(refs))
    for reference in response['results']:
        del refs[reference['id']]

    # upload design references
    for id, filename in refs.items():
        with open(filename, 'rb') as stl:
            api.design_reference.post({'id': id}, files={'stl': stl})

    # upload material references
    with open('data/material_references.json') as in_file:
        api.material_reference.put(json.load(in_file))

    # upload prints
    with open('data/prints.json') as in_file:
        api.print.put(json.load(in_file))

    # upload print attributes
    with open('data/print_attributes.json') as in_file:
        api.print_attribute.put(json.load(in_file))

    # upload views
    with open('data/views.json') as in_file:
        api.view.put(json.load(in_file))

    # upload batches
    with open('data/batches.json') as in_file:
        api.batch.put(json.load(in_file))

    # upload query categories
    with open('data/query_categories.json') as in_file:
        api.query_category.put(json.load(in_file))

    # upload queries
    with open('data/queries.json') as in_file:
        api.query.put(json.load(in_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AM-Vision API uploader')
    parser.add_argument(
        'token', type=str, help='API token'
    )
    parser.add_argument(
        '-a', '--address', type=str, help='Server address', default='localhost'
    )
    parser.add_argument(
        '-p', '--port', type=str, help='API port', default='8000'
    )
    args = parser.parse_args()
    logging.basicConfig(
        stream=sys.stdout, level=logging.INFO,
        format='[%(asctime)s: %(levelname)s] %(message)s'
    )

    log.info("Starting upload")
    upload_all(args.address, args.port, args.token)
    log.info("Upload completed")
