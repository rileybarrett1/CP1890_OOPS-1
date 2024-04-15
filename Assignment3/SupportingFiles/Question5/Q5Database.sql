CREATE TABLE "Sales" (
    "ID"         INTEGER NOT NULL,
    "amount"     REAL NOT NULL,
    "salesDate"  TEXT NOT NULL,
    "region"     TEXT NOT NULL,
    PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE "Region" (
    "code" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    PRIMARY KEY("code")
);
CREATE TABLE "ImportedFiles" (
    "fileName"   TEXT NOT NULL,
    PRIMARY KEY("fileName")
);