CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    ,name STRING NOT NULL
    ,num_order INTEGER NOT NULL
);

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    ,title STRING NOT NULL
    ,description STRING
    ,id_category INTEGER NOT NULL
    ,FOREIGN KEY(id_category) REFERENCES category(id)
);
