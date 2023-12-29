select * from russia_losses_equipment rle;
select * from russia_losses_personnel rlp ; 

--1. Total personnel losses over all days:

SELECT SUM(personnel) AS total_personnel_losses
FROM russia_losses_personnel;


--2. Average tank losses per day:

SELECT AVG(tank) AS average_tank_losses
FROM russia_losses_equipment;


--3. Date with the highest helicopter losses:

SELECT date, helicopter
FROM russia_losses_equipment
ORDER BY helicopter DESC
LIMIT 1;


--4. Top 3 days with the most personnel losses:

SELECT date, SUM(personnel) AS total_personnel_losses
FROM russia_losses_personnel
GROUP BY date
ORDER BY total_personnel_losses DESC
LIMIT 3;


--5. Days with personnel losses exceeding 5000:

SELECT date, personnel
FROM russia_losses_personnel
WHERE personnel > 5000;


--6. Cumulative tank losses:

SELECT date, 
       SUM(tank) OVER (ORDER BY date) AS cumulative_tank_losses
FROM russia_losses_equipment;


--7. Date with the highest total losses (personnel + equipment)

SELECT date,
       (SELECT SUM(personnel) FROM russia_losses_personnel WHERE date = re.date)
       + (SELECT SUM(aircraft  + helicopter  + tank  + "APC"  + "field artillery"  + "MRL"  + "military auto"  + "fuel tank"  + drone 
                     + "naval ship"  + "anti-aircraft warfare"  + "special equipment"  + "vehicles and fuel tanks"  
                     + "cruise missiles"  + submarines) 
          FROM russia_losses_equipment WHERE date = re.date) AS total_losses
FROM russia_losses_equipment re
GROUP BY date
ORDER BY total_losses DESC
LIMIT 1;


--8. Days with personnel losses higher than the daily average:

SELECT date, personnel
FROM russia_losses_personnel
WHERE personnel > (SELECT AVG(personnel) FROM russia_losses_personnel);


--9. Top 3 days with the most fuel tank losses

SELECT date, SUM("fuel tank") AS total_fuel_tank_losses
FROM russia_losses_equipment
GROUP BY date
ORDER BY total_fuel_tank_losses DESC
LIMIT 5;


--10. Retrieve dates with equipment losses in the 'Donetsk':

SELECT date, "greatest losses direction" 
FROM russia_losses_equipment
where "greatest losses direction" = 'Donetsk';


