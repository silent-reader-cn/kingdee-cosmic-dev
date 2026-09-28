# 待签收信息-note_sim_reply

## 待签收信息-多语言表 t_note_sim_reply_l

- **表名称：** 待签收信息-多语言表
- **表名：** t_note_sim_reply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 持票人名称 | varchar | 255 |  | √ | ' ' | 持票人名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_sim_reply_l_pkey |  | fpkid |

---

## 待签收信息-主表 t_note_sim_reply

- **表名称：** 待签收信息-主表
- **表名：** t_note_sim_reply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbankrefkey | 业务参考号 | varchar | 50 |  | √ | ' ' | 业务参考号 |
| 3 | fname | 持票人名称 | varchar | 255 |  | √ | ' ' | 持票人名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fendno | 结束区间 | varchar | 50 |  | √ | ' ' | 结束区间 |
| 7 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 8 | fbankname | 持票人银行名称 | varchar | 255 |  | √ | ' ' | 持票人银行名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | faccno | 待签收账号 | varchar | 50 |  | √ | ' ' | 待签收账号 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 1 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | ftype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 持票账号 | varchar | 50 |  | √ | ' ' | 持票账号 |
| 17 | fbillno | 票号 | varchar | 50 |  | √ | ' ' | 票号 |
| 18 | fstartno | 起始区间 | varchar | 50 |  | √ | ' ' | 起始区间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_sim_reply_pkey |  | fid |
