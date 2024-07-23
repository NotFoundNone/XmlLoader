# XmlLoader

XmlLoader is a project designed to handle XML data loading into a relational database.

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
CREATE TABLE IF NOT EXISTS apvo2_response (
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

COMMENT ON COLUMN apvo2_response.allAccepted IS 'Признак «Все согласования выполнены»';
COMMENT ON COLUMN apvo2_response.dor_kod IS 'Код дороги (АС ЦНСИ. Справочник «Железные дороги»)';
COMMENT ON COLUMN apvo2_response.dt_corr IS 'Дата и время корректировки «окна» (Формат «yyyy-MM-dd HH:mm»)';
COMMENT ON COLUMN apvo2_response.duId IS 'ИД диспетчерского участка в формате ЦНСИ (АС ЦНСИ. Справочник «Диспетчеркие участки»)';
COMMENT ON COLUMN apvo2_response.duName IS 'Наименование диспетчерского участка';
COMMENT ON COLUMN apvo2_response.flg_volt IS 'Признак необходимости снятия напряжения (1=Требуется снять напряжение)';
COMMENT ON COLUMN apvo2_response.flg_wnd IS 'Не используется';
COMMENT ON COLUMN apvo2_response.idMa IS 'Идентификатор участка ремонта месячного планирования';
COMMENT ON COLUMN apvo2_response.idTuch IS 'Идентификатор участка ремонта годового планирования';
COMMENT ON COLUMN apvo2_response.id_overtime IS 'ИД причины передержки «окна» (АС АПВО-2. Справочник причин срывов, отмен и передержек «окон». Группа причин «Передержка окна на этапе выполнения»)';
COMMENT ON COLUMN apvo2_response.id_overtime_sl IS 'ИД службы, виновной в передержке «окна» (АС АПВО-2. Справочник «Службы, дирекции»)';
COMMENT ON COLUMN apvo2_response.id_reject IS 'ИД причины отмены «окна» при планировании (АС АПВО-2. Справочник причин срывов, отмен и передержек «окон». Группа причин «Несогласование заявки при планировании»)';
COMMENT ON COLUMN apvo2_response.id_reject_fact IS 'ИД причины срыва или отмены «окна» при фактическом исполнении (АС АПВО-2. Справочник причин срывов, отмен и передержек «окон». Группа причин «Причины срыва»)';
COMMENT ON COLUMN apvo2_response.id_reject_fact_sl IS 'ИД службы, виновной в срыве «окна» (АС АПВО-2. Справочник «Службы, дирекции»)';
COMMENT ON COLUMN apvo2_response.overtime IS 'Время передержки «окна», минут';
COMMENT ON COLUMN apvo2_response.pred_id IS 'ИД предприятия-исполнителя (АС ЦНСИ, справочник предприятий)';
COMMENT ON COLUMN apvo2_response.pred_name IS 'Наименование предприятия-исполнителя';
COMMENT ON COLUMN apvo2_response.status_fact IS 'Статус фактического исполнения (0 – нет данных, 1 – окно выполняется, 2 – окно завершено, 3 – окно сорвано)';
COMMENT ON COLUMN apvo2_response.status_pl IS 'Статус планирования (0 – заявка не рассмотрена, 1 – заявка утверждена «по согласованию ДНЦ», 2 – заявка согласована, 3 – заявка отклонена)';
COMMENT ON COLUMN apvo2_response.timeVoltage IS 'Продолжительность снятия напряжения, минут';
COMMENT ON COLUMN apvo2_response.wid IS 'Идентификатор заявки на работу в «окно»';

COMMENT ON TABLE apvo2_response IS 'Таблица с данными о выполненных и планируемых окнах';

CREATE TABLE apvo2_personal (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES apvo2_response(id),
    fio TEXT,
    id_otv INTEGER,
    id_pers INTEGER,
    pred_id INTEGER
);

CREATE TABLE IF NOT EXISTS apvo2_places (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES apvo2_response(id),
    pereg_ms_id INTEGER,
    place_type INTEGER,
    stan1_id INTEGER,
    stan2_id INTEGER
);

COMMENT ON COLUMN apvo2_places.pereg_ms_id IS 'ИД межстанционного перегона (АС ЦНСИ, справочник межстанционных перегонов)';
COMMENT ON COLUMN apvo2_places.place_type IS 'Код типа места проведения (1 – на перегоне, 2 – на станции)';
COMMENT ON COLUMN apvo2_places.stan1_id IS 'ИД станции 1 (АС ЦНСИ, справочник раздельных пунктов)';
COMMENT ON COLUMN apvo2_places.stan2_id IS 'ИД станции 2 (АС ЦНСИ, справочник раздельных пунктов)';

COMMENT ON TABLE apvo2_places IS 'Таблица с данными о местах проведения работ';

CREATE TABLE IF NOT EXISTS apvo2_objects (
    id SERIAL PRIMARY KEY,
    places_id INTEGER REFERENCES apvo2_places(id),
    id_obj INTEGER,
    id_obj_type INTEGER,
    obj_txt TEXT
);

COMMENT ON COLUMN apvo2_objects.id_obj IS 'ИД объекта (АС АПВО-2. Справочник типов объектов)';
COMMENT ON COLUMN apvo2_objects.id_obj_type IS 'Тип объекта';
COMMENT ON COLUMN apvo2_objects.obj_txt IS 'Наименование объекта';

COMMENT ON TABLE apvo2_objects IS 'Таблица с данными об объектах';

CREATE TABLE IF NOT EXISTS apvo2_ways (
    id SERIAL PRIMARY KEY,
    places_id INTEGER REFERENCES apvo2_places(id),
    kmk INTEGER,
    kmn INTEGER,
    pkk INTEGER,
    pkn INTEGER,
    way_id INTEGER,
    way_txt TEXT,
    way_type INTEGER
);

COMMENT ON COLUMN apvo2_ways.kmk IS 'Километр конца работ';
COMMENT ON COLUMN apvo2_ways.kmn IS 'Километр начала работ';
COMMENT ON COLUMN apvo2_ways.pkk IS 'Пикет конца работ';
COMMENT ON COLUMN apvo2_ways.pkn IS 'Пикет начала работ';
COMMENT ON COLUMN apvo2_ways.way_id IS 'ИД пути (АС ЦНСИ, справочник путей станций)';
COMMENT ON COLUMN apvo2_ways.way_txt IS 'Наименование пути';
COMMENT ON COLUMN apvo2_ways.way_type IS 'Тип пути (1 – Главный путь, 2 – Станционный путь)';

COMMENT ON TABLE apvo2_ways IS 'Таблица с данными о путях';

CREATE TABLE IF NOT EXISTS apvo2_plan_times (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES apvo2_response(id),
    dl INTEGER,
    kd TIMESTAMP,
    nd TIMESTAMP
);

COMMENT ON COLUMN apvo2_plan_times.dl IS 'Продолжительность «окна» в минутах';
COMMENT ON COLUMN apvo2_plan_times.kd IS 'Дата и время окончания «окна»';
COMMENT ON COLUMN apvo2_plan_times.nd IS 'Дата и время начала «окна»';

COMMENT ON TABLE apvo2_plan_times IS 'Таблица с плановыми временами «окна»';


CREATE TABLE IF NOT EXISTS apvo2_trainGraph (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES apvo2_response(id),
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

COMMENT ON COLUMN apvo2_trainGraph.cancelEvenCargo IS 'Съем четных грузовых поездов';
COMMENT ON COLUMN apvo2_trainGraph.cancelEvenPassanger IS 'Съем четных пассажирских поездов';
COMMENT ON COLUMN apvo2_trainGraph.cancelEvenSuburban IS 'Съем четных пригородных поездов';
COMMENT ON COLUMN apvo2_trainGraph.cancelOddCargo IS 'Съем нечетных грузовых поездов';
COMMENT ON COLUMN apvo2_trainGraph.cancelOddPassanger IS 'Съем нечетных пассажирских поездов';
COMMENT ON COLUMN apvo2_trainGraph.cancelOddSuburban IS 'Съем нечетных пригородных поездов';
COMMENT ON COLUMN apvo2_trainGraph.changesEvenCargo IS 'Изменение расписания четных грузовых поездов';
COMMENT ON COLUMN apvo2_trainGraph.changesEvenPassanger IS 'Изменение расписания четных пассажирских поездов';
COMMENT ON COLUMN apvo2_trainGraph.changesEvenSuburban IS 'Изменение расписания четных пригородных поездов';
COMMENT ON COLUMN apvo2_trainGraph.changesOddCargo IS 'Изменение расписания нечетных грузовых поездов';
COMMENT ON COLUMN apvo2_trainGraph.changesOddPassanger IS 'Изменение расписания нечетных пассажирских поездов';
COMMENT ON COLUMN apvo2_trainGraph.changesOddSuburban IS 'Изменение расписания нечетных пригородных поездов';
COMMENT ON COLUMN apvo2_trainGraph.delayEvenCargoCount IS 'Задержка четных грузовых поездов, количество';
COMMENT ON COLUMN apvo2_trainGraph.delayEvenCargoTime IS 'Задержка четных грузовых поездов, время, минут';
COMMENT ON COLUMN apvo2_trainGraph.delayEvenPassangerCount IS 'Задержка четных пассажирских поездов, количество';
COMMENT ON COLUMN apvo2_trainGraph.delayEvenPassangerTime IS 'Задержка четных пассажирских поездов, время, минут';
COMMENT ON COLUMN apvo2_trainGraph.delayEvenSuburbanCount IS 'Задержка четных пригородных поездов, количество';
COMMENT ON COLUMN apvo2_trainGraph.delayEvenSuburbanTime IS 'Задержка четных пригородных поездов, время, минут';
COMMENT ON COLUMN apvo2_trainGraph.delayOddCargoCount IS 'Задержка нечетных грузовых поездов, количество';
COMMENT ON COLUMN apvo2_trainGraph.delayOddCargoTime IS 'Задержка нечетных грузовых поездов, время, минут';
COMMENT ON COLUMN apvo2_trainGraph.delayOddPassangerCount IS 'Задержка нечетных пассажирских поездов, количество';
COMMENT ON COLUMN apvo2_trainGraph.delayOddPassangerTime IS 'Задержка нечетных пассажирских поездов, время, минут';
COMMENT ON COLUMN apvo2_trainGraph.delayOddSuburbanCount IS 'Задержка нечетных пригородных поездов, количество';
COMMENT ON COLUMN apvo2_trainGraph.delayOddSuburbanTime IS 'Задержка нечетных пригородных поездов, время, минут';
COMMENT ON COLUMN apvo2_trainGraph.sizeMovEvenCargo IS 'Размер движения четных грузовых поездов';
COMMENT ON COLUMN apvo2_trainGraph.sizeMovEvenPassanger IS 'Размер движения четных пассажирских поездов';
COMMENT ON COLUMN apvo2_trainGraph.sizeMovEvenSuburban IS 'Размер движения четных пригородных поездов';
COMMENT ON COLUMN apvo2_trainGraph.sizeMovOddCargo IS 'Размер движения нечетных грузовых поездов';
COMMENT ON COLUMN apvo2_trainGraph.sizeMovOddPassanger IS 'Размер движения нечетных пассажирских поездов';
COMMENT ON COLUMN apvo2_trainGraph.sizeMovOddSuburban IS 'Размер движения нечетных пригородных поездов';

COMMENT ON TABLE apvo2_trainGraph IS 'Таблица с данными о графике поездов';

CREATE TABLE IF NOT EXISTS apvo2_works (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES apvo2_response(id),
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

COMMENT ON COLUMN apvo2_works.ei_id IS 'Идентификатор единицы измерения (АС ЦНСИ, справочник единиц измерения)';
COMMENT ON COLUMN apvo2_works.ei_name IS 'Наименование единицы измерения';
COMMENT ON COLUMN apvo2_works.fact_added IS 'Признак добавления работы при фактическом исполнении (True – работа не планировалась, добавлена при фактическом исполнении)';
COMMENT ON COLUMN apvo2_works.fact_v IS 'Фактический объем работы';
COMMENT ON COLUMN apvo2_works.id_reason IS 'Идентификатор причины отмены работы (АС АПВО-2. Справочник причин срывов, отмен и передержек "окон". Раздел "Причины сокращения объемов работ при фактическом исполнении")';
COMMENT ON COLUMN apvo2_works.plan_v IS 'Плановый объем работы';
COMMENT ON COLUMN apvo2_works.repair_id IS 'Идентификатор вида ремонта (АС ЦНСИ, справочник видов ремонта)';
COMMENT ON COLUMN apvo2_works.repair_name IS 'Наименование вида ремонта';
COMMENT ON COLUMN apvo2_works.work_id IS 'Идентификатор вида работы (АС АПВО-2, справочник видов работ)';
COMMENT ON COLUMN apvo2_works.work_name IS 'Наименование вида работы';

COMMENT ON TABLE apvo2_works IS 'Таблица с описанием работ в "окно"';

CREATE TABLE apvo2_locos (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES apvo2_response(id),
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

CREATE TABLE apvo2_techs (
    id SERIAL PRIMARY KEY,
    response_id INTEGER REFERENCES apvo2_response(id),
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


ALTER TABLE apvo2_personal
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES apvo2_response(id);

ALTER TABLE apvo2_places
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES apvo2_response(id);

ALTER TABLE apvo2_objects
ADD CONSTRAINT fk_places_id
FOREIGN KEY (places_id) REFERENCES apvo2_places(id);

ALTER TABLE apvo2_plan_times
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES apvo2_response(id);

ALTER TABLE apvo2_trainGraph
ADD CONSTRAINT fk_response_id
FOREIGN KEY (response_id) REFERENCES apvo2_response(id);

ALTER TABLE apvo2_response ADD CONSTRAINT unique_wid UNIQUE (wid);

ALTER TABLE apvo2_locos ADD CONSTRAINT unique_zlid UNIQUE (zlid);

ALTER TABLE apvo2_objects ADD CONSTRAINT unique_obj_id_txt UNIQUE (id_obj, obj_txt);

ALTER TABLE apvo2_personal ADD CONSTRAINT uniquePersonal UNIQUE (fio, id_pers);

ALTER TABLE apvo2_places ADD CONSTRAINT uniquePlaces UNIQUE (stan1_id, stan2_id);

ALTER TABLE apvo2_plan_times ADD CONSTRAINT uniquePlanTimes UNIQUE (response_id, dl, kd, nd);

ALTER TABLE apvo2_techs ADD CONSTRAINT uniqueTechs UNIQUE (tech_id, tech_text, type_tech_name);

ALTER TABLE apvo2_ways ADD CONSTRAINT uniqueWays UNIQUE (kmk, pkk, way_txt);

ALTER TABLE apvo2_works ADD CONSTRAINT uniqueWorks UNIQUE (ei_id, ei_name, repair_id);
```
