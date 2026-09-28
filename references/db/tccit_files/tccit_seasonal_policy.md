# 政策确认-tccit_seasonal_policy

## 资质单据体-子表 t_tccit_apitudeinfo_s

- **表名称：** 资质单据体-子表
- **表名：** t_tccit_apitudeinfo_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditrating | 信用等级 | varchar | 30 |  | √ | ' ' | 信用等级,枚举: 1 :A 2 :B 3 :M 4 :C 5 :D |
| 3 | fprofitmyear | 开始计算优惠年度： | varchar | 100 |  | √ | ' ' | 开始计算优惠年度： |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsocietytype | 下拉列表 | varchar | 30 |  | √ | ' ' | 下拉列表,枚举: 301 :残疾人人数 302 :随军家属人数 303 :军队转业干部人数 305 :重点群体人数 |
| 6 | fprioritytion | fprioritytion | varchar | 100 |  | √ | ' ' |  |
| 7 | fexporttype | 出口类型 | varchar | 30 |  | √ | ' ' | 出口类型,枚举: 1 :一类 2 :二类 3 :三类 4 :四类 |
| 8 | fenddate |  | timestamp | 0 |  |  | null |  |
| 9 | fannualcome | 收入年度 | varchar | 100 |  | √ | ' ' | 收入年度 |
| 10 | fstartdate |  | timestamp | 0 |  |  | null |  |
| 11 | fcompanytype | 企业类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 12 | fworkertotal | 职工数量 | int8 | 64 |  | √ | 0 | 职工数量 |
| 13 | fprofittype | 优惠类型： | varchar | 30 |  | √ | ' ' | 优惠类型： |
| 14 | fsocietytotal | 残疾人数量 | int8 | 64 |  | √ | 0 | 残疾人数量 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fyxsy | 优先适用 | bpchar | 1 |  | √ | ' ' | 优先适用 |
| 17 | fapitudetype | 资质类型 | varchar | 30 |  | √ | ' ' | 资质类型,枚举: 1 :软件、集成电路类 2 :技术先进型服务类 3 :区域类税收优惠 4 :高新技术类 5 :其他税收优惠 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_apitudeinfo_s_fk |  | fid |
| 2 | t_tccit_apitudeinfo_s_pkey |  | fentryid |

---

## 政策确认-主表 t_tccit_seasonal_policy

- **表名称：** 政策确认-主表
- **表名：** t_tccit_seasonal_policy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fillegal | 从事国家限制或禁止行业 | bpchar | 1 |  | √ | ' ' | 从事国家限制或禁止行业 |
| 3 | feospersonnum | 季末从业人数 | int8 | 64 |  | √ | 0 | 季末从业人数 |
| 4 | fresidenttype | 居民企业类型 | varchar | 50 |  | √ | ' ' | 居民企业类型,枚举: jmqy :居民企业 fjmqy :非居民企业 |
| 5 | fsospersonnum | 季初从业人数 | int8 | 64 |  | √ | 0 | 季初从业人数 |
| 6 | feosassets | 季末资产总额（万元） | numeric | 23 | 10 | √ | 0.0000000000 | 季末资产总额（万元） |
| 7 | fzjgftbl | 总机构分摊比例 | numeric | 23 | 10 | √ | 0 | 总机构分摊比例 |
| 8 | forgid | 组织名称： | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsuittype | 软件集成电路企业优惠政策适用类型： | varchar | 50 |  | √ | ' ' | 软件集成电路企业优惠政策适用类型：,枚举: 1 :新政策 2 :原政策 |
| 10 | flevytype | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: hdzs :核定征收 czzs :查账征收 3 :单选按钮2 4 :单选按钮3 |
| 11 | fqbfzjgftbl | 全部分支机构分摊比例 | numeric | 23 | 10 | √ | 0 | 全部分支机构分摊比例 |
| 12 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 3 :第三步 4 :第四步 5 :第五步 |
| 14 | fsosassets | 季初资产总额（万元） | numeric | 23 | 10 | √ | 0.0000000000 | 季初资产总额（万元） |
| 15 | fczjzfpbl | 财政集中分配比例 | numeric | 23 | 10 | √ | 0 | 财政集中分配比例 |
| 16 | ftaxperiod | 所属税期： | timestamp | 0 |  |  | null | 所属税期： |
| 17 | ftaxableincomerate | 应税所得率： | numeric | 23 | 10 | √ | 0 | 应税所得率： |
| 18 | fcheckcollectway | 核定征收方式： | varchar | 50 |  | √ | ' ' | 核定征收方式：,枚举: rate-income :核定应税所得率（能核算收入总额的） rate-cost :核定应税所得率（能核算成本费用总额的） amount-income :核定应纳所得税额 |
| 19 | fdeclaretype | 申报企业类型： | varchar | 30 |  | √ | ' ' | 申报企业类型：,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 20 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 21 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 22 | fprepaytype | 预缴方式： | varchar | 30 |  | √ | ' ' | 预缴方式：,枚举: 1 :按照实际利润额预缴 2 :按照上一纳税年度应纳税所得额平均额预缴 3 :按照税务机关确定的其他方法预缴 |
| 23 | fyear | 所属税期： | varchar | 30 |  | √ | ' ' | 所属税期：,枚举: 2019 :2019年 : |
| 24 | fjidu | 季度 | varchar | 30 |  | √ | ' ' | 季度,枚举: 1 :一季度 2 :二季度 3 :三季度 4 :四季度 |
| 25 | fyjprofitslogic | 预缴底稿会计利润取数逻辑 | varchar | 50 |  | √ | ' ' | 预缴底稿会计利润取数逻辑,枚举: bqfse :本期发生额 bnlje :本年累计额 |
| 26 | fregistertype | 登记注册类型： | int8 | 64 |  | √ | 0 | [注册登记类型 tax_info_registertype](../tctb_files/tax_info_registertype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_seasonal_policy |  | forgid,fenddate,fstartdate |
| 2 | t_tccit_seasonal_policy_pkey |  | fid |

---

## 资质单据体-子表 t_tccit_apitudeinfo_branc

- **表名称：** 资质单据体-子表
- **表名：** t_tccit_apitudeinfo_branc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbranchapitudestartdate |  | timestamp | 0 |  |  | null |  |
| 3 | fbranchapitudetype | 资质类型 | varchar | 50 |  | √ | ' ' | 资质类型,枚举: 1 :软件、集成电路类 2 :技术先进型服务类 3 :区域类税收优惠 4 :高新技术类 5 :其他税收优惠 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbranchapitudeenddate |  | timestamp | 0 |  |  | null |  |
| 6 | fbranchcompanytype | 企业类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 7 | fbranceprofitmyear | 开始计算优惠年度： | varchar | 50 |  | √ | ' ' | 开始计算优惠年度： |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbranchprofittype | 优惠类型： | varchar | 50 |  | √ | ' ' | 优惠类型： |
| 10 | fbranchorgid | 分支机构: | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_apitudeinfo_branc_fk |  | fid |
| 2 | pk_tccit_apitudeinfo_branc |  | fentryid |

---

## 税收优惠单据体-子表 t_tccit_itemchioce_s

- **表名称：** 税收优惠单据体-子表
- **表名：** t_tccit_itemchioce_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 项目类型 | varchar | 30 |  | √ | ' ' | 项目类型,枚举: 1 :免税收入 2 :减计收入 3 :所得减免 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fitemchoiceid | 项目取数ID | int8 | 64 |  | √ | 0 | 项目取数ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_itemchioce_s_fk |  | fid |
| 2 | t_tccit_itemchioce_s_pkey |  | fentryid |

---

## 树形单据体-子表 t_tccit_policy_orgs

- **表名称：** 树形单据体-子表
- **表名：** t_tccit_policy_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [税务组织信息 bastax_taxorg](../bastax_files/bastax_taxorg.md) |
| 3 | fkdqjyqylx | 跨地区经营企业类型 | varchar | 50 |  | √ | ' ' | 跨地区经营企业类型,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） : |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | fdeclaration | 申报方式 | varchar | 30 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 7 | fshareid | 分摊标识 | bpchar | 1 |  | √ | ' ' | 分摊标识 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_policy_orgs_pkey |  | fentryid |
| 2 | idx_tccit_policy_orgs_fk |  | fid |

---

## 配置规则单据体-子表 t_tccit_seasonal_rule

- **表名称：** 配置规则单据体-子表
- **表名：** t_tccit_seasonal_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemtype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: profits :会计利润及资产负债项目 depreciate :资产加速折旧摊销项目 income :优惠项目 yjother :其他项目 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_seasonal_rule |  | fentryid |
| 2 | idx_tccit_seasonal_rule_fk |  | fid |
