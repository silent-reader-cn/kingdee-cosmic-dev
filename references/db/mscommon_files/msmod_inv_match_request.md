# 标准库存与需求单据的匹配条件（废弃）-msmod_inv_match_request

## 标准库存与需求单据的匹配条件（废弃）-多语言表 t_msmod_req_match_l

- **表名称：** 标准库存与需求单据的匹配条件（废弃）-多语言表
- **表名：** t_msmod_req_match_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_name | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_req_match_l |  | fpkid |
| 2 | idx_t_msmod_req_match_l_id |  | fid,flocaleid |

---

## 可用库存匹配条件-子表 t_stock_match_entry

- **表名称：** 可用库存匹配条件-子表
- **表名：** t_stock_match_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 标准库存与需求单据的匹配条件（废弃）-主表 t_msmod_req_match

- **表名称：** 标准库存与需求单据的匹配条件（废弃）-主表
- **表名：** t_msmod_req_match

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_request_bill_id | 需求单据 | int8 | 64 |  | √ | 0 | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | f_enable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | f_number | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | f_name | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 9 | f_creator_id | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | f_status | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_req_match_fnum |  | f_number |
| 2 | pk_msmod_req_match |  | fid |
