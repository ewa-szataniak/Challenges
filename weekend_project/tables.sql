CREATE TABLE "parts" (
  "parts_id" SERIAL,
  "part_name" VARCHAR(50),
  "price" NUMERIC(10,2),
  PRIMARY KEY ("parts_id")
);

CREATE TABLE "customer" (
  "customer_id" SERIAL,
  "first_name" VARCHAR(100),
  "last_name" VARCHAR(100),
  "email" VARCHAR(100),
  PRIMARY KEY ("customer_id")
);

CREATE TABLE "sales_invoice" (
  "s_invoice_id" SERIAL,
  "customer_id" INTEGER,
  "inventory_id" INTEGER,
  "salesperson_id" INTEGER,
  PRIMARY KEY ("s_invoice_id"),
  CONSTRAINT "FK_sales_invoice.inventory_id"
    FOREIGN KEY ("inventory_id")
      REFERENCES "customer"("last_name")
);

CREATE TABLE "service" (
  "service_id" SERIAL,
  "service provided" VARCHAR(100),
  "price" NUMERIC(10,2),
  PRIMARY KEY ("service_id")
);

CREATE TABLE "mechanic" (
  "mechanic_id" SERIAL,
  "first_name" VARCHAR(100),
  "last_name" VARCHAR(100),
  "price" NUMERIC(5,2),
  PRIMARY KEY ("mechanic_id")
);

CREATE TABLE "car" (
  "car_id" SERIAL,
  "color" VARCHAR(50),
  "year" INTEGER,
  "make" VARCHAR(100),
  "model" VARCHAR(100),
  "service_history" BOOLEAN,
  "customer_id" INTEGER,
  PRIMARY KEY ("car_id")
);

CREATE TABLE "salesperson" (
  "salesperson_id" SERIAL,
  "first_name" VARCHAR(100),
  "last_name" VARCHAR(100),
  "email" VARCHAR(100),
  "cars_sold" INTEGER,
  PRIMARY KEY ("salesperson_id")
);

CREATE TABLE "service_invoice" (
  "mec_service_id" SERIAL,
  "total_price" NUMERIC(8,2),
  "mechanic_id" INTEGER,
  "parts_id" INTEGER,
  "service_id" INTEGER,
  "customer_id" INTEGER,
  PRIMARY KEY ("mec_service_id"),
  CONSTRAINT "FK_service_invoice.mechanic_id"
    FOREIGN KEY ("mechanic_id")
      REFERENCES "customer"("email"),
  CONSTRAINT "FK_service_invoice.mec_service_id"
    FOREIGN KEY ("mec_service_id")
      REFERENCES "parts"("parts_id")
);

CREATE TABLE "inventory" (
  "inventory_id" SERIAL,
  "price" NUMERIC(10,2),
  "color" VARCHAR(50),
  "year" INTEGER,
  "make" VARCHAR(100),
  "model" VARCHAR(100),
  "service_history" VARCHAR(1000),
  "pre_owned" BOOLEAN,
  "s_invoice_id" INTEGER,
  PRIMARY KEY ("inventory_id")
);
