ALTER TABLE car
ADD COLUMN is_serviced BOOLEAN;

CREATE OR REPLACE PROCEDURE is_serviced()
LANGUAGE plpgsql
BEGIN
    UPDATE "car"
    SET is_serviced = true 
    FROM service
    WHERE "car".car_id = service.car_id
    AND service_history = false
    AND service_provided = 'Oil Change';

    COMMIT;
END;
$$

CALL is_serviced();