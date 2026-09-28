# 经营报告配置-mai_bizreportcfg_new

## 单据体-子表 t_mai_chapter_entry

- **表名称：** 单据体-子表
- **表名：** t_mai_chapter_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchaptername | 章节名称 | varchar | 50 |  | √ | ' ' | 章节名称 |
| 3 | fsourceid | 源节点编码 | varchar | 50 |  | √ | ' ' | 源节点编码 |
| 4 | fnodeid | 树节点编码 | varchar | 50 |  | √ | ' ' | 树节点编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_chapter_entry_fid |  | fid |
| 2 | pk_t_mai_chapter_entry |  | fentryid |

---

## 接收用户-多选基础资料表 t_mai_reportuser

- **表名称：** 接收用户-多选基础资料表
- **表名：** t_mai_reportuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_reportuser |  | fid |
| 2 | pk_mai_reportuser |  | fpkid |

---

## 经营报告配置-多语言表 t_mai_bizreportcfg_new_l

- **表名称：** 经营报告配置-多语言表
- **表名：** t_mai_bizreportcfg_new_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 报告名称 | varchar | 100 |  | √ | ' ' | 报告名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_bizreportcfg_new_l |  | fpkid |
| 2 | idx_bizreportcfg_l_fid |  | fid |

---

## 指标引用单据体-子表 t_mai_index_quote_entry

- **表名称：** 指标引用单据体-子表
- **表名：** t_mai_index_quote_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcharttype | 图表展示 | varchar | 200 |  | √ | ' ' | 图表展示,枚举: bar :柱状图 line :折线图 horizon :横向图 pie :环形图 |
| 3 | findex | 指标名称 | int8 | 64 |  | √ | 0 | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |
| 4 | fdimensionid | 统计维度行id | varchar | 200 |  | √ | ' ' | 统计维度行id |
| 5 | fisimpute | 归因分析 | bpchar | 1 |  | √ | ' ' | 归因分析 |
| 6 | findexchapterid | 章节id | varchar | 200 |  | √ | ' ' | 章节id |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fischart | 是否展示图表 | bpchar | 1 |  | √ | ' ' | 是否展示图表 |
| 9 | ffilter_tag | 筛选条件属性_详情 | text | 0 |  |  | null | 筛选条件属性_详情 |
| 10 | fdategranularity | 时间粒度 | varchar | 200 |  | √ | ' ' | 时间粒度,枚举: year :年 quarter :季 month :月 day :日 |
| 11 | fsort | 排序字段 | varchar | 200 |  | √ | ' ' | 排序字段 |
| 12 | ffilter | 筛选条件属性 | varchar | 255 |  | √ | ' ' | 筛选条件属性 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ftop | 数据条数 | varchar | 20 |  | √ | ' ' | 数据条数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_index_quote_entry |  | fid |
| 2 | pk_mai_index_quote_entry |  | fentryid |

---

## 分析要求-子表 t_mai_req_entry

- **表名称：** 分析要求-子表
- **表名：** t_mai_req_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequestcontent | 分析要求 | varchar | 255 |  | √ | ' ' | 分析要求 |
| 3 | fnodeid | 树节点id | varchar | 50 |  | √ | ' ' | 树节点id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | frequestcontent_tag | 分析要求_详情 | text | 0 |  |  | null | 分析要求_详情 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_req_entry_fid |  | fid |
| 2 | pk_t_mai_req_entry |  | fentryid |

---

## 经营报告配置-主表 t_mai_bizreportcfg_new

- **表名称：** 经营报告配置-主表
- **表名：** t_mai_bizreportcfg_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 报告名称 | varchar | 50 |  | √ | ' ' | 报告名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frepeattime | 发送时间 | int4 | 32 |  | √ | 0 | 发送时间 |
| 7 | fapptype | 消息接收应用 | varchar | 50 |  | √ | ' ' | 消息接收应用,枚举: 0 :轻应用 1 :微信小程序 |
| 8 | frepeatday | 发送日期 | varchar | 50 |  | √ | ' ' | 发送日期,枚举: |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | frepeatmode | 发送频率 | varchar | 50 |  | √ | ' ' | 发送频率,枚举: DAY :每日 WEEK :每周 MONTH :每月 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftree | 树结构 | varchar | 255 |  | √ | ' ' | 树结构 |
| 14 | ftree_tag | 树结构_详情 | text | 0 |  |  | null | 树结构_详情 |
| 15 | fenable | 可用状态 | varchar | 10 |  | √ | '0' | 可用状态,枚举: 1 :启用 0 :禁用 |
| 16 | fbillno | 报告编码 | varchar | 30 |  | √ | ' ' | 报告编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bizreportcfgnew_fno |  | fbillno |
| 2 | pk_t_mai_bizreportcfg_new |  | fid |
