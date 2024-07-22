# XmlLoader

XmlLoader is a versatile and efficient library designed to simplify the process of loading and parsing XML data in your applications. Whether you are dealing with simple XML files or complex nested structures, XmlLoader provides an intuitive API to make XML handling easy and seamless.

## Project Structure

```
JsonLoader/
│
├── files/
│   ├── data.xml
│
├── import_data.log
├── db_config.py
├── process_nested.py
├── process_response.py
├── main.py
├── utils.txt
└── local.env
```

## Prerequisites

- Python 3.7+
- PostgreSQL

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/NotFoundNone/XmlLoader.git
    cd XmlLoader
    ```

2. Set up the PostgreSQL database:
    - Create a new PostgreSQL database.
    - Run the DDL statements provided below to create the necessary tables and sequence.

3. Configure the database connection:
    - Update the `.env` file with your database credentials.

## Database DDL

Run the following DDL statements to set up your PostgreSQL database:

```sql
CREATE TABLE IF NOT EXISTS response (
    id SERIAL PRIMARY KEY,
    allAccepted BOOLEAN,
    dor_kod INTEGER,
    dt_corr TIMESTAMP,
    duId INTEGER,
    duName TEXT,
    duSort INTEGER,
    flg_volt INTEGER,
    flg_wnd INTEGER,
    idMa INTEGER,
    idTuch INTEGER,
    id_overtime INTEGER,
    id_overtime_sl INTEGER,
    id_reject INTEGER,
    id_reject_fact INTEGER,
    id_reject_fact_sl INTEGER,
    overtime INTEGER,
    pred_id INTEGER,
    pred_name TEXT,
    seqVoltage INTEGER,
    status_fact INTEGER,
    status_pl INTEGER,
    timeVoltage INTEGER,
    wid INTEGER
);

CREATE TABLE personal (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES response(id),
    fio TEXT,
    id_otv INTEGER,
    id_pers INTEGER,
    pred_id INTEGER
);

CREATE TABLE IF NOT EXISTS places (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES response(id),
    pereg_ms_id INTEGER,
    place_type INTEGER,
    stan1_id INTEGER,
    stan2_id INTEGER
);

CREATE TABLE IF NOT EXISTS objects (
    id SERIAL PRIMARY KEY,
    places_id INTEGER REFERENCES places(id),
    id_obj INTEGER,
    id_obj_type INTEGER,
    obj_txt TEXT
);

CREATE TABLE IF NOT EXISTS ways (
    id SERIAL PRIMARY KEY,
    places_id INTEGER REFERENCES places(id),
    kmk INTEGER,
    kmn INTEGER,
    pkk INTEGER,
    pkn INTEGER,
    way_id INTEGER,
    way_txt TEXT,
    way_type INTEGER
);

CREATE TABLE IF NOT EXISTS plan_times (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES response(id),
    dl INTEGER,
    kd TIMESTAMP,
    nd TIMESTAMP
);


CREATE TABLE IF NOT EXISTS trainGraph (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES response(id),
    cancelEvenCargo INTEGER,
    cancelEvenPassanger INTEGER,
    cancelEvenSuburban INTEGER,
    cancelOddCargo INTEGER,
    cancelOddPassanger INTEGER,
    cancelOddSuburban INTEGER,
    changesEvenCargo INTEGER,
    changesEvenPassanger INTEGER,
    changesEvenSuburban INTEGER,
    changesOddCargo INTEGER,
    changesOddPassanger INTEGER,
    changesOddSuburban INTEGER,
    delayEvenCargoCount INTEGER,
    delayEvenCargoTime INTEGER,
    delayEvenPassangerCount INTEGER,
    delayEvenPassangerTime INTEGER,
    delayEvenSuburbanCount INTEGER,
    delayEvenSuburbanTime INTEGER,
    delayOddCargoCount INTEGER,
    delayOddCargoTime INTEGER,
    delayOddPassangerCount INTEGER,
    delayOddPassangerTime INTEGER,
    delayOddSuburbanCount INTEGER,
    delayOddSuburbanTime INTEGER,
    sizeMovEvenCargo INTEGER,
    sizeMovEvenPassanger INTEGER,
    sizeMovEvenSuburban INTEGER,
    sizeMovOddCargo INTEGER,
    sizeMovOddPassanger INTEGER,
    sizeMovOddSuburban INTEGER,
    truncateEvenSuburban INTEGER,
    truncateOddSuburban INTEGER
);

CREATE TABLE IF NOT EXISTS works (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES response(id),
    ei_id INTEGER,
    ei_name TEXT,
    fact_added BOOLEAN,
    fact_v DECIMAL,
    id_reason INTEGER,
    plan_v DECIMAL,
    repair_id INTEGER,
    repair_name TEXT,
    work_id INTEGER,
    work_name TEXT
);

CREATE TABLE locos (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES response(id),
    br_change INTEGER,
    count INTEGER,
    depo_id INTEGER,
    duration INTEGER,
    fin INTEGER,
    id_ser_loco INTEGER,
    id_series INTEGER,
    kd TIMESTAMP,
    length INTEGER,
    nd TIMESTAMP,
    pred_id INTEGER,
    pred_name TEXT,
    stan1_id INTEGER,
    stan1_name TEXT,
    stan2_id INTEGER,
    stan2_name TEXT,
    stan3_id INTEGER,
    stan3_name TEXT,
    status INTEGER,
    status_fact INTEGER,
    time_dept TIMESTAMP,
    txt TEXT,
    weight INTEGER,
    work_type INTEGER,
    zlid INTEGER
);

CREATE TABLE techs (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES response(id),
    arrival_time TIMESTAMP,
    dispatch_time TIMESTAMP,
    ei_id INTEGER,
    repair_id INTEGER,
    tech_id INTEGER,
    tech_num INTEGER,
    tech_text TEXT,
    type_tech_id INTEGER,
    type_tech_name TEXT,
    work_id INTEGER
);


ALTER TABLE personal
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES response(id);

ALTER TABLE places
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES response(id);

ALTER TABLE objects
ADD CONSTRAINT fk_places_id
FOREIGN KEY (places_id) REFERENCES places(id);

ALTER TABLE plan_times
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES response(id);

ALTER TABLE trainGraph
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES response(id);

ALTER TABLE response ADD CONSTRAINT unique_wid UNIQUE (wid);

ALTER TABLE locos ADD CONSTRAINT unique_zlid UNIQUE (zlid);

ALTER TABLE objects ADD CONSTRAINT unique_obj_id_txt UNIQUE (id_obj, obj_txt);

ALTER TABLE personal ADD CONSTRAINT uniquePersonal UNIQUE (fio, id_pers);

ALTER TABLE places ADD CONSTRAINT uniquePlaces UNIQUE (stan1_id, stan2_id);

ALTER TABLE plan_times ADD CONSTRAINT uniquePlanTimes UNIQUE (response_id, dl, kd, nd);

ALTER TABLE techs ADD CONSTRAINT uniqueTechs UNIQUE (tech_id, tech_text, type_tech_name);

ALTER TABLE ways ADD CONSTRAINT uniqueWays UNIQUE (kmk, pkk, way_txt);

ALTER TABLE works ADD CONSTRAINT uniqueWorks UNIQUE (ei_id, ei_name, repair_id);
```
