# 映射结构弹性域元数据定义-fah_flex_struc

## 映射结构弹性域元数据定义-主表 t_fah_flex_struc

- **表名称：** 映射结构弹性域元数据定义-主表
- **表名：** t_fah_flex_struc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 所属父记录ID | int8 | 64 |  | √ | 0 | [映射结构定义 fah_valmap_struc](../edah_files/fah_valmap_struc.md) |
| 2 | freffieldnum | 下拉列表所在的字段 | varchar | 30 |  | √ | ' ' | 下拉列表所在的字段 |
| 3 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fflexfieldnum | 存储的弹性域字段编码 | varchar | 30 |  | √ | ' ' | 存储的弹性域字段编码 |
| 6 | fattnum | 属性的编码 | varchar | 50 |  | √ | ' ' | 属性的编码 |
| 7 | fattdatatype | 数据类型 | varchar | 2 |  | √ | ' ' | 数据类型,枚举: |
| 8 | ffieldusagetype | 字段的使用类型 | int2 | 16 |  | √ | 0 | 字段的使用类型 |
| 9 | fattname | 属性的展示名称 | varchar | 50 |  | √ | ' ' | 属性的展示名称 |
| 10 | frefentity | 引用的实体对象 | varchar | 50 |  | √ | ' ' | 引用的实体对象 |
| 11 | freftypeid | 引用的类型id | int8 | 64 |  | √ | 0 | 引用的类型id |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fownernum | 来源类型的元数据编码 | varchar | 30 |  | √ | ' ' | 来源类型的元数据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fah_flex_struc |  | fentryid |
| 2 | idx_fah_flex_struc_f |  | fid,fattnum |
