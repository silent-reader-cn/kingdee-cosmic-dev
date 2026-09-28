# 币别维度成员（废弃）-fpm_currencymember

## 币别维度成员（废弃）-多语言表 t_fpm_member_l

- **表名称：** 币别维度成员（废弃）-多语言表
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

## 币别维度成员（废弃）-主表 t_fpm_member

- **表名称：** 币别维度成员（废弃）-主表
- **表名：** t_fpm_member

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodel | fmodel | varchar | 50 |  | √ | ' ' |  |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [币别维度成员（废弃） fpm_currencymember](../fpm_files/fpm_currencymember.md) |
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
