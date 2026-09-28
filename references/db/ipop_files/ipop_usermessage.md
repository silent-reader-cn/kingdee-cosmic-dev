# 用户消息-ipop_usermessage

## 用户消息-主表 t_ipop_usermessage

- **表名称：** 用户消息-主表
- **表名：** t_ipop_usermessage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 消息状态 | varchar | 50 |  | √ | '0' | 消息状态,枚举: 0 :未读 1 :已读 |
| 3 | fmessageid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fusestatus | 有效状态 | varchar | 50 |  | √ | '1' | 有效状态,枚举: 0 :失效 1 :有效 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_usermessage_g |  | fuserid,fstatus,fusestatus |
| 2 | pk_ipop_usermessage |  | fid |
