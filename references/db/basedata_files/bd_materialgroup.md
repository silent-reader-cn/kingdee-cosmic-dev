# 物料分类-bd_materialgroup

## 物料分类-多语言表 t_bd_materialgroup_l

- **表名称：** 物料分类-多语言表
- **表名：** t_bd_materialgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 255 |  |  | null | 名称 |
| 3 | ffullname | 全称 | varchar | 255 |  |  | null | 全称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_materialgroup_l_pkey |  | fpkid |
| 2 | idx_t_bd_materialgroup_l_fid |  | fid,flocaleid |

---

## 物料分类-主表 t_bd_materialgroup

- **表名称：** 物料分类-主表
- **表名：** t_bd_materialgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fsuppliervisible | 供应商可见 | bpchar | 1 |  | √ | '0' | 供应商可见 |
| 5 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 10 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 10 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | flongnumber | 长编码 | varchar | 255 |  |  | null | 长编码 |
| 17 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 20 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '' | 控制策略,枚举: 1 :全局共享 2 :私有 |
| 21 | flevel | 级次 | int8 | 64 |  |  | null | 级次 |
| 22 | fstandardid | 物料分类标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 25 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_materialgroup_combine |  | fstandardid,fparentid,fcreateorgid |
| 2 | t_bd_materialgroup_pkey |  | fid |
| 3 | idx_t_bd_materialgroup_number |  | fnumber |
