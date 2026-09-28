# 采购计划平台-ssm_purplan

## 采购计划平台-主表 t_ssm_workbench

- **表名称：** 采购计划平台-主表
- **表名：** t_ssm_workbench

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fasofdate | fasofdate | timestamp | 0 |  |  | null |  |
| 4 | fwarehousetype | fwarehousetype | varchar | 50 |  | √ | ' ' |  |
| 5 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fplanmonth | fplanmonth | int8 | 64 |  | √ | 0 |  |
| 8 | fwarehousestate | fwarehousestate | varchar | 50 |  | √ | ' ' |  |
| 9 | fplanday | fplanday | int8 | 64 |  | √ | 0 |  |
| 10 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 11 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 12 | fwarehouse | fwarehouse | varchar | 50 |  | √ | ' ' |  |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | fpredate | fpredate | int8 | 64 |  | √ | 0 |  |
| 15 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 16 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 17 | frange | 组合范围 | varchar | 50 |  | √ | ' ' | 组合范围 |
| 18 | fplanweek | fplanweek | int8 | 64 |  | √ | 0 |  |
| 19 | fmaterial | fmaterial | varchar | 50 |  | √ | ' ' |  |
| 20 | fschemelist1 |  | varchar | 50 |  | √ | ' ' | ,枚举: |
| 21 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 22 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 23 | freceiveorg | freceiveorg | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssm_workbench_m0 |  | fbillno |
| 2 | pk_ssm_workbench |  | fid |
