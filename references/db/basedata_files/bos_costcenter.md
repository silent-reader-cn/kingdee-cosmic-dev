# 成本中心-bos_costcenter

## 曾用名列表-子表 t_bas_costcenternh

- **表名称：** 曾用名列表-子表
- **表名：** t_bas_costcenternh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fenable | 是否生效 | bpchar | 1 |  | √ | '1' | 是否生效 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_costcenternh |  | fentryid |
| 2 | idx_t_bas_costcenternh_fid |  | fid |

---

## 单据体-子表 t_bas_costcenterentry

- **表名称：** 单据体-子表
- **表名：** t_bas_costcenterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcetypeobj | 来源类型2 | varchar | 255 |  | √ | ' ' | 来源类型2,枚举: bos_adminorg :行政组织（部门） |
| 3 | fdataid | 来源数据编号 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 4 | fsourcetypeid | 来源类型1 | int8 | 64 |  | √ | 0 | [来源类型 bos_costcentersourcetype](../basedata_files/bos_costcentersourcetype.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_costcenterentry |  | fid,fentryid |
| 2 | pk_bas_costcenterentry |  | fentryid |

---

## 成本中心-多语言表 t_bas_costcenter_l

- **表名称：** 成本中心-多语言表
- **表名：** t_bas_costcenter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_costcenter_l_pkey |  | fpkid |
| 2 | idx_t_bas_costcenter_l_fid |  | fid,flocaleid,fname |

---

## 成本中心-主表 t_bas_costcenter

- **表名称：** 成本中心-主表
- **表名：** t_bas_costcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | forgdutyid | 类型，部门属性，弃 | int8 | 64 |  | √ | 0 | [部门属性 bos_org_duty](../base_files/bos_org_duty.md) |
| 5 | forg | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: bos_adminorg :行政组织（部门） bd_supplier :供应商 sfc_workcenter :工作中心 |
| 12 | fadminorg | 部门 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 13 | forgdutyem | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :管理 2 :研发 3 :销售 4 :基本生产 5 :辅助生产 6 :采购 7 :委外 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 22 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | faccountorgid | 对应核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_costcenter_number |  | fnumber,fstatus,fenable,fisleaf |
| 2 | t_bas_costcenter_pkey |  | fid |

---

## 曾用名列表-多语言表 t_bas_costcenternh_l

- **表名称：** 曾用名列表-多语言表
- **表名：** t_bas_costcenternh_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_costcenternh_l_id |  | fpkid |
| 2 | idx_t_bas_costcenternh_l |  | fentryid,flocaleid |
