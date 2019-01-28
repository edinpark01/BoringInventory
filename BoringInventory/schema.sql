DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS cabinet_info;
DROP TABLE IF EXISTS cabinets;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE cabinet_info (
  id TEXT PRIMARY KEY,
  make TEXT,
  model TEXT
);

CREATE TABLE cabinets (
  rowid INTEGER PRIMARY KEY AUTOINCREMENT,
  cabinet TEXT,
  location INTEGER,
  hostname TEXT,
  manufacturer TEXT,
  model TEXT,
  description TEXT,
  asset_tag TEXT,
  serial TEXT,
  owners TEXT,
  notes TEXT,
  FOREIGN KEY (cabinet) REFERENCES cabinet_info(id)
);

INSERT INTO cabinet_info (id, make, model) VALUES ('test1', 'HP', 'zoom3');
INSERT INTO cabinet_info (id, make, model) VALUES ('test2', 'DELL', 'pinga3');
INSERT INTO cabinet_info (id, make, model) VALUES ('test3', 'LIMAO', 'caipirinha');

INSERT INTO
  cabinets (cabinet, location, hostname, manufacturer, model, description, asset_tag, serial, owners, notes)
VALUES
       ('test1', 25, 'NPKDSV8001', 'HP', 'HP ProLiant', 'Oh boy', '2011234', 'ADV123', 'John Doe', 'Swithing owners soon');
INSERT INTO
  cabinets (cabinet, location, hostname, manufacturer, model, description, asset_tag, serial, owners)
VALUES
       ('test2', 25, 'NPKDSV8002', 'Panasonic', 'Lumen', 'Oh girl', '2011232', 'TGH713', 'Mary Doe');
INSERT INTO
  cabinets (cabinet, location, hostname, manufacturer, model, description, asset_tag, serial, owners)
VALUES
       ('test3', 25, 'NPKDSV8007', 'Cisco', 'Cabecao', 'Oh guys', '20145634', 'EFD456', 'Junior Doe');