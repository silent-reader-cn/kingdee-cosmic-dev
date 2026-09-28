# 业务类型-bd_biztype

## 业务类型-多语言表 t_bd_biztype_l

- **表名称：** 业务类型-多语言表
- **表名：** t_bd_biztype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_biztype_l_pkey |  | fpkid |
| 2 | idx_bd_biztype_l_fid |  | fid,flocaleid |

---

## 业务类型-主表 t_bd_biztype

- **表名称：** 业务类型-主表
- **表名：** t_bd_biztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fissale | 销售 | bpchar | 1 |  | √ | '0' | 销售 |
| 6 | fdomain | 领域 | varchar | 80 |  | √ | '0' | 领域,枚举: 0 :销售 1 :采购 2 :库存 3 :生产 5 :委外 4 :其他 6 :VMI 7 :检修 8 :质量 9 :应收 10 :应付 11 :出纳 12 :滚动销售 13 :零售 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fisinventory | 库存 | bpchar | 1 |  | √ | '0' | 库存 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fispurchase | 采购 | bpchar | 1 |  | √ | '0' | 采购 |
| 17 | fbizcategory | 业务分类 | varchar | 5 |  | √ | ' ' | 业务分类,枚举: BZ :标准 WW :委外 FY :费用 ZC :资产 VMI :VMI ZY :直运 FX :分销 JS :寄售 ST :受托 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_biztype_number |  | fnumber |
| 2 | t_bd_biztype_pkey |  | fid |

---

## 关联行类型分录-子表 t_bd_linetypeentry

- **表名称：** 关联行类型分录-子表
- **表名：** t_bd_linetypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | flinetypeid | 编码 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 5 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 6 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_bd_linetypeentry_fid |  | fid |
| 2 | pk_t_bd_linetypeentry |  | fentryid |

---

## 单据体-子表 t_sbd_biztypebillentity

- **表名称：** 单据体-子表
- **表名：** t_sbd_biztypebillentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillform | 单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sbd_biztypebillentity_pkey |  | fentryid |
| 2 | idx_sbd_btt_e |  | fid |
