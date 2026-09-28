# 申报表政策确认-tccit_policy_confirm2

## 单据体-子表 t_tccit_policy_fhsbb

- **表名称：** 单据体-子表
- **表名：** t_tccit_policy_fhsbb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvestrate | 投资比例（%） | numeric | 23 | 10 |  | null | 投资比例（%） |
| 3 | fnationality | 国籍 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fgdname | 股东名称 | varchar | 50 |  | √ | ' ' | 股东名称 |
| 7 | ffidtype | 证件类型 | varchar | 50 |  | √ | ' ' | 证件类型,枚举: 1 :居民身份证 2 :中国护照 3 :税务登记证 4 :营业执照 5 :组织机构代码证 6 :其他单位证件 7 :香港特别行政区护照 8 :澳门特别行政区护照 9 :港澳居民来往内地通行证 10 :中华人民共和国往来港澳通行证 11 :台湾居民来往大陆通行证 12 :大陆居民往来台湾通行证 13 :香港永久性居民身份证 14 :台湾身份证 15 :澳门特别行政区永久性居民身份证 16 :外国护照 17 :外国人身份证件 18 :其他个人证件 |
| 8 | fidnumber | 证件号码 | varchar | 50 |  | √ | ' ' | 证件号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_policy_fhsbb_fk |  | fid |
| 2 | pk_tccit_policy_fhsbb |  | fentryid |

---

## 资质单据体-子表 t_tccit_apitudeinfosbb

- **表名称：** 资质单据体-子表
- **表名：** t_tccit_apitudeinfosbb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditrating | 信用等级 | varchar | 50 |  | √ | ' ' | 信用等级,枚举: 1 :A 2 :B 3 :M 4 :C 5 :D |
| 3 | fprofitmyear | 开始计算优惠年度： | varchar | 50 |  | √ | ' ' | 开始计算优惠年度： |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsocietytype | 下拉列表 | varchar | 50 |  | √ | ' ' | 下拉列表,枚举: 301 :残疾人人数 302 :随军家属人数 303 :军队转业干部人数 305 :重点群体人数 |
| 6 | fexporttype | 出口类型 | varchar | 50 |  | √ | ' ' | 出口类型,枚举: 1 :一类 2 :二类 3 :三类 4 :四类 |
| 7 | fenddate |  | timestamp | 0 |  |  | null |  |
| 8 | fannualcome | 收入年度 | varchar | 50 |  | √ | ' ' | 收入年度 |
| 9 | fstartdate |  | timestamp | 0 |  |  | null |  |
| 10 | fcompanytype | 企业类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 11 | fworkertotal | 职工数量 | int8 | 64 |  | √ | 0 | 职工数量 |
| 12 | fprofittype | 优惠类型： | varchar | 50 |  | √ | ' ' | 优惠类型： |
| 13 | fsocietytotal | 残疾人数量 | int8 | 64 |  | √ | 0 | 残疾人数量 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fyxsy | 优先适用 | bpchar | 1 |  | √ | ' ' | 优先适用 |
| 16 | fapitudetype | 资质类型 | varchar | 50 |  | √ | ' ' | 资质类型,枚举: 1 :软件、集成电路类 2 :技术先进型服务类 3 :区域类税收优惠 4 :高新技术类 5 :其他税收优惠 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_apitudeinfosbb |  | fentryid |
| 2 | idx_tccit_apitudeinfosbb_fk |  | fid |

---

## 树形单据体-子表 t_tccit_policy_orgssbb

- **表名称：** 树形单据体-子表
- **表名：** t_tccit_policy_orgssbb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 5 | fdeclaration | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 6 | fshareid | 分摊标识 | bpchar | 1 |  | √ | ' ' | 分摊标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_policy_orgssbb |  | fentryid |
| 2 | idx_tccit_policy_orgssbb_fk |  | fid |

---

## 申报表政策确认-主表 t_tccit_policysbb

- **表名称：** 申报表政策确认-主表
- **表名：** t_tccit_policysbb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 3 :第三步 4 :第四步 5 :第五步 |
| 4 | fillegal | 从事国家限制或禁止行业： | varchar | 50 |  | √ | ' ' | 从事国家限制或禁止行业：,枚举: 1 :是 0 :否 |
| 5 | fstartdate | 年度期间： | timestamp | 0 |  |  | null | 年度期间： |
| 6 | forgid | 组织名称： | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcodeandname | 行业代码及名称： | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 8 | fdeclaretype | 申报企业类型： | varchar | 50 |  | √ | ' ' | 申报企业类型：,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 9 | fregistertype | 登记注册类型： | int8 | 64 |  | √ | 0 | 注册登记类型 tax_info_registertype |
| 10 | faccountcriterion | 会计准则或会计制度： | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_policysbb |  | forgid,fstartdate,fenddate |
| 2 | pk_tccit_policysbb |  | fid |
