# 回单缺失报表查询-receipt_defect_sta_by_mon

## 回单缺失报表查询-主表 t_receipt_defect_stats

- **表名称：** 回单缺失报表查询-主表
- **表名：** t_receipt_defect_stats

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbank_login | 前置机 | int8 | 64 |  |  | 0 | [银企连接通道配置 aqap_bank_login](../aqap_files/aqap_bank_login.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdefect_year | 缺失年份 | varchar | 50 |  | √ | ' ' | 缺失年份,枚举: 2019 :2019年 2020 :2020年 2021 :2021年 2022 :2022年 |
| 7 | facc_no | 银行账号 | int8 | 64 |  |  | 0 | [银企账户 aqap_bank_acnt](../aqap_files/aqap_bank_acnt.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdefect_day | 回单缺失天数 | int8 | 64 |  |  | 0 | 回单缺失天数 |
| 11 | faccno | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 12 | fbank_version | 银行版本 | int8 | 64 |  |  | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 13 | fbank_name | 银行版本名称 | varchar | 255 |  | √ | ' ' | 银行版本名称 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbank_login_number | 前置机编码 | varchar | 255 |  | √ | ' ' | 前置机编码 |
| 16 | fdefect_month | 缺失月份 | varchar | 50 |  | √ | ' ' | 缺失月份,枚举: 01 :1月 02 :2月 03 :3月 04 :4月 05 :5月 06 :6月 07 :7月 08 :8月 09 :9月 10 :10月 11 :11月 12 :12月 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_defect_stats_pkey |  | fid |
