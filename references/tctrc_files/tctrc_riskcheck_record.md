# 风险检查概况历史记录表-tctrc_riskcheck_record

## 风险检查概况历史记录表-主表 t_tctrc_riskcheck_record

- **表名称：** 风险检查概况历史记录表-主表
- **表名：** t_tctrc_riskcheck_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | friskcollect | 风险分布json | varchar | 2000 |  | √ | ' ' | 风险分布json |
| 3 | friskpkids_tag | 风险分布id_详情 | text | 0 |  |  | null | 风险分布id_详情 |
| 4 | ftaxtypepkids | 税种分布id | varchar | 255 |  | √ | ' ' | 税种分布id |
| 5 | ftaxtypecollect | 税种分布json | varchar | 2000 |  | √ | ' ' | 税种分布json |
| 6 | fsbbid | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 7 | ftaxtypepkids_tag | 税种分布id_详情 | text | 0 |  |  | null | 税种分布id_详情 |
| 8 | friskpkids | 风险分布id | varchar | 255 |  | √ | ' ' | 风险分布id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_riskr_sbbid |  | fsbbid |
| 2 | pk_tctrc_riskcheck_record |  | fid |

---

## 单据体-子表 t_tctrc_riskch_record_djt

- **表名称：** 单据体-子表
- **表名：** t_tctrc_riskch_record_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomcount1 | 自定义1数量 | varchar | 50 |  | √ | ' ' | 自定义1数量 |
| 3 | fcustomcount3 | 自定义3数量 | varchar | 50 |  | √ | ' ' | 自定义3数量 |
| 4 | fcustomcount2 | 自定义2数量 | varchar | 50 |  | √ | ' ' | 自定义2数量 |
| 5 | fhitcount | 命中数量 | varchar | 50 |  | √ | ' ' | 命中数量 |
| 6 | fcustomcount5 | 自定义5数量 | varchar | 50 |  | √ | ' ' | 自定义5数量 |
| 7 | fmeddiescount | 中风险数量 | varchar | 50 |  | √ | ' ' | 中风险数量 |
| 8 | fcustomcount4 | 自定义4数量 | varchar | 50 |  | √ | ' ' | 自定义4数量 |
| 9 | fcustomcount7 | 自定义7数量 | varchar | 50 |  | √ | ' ' | 自定义7数量 |
| 10 | fcustomcount6 | 自定义6数量 | varchar | 50 |  | √ | ' ' | 自定义6数量 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | flowcountids | 低风险ids | varchar | 255 |  | √ | ' ' | 低风险ids |
| 13 | fmeddiescountids_tag | 中风险ids_详情 | text | 0 |  |  | null | 中风险ids_详情 |
| 14 | fhighcountids | 高风险ids | varchar | 255 |  | √ | ' ' | 高风险ids |
| 15 | fhitcountids | 命中ids | varchar | 255 |  | √ | ' ' | 命中ids |
| 16 | fmeddiescountids | 中风险ids | varchar | 255 |  | √ | ' ' | 中风险ids |
| 17 | fcustomcount6ids_tag | 自定义6数量ids_详情 | text | 0 |  |  | null | 自定义6数量ids_详情 |
| 18 | fcustomcount5ids_tag | 自定义5数量ids_详情 | text | 0 |  |  | null | 自定义5数量ids_详情 |
| 19 | fcustomcount7ids_tag | 自定义7数量ids_详情 | text | 0 |  |  | null | 自定义7数量ids_详情 |
| 20 | fhitcountids_tag | 命中ids_详情 | text | 0 |  |  | null | 命中ids_详情 |
| 21 | fcustomcount5ids | 自定义5数量ids | varchar | 255 |  | √ | ' ' | 自定义5数量ids |
| 22 | fcustomcount7ids | 自定义7数量ids | varchar | 255 |  | √ | ' ' | 自定义7数量ids |
| 23 | findexcountids_tag | 指标ids_详情 | text | 0 |  |  | null | 指标ids_详情 |
| 24 | findexcountids | 指标ids | varchar | 255 |  | √ | ' ' | 指标ids |
| 25 | fcustomcount1ids | 自定义1数量ids | varchar | 255 |  | √ | ' ' | 自定义1数量ids |
| 26 | fcustomcount3ids | 自定义3数量ids | varchar | 255 |  | √ | ' ' | 自定义3数量ids |
| 27 | flowcountids_tag | 低风险ids_详情 | text | 0 |  |  | null | 低风险ids_详情 |
| 28 | fcustomcount1ids_tag | 自定义1数量ids_详情 | text | 0 |  |  | null | 自定义1数量ids_详情 |
| 29 | fcustomcount2ids_tag | 自定义2数量ids_详情 | text | 0 |  |  | null | 自定义2数量ids_详情 |
| 30 | fcustomcount3ids_tag | 自定义3数量ids_详情 | text | 0 |  |  | null | 自定义3数量ids_详情 |
| 31 | fcustomcount4ids_tag | 自定义4数量ids_详情 | text | 0 |  |  | null | 自定义4数量ids_详情 |
| 32 | fhighcount | 高风险数量 | varchar | 50 |  | √ | ' ' | 高风险数量 |
| 33 | flowcount | 低风险数量 | varchar | 50 |  | √ | ' ' | 低风险数量 |
| 34 | fscandimensions | 扫描维度 | varchar | 50 |  | √ | ' ' | 扫描维度 |
| 35 | fcustomcount6ids | 自定义6数量ids | varchar | 255 |  | √ | ' ' | 自定义6数量ids |
| 36 | fhighcountids_tag | 高风险ids_详情 | text | 0 |  |  | null | 高风险ids_详情 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | findexcount | 指标数量 | varchar | 50 |  | √ | ' ' | 指标数量 |
| 39 | fcustomcount4ids | 自定义4数量ids | varchar | 255 |  | √ | ' ' | 自定义4数量ids |
| 40 | fcustomcount2ids | 自定义2数量ids | varchar | 255 |  | √ | ' ' | 自定义2数量ids |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_riskch_record_djt |  | fentryid |
| 2 | idx_tctrc_riskch_record_djt_fk |  | fid |
