# 运输单元类型-lgm_shipunittype

## 运输单元类型-使用范围表 t_lgm_shipunittype_u

- **表名称：** 运输单元类型-使用范围表
- **表名：** t_lgm_shipunittype_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_shipunittype_u |  | fdataid |
| 2 | idx_lgm_shipunittype_u |  | fcreateorgid,fdataid |

---

## 运输单元类型-多语言表 t_lgm_shipunittype_l

- **表名称：** 运输单元类型-多语言表
- **表名：** t_lgm_shipunittype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_shipunittype_l |  | fpkid |
| 2 | idx_lgm_shipunittype_l |  | fid |

---

## 运输单元类型-主表 t_lgm_shipunittype

- **表名称：** 运输单元类型-主表
- **表名：** t_lgm_shipunittype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [运输单元类型分组 lgm_shipunittypegrp](../lgm_files/lgm_shipunittypegrp.md) |
| 4 | fvolumeunitid | 容积单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | finsidewide | 内部尺寸宽 | numeric | 23 | 10 | √ | 0 | 内部尺寸宽 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fmaxvolume | 最大装载容积 | numeric | 23 | 10 | √ | 0 | 最大装载容积 |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fname | 名称 | varchar | 128 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fweightunitid | 重量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | finsidehigh | 内部尺寸高 | numeric | 23 | 10 | √ | 0 | 内部尺寸高 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fsyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 27 | fmaxload | 最大载重 | numeric | 23 | 10 | √ | 0 | 最大载重 |
| 28 | fenable | 禁用状态 | varchar | 5 |  | √ | ' ' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 30 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | finsidelong | 内部尺寸长 | numeric | 23 | 10 | √ | 0 | 内部尺寸长 |
| 32 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 33 | fsizeunitid | 尺寸单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_shipunittype_num |  | fnumber |
| 2 | pk_lgm_shipunittype |  | fid |
| 3 | idx_t_lgm_shipunittype_master |  | fmasterid |
| 4 | idx_lgm_shipunittype_ma |  | fmasterid |
| 5 | idx_t_lgm_shipunittype_createorg |  | fcreateorgid |
