-- 1. В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
-- Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции

START TRANSACTION;
INSERT INTO sample.users (SELECT * FROM shop.users WHERE shop.users.id = 1);
COMMIT;

-- 2. Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название 
-- каталога name из таблицы catalogs.

CREATE OR REPLACE VIEW v AS 
  SELECT products.name AS p_name, catalogs.name AS c_name 
    FROM products,catalogs 
      WHERE products.catalog_id = catalogs.id;