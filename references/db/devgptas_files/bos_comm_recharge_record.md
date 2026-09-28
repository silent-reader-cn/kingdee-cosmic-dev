# 充值记录-bos_comm_recharge_record

## 充值记录-主表 t_comm_recharge_record

- **表名称：** 充值记录-主表
- **表名：** t_comm_recharge_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedtime | 充值时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 充值时间 |
| 3 | fcuser | 用户 | int8 | 64 |  | √ | 0 | 社区用户 bos_comm_user |
| 4 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | frechargesize | 充值额度 | int4 | 32 |  | √ | 0 | 充值额度 |
| 6 | fcredittype | 消费类型 | int4 | 32 |  | √ | 0 | 消费类型,枚举: 1 :WEB 2 :IDEA 3 :VSCODE 99 :OTHER |
| 7 | fcreatorid | 创建人 | varchar | 50 |  | √ | ' ' | 人员 bos_user |
| 8 | fmasterid | 主数据内码（考虑隐藏） | int8 | 64 |  | √ | 0 | 主数据内码（考虑隐藏） |
| 9 | frechargetype | 充值方式 | int4 | 32 |  | √ | 0 | 充值方式,枚举: 1 :人工 2 :系统刷新 |
| 10 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | frechargestatus | 充值状态 | int4 | 32 |  | √ | 0 | 充值状态,枚举: 1 :成功 2 :失败 |
| 12 | fuid | 用户UID（考虑隐藏） | int8 | 64 |  | √ | 0 | 用户UID（考虑隐藏） |
| 13 | fnumber | 编码 | varchar | 512 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_comm_recharge_record |  | fid |
| 2 | idx_c_recharge_record |  | fuid |

---

## 充值记录-多语言表 t_comm_recharge_record_l

- **表名称：** 充值记录-多语言表
- **表名：** t_comm_recharge_record_l

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
| 1 | pk_comm_recharge_record_l |  | fpkid |
| 2 | idx_c_recharge_r_l |  | fid,flocaleid |
