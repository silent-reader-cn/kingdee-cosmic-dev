# 消费记录-bos_comm_consume

## 消费记录-主表 t_comm_consume

- **表名称：** 消费记录-主表
- **表名：** t_comm_consume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 消费时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 消费时间 |
| 3 | fcompany | fcompany | varchar | 255 |  | √ | ' ' |  |
| 4 | fconsumesize | 消费额度 | int4 | 32 |  | √ | 0 | 消费额度 |
| 5 | fcuser | 用户 | int8 | 64 |  | √ | 0 | 社区用户 bos_comm_user |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | varchar | 50 |  | √ | ' ' | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 9 | fexecstatus | 执行状态 | int4 | 32 |  | √ | 0 | 执行状态,枚举: 1 :成功 2 :失败 |
| 10 | fsessionid | 会话ID | varchar | 50 |  | √ | ' ' | 会话ID |
| 11 | fclientype | 客户端类型 | int4 | 32 |  | √ | 0 | 客户端类型,枚举: 1 :WEBCHAT 2 :IDEA 3 :VCODE 99 :OTHER |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fuid | 用户UID | int8 | 64 |  | √ | 0 | 用户UID |
| 14 | fnumber | 编码 | varchar | 512 |  | √ | ' ' | 编码 |
| 15 | fusertype | fusertype | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_comm_consume |  | fuid |
| 2 | pk_comm_consume |  | fid |

---

## 消费记录-多语言表 t_comm_consume_l

- **表名称：** 消费记录-多语言表
- **表名：** t_comm_consume_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_comm_consume_l |  | fpkid |
| 2 | idx_comm_consume_l |  | fid,flocaleid |
