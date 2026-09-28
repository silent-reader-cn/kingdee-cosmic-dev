# 群消息机器人-mbase_msgbot

## 群消息机器人-主表 t_mbase_msgbot

- **表名称：** 群消息机器人-主表
- **表名：** t_mbase_msgbot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 机器人名称 | varchar | 50 |  | √ | ' ' | 机器人名称 |
| 3 | fsecretkey | 密钥 | varchar | 255 |  | √ | ' ' | 密钥 |
| 4 | fkeyword | 关键字 | varchar | 50 |  | √ | ' ' | 关键字 |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fcorpid | CorpId | varchar | 50 |  | √ | ' ' | CorpId |
| 8 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fentryrolename | 平台类型 | varchar | 50 |  | √ | ' ' | 平台类型 |
| 10 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fentryrole | 平台类型编码 | bpchar | 1 |  | √ | '0' | 平台类型编码 |
| 13 | fwebhook | webhook | varchar | 500 |  | √ | ' ' | webhook |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_msgbot_fnumber |  | fnumber |
| 2 | pk_mbase_msgbot |  | fid |
