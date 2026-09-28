# 信用评估方案-ccm_evalscheme

## 树形单据体-子表 t_ccm_evalschemeentry

- **表名称：** 树形单据体-子表
- **表名：** t_ccm_evalschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 层级 | varchar | 50 |  | √ | ' ' | 层级 |
| 3 | fweight | 权重（%） | numeric | 23 | 10 | √ | 0 | 权重（%） |
| 4 | fmetricsid | 评估指标编码 | int8 | 64 |  | √ | 0 | [信用评估指标 ccm_evalmetrics](../ccm_files/ccm_evalmetrics.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | fscoremode | 评分方式 | varchar | 50 |  | √ | ' ' | 评分方式,枚举: auto :自动评分 manual :人工评分 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmetricsscore | 指标分值 | numeric | 23 | 10 | √ | 0 | 指标分值 |
| 10 | fgrouptype | 分类指标类型 | varchar | 50 |  | √ | ' ' | 分类指标类型,枚举: group :分类指标 detail :明细指标 |
| 11 | fgroupmetricsid | 上级分类指标 | int8 | 64 |  | √ | 0 | [信用评估指标 ccm_evalmetrics](../ccm_files/ccm_evalmetrics.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_evalschemeentry |  | fid |
| 2 | pk_ccm_evalschemeentry |  | fentryid |

---

## 信用评估方案-多语言表 t_ccm_evalscheme_l

- **表名称：** 信用评估方案-多语言表
- **表名：** t_ccm_evalscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 评估方案名称 | varchar | 100 |  | √ | ' ' | 评估方案名称 |
| 3 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
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
| 1 | pk_ccm_evalscheme_l |  | fpkid |
| 2 | idx_ccm_evalscheme_l |  | fid |

---

## 信用评估方案-主表 t_ccm_evalscheme

- **表名称：** 信用评估方案-主表
- **表名：** t_ccm_evalscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 评估方案名称 | varchar | 100 |  | √ | ' ' | 评估方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | ftotalscore | 评估方案总分 | numeric | 23 | 10 | √ | 0 | 评估方案总分 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fnumber | 评估方案编码 | varchar | 80 |  | √ | ' ' | 评估方案编码 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_evalscheme |  | fnumber |
| 2 | pk_ccm_evalscheme |  | fid |
