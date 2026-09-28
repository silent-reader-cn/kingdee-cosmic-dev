# 噪声信息采集表-tdm_noise_info

## 噪声信息采集表-主表 t_tdm_noise_info

- **表名称：** 噪声信息采集表-主表
- **表名：** t_tdm_noise_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyjstand | 标准值-夜间 | int8 | 64 |  | √ | 0 | 标准值-夜间 |
| 3 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | ffbmonitor | 监测分贝数 | int8 | 64 |  | √ | 0 | 监测分贝数 |
| 9 | fmulti | 两处以上噪声超标 | varchar | 50 |  | √ | ' ' | 两处以上噪声超标,枚举: 1 :是 0 :否 |
| 10 | fmonth | 税款所属月份 | timestamp | 0 |  |  | null | 税款所属月份 |
| 11 | ftaxdepend | 计税依据 | varchar | 50 |  | √ | ' ' | 计税依据 |
| 12 | fzjstand | 标准值-昼间 | int8 | 64 |  | √ | 0 | 标准值-昼间 |
| 13 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftaxauthority | 排放口所属主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | funittax | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 18 | fzyproduction | 昼夜产生 | varchar | 50 |  | √ | ' ' | 昼夜产生,枚举: 1 :是 0 :否 |
| 19 | fdayratio | 超标不足15天系数 | numeric | 23 | 10 | √ | 0 | 超标不足15天系数 |
| 20 | fsourcenumber | 税源编号 | int8 | 64 |  | √ | 0 | 排污口基础信息 tcret_pollution_basedata |
| 21 | ffbexc | 超标分贝数 | int8 | 64 |  | √ | 0 | 超标分贝数 |
| 22 | fnoiseratio | 两处以上噪声超标系数 | numeric | 23 | 10 | √ | 0 | 两处以上噪声超标系数 |
| 23 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :模板引入 |
| 26 | foverlimit | 超标不足15天 | varchar | 50 |  | √ | ' ' | 超标不足15天,枚举: 1 :是 0 :否 |
| 27 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 28 | fnoisetime | 噪声时段 | varchar | 50 |  | √ | ' ' | 噪声时段,枚举: day :昼间 night :夜间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_noise_info |  | fnumber |
| 2 | pk_tdm_noise_info |  | fid |

---

## 噪声信息-子表 t_tdm_noise_info_entry

- **表名称：** 噪声信息-子表
- **表名：** t_tdm_noise_info_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fzysd | 噪声时段 | varchar | 50 |  | √ | ' ' | 噪声时段,枚举: day :昼间 night :夜间 |
| 3 | flcyszycb | 两处以上噪声超标 | bpchar | 1 |  | √ | '0' | 两处以上噪声超标 |
| 4 | fsm | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 5 | flcyszycbrate | 两处以上噪声超标系数 | numeric | 23 | 10 | √ | 0 | 两处以上噪声超标系数 |
| 6 | fdwse | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcbbzswt | 超标不足15天 | bpchar | 1 |  | √ | '0' | 超标不足15天 |
| 9 | fjcfbs | 监测分贝数 | int8 | 64 |  | √ | 0 | 监测分贝数 |
| 10 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 11 | fjsyj | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |
| 12 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcbfbs | 超标分贝数 | int8 | 64 |  | √ | 0 | 超标分贝数 |
| 15 | fcbbzswtrate | 超标不足15天系数 | numeric | 23 | 10 | √ | 0 | 超标不足15天系数 |
| 16 | fbqyjse | 本期已缴税额 | numeric | 23 | 10 | √ | 0 | 本期已缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_noise_info_entry |  | fentryid |
| 2 | idx_tdm_noise_info_entry_fk |  | fid |

---

## 噪声信息采集表-多语言表 t_tdm_noise_info_l

- **表名称：** 噪声信息采集表-多语言表
- **表名：** t_tdm_noise_info_l

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
| 1 | pk_tdm_noise_info_l |  | fpkid |
| 2 | idx_tdm_noise_info_l_0 |  | fid,flocaleid |
