# 融资方案-cfm_financingscheme

## 融资方案-主表 t_cfm_financingscheme

- **表名称：** 融资方案-主表
- **表名：** t_cfm_financingscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 50 |  | √ | ' ' | 期限（ymd） |
| 3 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 4 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 5 | forgid | 借款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fratecycle | 利率重置周期 | int4 | 32 |  | √ | 0 | 利率重置周期 |
| 7 | fcompcost | 综合成本 | numeric | 23 | 10 | √ | 0 | 综合成本 |
| 8 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: undetermined :待定 accept :采纳 abandoned :废弃 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | famount | 融资金额 | numeric | 23 | 10 | √ | 0 | 融资金额 |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 17 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreditordatatype | fcreditordatatype | varchar | 50 |  | √ | ' ' |  |
| 19 | fratefloatpoint | 利率浮动基点 | numeric | 23 | 10 | √ | 0 | 利率浮动基点 |
| 20 | ffloatingratio | 逾期利率浮动比例（%） | numeric | 23 | 10 | √ | 0 | 逾期利率浮动比例（%） |
| 21 | fsettledate | fsettledate | varchar | 50 |  | √ | ' ' |  |
| 22 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 23 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 25 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 26 | fcomment | 其他补充说明 | varchar | 255 |  | √ | ' ' | 其他补充说明 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fcompcostrate | 综合成本率（%） | numeric | 23 | 10 | √ | 0 | 综合成本率（%） |
| 29 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 30 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 32 | frepaymentway | 还款方式 | varchar | 50 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 33 | finterestcycle | finterestcycle | varchar | 19 |  | √ | ' ' |  |
| 34 | floanapplyid | 融资申请 | int8 | 64 |  | √ | 0 | [融资申请 cfm_loan_apply_f7](../cfm_files/cfm_loan_apply_f7.md) |
| 35 | fsettleschemeid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 36 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 37 | fcreditortype | 债权人类型 | varchar | 50 |  | √ | ' ' | 债权人类型,枚举: bank :银行 finorg :非银金融机构 settlecenter :结算中心 innerunit :内部单位 custom :客商 other :其他 |
| 38 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fopinion | 方案选择意见 | varchar | 255 |  | √ | ' ' | 方案选择意见 |
| 40 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 41 | ffintype | 融资业务分类 | varchar | 30 |  | √ | ' ' | 融资业务分类,枚举: loan :普通贷款 entrust :委托贷款 sl :银团贷款 ec :企业往来 |
| 42 | fguaranteeway | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 1 :信用 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :无担保 |
| 43 | fcurrencyid | 融资币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | finterestrate | 贷款年利率（%） | numeric | 23 | 10 | √ | 0 | 贷款年利率（%） |
| 45 | fratecyclesign | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: W :按周 M :按月 |
| 46 | fauditorid | 方案审批人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_financingscheme |  | fnumber |
| 2 | pk_t_cfm_financingscheme |  | fid |

---

## 融资方案-多语言表 t_cfm_financingscheme_l

- **表名称：** 融资方案-多语言表
- **表名：** t_cfm_financingscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 3 | fcomment | 其他补充说明 | varchar | 50 |  | √ | ' ' | 其他补充说明 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_financingscheme_l |  | fpkid |
| 2 | idx_cfm_financingscheme_l |  | fid,flocaleid |

---

## 单据体-子表 t_cfm_finscheme_entry

- **表名称：** 单据体-子表
- **表名：** t_cfm_finscheme_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostamt | 成本金额 | numeric | 23 | 10 | √ | 0 | 成本金额 |
| 3 | fecomment | fecomment | varchar | 255 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | finterestrate | 年化利率\费率（%） | numeric | 23 | 10 | √ | 0 | 年化利率\费率（%） |
| 7 | fetextcost | 成本构成 | varchar | 255 |  | √ | ' ' | 成本构成 |
| 8 | fcost | 成本构成 | int8 | 64 |  | √ | 0 | [费用类型 fbd_feetype](../fbd_files/fbd_feetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_finscheme_entry |  | fentryid |
| 2 | idx_cfm_finscheme_entry |  | fid |
