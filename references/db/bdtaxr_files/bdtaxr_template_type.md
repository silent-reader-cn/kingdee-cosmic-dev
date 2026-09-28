# 模板类型-bdtaxr_template_type

## 税种-多选基础资料表 t_bdtaxr_template_taxtype

- **表名称：** 税种-多选基础资料表
- **表名：** t_bdtaxr_template_taxtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [税务云税种分类 bdtaxr_tax_type](../bdtaxr_files/bdtaxr_tax_type.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_template_taxtype_fk |  | fid |
| 2 | pk_bdtaxr_template_taxtype |  | fpkid |

---

## 单据体-子表 t_bdtaxr_templatetype_det

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_templatetype_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fentityname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentityid | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_templatetype_det |  | fentryid |
| 2 | idx_bdtaxr_templatetype_det_fk |  | fid |

---

## 模板类型-主表 t_bdtaxr_templatetype

- **表名称：** 模板类型-主表
- **表名：** t_bdtaxr_templatetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 类型名称 | varchar | 50 |  | √ | ' ' | 类型名称 |
| 3 | funiquetype | 唯一约束 | varchar | 50 |  | √ | ' ' | 唯一约束,枚举: unique :唯一 multiple :不唯一 number :编码唯一 |
| 4 | fmaintable | 主表 | varchar | 50 |  | √ | ' ' | 主表,枚举: tcvat_nsrxx :纳税申报主表 tdm_finance_main :财务报表主表 |
| 5 | fnumber | 类型编码 | varchar | 50 |  | √ | ' ' | 类型编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_templatetype |  | fnumber |
| 2 | pk_bdtaxr_templatetype |  | fid |
