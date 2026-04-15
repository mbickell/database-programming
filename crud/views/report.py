from utils import execute


def get_total_consumption(cursor):
    execute("""
SELECT 
    p.name,
    SUM(e.value) AS total_kwh
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name;
          """)

    data = cursor.fetchall()
    return data


def get_most_energy_intensive(cursor):
    execute("""
SELECT 
    p.name,
    SUM(e.value) AS total_kwh
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name
ORDER BY total_kwh DESC
LIMIT 1;
          """)

    data = cursor.fetchone()
    print(data)


def get_average_daily(cursor):
    execute("""
SELECT 
    p.name,
    AVG(e.value) AS avg_kwh
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name;
        """)

    data = cursor.fetchall()
    print(data)


def get_full_report(cursor):
    execute("""
SELECT 
    p.name,
    SUM(e.value) AS total,
    AVG(e.value) AS avg_daily,
    MAX(e.value) AS max_daily
FROM electricity e
JOIN property p ON p.id = e.property
GROUP BY p.name;
      """)

    data = cursor.fetchall()
    print(data)


def get_detected_anomalies(cursor):
    execute("""
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
      """)

    data = cursor.fetchall()
    print(data)


def get_highest_daily(cursor):
    execute("""
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
      """)

    data = cursor.fetchall()
    print(data)


def get_daily_ranking(cursor):
    execute("""
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
      """)

    data = cursor.fetchall()
    print(data)


def get_3_day_moving_average(cursor):
    execute("""
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
      """)

    data = cursor.fetchall()
    print(data)
