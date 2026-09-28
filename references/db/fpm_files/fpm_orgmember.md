# 组织维度成员（废弃）-fpm_orgmember

## 组织维度成员（废弃）-多语言表 t_fpm_member_l

- **表名称：** 组织维度成员（废弃）-多语言表
- **表名：** t_fpm_member_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | inx_memberl_name |  | fname |
| 2 | pk_t_fpm_member_l |  | fpkid |

---

## 组织维度成员（废弃）-分表 t_fpm_member_e

- **表名称：** 组织维度成员（废弃）-分表
- **表名：** t_fpm_member_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgfield | forgfield | int8 | 64 |  | √ | 0 |  |
| 3 | fbeginorendmark | fbeginorendmark | varchar | 5 |  | √ | ' ' |  |
| 4 | fformulavalue | fformulavalue | varchar | 255 |  | √ | ' ' |  |
| 5 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 6 | fcaporg | fcaporg | int8 | 64 |  | √ | 0 |  |
| 7 | fissum | 是否汇总节点 | bpchar | 1 |  | √ | '0' | 是否汇总节点 |
| 8 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 9 | fdeclarestatus | fdeclarestatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fformulavalue_tag | fformulavalue_tag | text | 0 |  |  | ' ' |  |
| 11 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 12 | fyear | fyear | int4 | 32 |  | √ | 0 |  |
| 13 | fbodysysmanage | fbodysysmanage | int8 | 64 |  | √ | 0 |  |
| 14 | fformula | fformula | varchar | 1000 |  | √ | ' ' |  |
| 15 | fperiodtype | fperiodtype | varchar | 50 |  | √ | ' ' |  |
| 16 | freporttype | freporttype | varchar | 100 |  |  | ' ' |  |
| 17 | freporttype_c | freporttype_c | int8 | 64 |  | √ | 0 |  |
| 18 | fflow | fflow | varchar | 5 |  | √ | ' ' |  |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | flinksubject | flinksubject | int8 | 64 |  | √ | 0 |  |
| 21 | fways | fways | varchar | 5 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | inx_membere_ways |  | fways |
| 2 | pk_t_fpm_member_e |  | fid |

---

## 组织维度成员（废弃）-主表 t_fpm_member

- **表名称：** 组织维度成员（废弃）-主表
- **表名：** t_fpm_member

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodel | fmodel | varchar | 50 |  | √ | ' ' |  |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [组织维度成员（废弃） fpm_orgmember](../fpm_files/fpm_orgmember.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 500 |  | √ | ' ' |  |
| 9 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | [维度（废弃） fpm_dimension](../fpm_files/fpm_dimension.md) |
| 10 | fsourceid | 源ID | int8 | 64 |  | √ | 0 | 源ID |
| 11 | fserial | 序列号 | int8 | 64 |  | √ | 0 | 序列号 |
| 12 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 13 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 14 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | flevel | 层级 | int4 | 32 |  | √ | 0 | 层级 |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdimtype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型,枚举: Settlement Method :结算方式 Org :组织 Period :期间 Currency :币别 Subjects :科目 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fbodysystem | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 24 | fsourceparentid | 源父ID | int8 | 64 |  | √ | 0 | 源父ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_member_1 |  | fbodysystem |
| 2 | pk_t_fpm_member |  | fid |
| 3 | idx_fpm_member_2 |  | fdimtype |
| 4 | inx_dimmember_parentid |  | fparentid |
| 5 | idx_fpm_member_3 |  | fsourceid |
