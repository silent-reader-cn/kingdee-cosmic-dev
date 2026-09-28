# 维度成员模板_计划科目（废弃）-fpm_membersubject

## 维度成员模板_计划科目（废弃）-多语言表 t_fpm_member_l

- **表名称：** 维度成员模板_计划科目（废弃）-多语言表
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

## 维度成员模板_计划科目（废弃）-分表 t_fpm_member_e

- **表名称：** 维度成员模板_计划科目（废弃）-分表
- **表名：** t_fpm_member_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgfield | 关联资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbeginorendmark | 期初期末标志 | varchar | 5 |  | √ | ' ' | 期初期末标志,枚举: 1 :期初 2 :期末 |
| 4 | fformulavalue | 公式值 | varchar | 255 |  | √ | ' ' | 公式值 |
| 5 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 6 | fcaporg | 关联业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fissum | 是否汇总节点 | bpchar | 1 |  | √ | '0' | 是否汇总节点 |
| 8 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fdeclarestatus | fdeclarestatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fformulavalue_tag | 公式值_详情 | text | 0 |  |  | ' ' | 公式值_详情 |
| 11 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 12 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 13 | fbodysysmanage | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 14 | fformula | 公式 | varchar | 1000 |  | √ | ' ' | 公式 |
| 15 | fperiodtype | 编报期间类型 | varchar | 50 |  | √ | ' ' | 编报期间类型,枚举: D :日 MW :周 TD :旬 M :月 YW :周 Y :年 |
| 16 | freporttype | freporttype | varchar | 100 |  |  | ' ' |  |
| 17 | freporttype_c | 编报类型 | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 18 | fflow | 流向 | varchar | 5 |  | √ | ' ' | 流向,枚举: A :余额 B :流入 C :流出 |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | flinksubject | 对应期初科目 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 21 | fways | 填报方式 | varchar | 5 |  | √ | ' ' | 填报方式,枚举: 0 :手工录入 1 :公式项 2 :汇总项 3 :明细填报 |

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

## 维度成员模板_计划科目（废弃）-主表 t_fpm_member

- **表名称：** 维度成员模板_计划科目（废弃）-主表
- **表名：** t_fpm_member

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodel | fmodel | varchar | 50 |  | √ | ' ' |  |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 6 | fparentid | 上级科目名称 | int8 | 64 |  | √ | 0 | [维度成员模板_计划科目（废弃） fpm_membersubject](../fpm_files/fpm_membersubject.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 500 |  | √ | ' ' |  |
| 9 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | [维度（废弃） fpm_dimension](../fpm_files/fpm_dimension.md) |
| 10 | fsourceid | 源ID | int8 | 64 |  | √ | 0 | 源ID |
| 11 | fserial | 序列号 | int8 | 64 |  | √ | 0 | 序列号 |
| 12 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 13 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 14 | forg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdimtype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型,枚举: Settlement Method :结算方式 Org :编报主体 Period :期间 Currency :币别 Subjects :科目 Company :公司 |
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
