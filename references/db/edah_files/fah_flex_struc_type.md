# 值集扩展字段定义-fah_flex_struc_type

## 值集扩展字段定义-子表 t_fah_flex_struc

- **表名称：** 值集扩展字段定义-子表
- **表名：** t_fah_flex_struc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freffieldnum | freffieldnum | varchar | 30 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fflexfieldnum | 数据位置 | varchar | 30 |  | √ | ' ' | 数据位置,枚举: ftxtattr1 :文本字段1 ftxtattr2 :文本字段2 ftxtattr3 :文本字段3 ftxtattr4 :文本字段4 ftxtattr5 :文本字段5 ftxtattr6 :文本字段6 ftxtattr7 :文本字段7 ftxtattr8 :文本字段8 ftxtattr9 :文本字段9 ftxtattr10 :文本字段10 ftxtattr11 :文本字段11 ftxtattr12 :文本字段12 ftxtattr13 :文本字段13 ftxtattr14 :文本字段14 ftxtattr15 :文本字段15 ftxtattr16 :文本字段16 ftxtattr17 :文本字段17 ftxtattr18 :文本字段18 ftxtattr19 :文本字段19 ftxtattr20 :文本字段20 |
| 6 | fattnum | 段编码 | varchar | 50 |  | √ | ' ' | 段编码 |
| 7 | fattdatatype | 数据类型 | varchar | 2 |  | √ | ' ' | 数据类型,枚举: 6 :文本 1 :基础资料 2 :辅助资料 20 :外部数据值集 |
| 8 | ffieldusagetype | 字段的使用类型 | int2 | 16 |  | √ | 0 | 字段的使用类型 |
| 9 | fattname | 段名称 | varchar | 50 |  | √ | ' ' | 段名称 |
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

---

## 值集扩展字段定义-主表 t_fah_flex_struc_type

- **表名称：** 值集扩展字段定义-主表
- **表名：** t_fah_flex_struc_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fenable | 启用状态 | bpchar | 1 |  | √ | ' ' | 启用状态 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fah_flex_struc_type |  | fid |
| 2 | idx_fah_flex_struc_type_no |  | fnumber |
