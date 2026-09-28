# 费用MQ日志-er_mqlog

## 费用MQ日志-主表 t_er_mqlog

- **表名称：** 费用MQ日志-主表
- **表名：** t_er_mqlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessagecontent_tag | 消息详情_详情 | text | 0 |  |  | ' ' | 消息详情_详情 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmessagecontent | 消息详情 | varchar | 255 |  | √ | ' ' | 消息详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mqlog_createtime |  | fcreatetime |
| 2 | pk_er_mqlog |  | fid |
