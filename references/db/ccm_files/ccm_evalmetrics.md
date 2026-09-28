# 信用评估指标-ccm_evalmetrics

## 信用评估指标-多语言表 t_ccm_evalmetrics_l

- **表名称：** 信用评估指标-多语言表
- **表名：** t_ccm_evalmetrics_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 指标描述 | varchar | 255 |  | √ | ' ' | 指标描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fmetricsstandard | 指标得分标准 | varchar | 2000 |  | √ | ' ' | 指标得分标准 |
| 7 | fmetricsnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalmetrics_l |  | fpkid |
| 2 | idx_ccm_evalmetrics_l |  | fid |

---

## 信用评估指标-主表 t_ccm_evalmetrics

- **表名称：** 信用评估指标-主表
- **表名：** t_ccm_evalmetrics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 指标分类 | int8 | 64 |  | √ | 0 | [评估指标分类 ccm_metricsgroup](../ccm_files/ccm_metricsgroup.md) |
| 3 | forgfield | 指标组织维度 | varchar | 50 |  | √ | ' ' | 指标组织维度,枚举: |
| 4 | fmetricstype | 指标类型 | varchar | 50 |  | √ | ' ' | 指标类型,枚举: Quantitative :定量 Qualitative :定性 |
| 5 | fscmmetricsid | 选择数智指标 | int8 | 64 |  | √ | 0 | [数据指标 sbs_datametrics](../sbs_files/sbs_datametrics.md) |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fcustmasteridfield | 指标客户主ID维度 | varchar | 50 |  | √ | ' ' | 指标客户主ID维度,枚举: |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcondition | 指标数据范围 | varchar | 255 |  | √ | ' ' | 指标数据范围 |
| 13 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmetricsnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcondition_tag | 指标数据范围_详情 | text | 0 |  |  | null | 指标数据范围_详情 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fdescription | 指标描述 | varchar | 255 |  | √ | ' ' | 指标描述 |
| 21 | fisgroup | 类别指标 | bpchar | 1 |  | √ | '0' | 类别指标 |
| 22 | fvaluetype | 数值类型 | varchar | 50 |  | √ | ' ' | 数值类型,枚举: normal :正常 percent :百分比 |
| 23 | fmetricsscore | 指标分值 | numeric | 23 | 10 | √ | 0 | 指标分值 |
| 24 | fmetricsstandard | 指标得分标准 | varchar | 2000 |  | √ | ' ' | 指标得分标准 |
| 25 | fcustfield | 指标客户维度 | varchar | 50 |  | √ | ' ' | 指标客户维度,枚举: |
| 26 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fdatasource | 指标取值来源 | varchar | 50 |  | √ | ' ' | 指标取值来源,枚举: scmmetrics :供应链数据指标 manual :手工录入 |
| 29 | fnumber | 指标编码 | varchar | 80 |  | √ | ' ' | 指标编码 |
| 30 | fscoremode | 评分方式 | varchar | 50 |  | √ | ' ' | 评分方式,枚举: auto :自动评分 manual :人工评分 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_evalmetrics |  | fid |
| 2 | idx_ccm_evalmetrics |  | fnumber |

---

## 评分标准-多语言表 t_ccm_evalmetricsentry_l

- **表名称：** 评分标准-多语言表
- **表名：** t_ccm_evalmetricsentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fscorestandard | 得分标准 | varchar | 255 |  | √ | ' ' | 得分标准 |
| 2 | fnote | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
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
| 1 | idx_ccm_evalmetricsentry_l |  | fentryid,flocaleid |
| 2 | pk_ccm_evalmetricsentry_l |  | fpkid |

---

## 评分标准-子表 t_ccm_evalmetricsentry

- **表名称：** 评分标准-子表
- **表名：** t_ccm_evalmetricsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscorestandard | 得分标准 | varchar | 255 |  | √ | ' ' | 得分标准 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 5 | fvalfrom | 指标数值从（大于等于） | numeric | 23 | 10 | √ | 0 | 指标数值从（大于等于） |
| 6 | fvalto | 指标数值至（小于） | numeric | 23 | 10 | √ | 0 | 指标数值至（小于） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_evalmetricsentry |  | fid |
| 2 | pk_ccm_evalmetricsentry |  | fentryid |
