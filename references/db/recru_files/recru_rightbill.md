# 权益消费账单-recru_rightbill

## 权益消费账单-多语言表 t_recru_rightbill_l

- **表名称：** 权益消费账单-多语言表
- **表名：** t_recru_rightbill_l

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
| 1 | idx_recru_rightbill_l_fid |  | fid,flocaleid |
| 2 | pk_recru_rightbill_l |  | fpkid |

---

## 权益消费账单-主表 t_recru_rightbill

- **表名称：** 权益消费账单-主表
- **表名：** t_recru_rightbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | famount | 消耗额度 | numeric | 23 | 10 | √ | 0 | 消耗额度 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fskurightinsid | 权益实例 | int8 | 64 |  | √ | 0 | [sku权益实例 recru_skurightins](../recru_files/recru_skurightins.md) |
| 8 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fdealstatus | 处理状态 | varchar | 50 |  | √ | ' ' | 处理状态,枚举: 10 :成功 20 :失败 30 :处理中 |
| 12 | fsessionid | 会话 | varchar | 50 |  | √ | ' ' | 会话 |
| 13 | fuseuserid | 消费的用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fdirection | 扣减方向 | varchar | 50 |  | √ | ' ' | 扣减方向,枚举: 10 :扣减 20 :返回 30 :增加 |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | frequestid | 请求ID | varchar | 50 |  | √ | ' ' | 请求ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_rightbill_uniq_sesre |  | fsessionid,frequestid |
| 2 | pk_recru_rightbill |  | fid |
