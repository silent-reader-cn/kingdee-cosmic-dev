# 财务报告模板-fgptas_fireporttemplate

## 查询参数-多选基础资料表 t_fgptas_templ_qparam

- **表名称：** 查询参数-多选基础资料表
- **表名：** t_fgptas_templ_qparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [查询参数 fgptas_tablecolmapping](../fgptas_files/fgptas_tablecolmapping.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_templqparam_fk |  | fid |
| 2 | pk_fgptas_templ_qparam |  | fpkid |

---

## 财务报告模板-多语言表 t_fgptas_fireporttemplate_l

- **表名称：** 财务报告模板-多语言表
- **表名：** t_fgptas_fireporttemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_fireporttemplate_l |  | fpkid |
| 2 | idx_fgptas_firpttpl_l_0 |  | fid,flocaleid |

---

## 财务报告模板-主表 t_fgptas_fireporttemplate

- **表名称：** 财务报告模板-主表
- **表名：** t_fgptas_fireporttemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcovercontent | 封面内容 | varchar | 255 |  | √ | ' ' | 封面内容 |
| 3 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdocumenttype | 文档类型 | varchar | 50 |  | √ | '1' | 文档类型,枚举: 1 :Word 2 :PPT |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 15 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_fireporttemplate |  | fid |
| 2 | idx_fgptas_tmplnumber |  | fnumber |

---

## 报告大纲-子表 t_fgptas_templateoutline

- **表名称：** 报告大纲-子表
- **表名：** t_fgptas_templateoutline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparentid | 大纲父节点id | varchar | 50 |  | √ | ' ' | 大纲父节点id |
| 3 | fparagraphid | 大纲章节 | int8 | 64 |  | √ | 0 | 大纲章节 |
| 4 | fnodeid | 大纲节点id | varchar | 50 |  | √ | ' ' | 大纲节点id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foutlinenumber | 大纲编码 | varchar | 50 |  | √ | ' ' | 大纲编码 |
| 7 | fparagraphisinlib | 章节是否来源章节库 | bpchar | 1 |  | √ | ' ' | 章节是否来源章节库 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | foutlinename | 大纲名称 | varchar | 255 |  | √ | ' ' | 大纲名称 |
| 10 | flayoutjson | 布局类型 | varchar | 2000 |  | √ | '{}' | 布局类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_templateol_pk |  | fid |
| 2 | pk_fgptas_templateoutline |  | fentryid |

---

## 报告大纲-多语言表 t_fgptas_templateoutline_l

- **表名称：** 报告大纲-多语言表
- **表名：** t_fgptas_templateoutline_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | foutlinename | 大纲名称 | varchar | 255 |  | √ | ' ' | 大纲名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_templateol_l_0 |  | fentryid,flocaleid |
| 2 | pk_fgptas_templateoutline_l |  | fpkid |
