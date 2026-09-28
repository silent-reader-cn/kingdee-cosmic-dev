# 税务产品-bastax_taxproduct

## 税务产品-主表 t_bastax_taxproduct

- **表名称：** 税务产品-主表
- **表名：** t_bastax_taxproduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fparentid | 上级税务产品 | int8 | 64 |  | √ | 0 | 税务产品 bastax_taxproduct |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 15 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 24 | fcountry | 国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxproduct |  | forgid |
| 2 | idx_t_bastax_taxproduct_master |  | fmasterid |
| 3 | pk_bastax_taxproduct |  | fid |
| 4 | idx_t_bastax_taxproduct_createorg |  | fcreateorgid |

---

## 税务产品-多语言表 t_bastax_taxproduct_l

- **表名称：** 税务产品-多语言表
- **表名：** t_bastax_taxproduct_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxproduct_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_taxproduct_l |  | fpkid |

---

## 税务产品-使用范围位图表 t_bastax_taxproduct_m

- **表名称：** 税务产品-使用范围位图表
- **表名：** t_bastax_taxproduct_m

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
| 1 | pk_t_bastax_taxproduct_m |  | forgid |

---

## 税务产品-使用范围表 t_bastax_taxproduct_u

- **表名称：** 税务产品-使用范围表
- **表名：** t_bastax_taxproduct_u

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
| 1 | pk_t_bastax_taxproduct_u |  | fdataid,fuseorgid |
| 2 | idx_t_bastax_taxproduct_u_uo |  | fuseorgid |
