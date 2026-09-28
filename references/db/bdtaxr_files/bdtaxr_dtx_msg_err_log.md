# 分布式事务消息错误日志表-bdtaxr_dtx_msg_err_log

## 分布式事务消息错误日志表-主表 t_bdtaxr_dtx_msg_err_log

- **表名称：** 分布式事务消息错误日志表-主表
- **表名：** t_bdtaxr_dtx_msg_err_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | ferrorinfo | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 5 | fmsgid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ferrorinfo_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_dtx_msg_err_log |  | fid |
