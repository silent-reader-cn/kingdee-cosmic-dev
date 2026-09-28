# 数据来源-fgptas_datatableconfig

## 数据表数据规范-多语言表 t_fgptas_dtxkdatasr_l

- **表名称：** 数据表数据规范-多语言表
- **表名：** t_fgptas_dtxkdatasr_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffielddesc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 2 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_dtxkdatasr_l_0 |  | fentryid,flocaleid |
| 2 | pk_fgptas_dtxkdatasr_l |  | fpkid |

---

## 数据来源-主表 t_fgptas_datatableconfig

- **表名称：** 数据来源-主表
- **表名：** t_fgptas_datatableconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 数据表名称 | varchar | 255 |  | √ | ' ' | 数据表名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsourceapp | 报表数据来源 | varchar | 50 |  | √ | ' ' | 报表数据来源,枚举: 1 :报表应用 2 :合并报表应用 3 :总账 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fmgrpttype | 报表类型 | varchar | 10 |  | √ | '2' | 报表类型,枚举: 1 :合并报表 2 :个别报表 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fouterdatatable | 外部数据表 | int8 | 64 |  | √ | 0 | [外部数据表 fgptas_outer_datatable](../fgptas_files/fgptas_outer_datatable.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fpreset | 预置 | bpchar | 1 |  | √ | ' ' | 预置 |
| 15 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftemplateschema | ftemplateschema | int8 | 64 |  | √ | 0 |  |
| 17 | ftemplateschemaid | 模板样式方案 | varchar | 60 |  | √ | ' ' | 模板样式方案,枚举: |
| 18 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fdatasource | 数据表来源 | varchar | 50 |  | √ | ' ' | 数据表来源,枚举: 1 :星空财务报表 2 :外部数据 |
| 20 | fmetareporttype | 主表类型 | varchar | 50 |  | √ | ' ' | 主表类型,枚举: 1 :资产负债表 2 :利润表 3 :现金流量表 |
| 21 | fmergeschema | 报表合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 22 | fnumber | 数据表编号 | varchar | 30 |  | √ | ' ' | 数据表编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_dtbconfig_number |  | fnumber |
| 2 | pk_fgptas_datatableconfig |  | fid |

---

## 外部数据表数据规范-多语言表 t_fgptas_otifsrentry_l

- **表名称：** 外部数据表数据规范-多语言表
- **表名：** t_fgptas_otifsrentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fouterfieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_otifsrentry_l |  | fpkid |
| 2 | idx_fgptas_otifsrentry_l_0 |  | fentryid,flocaleid |

---

## 外部数据表数据规范-子表 t_fgptas_otifsrentry

- **表名称：** 外部数据表数据规范-子表
- **表名：** t_fgptas_otifsrentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fouterfieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: Basedata :基础资料 Text :文本 Integer :数值 Date :日期 Assistant :辅助资料 Combo :下拉列表 |
| 3 | fottbmappingid | 查询参数映射 | int8 | 64 |  | √ | 0 | [查询参数 fgptas_tablecolmapping](../fgptas_files/fgptas_tablecolmapping.md) |
| 4 | fouterfieldnumber | 字段编码 | varchar | 100 |  | √ | ' ' | 字段编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fvaluetype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型,枚举: 1 :基本信息 2 :字段 |
| 7 | fouterfieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_otifsrentry_fk |  | fid |
| 2 | pk_fgptas_otifsrentry |  | fentryid |

---

## 报表项目规范-子表 t_fgptas_dtxkprojectsr

- **表名称：** 报表项目规范-子表
- **表名：** t_fgptas_dtxkprojectsr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 3 | fprojectnumber | 项目编码 | varchar | 25 |  | √ | ' ' | 项目编码 |
| 4 | fprojectid | 源项目id | int8 | 64 |  | √ | 0 | 源项目id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fprojectdesc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_dtxkprojectsr |  | fentryid |
| 2 | idx_fgptas_dtxkprojectsr_fk |  | fid |

---

## 报表项目规范-多语言表 t_fgptas_dtxkprojectsr_l

- **表名称：** 报表项目规范-多语言表
- **表名：** t_fgptas_dtxkprojectsr_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprojectname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fprojectdesc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_dtxkprojectsr_l |  | fpkid |
| 2 | idx_fgptas_dtxkprojectsr_l_0 |  | fentryid,flocaleid |

---

## 数据来源-多语言表 t_fgptas_datatableconfig_l

- **表名称：** 数据来源-多语言表
- **表名：** t_fgptas_datatableconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据表名称 | varchar | 255 |  | √ | ' ' | 数据表名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_dtbconfig_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_datatableconfig_l |  | fpkid |

---

## 数据表数据规范-子表 t_fgptas_dtxkdatasr

- **表名称：** 数据表数据规范-子表
- **表名：** t_fgptas_dtxkdatasr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 字段编码 | varchar | 25 |  | √ | ' ' | 字段编码 |
| 3 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: Text :单行文本 Integer :整数 Decimal :小数 Basedata :基础资料 Assistant :辅助资料 Combo :下拉列表 Org :组织 Supplier :供应商 User :用户 Customer :客户 Currency :币别 Amount :金额 Materiel :物料 |
| 4 | ffielddesc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 5 | ffieldmappingid | 查询参数映射 | int8 | 64 |  | √ | 0 | [查询参数 fgptas_tablecolmapping](../fgptas_files/fgptas_tablecolmapping.md) |
| 6 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_dtxkdatasr |  | fentryid |
| 2 | idx_fgptas_dtxkdatasr_fk |  | fid |
