from utils import parse_element_text, insert_into_table

def process_personal(cur, personal_element, response_id):
    personal_data = {
        "response_id": response_id,
        "fio": parse_element_text(personal_element, 'fio'),
        "id_otv": parse_element_text(personal_element, 'id_otv', data_type=int),
        "id_pers": parse_element_text(personal_element, 'id_pers', data_type=int),
        "pred_id": parse_element_text(personal_element, 'pred_id', data_type=int)
    }
    insert_into_table(cur, 'apvo2_personal', personal_data)

def process_places(cur, places_element, response_id):
    places_data = {
        "response_id": response_id,
        "pereg_ms_id": parse_element_text(places_element, 'pereg_ms_id', data_type=int),
        "place_type": parse_element_text(places_element, 'place_type', data_type=int),
        "stan1_id": parse_element_text(places_element, 'stan1_id', data_type=int),
        "stan2_id": parse_element_text(places_element, 'stan2_id', data_type=int)
    }
    place_id = insert_into_table(cur, 'apvo2_places', places_data, returning_id=True)

    for objects_element in places_element.findall('.//objects'):
        objects_data = {
            "places_id": place_id,
            "id_obj": parse_element_text(objects_element, 'id_obj', data_type=int),
            "id_obj_type": parse_element_text(objects_element, 'id_obj_type', data_type=int),
            "obj_txt": parse_element_text(objects_element, 'obj_txt')
        }
        insert_into_table(cur, 'apvo2_objects', objects_data)

    for ways_element in places_element.findall('.//ways'):
        ways_data = {
            "places_id": place_id,
            "kmk": parse_element_text(ways_element, 'kmk', data_type=int),
            "kmn": parse_element_text(ways_element, 'kmn', data_type=int),
            "pkk": parse_element_text(ways_element, 'pkk', data_type=int),
            "pkn": parse_element_text(ways_element, 'pkn', data_type=int),
            "way_id": parse_element_text(ways_element, 'way_id', data_type=int),
            "way_txt": parse_element_text(ways_element, 'way_txt'),
            "way_type": parse_element_text(ways_element, 'way_type', data_type=int)
        }
        insert_into_table(cur, 'apvo2_ways', ways_data)

def process_plan_times(cur, plan_times_element, response_id):
    plan_times_data = {
        "response_id": response_id,
        "dl": parse_element_text(plan_times_element, 'dl', data_type=int),
        "kd": parse_element_text(plan_times_element, 'kd'),
        "nd": parse_element_text(plan_times_element, 'nd')
    }
    insert_into_table(cur, 'apvo2_plan_times', plan_times_data)

def process_trainGraph(cur, trainGraph_element, response_id):
    trainGraph_data = {
        "response_id": response_id,
        "cancelEvenCargo": parse_element_text(trainGraph_element, 'cancelEvenCargo', data_type=int),
        "cancelEvenPassanger": parse_element_text(trainGraph_element, 'cancelEvenPassanger', data_type=int),
        "cancelEvenSuburban": parse_element_text(trainGraph_element, 'cancelEvenSuburban', data_type=int),
        "cancelOddCargo": parse_element_text(trainGraph_element, 'cancelOddCargo', data_type=int),
        "cancelOddPassanger": parse_element_text(trainGraph_element, 'cancelOddPassanger', data_type=int),
        "cancelOddSuburban": parse_element_text(trainGraph_element, 'cancelOddSuburban', data_type=int),
        "changesEvenCargo": parse_element_text(trainGraph_element, 'changesEvenCargo', data_type=int),
        "changesEvenPassanger": parse_element_text(trainGraph_element, 'changesEvenPassanger', data_type=int),
        "changesEvenSuburban": parse_element_text(trainGraph_element, 'changesEvenSuburban', data_type=int),
        "changesOddCargo": parse_element_text(trainGraph_element, 'changesOddCargo', data_type=int),
        "changesOddPassanger": parse_element_text(trainGraph_element, 'changesOddPassanger', data_type=int),
        "changesOddSuburban": parse_element_text(trainGraph_element, 'changesOddSuburban', data_type=int),
        "delayEvenCargoCount": parse_element_text(trainGraph_element, 'delayEvenCargoCount', data_type=int),
        "delayEvenCargoTime": parse_element_text(trainGraph_element, 'delayEvenCargoTime', data_type=int),
        "delayEvenPassangerCount": parse_element_text(trainGraph_element, 'delayEvenPassangerCount', data_type=int),
        "delayEvenPassangerTime": parse_element_text(trainGraph_element, 'delayEvenPassangerTime', data_type=int),
        "delayEvenSuburbanCount": parse_element_text(trainGraph_element, 'delayEvenSuburbanCount', data_type=int),
        "delayEvenSuburbanTime": parse_element_text(trainGraph_element, 'delayEvenSuburbanTime', data_type=int),
        "delayOddCargoCount": parse_element_text(trainGraph_element, 'delayOddCargoCount', data_type=int),
        "delayOddCargoTime": parse_element_text(trainGraph_element, 'delayOddCargoTime', data_type=int),
        "delayOddPassangerCount": parse_element_text(trainGraph_element, 'delayOddPassangerCount', data_type=int),
        "delayOddPassangerTime": parse_element_text(trainGraph_element, 'delayOddPassangerTime', data_type=int),
        "delayOddSuburbanCount": parse_element_text(trainGraph_element, 'delayOddSuburbanCount', data_type=int),
        "delayOddSuburbanTime": parse_element_text(trainGraph_element, 'delayOddSuburbanTime', data_type=int),
        "sizeMovEvenCargo": parse_element_text(trainGraph_element, 'sizeMovEvenCargo', data_type=int),
        "sizeMovEvenPassanger": parse_element_text(trainGraph_element, 'sizeMovEvenPassanger', data_type=int),
        "sizeMovEvenSuburban": parse_element_text(trainGraph_element, 'sizeMovEvenSuburban', data_type=int),
        "sizeMovOddCargo": parse_element_text(trainGraph_element, 'sizeMovOddCargo', data_type=int),
        "sizeMovOddPassanger": parse_element_text(trainGraph_element, 'sizeMovOddPassanger', data_type=int),
        "sizeMovOddSuburban": parse_element_text(trainGraph_element, 'sizeMovOddSuburban', data_type=int),
        "truncateEvenSuburban": parse_element_text(trainGraph_element, 'truncateEvenSuburban', data_type=int),
        "truncateOddSuburban": parse_element_text(trainGraph_element, 'truncateOddSuburban', data_type=int)
    }
    insert_into_table(cur, 'apvo2_trainGraph', trainGraph_data)

def process_locos(cur, locos_element, response_id):
    locos_data = {
        "response_id": response_id,
        "br_change": parse_element_text(locos_element, 'brChange', data_type=int),
        "count": parse_element_text(locos_element, 'count', data_type=int),
        "depo_id": parse_element_text(locos_element, 'depo_id', data_type=int),
        "duration": parse_element_text(locos_element, 'duration', data_type=int),
        "fin": parse_element_text(locos_element, 'fin', data_type=int),
        "id_ser_loco": parse_element_text(locos_element, 'idSerLoco', data_type=int),
        "id_series": parse_element_text(locos_element, 'id_series', data_type=int),
        "kd": parse_element_text(locos_element, 'kd'),
        "length": parse_element_text(locos_element, 'length', data_type=int),
        "nd": parse_element_text(locos_element, 'nd'),
        "pred_id": parse_element_text(locos_element, 'pred_id', data_type=int),
        "pred_name": parse_element_text(locos_element, 'pred_name'),
        "stan1_id": parse_element_text(locos_element, 'stan1_id', data_type=int),
        "stan1_name": parse_element_text(locos_element, 'stan1_name'),
        "stan2_id": parse_element_text(locos_element, 'stan2_id', data_type=int),
        "stan2_name": parse_element_text(locos_element, 'stan2_name'),
        "stan3_id": parse_element_text(locos_element, 'stan3_id', data_type=int),
        "stan3_name": parse_element_text(locos_element, 'stan3_name'),
        "status": parse_element_text(locos_element, 'status', data_type=int),
        "status_fact": parse_element_text(locos_element, 'status_fact', data_type=int),
        "time_dept": parse_element_text(locos_element, 'time_dept'),
        "txt": parse_element_text(locos_element, 'txt'),
        "weight": parse_element_text(locos_element, 'weight', data_type=int),
        "work_type": parse_element_text(locos_element, 'workType', data_type=int),
        "zlid": parse_element_text(locos_element, 'zlid', data_type=int)
    }
    insert_into_table(cur, 'apvo2_locos', locos_data)

def process_works(cur, works_element, response_id):
    works_data = {
        "response_id": response_id,
        "ei_id": parse_element_text(works_element, 'ei_id', data_type=int),
        "ei_name": parse_element_text(works_element, 'ei_name'),
        "fact_added": parse_element_text(works_element, 'fact_added', default='false', data_type=lambda x: x == 'true'),
        "fact_v": parse_element_text(works_element, 'fact_v', data_type=float),
        "id_reason": parse_element_text(works_element, 'id_reason', data_type=int),
        "plan_v": parse_element_text(works_element, 'plan_v', data_type=float),
        "repair_id": parse_element_text(works_element, 'repair_id', data_type=int),
        "repair_name": parse_element_text(works_element, 'repair_name'),
        "work_id": parse_element_text(works_element, 'work_id', data_type=int),
        "work_name": parse_element_text(works_element, 'work_name')
    }
    insert_into_table(cur, 'apvo2_works', works_data)

def process_techs(cur, techs_element, response_id):
    techs_data = {
        "response_id": response_id,
        "arrival_time": parse_element_text(techs_element, 'arrivalTime'),
        "dispatch_time": parse_element_text(techs_element, 'dispatchTime'),
        "ei_id": parse_element_text(techs_element, 'ei_id', data_type=int),
        "repair_id": parse_element_text(techs_element, 'repair_id', data_type=int),
        "tech_id": parse_element_text(techs_element, 'tech_id', data_type=int),
        "tech_num": parse_element_text(techs_element, 'tech_num', data_type=int),
        "tech_text": parse_element_text(techs_element, 'tech_text'),
        "type_tech_id": parse_element_text(techs_element, 'type_tech_id', data_type=int),
        "type_tech_name": parse_element_text(techs_element, 'type_tech_name'),
        "work_id": parse_element_text(techs_element, 'work_id', data_type=int)
    }
    insert_into_table(cur, 'apvo2_techs', techs_data)
