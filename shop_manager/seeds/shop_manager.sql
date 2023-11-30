DROP TABLE IF EXISTS "public"."products_orders";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."products_orders" (
    "product_id" int4,
    "order_id" int4,
    "order_quantity" INTEGER
);

DROP TABLE IF EXISTS "public"."products";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."products" (
    "id" SERIAL,
    "name" text,
    "unit_price" float,
    "quantity" INTEGER,
    PRIMARY KEY ("id")
);



DROP TABLE IF EXISTS "public"."orders";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."orders" (
    "id" SERIAL,
    "customer_name" text,
    "order_date" date,
    PRIMARY KEY ("id")
);

INSERT INTO "public"."products" ("name", "unit_price", "quantity") VALUES
('product1', 1.99, 101),
('product2', 2.99, 102),
('product3', 3.99, 103),
('product4', 4.99, 104),
('product5', 5.99, 105);

INSERT INTO "public"."orders" ("customer_name", "order_date") VALUES
('customer1', '2023-01-01'),
('customer2', '2023-01-02'),
('customer3', '2023-01-03'),
('customer4', '2023-01-04');

INSERT INTO "public"."products_orders" ("product_id", "order_id", "order_quantity") VALUES
(1, 1, 1),
(1, 2, 1),
(2, 2, 1),
(2, 3, 1),
(3, 3, 1),
(3, 4, 1),
(4, 4, 1),
(4, 1, 1),
(5, 1, 1),
(5, 3, 1);

ALTER TABLE "public"."products_orders" ADD FOREIGN KEY ("product_id") REFERENCES "public"."products"("id");
ALTER TABLE "public"."products_orders" ADD FOREIGN KEY ("order_id") REFERENCES "public"."orders"("id");
