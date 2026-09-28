# 财务报告章节-fgptas_reportparagraph

## 财务报告章节-多语言表 t_fgptas_reportparagraph_l

- **表名称：** 财务报告章节-多语言表
- **表名：** t_fgptas_reportparagraph_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fbackground |  | varchar | 1800 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_reportparagraph_l |  | fpkid |
| 2 | idx_fgptas_rptparagraph_l_0 |  | fid,flocaleid |

---

## 数据来源-子表 t_fgptas_paragraphds

- **表名称：** 数据来源-子表
- **表名：** t_fgptas_paragraphds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatatablefield | 数据表字段 | varchar | 2000 |  | √ | ' ' | 数据表字段,枚举: |
| 3 | ffiltercondition_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 7 | fdatatableid | 数据表编码 | int8 | 64 |  | √ | 0 | [数据来源 fgptas_datatableconfig](../fgptas_files/fgptas_datatableconfig.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_paragraphds_fk |  | fid |
| 2 | pk_fgptas_paragraphds |  | fentryid |

---

## 财务报告章节-主表 t_fgptas_reportparagraph

- **表名称：** 财务报告章节-主表
- **表名：** t_fgptas_reportparagraph

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbackground |  | varchar | 600 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_rppgnumber |  | fnumber |
| 2 | pk_fgptas_reportparagraph |  | fid |

---

## 内容要求-子表 t_fgptas_paragraphcr

- **表名称：** 内容要求-子表
- **表名：** t_fgptas_paragraphcr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontentdsid | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: |
| 3 | fcontentrequiretext_tag | 内容要求_详情 | text | 0 |  |  | null | 内容要求_详情 |
| 4 | frowindex | 行ID | int4 | 32 |  | √ | 0 | 行ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcontenttype | 内容类型 | varchar | 50 |  | √ | ' ' | 内容类型,枚举: 1 :图表 2 :文本 |
| 7 | fcontentrequiretext | 内容要求 | varchar | 255 |  | √ | ' ' | 内容要求 |
| 8 | fcrfiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcrfiltercondition_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_paragraphcr |  | fentryid |
| 2 | idx_fgptas_paragraphcr_fk |  | fid |
