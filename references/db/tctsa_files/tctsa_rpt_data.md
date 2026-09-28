# 报表数据集-tctsa_rpt_data

## 值单据体-子表 t_tctsa_rpt_value

- **表名称：** 值单据体-子表
- **表名：** t_tctsa_rpt_value

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: str :字符串 je :金额 sl :数量 id :ID date :日期 xs :小数 |
| 3 | ffieldno | 字段编码 | varchar | 200 |  | √ | ' ' | 字段编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fvalueargjson | 自定义过滤条件 | varchar | 2000 |  | √ | ' ' | 自定义过滤条件 |
| 6 | fvaluedefaultformula | 预设表达式 | varchar | 50 |  | √ | ' ' | 预设表达式,枚举: |
| 7 | fvaluename | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 8 | fvalueformula | 自定义计算表达式 | varchar | 2000 |  | √ | ' ' | 自定义计算表达式 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fvalueargname | 自定义参数 | varchar | 2000 |  | √ | ' ' | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_rpt_value |  | fentryid |
| 2 | idx_tctsa_rpt_value_fk |  | fid |

---

## 参数单据体-子表 t_tctsa_rpt_arg

- **表名称：** 参数单据体-子表
- **表名：** t_tctsa_rpt_arg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fargname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称,枚举: |
| 3 | fargdebug | 调试参数 | varchar | 2000 |  | √ | ' ' | 调试参数 |
| 4 | fargtype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: Org :Org Long :Long Text :Text BillStatus :BillStatus Combo :Combo Boolean :Boolean Basedata :Basedata Date :Date DateTime :DateTime Varchar :Varchar |
| 5 | fargdefault | 默认值 | varchar | 2000 |  | √ | ' ' | 默认值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fargmustinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 9 | fargunique | 是否唯一 | bpchar | 1 |  | √ | '0' | 是否唯一 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_rpt_arg |  | fentryid |
| 2 | idx_tctsa_rpt_arg_fk |  | fid |

---

## 报表数据集-主表 t_tctsa_rpt_data

- **表名称：** 报表数据集-主表
- **表名：** t_tctsa_rpt_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsbbtwotype | 2.0申报表模板 | varchar | 50 |  | √ | ' ' | 2.0申报表模板,枚举: |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fplugintype | 插件类型 | varchar | 50 |  | √ | ' ' | 插件类型,枚举: vat :海外增值税 usacit :美国所得税 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 数据集类型 | varchar | 50 |  | √ | ' ' | 数据集类型,枚举: 3.0 :3.0申报表 2.0 :2.0申报表 tz :台账(凭证、基础资料) |
| 13 | ftable | 台账元数据标识 | varchar | 50 |  | √ | ' ' | 台账元数据标识,枚举: |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fsbbtype | 3.0申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_rptdata_num |  | fnumber |
| 2 | pk_tctsa_rpt_data |  | fid |

---

## 报表数据集-多语言表 t_tctsa_rpt_data_l

- **表名称：** 报表数据集-多语言表
- **表名：** t_tctsa_rpt_data_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_rpt_data_l |  | fpkid |
| 2 | idx_tctsa_rpt_data_l_0 |  | fid,flocaleid |

---

## 单元格单据体-子表 t_tctsa_rpt_cell

- **表名称：** 单元格单据体-子表
- **表名：** t_tctsa_rpt_cell

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcellbref | 申报表表头取值 | varchar | 50 |  | √ | ' ' | 申报表表头取值,枚举: |
| 3 | fcelltype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: str :字符串 je :金额 sl :数量 id :ID date :时间 xs :小数 |
| 4 | fcellno | 字段编码 | varchar | 200 |  | √ | ' ' | 字段编码 |
| 5 | fcellargjson | 自定义过滤条件 | varchar | 2000 |  | √ | ' ' | 自定义过滤条件 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcellname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 8 | fcelljczllw | 基础资料列维 | int8 | 64 |  | √ | 0 | 列维成员管理 tpo_col_member |
| 9 | fcellargname | 自定义参数 | varchar | 2000 |  | √ | ' ' | 自定义参数 |
| 10 | fcellby | 取值方式 | varchar | 50 |  | √ | ' ' | 取值方式,枚举: bt :取表头 gd :取固定格 dth :取动态行 |
| 11 | fcellremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 12 | fcellfield | 台账字段名称 | varchar | 50 |  | √ | ' ' | 台账字段名称 |
| 13 | fcellhw | 行维 | int8 | 64 |  | √ | 0 | 行维成员管理 tpo_row_member |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fcelllw | 列维 | int8 | 64 |  | √ | 0 | 列维成员管理 tpo_col_member |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_rpt_cell |  | fentryid |
| 2 | idx_tctsa_rpt_cell_fk |  | fid |
