# 差旅报销单自动生成记录-er_autocreate_reim_log

## 差旅报销单自动生成记录-主表 t_er_autocreatereimlog

- **表名称：** 差旅报销单自动生成记录-主表
- **表名：** t_er_autocreatereimlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fto | 目的地 | varchar | 200 |  | √ | ' ' | 目的地 |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 4 | fissuccess | 自动生成成功 | bpchar | 1 |  | √ | '0' | 自动生成成功 |
| 5 | fpushtime | 推送时间 | timestamp | 0 |  |  | null | 推送时间 |
| 6 | ferrormsg | 失败原因 | varchar | 200 |  | √ | ' ' | 失败原因 |
| 7 | fcompany | 申请人公司 | int8 | 64 |  | √ | 0 | 申请人公司 |
| 8 | fautocreateconfig | 差旅报销单自动生成配置 | int8 | 64 |  | √ | 0 | [自动差旅报销 er_tripreim_autocreate](../em_files/er_tripreim_autocreate.md) |
| 9 | ftripreimbursetype | 可下推单据类型 | varchar | 30 |  | √ | ' ' | 可下推单据类型,枚举: card :卡片式 grid :表格式 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | frstartdate | 出发日期 | timestamp | 0 |  |  | null | 出发日期 |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | 申请人 |
| 14 | fpushtimeconfig | 推送时点 | int4 | 32 |  | √ | 0 | 推送时点 |
| 15 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 16 | frenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 17 | fbillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_autocreatereimlog |  | fid |
| 2 | idx_er_autocreatereimlog |  | fpushtime,fautocreateconfig |
| 3 | idx_er_autocreatereimlogbillid |  | fbillid |
