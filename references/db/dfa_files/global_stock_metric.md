# 全球股票指标-global_stock_metric

## 全球股票指标-主表 t_dfa_global_stock_metric

- **表名称：** 全球股票指标-主表
- **表名：** t_dfa_global_stock_metric

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | fisleaf | bpchar | 1 |  | √ | '1' |  |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [全球股票指标分组 global_stock_metric_group](../dfa_files/global_stock_metric_group.md) |
| 4 | fmodeltype | 财务健康评价模型分类 | varchar | 50 |  |  | ' ' | 财务健康评价模型分类,枚举: 695011 :盈利能力 695056 :收益质量 695110 :成长能力 695141 :资本结构 695157 :偿债能力 695179 :营运能力 695202 :现金流量 696153 :保险业专项指标 696275 :银行业专项指标 |
| 5 | fswitch_unit_zh | 中文转换单位 | varchar | 50 |  |  | ' ' | 中文转换单位,枚举: 0 :<无> yuan :元 ten_thousand :万元 hundred_million :亿元 percent :% |
| 6 | fmodeltypellm | 推送给大模型能力分类 | varchar | 1000 |  | √ | ' ' | 推送给大模型能力分类,枚举: 核心财务表现 :核心财务表现 主营业务变化分析 :主营业务变化分析 战略动向分析 :战略动向分析 风险扫描 :风险扫描 人效分析 :人效分析 费用分析 :费用分析 盈利能力分析 :盈利能力分析 成长能力分析 :成长能力分析 偿债能力分析 :偿债能力分析 营运能力分析 :营运能力分析 现金流分析 :现金流分析 资产质量分析 :资产质量分析 未来预测 :未来预测 三表主要项目分析 :三表主要项目分析 行业变化分析 :行业变化分析 指标对比 :指标对比 季报指标 :季报指标 基础信息(公共) :基础信息(公共) 财报分析简报 :财报分析简报 研发情况 :研发情况 公司信息 :公司信息 |
| 7 | fparams | 参数类型列表 | varchar | 50 |  | √ | ' ' | 参数类型列表 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fstatement_type | fstatement_type | varchar | 50 |  | √ | ' ' |  |
| 11 | fis_queryable | 是否允许大模型查询 | bpchar | 1 |  | √ | '0' | 是否允许大模型查询 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fdata_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型 |
| 15 | fparam_values | 参数值 | varchar | 1000 |  | √ | ' ' | 参数值 |
| 16 | fnamedescribe | 指标说明 | varchar | 1000 |  |  | ' ' | 指标说明 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 1000 |  | √ | ' ' | 名称 |
| 19 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fshowrow | 显示顺序 | int8 | 64 |  | √ | 0 | 显示顺序 |
| 22 | flongnumber | flongnumber | varchar | 50 |  | √ | ' ' |  |
| 23 | fissend | 是否推送大模型 | bpchar | 1 |  | √ | '0' | 是否推送大模型 |
| 24 | fparam_count | 参数数量 | int4 | 32 |  | √ | 0 | 参数数量 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 27 | fswitch_unit_en | 英文转换单位 | varchar | 50 |  |  | ' ' | 英文转换单位,枚举: 0 :<无> yuan :yuan(元) thousand :thousand(千元) million :million(百万) billion :billion(十亿) percent :% |
| 28 | funit | 原始单位 | varchar | 50 |  | √ | ' ' | 原始单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_global_stock_metric |  | fnumber |
| 2 | pk_dfa_global_stock_metric |  | fid |

---

## 全球股票指标-多语言表 t_dfa_global_stock_metric_l

- **表名称：** 全球股票指标-多语言表
- **表名：** t_dfa_global_stock_metric_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 1000 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 1000 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_global_stock_metric_l |  | fpkid |
| 2 | idx_dfa_gstock_metric_l_0 |  | fid |
