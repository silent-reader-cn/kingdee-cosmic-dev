# 采购业务组(封存)-bd_pmoperatorgroup

## 采购业务组(封存)-使用范围表 t_bd_operatorgroup_u

- **表名称：** 采购业务组(封存)-使用范围表
- **表名：** t_bd_operatorgroup_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_operatorgroup_u_uo |  | fuseorgid |
| 2 | t_bd_operatorgroup_u_pkey |  | fdataid,fuseorgid |

---

## 采购业务组(封存)-多语言表 t_bd_operatorgroup_l

- **表名称：** 采购业务组(封存)-多语言表
- **表名：** t_bd_operatorgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
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
| 1 | t_bd_operatorgroup_l_pkey |  | fpkid |
| 2 | idx_bd_operatorgroup_l_fid |  | fid,flocaleid |

---

## 采购业务组(封存)-使用范围位图表 t_bd_operatorgroup_m

- **表名称：** 采购业务组(封存)-使用范围位图表
- **表名：** t_bd_operatorgroup_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_operatorgroup_m |  | forgid |

---

## 采购业务组(封存)-主表 t_bd_operatorgroup

- **表名称：** 采购业务组(封存)-主表
- **表名：** t_bd_operatorgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | foperatorgrouptype | 业务组类型 | varchar | 5 |  | √ | ' ' | 业务组类型,枚举: CGZ :采购组 KCZ :库管组 XSZ :销售组 JHZ :计划组 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_operatorgroup_number |  | fnumber |
| 2 | idx_t_bd_operatorgroup_createorg |  | fcreateorgid |
| 3 | idx_t_bd_operatorgroup_master |  | fmasterid |
| 4 | t_bd_operatorgroup_pkey |  | fid |

---

## 单据体-子表 t_bd_operatorgroupentry

- **表名称：** 单据体-子表
- **表名：** t_bd_operatorgroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | foperatorid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fopergrptype | 业务组类型 | varchar | 5 |  | √ | ' ' | 业务组类型,枚举: CGZ :采购组 KCZ :库存组 XSZ :销售组 JHZ :计划组 ZJZ :质检组 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fopergrpnumber | 业务组编码 | varchar | 80 |  | √ | ' ' | 业务组编码 |
| 7 | foperatorname | 业务员名称 | varchar | 255 |  |  | ' ' | 业务员名称 |
| 8 | finvalid | 失效 | bpchar | 1 |  | √ | '0' | 失效 |
| 9 | fposition | fposition | varchar | 255 |  | √ | ' ' |  |
| 10 | foperatornumber | 业务员编码 | varchar | 80 |  | √ | ' ' | 业务员编码 |
| 11 | fopergrpname | 业务组名称 | varchar | 50 |  | √ | ' ' | 业务组名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_operatorgroupentry_pkey |  | fentryid |
| 2 | idx_bd_operatorgroupentry_fid |  | fid |

---

## 单据体-多语言表 t_bd_operatorgroupentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_bd_operatorgroupentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperatorname | 业务员名称 | varchar | 255 |  |  | ' ' | 业务员名称 |
| 2 | fposition | fposition | varchar | 255 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fopergrpname | 业务组名称 | varchar | 50 |  | √ | ' ' | 业务组名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_operatorgroupentry_l |  | fentryid,flocaleid |
| 2 | t_bd_operatorgroupentry_l_pkey |  | fpkid |
