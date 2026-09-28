# 通用审核单类型分类-task_isomertasktype_group

## 通用审核单类型分类-使用范围表 t_tk_isomertasktype_group_u

- **表名称：** 通用审核单类型分类-使用范围表
- **表名：** t_tk_isomertasktype_group_u

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
| 1 | idx_t_tk_isomertasktype_group_u_uo |  | fuseorgid |
| 2 | pk_t_tk_isomertasktype_group_u |  | fdataid,fuseorgid |

---

## 通用审核单类型分类-多语言表 t_tk_isomertasktype_group_l

- **表名称：** 通用审核单类型分类-多语言表
- **表名：** t_tk_isomertasktype_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 512 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_isomertasktype_group_l |  | fpkid |
| 2 | idx_ssc_isomtasktype_group_l |  | fid,flocaleid |

---

## 通用审核单类型分类-使用范围位图表 t_tk_isomertasktype_group_m

- **表名称：** 通用审核单类型分类-使用范围位图表
- **表名：** t_tk_isomertasktype_group_m

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
| 1 | pk_t_tk_isomertasktype_group_m |  | forgid |

---

## 通用审核单类型分类-主表 t_tk_isomertasktype_group

- **表名称：** 通用审核单类型分类-主表
- **表名：** t_tk_isomertasktype_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 7 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 通用审核单类型分类 task_isomertasktype_group |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_isomtasktype_parentid |  | fparentid |
| 2 | idx_t_tk_isomertasktype_group_createorg |  | fcreateorgid |
| 3 | idx_t_tk_isomertasktype_group_master |  | fmasterid |
| 4 | pk_t_tk_isomertasktype_group |  | fid |
