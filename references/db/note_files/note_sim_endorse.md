# 背面信息-note_sim_endorse

## 背面信息-主表 t_note_sim_endorse

- **表名称：** 背面信息-主表
- **表名：** t_note_sim_endorse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 发起人名称 | varchar | 255 |  | √ | ' ' | 发起人名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbizseq | 排序字段 | int8 | 64 |  |  | null | 排序字段 |
| 6 | fendno | 结束区间 | varchar | 50 |  | √ | ' ' | 结束区间 |
| 7 | fbankname | 发起人银行名称 | varchar | 255 |  | √ | ' ' | 发起人银行名称 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | foppbankname | 接收方银行名称 | varchar | 255 |  | √ | ' ' | 接收方银行名称 |
| 10 | ftransdate | 交易日期 | varchar | 50 |  | √ | ' ' | 交易日期 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 1 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 发起人账号 | varchar | 30 |  | √ | ' ' | 发起人账号 |
| 16 | foppname | 接收方账户名 | varchar | 255 |  | √ | ' ' | 接收方账户名 |
| 17 | foppaccno | 接收方账号 | varchar | 50 |  | √ | ' ' | 接收方账号 |
| 18 | fbillno | 票号 | varchar | 50 |  | √ | ' ' | 票号 |
| 19 | fstartno | 起始区间 | varchar | 50 |  | √ | ' ' | 起始区间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_sim_endorse_pkey |  | fid |

---

## 背面信息-多语言表 t_note_sim_endorse_l

- **表名称：** 背面信息-多语言表
- **表名：** t_note_sim_endorse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 发起人名称 | varchar | 255 |  | √ | ' ' | 发起人名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_sim_endorse_l_pkey |  | fpkid |
