# sku权益实例-recru_skurightins

## sku权益实例-多语言表 t_recru_skurightins_l

- **表名称：** sku权益实例-多语言表
- **表名：** t_recru_skurightins_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_skurightins_l |  | fpkid |
| 2 | idx_recru_skurightins_l_fid |  | fid,flocaleid |

---

## sku权益实例-主表 t_recru_skurightins

- **表名称：** sku权益实例-主表
- **表名：** t_recru_skurightins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | flimitcontrol | 额度控制 | bpchar | 1 |  | √ | '0' | 额度控制 |
| 5 | flimit | 额度 | numeric | 23 | 10 | √ | 0 | 额度 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fskuid | sku | int8 | 64 |  | √ | 0 | [sku recru_sku](../recru_files/recru_sku.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frightid | 权益项 | int8 | 64 |  | √ | 0 | [权益项 recru_rights](../recru_files/recru_rights.md) |
| 13 | fsessionid | 会话ID | varchar | 50 |  | √ | ' ' | 会话ID |
| 14 | fusedlimit | 已用额度 | numeric | 23 | 10 | √ | 0 | 已用额度 |
| 15 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_skurightins_session |  | fsessionid |
| 2 | pk_recru_skurightins |  | fid |
