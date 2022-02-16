import logging
import argparse
import sys

from api_client import APIClient


log = logging.getLogger(__name__)

def sort_to_next_step(url, token):
    log.info("Creating api client")
    api = APIClient(url, token)

    log.info('Uploading STL files')
    stls = {
        'airplane': 'stls/airplane.stl',
        'bus': 'stls/bus.stl',
        'flange': 'stls/flange.stl',
        'vase': 'stls/vase.stl',
        'bracket': 'stls/bracket.stl',
        'coupling': 'stls/coupling.stl',
        'knight': 'stls/knight.stl'
    }
    ids = {'id': ','.join(stls.keys())}
    response = api.design_reference.search.post(ids, page_size=len(stls))
    for reference in response['results']:
      del stls[reference['id']]  
    for id, filename in stls.items():
      with open(filename, 'rb') as stl:
        api.design_reference.post({'id': id}, files={'stl': stl})
    
    log.info('Uploading prints')
    prints = [
        {
            "id": "airplane",
            "title": "Airplane",
            "copies": 1,
            "design_reference": "airplane",
            "material_reference": "SLS_PA11",
            "extra_material_references": [],
            "attributes": {
                "prev_step": "printing",
                "next_step": "shipping",
                "technology": "SLS",
                "order_id": 168,
                "tray": "240",
                "target_date": "2022-07-23"
            }
        },  
        {
            "id": "bus",
            "title": "Bus",
            "copies": 5,
            "design_reference": "bus",
            "material_reference": "SLS_PA11",
            "extra_material_references": [],
            "attributes": {
                "prev_step": "Printing",
                "next_step": "shipping",
                "technology": "SLS",
                "order_id": 201,
                "tray": "240",
                "target_date": "2022-03-10"
            }
        },
        {
            "id": "bracket",
            "title": "Bracket",
            "copies": 1,
            "design_reference": "bracket",
            "material_reference": "MJF_PA12",
            "extra_material_references": [],
            "attributes": {
                "prev_step": "Printing",
                "next_step": "shipping",
                "technology": "MJF",
                "order_id": 201,
                "tray": "240",
                "target_date": "2022-03-10"
            }
        },
        {
            "id": "widget",
            "title": "Widget",
            "copies": 1,
            "design_reference": "bracket",
            "material_reference": "MJF_PA12",
            "extra_material_references": ["MJF_PA12-BLACK"],
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_black",
                "technology": "MJF",
                "order_id": 443,
                "tray": "240",
                "target_date": "2022-03-18"
            }
        },
        {
            "id": "coupling",
            "title": "Coupling",
            "copies": 1,
            "design_reference": "coupling",
            "material_reference": "SLS_PA11",
            "extra_material_references": ["SLS_PA11-BLACK"],
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_black",
                "technology": "SLS",
                "order_id": 302,
                "tray": "240",
                "target_date": "2022-03-18"
            }
        },
        {
            "id": "flange",
            "title": "Flange",
            "copies": 1,
            "design_reference": "flange",
            "material_reference": "SLS_PA11",
            "extra_material_references": ["SLS_PA11-RED"],
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_red",
                "technology": "SLS",
                "order_id": 201,
                "tray": "240",
                "target_date": "2022-03-10"
            }
        },
        {
            "id": "knight",
            "title": "Knight",
            "copies": 1,
            "design_reference": "knight",
            "material_reference": "MJF_PA12",
            "extra_material_references": ["MJF_PA12-RED"],
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_red",
                "technology": "MJF",
                "order_id": 302,
                "tray": "240",
                "target_date": "2022-03-18"
            }
        },
        {
            "id": "vase",
            "title": "Vase",
            "copies": 3,
            "design_reference": "vase",
            "material_reference": "MJF_PA12",
            "extra_material_references": ["MJF_PA12-RED"],
            "attributes": {
                "prev_step": "Printing",
                "next_step": "dye_red",
                "technology": "MJF",
                "order_id": 168,
                "tray": "240",
                "target_date": "2022-07-23"
            }
        }
    ]
    api.print.put(prints)

    log.info('Creating a batch')
    batch = {
        "id": "240",
        "title": "Tray 240",
        "query": "tray=240",
    }
    api.batch.put([batch])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AM-Vision API sorting by next step')
    parser.add_argument('url', type=str, help='API URL')
    parser.add_argument('token', type=str, help='API token')
    args = parser.parse_args()
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='[%(asctime)s: %(levelname)s] %(message)s')

    sort_to_next_step(args.url, args.token)





  

   
