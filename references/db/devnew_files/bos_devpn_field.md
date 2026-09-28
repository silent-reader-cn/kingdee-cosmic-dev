# 标准字段-bos_devpn_field

## 标准字段-多语言表 t_meta_fields_l

- **表名称：** 标准字段-多语言表
- **表名：** t_meta_fields_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_meta_fields_l_fid |  | fid,flocaleid |
| 2 | pk_t_meta_fields_l |  | fpkid |

---

## 单据体-子表 t_meta_fieldsentry

- **表名称：** 单据体-子表
- **表名：** t_meta_fieldsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 关联方式 | varchar | 50 |  | √ | ' ' | 关联方式,枚举: A :映射 R :引用 |
| 3 | ffieldcaption | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentityid | 实体对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffieldid | 字段id | varchar | 50 |  | √ | ' ' | 字段id |
| 8 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_meta_fieldsentry |  | fid,fseq |
| 2 | pk_meta_fieldsentry |  | fentryid |

---

## 标准字段-主表 t_meta_fields

- **表名称：** 标准字段-主表
- **表名：** t_meta_fields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fxml | xml | varchar | 255 |  | √ | ' ' | xml |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffieldname | 数据库字段名 | varchar | 50 |  | √ | ' ' | 数据库字段名 |
| 7 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fxml_tag | xml_详情 | text | 0 |  |  | null | xml_详情 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fdatastatus | 状态 | bpchar | 1 |  | √ | 'a' | 状态,枚举: a :草案 b :试用 c :标准 d :废止 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ffieldtype | 类型 | varchar | 50 |  |  | ' ' | 类型,枚举: TextProp :文本 TextAreaProp :多行文本 LargeTextProp :大文本 MuliLangTextProp :多语言文本 IntegerProp :整数 BigIntProp :长整数 DecimalProp :小数 DateProp :日期 DateTimeProp :长日期 TimeProp :时间 BooleanProp :复选框 ComboProp :下拉列表 MulComboProp :多选下拉列表 |
| 16 | flistitem | flistitem | varchar | 900 |  | √ | ' ' |  |
| 17 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fdesc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_meta_fields |  | fnumber |
| 2 | pk_t_meta_fields |  | fid |
