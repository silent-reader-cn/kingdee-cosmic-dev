# 财务报告模版-fgptas_fireport_template

## 报告大纲-子表 t_fgptas_outline

- **表名称：** 报告大纲-子表
- **表名：** t_fgptas_outline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisleaf | 是否末级 | bpchar | 1 |  | √ | '0' | 是否末级 |
| 3 | foutlinelevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 4 | fbackgroundprompt | 背景说明 | varchar | 500 |  | √ | ' ' | 背景说明 |
| 5 | fcontentprompt_tag | 内容要求_详情 | text | 0 |  |  | null | 内容要求_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | foutlinenumber | 大纲编码 | varchar | 50 |  | √ | ' ' | 大纲编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | foutlinename | 大纲名称 | varchar | 50 |  | √ | ' ' | 大纲名称 |
| 11 | fcontentprompt | 内容要求 | varchar | 255 |  | √ | ' ' | 内容要求 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_outline |  | fentryid |
| 2 | idx_fgptas_outline_fk |  | fid |

---

## 数据来源-子表 t_fgpta_datasource

- **表名称：** 数据来源-子表
- **表名：** t_fgpta_datasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdataprop | 数据表列 | varchar | 255 |  | √ | ' ' | 数据表列 |
| 2 | fdatafilter | 维度条件 | varchar | 255 |  | √ | ' ' | 维度条件 |
| 3 | fdatafiltervalue_tag | 维度条件json_详情 | text | 0 |  |  | null | 维度条件json_详情 |
| 4 | fdatafiltervalue | 维度条件json | varchar | 255 |  | √ | ' ' | 维度条件json |
| 5 | fdatatable | 数据表 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 6 | fdatapropnumber | 数据表列编码 | varchar | 255 |  | √ | ' ' | 数据表列编码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgpta_datasource |  | fdetailid |
| 2 | idx_fgpta_datasource_fk |  | fentryid |

---

## 财务报告模版-主表 t_fgptas_reporttempl

- **表名称：** 财务报告模版-主表
- **表名：** t_fgptas_reporttempl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcovercontent | 封面内容 | varchar | 255 |  | √ | ' ' | 封面内容 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmodeltype | 模型风格 | varchar | 15 |  | √ | ' ' | 模型风格,枚举: |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | freporttitle | 报告名称 | varchar | 50 |  | √ | ' ' | 报告名称 |
| 10 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '7' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | freporttype | 财务报告类型 | int8 | 64 |  | √ | 0 | 财务报告类型 fgptas_report_type |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 24 | flanmodel | 语言模型 | varchar | 15 |  | √ | ' ' | 语言模型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_reporttempl |  | fid |
| 2 | idx_t_fgptas_reporttempl_createorg |  | fcreateorgid |
| 3 | idx_fgptas_reporttempl_no |  | fnumber |
| 4 | idx_t_fgptas_reporttempl_master |  | fmasterid |

---

## 财务报告模版-使用范围表 t_fgptas_reporttempl_u

- **表名称：** 财务报告模版-使用范围表
- **表名：** t_fgptas_reporttempl_u

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
| 1 | idx_t_fgptas_reporttempl_u_uo |  | fuseorgid |
| 2 | pk_t_fgptas_reporttempl_u |  | fdataid,fuseorgid |

---

## 数据整体要求-多选基础资料表 t_fgptas_datarequire

- **表名称：** 数据整体要求-多选基础资料表
- **表名：** t_fgptas_datarequire

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 数据表字段映射 fgptas_tablecol_mapping |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_datarequire |  | fpkid |
| 2 | idx_fgptas_datarequire_fk |  | fid |

---

## 财务报告模版-多语言表 t_fgptas_reporttempl_l

- **表名称：** 财务报告模版-多语言表
- **表名：** t_fgptas_reporttempl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | freporttitle | 报告名称 | varchar | 50 |  | √ | ' ' | 报告名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_reporttempl_l |  | fpkid |
| 2 | idx_fgptas_reporttempl_l_0 |  | fid,flocaleid |
