# 行政组织-isc_api2ierp_org

## 行政组织-主表 t_ds_api2ierp_org

- **表名称：** 行政组织-主表
- **表名：** t_ds_api2ierp_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpresit_string_field_g | 预留字段g | varchar | 200 |  | √ | ' ' | 预留字段g |
| 3 | fpresit_string_field_h | 预留字段h | varchar | 200 |  | √ | ' ' | 预留字段h |
| 4 | fpresit_string_field_e | 预留字段e | varchar | 200 |  | √ | ' ' | 预留字段e |
| 5 | fpresit_string_field_f | 预留字段f | varchar | 200 |  | √ | ' ' | 预留字段f |
| 6 | forgid | 第三方组织id | varchar | 100 |  | √ | ' ' | 第三方组织id |
| 7 | flong_parent | 上级长编码 | varchar | 500 |  | √ | ' ' | 上级长编码 |
| 8 | fstatus | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态 |
| 9 | fisadministrative | 是否行政组织 | varchar | 10 |  | √ | ' ' | 是否行政组织 |
| 10 | fpresit_string_field_c | 预留字段c | varchar | 200 |  | √ | ' ' | 预留字段c |
| 11 | ffrom | 来源第三方系统 | varchar | 100 |  | √ | ' ' | 来源第三方系统 |
| 12 | fpresit_string_field_d | 预留字段d | varchar | 200 |  | √ | ' ' | 预留字段d |
| 13 | fpresit_string_field_a | 预留字段a | varchar | 200 |  | √ | ' ' | 预留字段a |
| 14 | fpresit_string_field_b | 预留字段b | varchar | 200 |  | √ | ' ' | 预留字段b |
| 15 | fname | 组织名称 | varchar | 100 |  | √ | ' ' | 组织名称 |
| 16 | fcomment | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 17 | fpresit_timestamp_a | 预留日期a | timestamp | 0 |  |  | null | 预留日期a |
| 18 | fpresit_timestamp_b | 预留日期b | timestamp | 0 |  |  | null | 预留日期b |
| 19 | fierp_org_id | 苍穹id反写 | int8 | 64 |  | √ | 0 | 苍穹id反写 |
| 20 | fpresit_bigint_b | 预留长整数b | int8 | 64 |  | √ | 0 | 预留长整数b |
| 21 | forgpattern | 组织形态 | varchar | 10 |  | √ | ' ' | 组织形态,枚举: 1 :公司 2 :分公司 3 :事业部 4 :部门 6 :工厂 7 :集团 8 :集团公司 |
| 22 | fpresit_bigint_a | 预留长整数a | int8 | 64 |  | √ | 0 | 预留长整数a |
| 23 | fisfreeze | 是否封存 | varchar | 10 |  | √ | ' ' | 是否封存,枚举: 1 :封存 0 :未封存 |
| 24 | ftrd_parent | 第三方上级组织id | varchar | 100 |  | √ | ' ' | 第三方上级组织id |
| 25 | fenable | 启用状态 | varchar | 10 |  | √ | ' ' | 启用状态,枚举: 1 :启用 0 :禁用 |
| 26 | fnumber | 组织编码 | varchar | 100 |  | √ | ' ' | 组织编码 |
| 27 | fcreatime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_isc_api2ierp_org_f |  | ffrom |
| 2 | index_t_isc_api2ierp_org_n |  | fnumber |
| 3 | pk_t_ds_api2ierp_org |  | fid |
| 4 | index_t_isc_api2ierp_org_o |  | forgid |
| 5 | index_t_isc_api2ierp_org_l |  | flong_parent |
