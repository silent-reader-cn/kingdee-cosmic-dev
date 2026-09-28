# 最低税额-bd_minimumtax

## 最低税额-主表 t_bd_minimumtax

- **表名称：** 最低税额-主表
- **表名：** t_bd_minimumtax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | ftaxarea | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 14 | fissystem | 系统预置 | varchar | 50 |  | √ | ' ' | 系统预置,枚举: 0 :否 1 :是 |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 18 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 22 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_minimumtax_master |  | fmasterid |
| 2 | idx_t_bd_minimumtax_createorg |  | fcreateorgid |
| 3 | pk_bd_minimumtax |  | fid |
| 4 | idx_t_bd_minimumtax_org |  | fuseorg,ftaxarea |

---

## 最低税额-多语言表 t_bd_minimumtax_l

- **表名称：** 最低税额-多语言表
- **表名：** t_bd_minimumtax_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_minimumtax_l_0 |  | fid,flocaleid |
| 2 | pk_bd_minimumtax_l |  | fpkid |

---

## 最低税额-使用范围表 t_bd_minimumtax_u

- **表名称：** 最低税额-使用范围表
- **表名：** t_bd_minimumtax_u

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
| 1 | idx_t_bd_minimumtax_u_uo |  | fuseorgid |
| 2 | pk_t_bd_minimumtax_u |  | fdataid,fuseorgid |

---

## 最低税额-子表 t_bd_minimumtax_entry

- **表名称：** 最低税额-子表
- **表名：** t_bd_minimumtax_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextentjson_tag | 区间json_详情 | text | 0 |  |  | null | 区间json_详情 |
| 3 | fextent | 区间 | varchar | 2000 |  | √ | ' ' | 区间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fminimumtax | 最低税额 | numeric | 23 | 10 | √ | 0 | 最低税额 |
| 6 | fextentjson | 区间json | varchar | 255 |  | √ | ' ' | 区间json |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_minimumtax_entry |  | fentryid |
| 2 | idx_bd_minimumtax_entry_fk |  | fid |
