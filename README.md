# First part
## Property.py
- list properties
- add properties
- delete properties

Terminal program with options (L - list, A - add, D - delete)

Needs more error handling

## Stat.py
- Which property - code
  - Min?
  - Max?
  - Avg?
  - Total?

- Also attach datetime to min and max

# Second Part
## Insert Electricity data

- Programattically
- Use a command line argument to get property code
  - Check if code exists in the property table
  - yes?
    - exit
  - no?
    - Insert property
    - get id
    - read electricty json
    - insert data

## Group by
- Group the electricity stats by property type
  - Use SQL

- Extensions
  - Some things overall?????

# Third Part

Add these sql methods:
## Task 1: Total Consumption per Property

```SQL
SELECT 
    p.name,
    SUM(e.value) AS total_kwh
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name;
```

## Task 2: Most Energy-Intensive Property

```SQL
SELECT 
    p.name,
    SUM(e.value) AS total_kwh
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name
ORDER BY total_kwh DESC
LIMIT 1;
```

## Task 3: Average Daily Consumption

```SQL
SELECT 
    p.name,
    AVG(e.value) AS avg_kwh
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name;
```

## Task 3a: Full Report

total consumption
average daily consumption
max daily consumption

```SQL
SELECT 
    p.name,
    SUM(e.value) AS total,
    AVG(e.value) AS avg_daily,
    MAX(e.value) AS max_daily
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name;
```

## Task 4: Detect Anomalies (2× average daily usage)

```SQL
SELECT 
    p.name,
    e.timestamp,
    e.value
FROM electricity e
JOIN property p ON p.id = e.property
WHERE e.value > (
    SELECT 2 * AVG(e2.value)
    FROM electricity e2
    WHERE e2.property = e.property
);
```


## Task 5: Highest Daily Consumption (and Date)

```SQL
SELECT 
    p.name,
    e.timestamp AS day,
    e.value
FROM electricity e
JOIN property p ON p.id = e.property
WHERE (e.property, e.value) IN (
    SELECT 
        property,
        MAX(value)
    FROM electricity
    GROUP BY property
);
```

OR

```SQL
SELECT 
    p.name,
    e.timestamp AS day,
    e.value
FROM electricity e
JOIN property p ON p.id = e.property
JOIN (
    SELECT property, MAX(value) AS max_value
    FROM electricity
    GROUP BY property
) m 
ON e.property = m.property 
AND e.value = m.max_value;
```


## Task 6: Daily Ranking

```SQL
SELECT 
    e.timestamp,
    p.name,
    e.value,
    RANK() OVER (
        PARTITION BY e.timestamp
        ORDER BY e.value DESC
    ) AS rank_pos
FROM electricity e
JOIN property p ON p.id = e.property
ORDER BY e.timestamp, rank_pos;
```


## Task 7: 3-Day Moving Average

```SQL
SELECT 
    p.name,
    e.timestamp,
    AVG(e.value) OVER (
        PARTITION BY e.property
        ORDER BY e.timestamp
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS avg_3_day
FROM electricity e
JOIN property p ON p.id = e.property
ORDER BY p.name, e.timestamp;
```

# TODO

- Remove id usage from stats cli

# Useful queries

## Get total energy price used by property day
```SQL
SELECT 
    pr.name, 
    DATE(e.timestamp), 
    e.value, 
    p.price_eur_mwhe, 
    CAST((e.value * p.price_eur_mwhe * 0.001) AS DECIMAL(15,2)) as total
FROM electricity e
JOIN prices p ON p.iso3_code = "FIN" AND p.date = DATE(e.timestamp)
JOIN property pr ON pr.id = e.property
```
With view:
```SQL
SELECT 
    pr.name, 
    DATE(e.timestamp), 
    e.value, 
    p.price_eur_mwhe, 
    CAST((e.value * p.price_eur_mwhe * 0.001) AS DECIMAL(15,2)) as total
FROM electricity e
JOIN fin_prices_2025 p ON p.date = DATE(e.timestamp)
JOIN property pr ON pr.id = e.property
```
