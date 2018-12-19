INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO temperature (device_id, sensor_reading, created)
VALUES
  (1, 11.1, '2018-01-01 00:00:00'),
  (2, 22.2, '2018-02-02 00:00:00'),
  (3, 33.3, '2018-03-03 00:00:00');

INSERT INTO device (owner_id, description)
VALUES
  (1, 'test sensor 1'),
  (1, 'test sensor 2'),
  (2, 'test sensor 3');