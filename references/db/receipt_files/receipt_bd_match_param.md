# 维护匹配字段-receipt_bd_match_param

## 维护匹配字段-多语言表 t_receipt_bd_match_param_l

- **表名称：** 维护匹配字段-多语言表
- **表名：** t_receipt_bd_match_param_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_receipt_bd_match_param_l_0 |  | fid,flocaleid |
| 2 | t_receipt_bd_match_param_l_pkey |  | fpkid |

---

## 维护匹配字段-主表 t_receipt_bd_match_param

- **表名称：** 维护匹配字段-主表
- **表名：** t_receipt_bd_match_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 6 | freceipt_param | 回单映射字段 | varchar | 50 |  | √ | ' ' | 回单映射字段 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 匹配字段 | varchar | 30 |  | √ | ' ' | 匹配字段 |
| 10 | fdetail_param | 明细映射字段 | varchar | 50 |  | √ | ' ' | 明细映射字段 |
| 11 | fref_id | 关联id | varchar | 50 |  | √ | ' ' | 关联id |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_bd_match_param_pkey |  | fid |
