# 礼券促销互斥规则-ocdbd_ticketsexclusive

## 礼券促销互斥规则-多语言表 t_ocdbd_exclusive_l

- **表名称：** 礼券促销互斥规则-多语言表
- **表名：** t_ocdbd_exclusive_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_exclusive_l |  | fpkid |
| 2 | idx_ocdbd_exclusivel_lid |  | fid,flocaleid |

---

## 促销子清单-子表 t_ocdbd_exclusivesub

- **表名称：** 促销子清单-子表
- **表名：** t_ocdbd_exclusivesub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubpromoteid | 促销方案ID | int8 | 64 |  | √ | 0 | 促销方案ID |
| 2 | fsubpromotetheme | 促销方案主题 | varchar | 100 |  | √ | ' ' | 促销方案主题 |
| 3 | fsubpromotiontype | 促销类型 | int8 | 64 |  | √ | 0 | [促销类型 ocdbd_promotetype](../ocdpm_files/ocdbd_promotetype.md) |
| 4 | fsubpromotionid | 促销活动 | int8 | 64 |  | √ | 0 | [促销活动 ocdbd_promotion](../ocdpm_files/ocdbd_promotion.md) |
| 5 | fsubpromoteenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsubpromotename | 促销方案名称 | varchar | 100 |  | √ | ' ' | 促销方案名称 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fsubpromotestartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 10 | fsubpromotenumber | 促销方案编码 | varchar | 80 |  | √ | ' ' | 促销方案编码 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_exclusivesub_eid |  | fentryid |
| 2 | pk_ocdbd_exclusivesub |  | fdetailid |

---

## 礼券促销互斥规则-主表 t_ocdbd_exclusive

- **表名称：** 礼券促销互斥规则-主表
- **表名：** t_ocdbd_exclusive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fpromotetypegroup | 促销类型 | bpchar | 1 |  | √ | '1' | 促销类型,枚举: 1 :所有促销方案 2 :指定促销方案 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fruletype | 规则类型 | bpchar | 1 |  | √ | 'A' | 规则类型,枚举: A :礼券互斥 B :促销互斥 C :礼券促销互斥 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fticketstypegroup | 礼券类型 | bpchar | 1 |  | √ | '1' | 礼券类型,枚举: 1 :所有礼券类型 2 :指定礼券类型 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 规则状态 | bpchar | 1 |  | √ | 'A' | 规则状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 17 | fenable | 禁用状态 | bpchar | 1 |  | √ | '1' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_exclusive_num |  | fnumber |
| 2 | pk_ocdbd_exclusive |  | fid |

---

## 礼券清单-子表 t_ocdbd_exclusiveticket

- **表名称：** 礼券清单-子表
- **表名：** t_ocdbd_exclusiveticket

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fticketstypeid | 礼券类型编码 | int8 | 64 |  | √ | 0 | 优惠券类型 rtvip_ticketstype |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_exclusiveticket_id |  | fid |
| 2 | pk_ocdbd_exclusiveticket |  | fentryid |

---

## 促销清单-子表 t_ocdbd_exclusivepromote

- **表名称：** 促销清单-子表
- **表名：** t_ocdbd_exclusivepromote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpromotionid | 促销活动 | int8 | 64 |  | √ | 0 | [促销活动 ocdbd_promotion](../ocdpm_files/ocdbd_promotion.md) |
| 3 | fpromoteenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | fpromotestartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fpromotiontypeid | 促销类型 | int8 | 64 |  | √ | 0 | [促销类型 ocdbd_promotetype](../ocdpm_files/ocdbd_promotetype.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpromoteid | 促销方案ID | int8 | 64 |  | √ | 0 | 促销方案ID |
| 8 | fpromotename | 促销方案名称 | varchar | 100 |  | √ | ' ' | 促销方案名称 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpromotenumber | 促销方案编码 | varchar | 80 |  | √ | ' ' | 促销方案编码 |
| 11 | fpromotetheme | 促销方案主题 | varchar | 100 |  | √ | ' ' | 促销方案主题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_exclusivepromote_id |  | fid |
| 2 | pk_ocdbd_exclusivepromote |  | fentryid |
