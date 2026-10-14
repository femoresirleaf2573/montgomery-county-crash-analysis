-- 1. Total number of crashes
SELECT COUNT(*) AS total_crashes
FROM crashes;

-- 2. Crashes by severity
SELECT
    "ACRS Report Type" AS severity,
    COUNT(*) AS total
FROM crashes
GROUP BY "ACRS Report Type"
ORDER BY total DESC;

-- 3. Fatal crashes only
SELECT COUNT(*) AS fatal_crashes
FROM crashes
WHERE "ACRS Report Type" = 'Fatal Crash';

-- 4. Crashes by year
SELECT
    SUBSTR("Crash Date/Time", 7, 4) AS year,
    COUNT(*) AS total_crashes
FROM crashes
GROUP BY year
ORDER BY year;

-- 5. Top 10 weather conditions recorded during crashes
SELECT
    Weather,
    COUNT(*) AS total_crashes
FROM crashes
WHERE Weather IS NOT NULL AND Weather != ''
GROUP BY Weather
ORDER BY total_crashes DESC
LIMIT 10;

-- 6. Standardize weather categories
SELECT
    CASE
        WHEN UPPER(Weather) = 'CLEAR' THEN 'Clear'
        WHEN UPPER(Weather) IN ('RAIN', 'RAINING') THEN 'Rain'
        WHEN UPPER(Weather) = 'CLOUDY' THEN 'Cloudy'
        WHEN UPPER(Weather) = 'SNOW' THEN 'Snow'
        ELSE Weather
    END AS weather_category,
    COUNT(*) AS total_crashes
FROM crashes
GROUP BY weather_category
ORDER BY total_crashes DESC
LIMIT 15;

-- 7. Fatal crashes by weather condition
SELECT
    UPPER(Weather) AS weather,
    COUNT(*) AS fatal_crashes
FROM crashes
WHERE "ACRS Report Type" = 'Fatal Crash'
GROUP BY UPPER(Weather)
ORDER BY fatal_crashes DESC
LIMIT 10;