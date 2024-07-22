from utils import parse_element_text, insert_into_table
from process_nested import process_personal, process_places, process_plan_times, process_trainGraph, process_locos, process_works, process_techs

def process_response(cur, return_element):
    response_data = {
        "allAccepted": parse_element_text(return_element, 'allAccepted', default='false', data_type=lambda x: x == 'true'),
        "dor_kod": parse_element_text(return_element, 'dor_kod', data_type=int),
        "dt_corr": parse_element_text(return_element, 'dt_corr'),
        "duId": parse_element_text(return_element, 'duId', data_type=int),
        "duName": parse_element_text(return_element, 'duName'),
        "duSort": parse_element_text(return_element, 'duSort', data_type=int),
        "flg_volt": parse_element_text(return_element, 'flg_volt', data_type=int),
        "flg_wnd": parse_element_text(return_element, 'flg_wnd', data_type=int),
        "idMa": parse_element_text(return_element, 'idMa', data_type=int),
        "idTuch": parse_element_text(return_element, 'idTuch', data_type=int),
        "id_overtime": parse_element_text(return_element, 'id_overtime', data_type=int),
        "id_overtime_sl": parse_element_text(return_element, 'id_overtime_sl', data_type=int),
        "id_reject": parse_element_text(return_element, 'id_reject', data_type=int),
        "id_reject_fact": parse_element_text(return_element, 'id_reject_fact', data_type=int),
        "id_reject_fact_sl": parse_element_text(return_element, 'id_reject_fact_sl', data_type=int),
        "overtime": parse_element_text(return_element, 'overtime', data_type=int),
        "pred_id": parse_element_text(return_element, 'pred_id', data_type=int),
        "pred_name": parse_element_text(return_element, 'pred_name'),
        "seqVoltage": parse_element_text(return_element, 'seqVoltage', data_type=int),
        "status_fact": parse_element_text(return_element, 'status_fact', data_type=int),
        "status_pl": parse_element_text(return_element, 'status_pl', data_type=int),
        "timeVoltage": parse_element_text(return_element, 'timeVoltage', data_type=int),
        "wid": parse_element_text(return_element, 'wid', data_type=int)
    }

    response_id = insert_into_table(cur, 'response', response_data, returning_id=True)

    for personal_element in return_element.findall('.//personal'):
        process_personal(cur, personal_element, response_id)

    for places_element in return_element.findall('.//places'):
        process_places(cur, places_element, response_id)

    for plan_times_element in return_element.findall('.//plan_times'):
        process_plan_times(cur, plan_times_element, response_id)

    for trainGraph_element in return_element.findall('.//trainGraph'):
        process_trainGraph(cur, trainGraph_element, response_id)

    for locos_element in return_element.findall('.//locos'):
        process_locos(cur, locos_element, response_id)

    for works_element in return_element.findall('.//works'):
        process_works(cur, works_element, response_id)

    for techs_element in return_element.findall('.//techs'):
        process_techs(cur, techs_element, response_id)
