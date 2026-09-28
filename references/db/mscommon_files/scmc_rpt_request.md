# 报表请求记录-scmc_rpt_request

## 报表请求记录-主表 t_scmc_rpt_request

- **表名称：** 报表请求记录-主表
- **表名：** t_scmc_rpt_request

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | ftype | 查询类型 | bpchar | 1 |  | √ | ' ' | 查询类型,枚举: A :报表页面查询 B :报表引出查询 C :代码调用查询 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | frepconf | 报表数据源配置 | int8 | 64 |  | √ | 0 | 报表数据源配置 scmc_report_conf |
| 6 | ftimeout | 超时时间点 | timestamp | 0 |  |  | null | 超时时间点 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scmc_rpt_request_fct |  | fcreatedate |
| 2 | pk_t_scmc_rpt_request |  | fid |
| 3 | idx_scmc_rpt_request_fto |  | ftimeout |
