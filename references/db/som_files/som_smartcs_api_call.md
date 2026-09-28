# 接口调用日志-som_smartcs_api_call

## 接口调用日志-主表 t_tk_scs_apicalled

- **表名称：** 接口调用日志-主表
- **表名：** t_tk_scs_apicalled

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fparameter | 调用参数 | varchar | 255 |  | √ | ' ' | 调用参数 |
| 4 | ftraceid | AI全链路id | varchar | 50 |  | √ | ' ' | AI全链路id |
| 5 | fbillstatus | 单据状态 | varchar | 4 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 7 | fprivateinput | 构建入参 | varchar | 255 |  | √ | ' ' | 构建入参 |
| 8 | fmethod | 调用接口 | varchar | 255 |  | √ | ' ' | 调用接口 |
| 9 | fresult | 调用结果 | varchar | 255 |  | √ | ' ' | 调用结果 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fresult_tag | 调用结果_详情 | text | 0 |  |  | null | 调用结果_详情 |
| 13 | fsuccess | 接口成功调用 | bpchar | 1 |  | √ | '0' | 接口成功调用 |
| 14 | foperate | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fprivateinput_tag | 构建入参_详情 | text | 0 |  |  | null | 构建入参_详情 |
| 17 | fparameter_tag | 调用参数_详情 | text | 0 |  |  | null | 调用参数_详情 |
| 18 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_scs_apicall_traceid |  | ftraceid |
| 2 | idx_ssc_scs_apicall_method |  | fmethod |
| 3 | pk_t_tk_scs_apicalled |  | fid |
| 4 | idx_ssc_scs_apicall_operate |  | foperate |
