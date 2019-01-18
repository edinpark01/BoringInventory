DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS cabinet_info;
DROP TABLE IF EXISTS cabinets;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT PRIMARY KEY UNIQUE NOT NULL ,
  password TEXT NOT NULL
);

CREATE TABLE cabinet_info (
  id TEXT PRIMARY KEY,
  make TEXT,
  model TEXT
);

CREATE TABLE cabinets (
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

