# 分布式事务消息表-bdtaxr_dtx_message

## 分布式事务消息表-主表 t_bdtaxr_dtx_message

- **表名称：** 分布式事务消息表-主表
- **表名：** t_bdtaxr_dtx_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmsgstatus | 消息状态 | varchar | 50 |  | √ | ' ' | 消息状态,枚举: pending :待发送 sent :已发送 failed :失败 processed :已处理 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmsgparam_tag | 消息参数_详情 | text | 0 |  |  | null | 消息参数_详情 |
| 5 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fservicename | 服务名称 | varchar | 50 |  | √ | ' ' | 服务名称 |
| 9 | fmsgparam | 消息参数 | varchar | 255 |  | √ | ' ' | 消息参数 |
| 10 | fretrycount | 失败重试次数 | int4 | 32 |  | √ | 0 | 失败重试次数 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fappid | 应用 | varchar | 50 |  | √ | ' ' | 应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_dtx_message |  | fid |
