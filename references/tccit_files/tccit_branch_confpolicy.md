# 分支机构政策确认-tccit_branch_confpolicy

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

## 分支机构政策确认-主表 t_tccit_branch_confpolicy

- **表名称：** 分支机构政策确认-主表
- **表名：** t_tccit_branch_confpolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期： | timestamp | 0 |  |  | null | 所属税期： |
| 3 | fillegal | 从事国家限制或禁止行业 | bpchar | 1 |  | √ | '0' | 从事国家限制或禁止行业 |
| 4 | forgid | 组织名称： | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsuittype | 软件集成电路企业优惠政策适用类型： | varchar | 50 |  | √ | ' ' | 软件集成电路企业优惠政策适用类型：,枚举: 1 :新政策 2 :原政策 |
| 6 | fdeclaretype | 申报企业类型： | varchar | 50 |  | √ | ' ' | 申报企业类型：,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 7 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 3 :第三步 4 :第四步 5 :第五步 |
| 9 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fprepaytype | 预缴方式： | varchar | 50 |  | √ | ' ' | 预缴方式：,枚举: 1 :按照实际利润额预缴 2 :按照上一纳税年度应纳税所得额平均额预缴 3 :按照税务机关确定的其他方法预缴 |
| 11 | fyear | 所属税期： | varchar | 50 |  | √ | ' ' | 所属税期：,枚举: 2019 :2019年 : |
| 12 | fjidu | 季度 | varchar | 50 |  | √ | ' ' | 季度,枚举: 1 :一季度 2 :二季度 3 :三季度 4 :四季度 |
| 13 | fregistertype | 登记注册类型： | int8 | 64 |  | √ | 0 | 注册登记类型 tax_info_registertype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_branch_confpolicy |  | fid |
| 2 | idx_tccit_branch_confpolicy_1 |  | forgid,fstartdate,fenddate |
