-- Coursework Part C: Task 5 OLAP Queries

-- 5.1 Slice: Lotus Care Colombo clinic branch
SELECT 
    c.clinic_name,
    dt.month,
    dt.month_name,
    COUNT(f.appointment_id) AS total_appointments,
    ROUND(AVG(f.wait_minutes), 2) AS avg_wait_minutes,
    ROUND(AVG(f.consultation_minutes), 2) AS avg_consultation_minutes,
    SUM(f.fee) AS total_revenue_lkr
FROM fact_appointment f
JOIN dim_clinic c ON f.clinic_key = c.clinic_key
JOIN dim_date dt ON f.date_key = dt.date_key
WHERE c.clinic_id = 'C01'
GROUP BY c.clinic_name, dt.month, dt.month_name
ORDER BY dt.month;

-- 5.2 Dice: Cardiology and Neurology in Western and Central (Q1 and Q2)
SELECT 
    c.province,
    c.clinic_name,
    d.specialty,
    dt.quarter_name,
    COUNT(f.appointment_id) AS appointment_count,
    SUM(f.fee) AS total_fee_lkr,
    ROUND(AVG(f.wait_minutes), 2) AS avg_wait_minutes
FROM fact_appointment f
JOIN dim_clinic c ON f.clinic_key = c.clinic_key
JOIN dim_doctor d ON f.doctor_key = d.doctor_key
JOIN dim_date dt ON f.date_key = dt.date_key
WHERE d.specialty IN ('Cardiology', 'Neurology')
  AND dt.quarter IN (1, 2)
  AND c.province IN ('Western', 'Central')
GROUP BY c.province, c.clinic_name, d.specialty, dt.quarter_name
ORDER BY c.province, c.clinic_name, d.specialty, dt.quarter_name;

-- 5.3 Roll Up: Hierarchy from Doctor to Specialty to Grand Total
SELECT 
    COALESCE(d.specialty, '--> GRAND TOTAL') AS specialty,
    COALESCE(d.doctor_name, '-> Subtotal') AS doctor_name,
    COUNT(f.appointment_id) AS appointment_count,
    SUM(f.consultation_minutes) AS total_consultation_minutes,
    ROUND(AVG(f.consultation_minutes), 2) AS avg_consultation_minutes,
    SUM(f.fee) AS total_fee_lkr
FROM fact_appointment f
JOIN dim_doctor d ON f.doctor_key = d.doctor_key
GROUP BY ROLLUP(d.specialty, d.doctor_name)
ORDER BY d.specialty NULLS LAST, d.doctor_name NULLS LAST;

-- 5.4 Drill Down: Quarterly summary down to Q3 monthly performance
-- Query 1: Quarterly summary
SELECT 
    dt.year,
    dt.quarter_name,
    COUNT(f.appointment_id) AS total_appointments,
    SUM(f.fee) AS total_fee_lkr,
    ROUND(AVG(f.wait_minutes), 2) AS avg_wait_minutes,
    ROUND(AVG(f.consultation_minutes), 2) AS avg_consultation_minutes
FROM fact_appointment f
JOIN dim_date dt ON f.date_key = dt.date_key
GROUP BY dt.year, dt.quarter, dt.quarter_name
ORDER BY dt.quarter;

-- Query 2: Q3 monthly breakdown
SELECT 
    dt.quarter_name,
    dt.month,
    dt.month_name,
    COUNT(f.appointment_id) AS total_appointments,
    SUM(f.fee) AS total_fee_lkr,
    ROUND(AVG(f.wait_minutes), 2) AS avg_wait_minutes,
    ROUND(AVG(f.consultation_minutes), 2) AS avg_consultation_minutes
FROM fact_appointment f
JOIN dim_date dt ON f.date_key = dt.date_key
WHERE dt.quarter = 3
GROUP BY dt.quarter_name, dt.month, dt.month_name
ORDER BY dt.month;

-- 5.5 Pivot: Clinic quarterly revenue cross-tabulation
SELECT 
    c.clinic_id,
    c.clinic_name,
    c.city,
    SUM(CASE WHEN dt.quarter = 1 THEN f.fee ELSE 0 END) AS q1_revenue_lkr,
    SUM(CASE WHEN dt.quarter = 2 THEN f.fee ELSE 0 END) AS q2_revenue_lkr,
    SUM(CASE WHEN dt.quarter = 3 THEN f.fee ELSE 0 END) AS q3_revenue_lkr,
    SUM(CASE WHEN dt.quarter = 4 THEN f.fee ELSE 0 END) AS q4_revenue_lkr,
    SUM(f.fee) AS total_annual_revenue_lkr
FROM fact_appointment f
JOIN dim_clinic c ON f.clinic_key = c.clinic_key
JOIN dim_date dt ON f.date_key = dt.date_key
GROUP BY c.clinic_id, c.clinic_name, c.city
ORDER BY c.clinic_id;
