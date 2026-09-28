# 系统集成日志-pur_apilog

## 系统集成日志-主表 t_pur_apilog

- **表名称：** 系统集成日志-主表
- **表名：** t_pur_apilog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 单据名称 | varchar | 50 |  | √ | ' ' | 单据名称 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | finputdata_tag | 传入数据_详情 | text | 0 |  |  | null | 传入数据_详情 |
| 5 | fcreatetime | 日志时间 | timestamp | 0 |  |  | null | 日志时间 |
| 6 | finputdata | 传入数据 | text | 0 |  |  | null | 传入数据 |
| 7 | foutputdata | 传出数据 | text | 0 |  |  | null | 传出数据 |
| 8 | finterface | 接口名称 | varchar | 50 |  | √ | ' ' | 接口名称 |
| 9 | foutputdata_tag | 传出数据_详情 | text | 0 |  |  | null | 传出数据_详情 |
| 10 | fapiconfigid | 系统集成方案 | int8 | 64 |  | √ | 0 | [系统集成配置 pur_apiconfig](../pbd_files/pur_apiconfig.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_apilog_fcreatetime |  | fcreatetime |
| 2 | idx_pur_apilog_fentityname |  | fentityname |
| 3 | idx_pur_apilog_finterface |  | finterface |
| 4 | idx_pur_apilog_fapiconfigid |  | fapiconfigid |
| 5 | t_pur_apilog_pkey |  | fid |
