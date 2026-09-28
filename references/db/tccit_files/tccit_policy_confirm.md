# 政策确认-tccit_policy_confirm

## 单据体-子表 t_tccit_policy_sharehold

- **表名称：** 单据体-子表
- **表名：** t_tccit_policy_sharehold

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvestrate | 投资比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 投资比例（%） |
| 3 | fcurryeardividend | 当年分配的股息红利金额 | numeric | 23 | 10 | √ | 0.0000000000 | 当年分配的股息红利金额 |
| 4 | fnationality | 国籍 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fgdname | 股东名称 | varchar | 50 |  | √ | ' ' | 股东名称 |
| 8 | fidnumber | 证件号码 | varchar | 50 |  | √ | ' ' | 证件号码 |
| 9 | ffidtype | 证件类型 | varchar | 50 |  | √ | ' ' | 证件类型,枚举: 1 :居民身份证 2 :中国护照 3 :税务登记证 4 :营业执照 5 :组织机构代码证 6 :其他单位证件 7 :香港特别行政区护照 8 :澳门特别行政区护照 9 :港澳居民来往内地通行证 10 :中华人民共和国往来港澳通行证 11 :台湾居民来往大陆通行证 12 :大陆居民往来台湾通行证 13 :香港永久性居民身份证 14 :台湾身份证 15 :澳门特别行政区永久性居民身份证 16 :外国护照 17 :外国人身份证件 18 :其他个人证件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_policy_sharehold_fk |  | fid |
| 2 | pk_tccit_policy_sharehold |  | fentryid |

---

## 政策确认-分表 t_tccit_policy_a

- **表名称：** 政策确认-分表
- **表名：** t_tccit_policy_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fselectall | 全选 | bpchar | 1 |  | √ | ' ' | 全选 |
| 3 | fincome9 | 不征税收入及支出 | bpchar | 1 |  | √ | ' ' | 不征税收入及支出 |
| 4 | fincome8 | 投资资产处置收益调整 | bpchar | 1 |  | √ | ' ' | 投资资产处置收益调整 |
| 5 | fincomeother | 工资、社保、公积金 | bpchar | 1 |  | √ | ' ' | 工资、社保、公积金 |
| 6 | fothertz | 其他调整 | bpchar | 1 |  | √ | ' ' | 其他调整 |
| 7 | ftaxcredit | 税额抵免 | bpchar | 1 |  | √ | ' ' | 税额抵免 |
| 8 | fdeduct13 | 非公益性捐赠支出 | bpchar | 1 |  | √ | ' ' | 非公益性捐赠支出 |
| 9 | fdeduct12 | 境外共同分摊的支出 | bpchar | 1 |  | √ | ' ' | 境外共同分摊的支出 |
| 10 | fdeduct11 | 捐赠支出 | bpchar | 1 |  | √ | ' ' | 捐赠支出 |
| 11 | fdeduct10 | 工会经费、职工福利费、党组织工作经费 | bpchar | 1 |  | √ | ' ' | 工会经费、职工福利费、党组织工作经费 |
| 12 | fincome10 | 备用 | bpchar | 1 |  | √ | ' ' | 备用 |
| 13 | fsofttype | 软件、集成电路企业类型： | varchar | 50 |  | √ | ' ' | 软件、集成电路企业类型：,枚举: |
| 14 | fyhsx2 | 其他项目所得减免 | bpchar | 1 |  | √ | ' ' | 其他项目所得减免 |
| 15 | fdksszbjtz | 特殊行业准备金 | bpchar | 1 |  | √ | ' ' | 特殊行业准备金 |
| 16 | fyhsx3 | 符合免税条件的投资收益 | bpchar | 1 |  | √ | ' ' | 符合免税条件的投资收益 |
| 17 | fyhsx4 | 其他免税收入、减计收入及加计扣除 | bpchar | 1 |  | √ | ' ' | 其他免税收入、减计收入及加计扣除 |
| 18 | fdeductway | 选择采用的境外所得抵免方式： | varchar | 50 |  | √ | ' ' | 选择采用的境外所得抵免方式：,枚举: 1 :分国（地区）不分项 2 :不分国（地区）不分项 |
| 19 | fyhsx5 | 研发费用加计扣除 | bpchar | 1 |  | √ | ' ' | 研发费用加计扣除 |
| 20 | fassetother | 其他调整 | bpchar | 1 |  | √ | ' ' | 其他调整 |
| 21 | fspectz | 特别纳税调整应税所得 | bpchar | 1 |  | √ | ' ' | 特别纳税调整应税所得 |
| 22 | fmbkstype | 弥补亏损企业类型： | varchar | 50 |  | √ | ' ' | 弥补亏损企业类型：,枚举: 100 :一般企业 200 :符合条件的高新技术企业 300 :符合条件的科技型中小企业 400 :线宽小于 130 纳米(含)的集成电路生产企业 500 :受疫情影响困难行业企业 600 :电影行业企业 |
| 23 | fassetexpense | 租赁支出 | bpchar | 1 |  | √ | ' ' | 租赁支出 |
| 24 | ftssxother | 其他调整 | bpchar | 1 |  | √ | ' ' | 其他调整 |
| 25 | fcurryeardividendsum | 当年分配全部股东股息红利总额 | numeric | 23 | 10 | √ | 0.0000000000 | 当年分配全部股东股息红利总额 |
| 26 | faccountcriterion | 会计准则或会计制度： | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 27 | fyhsx1 | 技术转让项目所得减免 | bpchar | 1 |  | √ | ' ' | 技术转让项目所得减免 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_policy_a |  | fincomeother |
| 2 | pk_tccit_policy_a |  | fid |

---

## 政策确认-主表 t_tccit_policy

- **表名称：** 政策确认-主表
- **表名：** t_tccit_policy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fincome1 | 视同销售业务 | bpchar | 1 |  | √ | ' ' | 视同销售业务 |
| 3 | fincome2 | 未按权责发生制确认收入 | bpchar | 1 |  | √ | ' ' | 未按权责发生制确认收入 |
| 4 | fincome5 | 销售折扣、折让和退回 | bpchar | 1 |  | √ | ' ' | 销售折扣、折让和退回 |
| 5 | fzjgftbl | 总机构分摊比例（%） | numeric | 23 | 10 | √ | 0 | 总机构分摊比例（%） |
| 6 | fincome6 | 投资资产初始成本调整 | bpchar | 1 |  | √ | ' ' | 投资资产初始成本调整 |
| 7 | fincome3 | 投资资产持有收益调整 | bpchar | 1 |  | √ | ' ' | 投资资产持有收益调整 |
| 8 | forgid | 组织名称： | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fincome4 | 房地产特定业务调整 | bpchar | 1 |  | √ | ' ' | 房地产特定业务调整 |
| 10 | fdeduct9 | 罚款、滞纳金、与收入无关的支出、赞助支出 | bpchar | 1 |  | √ | ' ' | 罚款、滞纳金、与收入无关的支出、赞助支出 |
| 11 | fincome7 | 公允价值变动损益调整 | bpchar | 1 |  | √ | ' ' | 公允价值变动损益调整 |
| 12 | fdeduct1 | 业务招待费 | bpchar | 1 |  | √ | ' ' | 业务招待费 |
| 13 | fdeduct2 | 广告宣传费 | bpchar | 1 |  | √ | ' ' | 广告宣传费 |
| 14 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fdeduct3 | 职工教育经费 | bpchar | 1 |  | √ | ' ' | 职工教育经费 |
| 16 | fdeduct4 | 永续债业务 | bpchar | 1 |  | √ | ' ' | 永续债业务 |
| 17 | fdeduct5 | 利息费用 | bpchar | 1 |  | √ | ' ' | 利息费用 |
| 18 | fdeduct6 | 佣金手续费 | bpchar | 1 |  | √ | ' ' | 佣金手续费 |
| 19 | fdeduct7 | 党组织工作经费 | bpchar | 1 |  | √ | ' ' | 党组织工作经费 |
| 20 | fdeduct8 | 涉农利息、保费 | bpchar | 1 |  | √ | ' ' | 涉农利息、保费 |
| 21 | fassets | 资产总额（万元） | numeric | 23 | 10 | √ | 0.0000000000 | 资产总额（万元） |
| 22 | fother2 | 政策性搬迁 | bpchar | 1 |  | √ | ' ' | 政策性搬迁 |
| 23 | fother3 | 技术转让 | bpchar | 1 |  | √ | ' ' | 技术转让 |
| 24 | fother4 | 境外所得 | bpchar | 1 |  | √ | ' ' | 境外所得 |
| 25 | fother5 | 清算或撤资业务 | bpchar | 1 |  | √ | ' ' | 清算或撤资业务 |
| 26 | fother6 | 准备金 | bpchar | 1 |  | √ | ' ' | 准备金 |
| 27 | fother7 | 销售未完工开发产品 | bpchar | 1 |  | √ | ' ' | 销售未完工开发产品 |
| 28 | fstartdate | 年度期间： | timestamp | 0 |  |  | null | 年度期间： |
| 29 | fother8 | 创业投资企业优惠 | bpchar | 1 |  | √ | ' ' | 创业投资企业优惠 |
| 30 | fregistertype | 登记注册类型： | int8 | 64 |  | √ | 0 | [注册登记类型 tax_info_registertype](../tctb_files/tax_info_registertype.md) |
| 31 | fother1 | 企业重组及递延纳税事项 | bpchar | 1 |  | √ | ' ' | 企业重组及递延纳税事项 |
| 32 | ftssx1 | 合伙企业法人合伙人应分得的应纳税所得额 | bpchar | 1 |  | √ | ' ' | 合伙企业法人合伙人应分得的应纳税所得额 |
| 33 | fillegal | 从事国家限制或禁止行业： | bpchar | 1 |  | √ | ' ' | 从事国家限制或禁止行业： |
| 34 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 3 :第三步 4 :第四步 5 :第五步 |
| 35 | faccountingstandards | faccountingstandards | varchar | 30 |  | √ | ' ' |  |
| 36 | fdeduct13 | fdeduct13 | bpchar | 1 |  | √ | ' ' |  |
| 37 | fczjzfpbl | 财政集中分配比例（%） | numeric | 23 | 10 | √ | 0 | 财政集中分配比例（%） |
| 38 | fdeduct12 | fdeduct12 | bpchar | 1 |  | √ | ' ' |  |
| 39 | fdeduct11 | fdeduct11 | bpchar | 1 |  | √ | ' ' |  |
| 40 | fdeduct10 | fdeduct10 | bpchar | 1 |  | √ | ' ' |  |
| 41 | fdeduct16 | 跨期扣除项目 | bpchar | 1 |  | √ | ' ' | 跨期扣除项目 |
| 42 | fdeduct15 | fdeduct15 | bpchar | 1 |  | √ | ' ' |  |
| 43 | fdeduct14 | fdeduct14 | bpchar | 1 |  | √ | ' ' |  |
| 44 | fasset2 | 资产损失 | bpchar | 1 |  | √ | ' ' | 资产损失 |
| 45 | fasset3 | 资产减值准备 | bpchar | 1 |  | √ | ' ' | 资产减值准备 |
| 46 | fcodeandname | 行业代码及名称： | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 47 | fdeclaretype | 申报企业类型： | varchar | 30 |  | √ | ' ' | 申报企业类型：,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 48 | fasset1 | 资产折旧、摊销费用 | bpchar | 1 |  | √ | ' ' | 资产折旧、摊销费用 |
| 49 | femployeesnum | 从业人数（填写平均值） | numeric | 23 | 10 | √ | 0.0000000000 | 从业人数（填写平均值） |
| 50 | ffzjgftbl | 分支机构分摊比例（%） | numeric | 23 | 10 | √ | 0 | 分支机构分摊比例（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_policy_pkey |  | fid |
| 2 | idx_tccit_policy |  | forgid |

---

## 单据体-子表 t_tccit_sure_declare

- **表名称：** 单据体-子表
- **表名：** t_tccit_sure_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdeclareid |  | int8 | 64 |  | √ | 0 | 企业所得税类型 tpo_qysds_types |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_sure_declare_pkey |  | fentryid |
| 2 | idx_tccit_sure_declare_fk |  | fid |

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

## 资质单据体-子表 t_tccit_apitudeinfo

- **表名称：** 资质单据体-子表
- **表名：** t_tccit_apitudeinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditrating | 信用等级 | varchar | 30 |  | √ | ' ' | 信用等级,枚举: 1 :A 2 :B 3 :M 4 :C 5 :D |
| 3 | fprofitmyear | 开始计算优惠年度： | varchar | 50 |  | √ | ' ' | 开始计算优惠年度： |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsocietytype | 下拉列表 | varchar | 30 |  | √ | ' ' | 下拉列表,枚举: 301 :残疾人人数 302 :随军家属人数 303 :军队转业干部人数 305 :重点群体人数 |
| 6 | fprioritytion | fprioritytion | varchar | 50 |  | √ | ' ' |  |
| 7 | fexporttype | 出口类型 | varchar | 30 |  | √ | ' ' | 出口类型,枚举: 1 :一类 2 :二类 3 :三类 4 :四类 |
| 8 | fenddate |  | timestamp | 0 |  |  | null |  |
| 9 | fannualcome | 收入年度 | varchar | 50 |  | √ | ' ' | 收入年度 |
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
| 1 | t_tccit_apitudeinfo_pkey |  | fentryid |
| 2 | idx_tccit_apitudeinfo_fk |  | fid |
