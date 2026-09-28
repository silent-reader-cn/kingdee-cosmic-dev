# 客户分类-bd_customergroup

## 客户分类-主表 t_bd_customergroup

- **表名称：** 客户分类-主表
- **表名：** t_bd_customergroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  |  | null | 是否叶子 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | 客户分类 bd_customergroup |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | flongnumber | 长编码 | varchar | 255 |  |  | null | 长编码 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | 人员 bos_user |
| 11 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 12 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | flevel | 级次 | int8 | 64 |  |  | null | 级次 |
| 15 | fstatus | 数据状态 | varchar | 10 |  |  | null | 数据状态,枚举: Z :暂存 A :创建 B :已提交 C :已审核 |
| 16 | fstandardid | 客户分类标准 | int8 | 64 |  | √ | 0 | 客户分类标准 bd_customergroupstandard |
| 17 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 19 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_customergroup_number |  | fnumber |
| 2 | t_bd_customergroup_pkey |  | fid |
| 3 | idx_t_bd_customergroup_combine |  | fstandardid,fparentid,fcreateorgid |

---

## 客户分类-多语言表 t_bd_customergroup_l

- **表名称：** 客户分类-多语言表
- **表名：** t_bd_customergroup_l

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
| 1 | idx_t_bd_customergroup_l_fid |  | fid,flocaleid |
| 2 | t_bd_customergroup_l_pkey |  | fpkid |
