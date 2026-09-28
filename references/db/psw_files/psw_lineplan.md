# 生产线计划平台-psw_lineplan

## 生产线计划平台-主表 t_psw_workbench

- **表名称：** 生产线计划平台-主表
- **表名：** t_psw_workbench

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  |  | null |  |
| 3 | fproductionline | fproductionline | varchar | 500 |  |  | null |  |
| 4 | fbillstatus | fbillstatus | varchar | 500 |  |  | null |  |
| 5 | fwarehousetype | fwarehousetype | varchar | 500 |  |  | null |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | forgid | forgid | int8 | 64 |  |  | null |  |
| 8 | fwarehousestate | fwarehousestate | varchar | 500 |  |  | null |  |
| 9 | fplanmonth | fplanmonth | int8 | 64 |  |  | null |  |
| 10 | fplanday | fplanday | int8 | 64 |  |  | null |  |
| 11 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 12 | freqiureorg | freqiureorg | varchar | 500 |  |  | null |  |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | fwarehouse | fwarehouse | varchar | 500 |  |  | null |  |
| 15 | fcreatorid | fcreatorid | int8 | 64 |  |  | null |  |
| 16 | fpredate | fpredate | int8 | 64 |  |  | null |  |
| 17 | fplangroup | fplangroup | varchar | 500 |  |  | null |  |
| 18 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 19 | fplanweek | fplanweek | int8 | 64 |  |  | null |  |
| 20 | fmaterial | fmaterial | varchar | 500 |  |  | null |  |
| 21 | fbillno | fbillno | varchar | 30 |  |  | null |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_wb_union |  | forgid |
| 2 | pk_t_psw_workbench |  | fid |
