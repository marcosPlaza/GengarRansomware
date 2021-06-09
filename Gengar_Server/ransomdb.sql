PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE infected_hosts(ip text primary key, key text not null, date text not null, state text);
INSERT INTO infected_hosts VALUES('192.168.1.107','b''sooFE--hT8BcnER05RjB1KVRrT0p3ZkN7yGlTxr1HEo=''','16/05/21','paid');
COMMIT;
