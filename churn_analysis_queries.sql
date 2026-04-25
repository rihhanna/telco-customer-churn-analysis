
-- ============================================
-- TELCO CUSTOMER CHURN ANALYSIS
-- SQL QUERIES FOR PORTFOLIO
-- ============================================

-- 1. Overall churn rate
SELECT 
    COUNT(*) as total_customers,
    SUM(Churn) as churned_customers,
    ROUND(100.0 * SUM(Churn) / COUNT(*), 2) as churn_rate_percent
FROM customers;

-- 2. Churn rate by contract type
SELECT 
    Contract,
    COUNT(*) as total_customers,
    SUM(Churn) as churned_customers,
    ROUND(100.0 * SUM(Churn) / COUNT(*), 2) as churn_rate_percent
FROM customers
GROUP BY Contract
ORDER BY churn_rate_percent DESC;

-- 3. Churn rate by payment method
SELECT 
    PaymentMethod,
    COUNT(*) as total_customers,
    SUM(Churn) as churned_customers,
    ROUND(100.0 * SUM(Churn) / COUNT(*), 2) as churn_rate_percent
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate_percent DESC;

-- 4. High-risk customer segment
SELECT 
    COUNT(*) as high_risk_customers,
    SUM(Churn) as churned_customers,
    ROUND(100.0 * SUM(Churn) / COUNT(*), 2) as churn_rate_percent
FROM customers
WHERE Contract = 'Month-to-month' 
  AND PaymentMethod = 'Electronic check';

-- 5. Churn rate by tenure group
SELECT 
    CASE 
        WHEN tenure <= 12 THEN '0-12 months'
        WHEN tenure <= 24 THEN '13-24 months'
        WHEN tenure <= 48 THEN '25-48 months'
        WHEN tenure <= 72 THEN '49-72 months'
        ELSE '73+ months'
    END as tenure_group,
    COUNT(*) as total_customers,
    SUM(Churn) as churned_customers,
    ROUND(100.0 * SUM(Churn) / COUNT(*), 2) as churn_rate_percent
FROM customers
GROUP BY tenure_group
ORDER BY churn_rate_percent DESC;
