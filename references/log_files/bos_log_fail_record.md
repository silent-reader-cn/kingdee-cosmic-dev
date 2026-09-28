# 失败消息记录-bos_log_fail_record

## 失败消息记录-主表 t_log_failrecord

- **表名称：** 失败消息记录-主表
- **表名：** t_log_failrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 消息 | varchar | 1024 |  | √ | ' ' | 消息 |
| 3 | fretrytimes | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 4 | fcreatetime | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 5 | fnextretrytime | 下次重试时间 | int8 | 64 |  | √ | 0 | 下次重试时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_log_failrecord_createtime |  | fcreatetime |
| 2 | pk_t_log_failrecord |  | fid |
