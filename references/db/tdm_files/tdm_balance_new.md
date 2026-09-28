# 涉税科目余额-tdm_balance_new

## 单据体-子表 t_tdm_account_balance

- **表名称：** 单据体-子表
- **表名：** t_tdm_account_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclosinglocalcurrency | 期末余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额本位币 |
| 3 | fsumdebitamount | 本年累计借方 | numeric | 23 | 10 | √ | 0 | 本年累计借方 |
| 4 | fopeninglocalcurrency | 期初余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额本位币 |
| 5 | fdebitlocalcurrency | 本期发生额借方 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额借方 |
| 6 | faccountdimension | 核算维度值 | varchar | 600 |  |  | ' ' | 核算维度值 |
| 7 | fsumcreditamount | 本年累计贷方 | numeric | 23 | 10 | √ | 0 | 本年累计贷方 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcreditlocalcurrency | 本期发生额贷方 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额贷方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_account_balance_fk |  | fid |
| 2 | t_tdm_account_balance_pkey |  | fentryid |

---

## 涉税科目余额-主表 t_tdm_balance

- **表名称：** 涉税科目余额-主表
- **表名：** t_tdm_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjust | 调整期 | varchar | 50 |  | √ | '0' | 调整期,枚举: 1 :是 0 :否 |
| 3 | fmeasureunit | 计量单位 | varchar | 100 |  | √ | ' ' | 计量单位 |
| 4 | fdebitlocalcurrency | 借方本币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借方本币金额 |
| 5 | fsubaccount18 | 辅助项18编号 | varchar | 100 |  | √ | ' ' | 辅助项18编号 |
| 6 | fdebitoriginalcurrency | 借方原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借方原币金额 |
| 7 | fsubaccount19 | 科目名称 | varchar | 500 |  | √ | ' ' | 科目名称 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsubaccount16 | 辅助项16编号 | varchar | 100 |  | √ | ' ' | 辅助项16编号 |
| 10 | fsubaccount17 | 辅助项17编号 | varchar | 100 |  | √ | ' ' | 辅助项17编号 |
| 11 | fsubaccount14 | 辅助项14编号 | varchar | 100 |  | √ | ' ' | 辅助项14编号 |
| 12 | fsubaccount15 | 辅助项15编号 | varchar | 100 |  | √ | ' ' | 辅助项15编号 |
| 13 | fsubaccount12 | 辅助项12编号 | varchar | 100 |  | √ | ' ' | 辅助项12编号 |
| 14 | fsubaccount13 | 辅助项13编号 | varchar | 100 |  | √ | ' ' | 辅助项13编号 |
| 15 | fsubaccount10 | 辅助项10编号 | varchar | 100 |  | √ | ' ' | 辅助项10编号 |
| 16 | fsubaccount11 | 辅助项11编号 | varchar | 100 |  | √ | ' ' | 辅助项11编号 |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fdebitamounti | 借方数量（本年累计） | numeric | 23 | 10 | √ | 0 | 借方数量（本年累计） |
| 19 | fclosingoriginalcurrency | 期末余额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额原币 |
| 20 | faccountcode | 科目编码 | varchar | 100 |  | √ | ' ' | 科目编码 |
| 21 | fclosingbalancetype | 期末余额方向 | varchar | 30 |  | √ | ' ' | 期末余额方向,枚举: 借 :借 贷 :贷 平 :平 |
| 22 | fcurrencytype | 币种编码 | varchar | 100 |  | √ | ' ' | 币种编码 |
| 23 | fopeningbalancetype | 期初余额方向 | varchar | 30 |  | √ | ' ' | 期初余额方向,枚举: 借 :借 贷 :贷 平 :平 |
| 24 | fsubaccount8 | 辅助项8编号 | varchar | 100 |  | √ | ' ' | 辅助项8编号 |
| 25 | fsubaccount7 | 辅助项7编号 | varchar | 100 |  | √ | ' ' | 辅助项7编号 |
| 26 | fsubaccount9 | 辅助项9编号 | varchar | 100 |  | √ | ' ' | 辅助项9编号 |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fsubaccount4 | 辅助项4编号 | varchar | 100 |  | √ | ' ' | 辅助项4编号 |
| 29 | fsubaccount3 | 辅助项3编号 | varchar | 100 |  | √ | ' ' | 辅助项3编号 |
| 30 | fopeningoriginalcurrency | 期初余额原币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额原币 |
| 31 | fsubaccount6 | 辅助项6编号 | varchar | 100 |  | √ | ' ' | 辅助项6编号 |
| 32 | fsubaccount5 | 辅助项5编号 | varchar | 100 |  | √ | ' ' | 辅助项5编号 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fcreditamount | 贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方数量 |
| 35 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 36 | fdebitamount | 借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 借方数量 |
| 37 | faccountperiod | 会计期间号 | varchar | 100 |  | √ | ' ' | 会计期间号,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 38 | fdatasource | 数据来源 | varchar | 100 |  | √ | ' ' | 数据来源 |
| 39 | faccountyear | 会计年度 | varchar | 100 |  | √ | ' ' | 会计年度 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fclosinglocalcurrency | 期末余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额本位币 |
| 42 | faccountcycle | 会计账期 | varchar | 100 |  | √ | ' ' | 会计账期 |
| 43 | fopeninglocalcurrency | 期初余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额本位币 |
| 44 | fdebitoriginalcurrencyi | 借方原币金额（本年累计） | numeric | 23 | 10 | √ | 0 | 借方原币金额（本年累计） |
| 45 | fadjperi | 调整期间 | varchar | 50 |  | √ | ' ' | 调整期间 |
| 46 | fcreditoriginalcurrency | 贷方原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方原币金额 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fopeningamount | 期初数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量 |
| 49 | faccountbookstype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型 |
| 50 | fsubaccount2 | 辅助项2编号 | varchar | 100 |  | √ | ' ' | 辅助项2编号 |
| 51 | fisadjust | 调整期 | bpchar | 1 |  | √ | '0' | 调整期 |
| 52 | fsubaccount1 | 辅助项1编号 | varchar | 100 |  | √ | ' ' | 辅助项1编号 |
| 53 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 55 | fcreditamounti | 贷方数量（本年累计） | numeric | 23 | 10 | √ | 0 | 贷方数量（本年累计） |
| 56 | fcreditlocalcurrency | 贷方本币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方本币金额 |
| 57 | fcreditoriginalcurrencyi | 贷方原币金额（本年累计） | numeric | 23 | 10 | √ | 0 | 贷方原币金额（本年累计） |
| 58 | fcreditlocalcurrencyi | 本年累计贷方本币金额 | numeric | 23 | 10 | √ | 0 | 本年累计贷方本币金额 |
| 59 | fclosingamount | 期末数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期末数量 |
| 60 | fbalanceid | 科目 | varchar | 36 |  | √ | ' ' | 科目 tdm_account |
| 61 | fdebitlocalcurrencyi | 本年累计借方本币金额 | numeric | 23 | 10 | √ | 0 | 本年累计借方本币金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_balance_pkey |  | fid |
| 2 | idx_t_tdm_balance |  | faccountcode |
| 3 | idx_t_tdm_balance_org |  | forgid,faccountyear,faccountperiod |
