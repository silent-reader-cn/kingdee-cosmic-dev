# 风险得分方案-tctrc_risk_score_scheme

## 风险得分方案-多语言表 t_tctrc_risk_score_scheme_l

- **表名称：** 风险得分方案-多语言表
- **表名：** t_tctrc_risk_score_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_risk_score_scheme_l |  | fpkid |
| 2 | idx_tctrc_risk_score_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_tctrc_risk_score_djt

- **表名称：** 单据体-子表
- **表名：** t_tctrc_risk_score_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frisklevel | 风险等级 | int8 | 64 |  | √ | 0 | 风险等级 tctrc_risk_level |
| 3 | fdefaultscore | 默认得分 | numeric | 23 | 10 | √ | 0 | 默认得分 |
| 4 | fscorestart | 得分从(大于等于) | numeric | 23 | 10 |  | null | 得分从(大于等于) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fscoreend | 得分至(小于等于) | numeric | 23 | 10 |  | null | 得分至(小于等于) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_risk_score_djt |  | fentryid |
| 2 | idx_tctrc_risk_score_djt_fk |  | fid |

---

## 风险得分方案-主表 t_tctrc_risk_score_scheme

- **表名称：** 风险得分方案-主表
- **表名：** t_tctrc_risk_score_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 1 :是 0 :否 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 14 | fscoreinterval | 分值间隔 | numeric | 23 | 10 | √ | 0 | 分值间隔 |
| 15 | fmaxscore | 风险最大分值 | varchar | 50 |  | √ | ' ' | 风险最大分值,枚举: 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_risk_score_scheme |  | fid |
| 2 | idx_tctrc_risk_score_scheme |  | fnumber |
