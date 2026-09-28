# 结算分批设置明细-ism_createsettlebatchset

## 结算分批设置明细-主表 t_ism_settlebatchset

- **表名称：** 结算分批设置明细-主表
- **表名：** t_ism_settlebatchset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fbatchnumber | 分批批次 | int4 | 32 |  | √ | 1 | 分批批次 |
| 4 | fsessionid | 线程ID | varchar | 50 |  | √ | ' ' | 线程ID |
| 5 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 6 | fentitykey | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 7 | fbillentrycount | 单据记录数 | int4 | 32 |  | √ | 0 | 单据记录数 |
| 8 | fjudgecfgid | 结算判定ID | int8 | 64 |  | √ | 0 | 结算判定ID |
| 9 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settlebatchset |  | fid |
| 2 | idx_ism_settlebatchset_sid |  | fsessionid,fentitykey,fentryid |
