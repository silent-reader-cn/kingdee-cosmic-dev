# 结算分批数据保存状态-ism_settlebatchdata

## 结算分批数据保存状态-主表 t_ism_settlebatch

- **表名称：** 结算分批数据保存状态-主表
- **表名：** t_ism_settlebatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbeginsavetime | 开始保存时间 | timestamp | 0 |  |  | null | 开始保存时间 |
| 3 | fbatchnumber | 分批批次 | int4 | 32 |  | √ | 1 | 分批批次 |
| 4 | fsessionid | 线程ID | varchar | 50 |  | √ | ' ' | 线程ID |
| 5 | fsavestatus | 保存状态 | varchar | 30 |  | √ | ' ' | 保存状态,枚举: 1 :开始保存 2 :完成保存 |
| 6 | fendsavetime | 完成保存时间 | timestamp | 0 |  |  | null | 完成保存时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settlebatch |  | fid |
| 2 | idx_ism_settlebatch_sid |  | fsessionid |
