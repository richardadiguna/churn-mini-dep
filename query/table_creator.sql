CREATE TABLE churn_correlation_matrix_1(
    report_date VARCHAR(10), kyc FLOAT, days_since_reg FLOAT, reg_with_promo FLOAT,
    android_user FLOAT, ios_user FLOAT, topup_freq FLOAT,
    withdraw_freq FLOAT, p2p_freq FLOAT, lucky_money_send_freq FLOAT,
    lucky_money_rec_freq FLOAT, offline_merchant FLOAT, offline_trx FLOAT,
    online_merchant FLOAT, online_trx FLOAT, issue_freq FLOAT,
    issue_rate FLOAT, redeem_freq FLOAT, redeem_rate FLOAT,
    bbm_user FLOAT, tix_user FLOAT, skywalker_user FLOAT,
    other_platform_user FLOAT, bukalapak_user FLOAT, bind_cc FLOAT,
    bind_dc FLOAT, week_active_rate FLOAT, reg_site_BBM FLOAT, 
    reg_site_Bukalapak FLOAT, reg_site_LAZADA FLOAT, reg_site_MAIN_APP FLOAT,
    reg_site_Other FLOAT, reg_site_Parkee FLOAT, reg_site_RAMAYANA FLOAT,
    reg_site_Reservasi FLOAT, reg_site_TIXid FLOAT, reg_site_UC FLOAT,
    reg_site_Upoint FLOAT, reg_site_Vidio FLOAT, churn FLOAT
);

CREATE TABLE churn_confusion_matrix_1(
    report_date VARCHAR(10),
    non_churn BIGINT,
    churn BIGINT
);

CREATE TABLE churn_data_composition_1(
    report_date VARCHAR(10),
    churn BIGINT,
    count BIGINT
);

CREATE TABLE churn_prediction_result(
    report_date VARCHAR(10)
    user_id VARCHAR(22),
    prediction FLOAT
)
