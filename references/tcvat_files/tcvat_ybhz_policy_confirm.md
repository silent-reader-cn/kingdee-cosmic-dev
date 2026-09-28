# 汇总一般企业政策确认-tcvat_ybhz_policy_confirm

## 单据体-子表 t_tcvat_ybhz_income

- **表名称：** 单据体-子表
- **表名：** t_tcvat_ybhz_income

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnrhzsb | 纳入汇总申报 | bpchar | 1 |  | √ | '1' | 纳入汇总申报 |
| 3 | forgid | 汇总组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :被汇总 2 :汇总 |
| 6 | ftaxation | 征税方式 | int8 | 64 |  | √ | 0 | 征收方式模板 tpo_tcvat_taxperiod |
| 7 | fjzjt | 即征即退 | varchar | 50 |  | √ | ' ' | 即征即退,枚举: 0 :否 1 :是 |
| 8 | fbelongsorg | 收入归属组织 | int8 | 64 |  | √ | 0 | 汇总方案子表 tctb_org_group_detail |
| 9 | frate | 税率/征收率 | int8 | 64 |  | √ | 0 | 税率模板 tpo_tcvat_taxrates |
| 10 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 11 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsuborg | 组织 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |
| 14 | fservicedesc | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybhz_income |  | fentryid |
| 2 | idx_tcvat_ybhz_income_fk |  | fid |

---

## 单据体-子表 t_tcvat_ybhz_assign

- **表名称：** 单据体-子表
- **表名：** t_tcvat_ybhz_assign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnormaltax | 一般项目应税服务分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 一般项目应税服务分配比例 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :被汇总 2 :汇总 |
| 6 | fissuesbb | 生成申报表 | varchar | 1 |  | √ | '0' | 生成申报表 |
| 7 | fnormalgoods | 一般项目货物及劳务分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 一般项目货物及劳务分配比例 |
| 8 | fjzjttax | 即征即退项目应税服务分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退项目应税服务分配比例 |
| 9 | fjzjtgoods | 即征即退项目货物及劳务分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退项目货物及劳务分配比例 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fassignrowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 12 | fassignorg | 方案组织 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |
| 13 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybhz_assign |  | fentryid |
| 2 | idx_tcvat_ybhz_assign_fk |  | fid |

---

## 汇总一般企业政策确认-主表 t_tcvat_ybhz_policy_conf

- **表名称：** 汇总一般企业政策确认-主表
- **表名：** t_tcvat_ybhz_policy_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprelevyrate | 预征率计算 | varchar | 50 |  | √ | ' ' | 预征率计算,枚举: 1 :固定比例 2 :累计销售额比例 3 :二级机构分配比例 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | flevytype | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: czzs :查账征收 aqhz :按期汇总 hdzs :核定征收 |
| 5 | fhzfs | 汇总方式： | varchar | 50 |  | √ | ' ' | 汇总方式：,枚举: 1 :预征方式 2 :分配方式 3 :仅汇总，不分配不预征 |
| 6 | fbqsfsyjzzc | 适用小微企业“六税两费”减免政策 | varchar | 50 |  | √ | ' ' | 适用小微企业“六税两费”减免政策,枚举: 1 :是 0 :否 |
| 7 | fhzqylx | 汇总企业类型： | varchar | 50 |  | √ | ' ' | 汇总企业类型：,枚举: 1 :航空运输企业 2 :铁路运输企业 3 :邮政企业 4 :电信企业 5 :一般企业 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 10 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 11 | ftaxplayeraptitude | 纳税人类型 | varchar | 100 |  | √ | ' ' | 纳税人类型,枚举: zzsybnsr :一般纳税人 zzsxgmnsr :小规模纳税人 |
| 12 | ffixedratio | 固定比例值 | numeric | 23 | 10 | √ | 0 | 固定比例值 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fzjggdbl | 总机构固定比例 | numeric | 23 | 10 | √ | 0 | 总机构固定比例 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcodeandname | 所属行业代码及名称 | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 20 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立申报 2 :汇总申报 3 :被汇总申报 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 23 | fassignplan | 总分机构税额分配方式 | varchar | 50 |  | √ | ' ' | 总分机构税额分配方式,枚举: 1 :按销售收入分配 2 :按固定比例分配 3 :按组织直接确定税额 4 :按总机构固定比例、分支机构销售收入比例分配 |
| 24 | fapplicablediffer | fapplicablediffer | bpchar | 1 |  | √ | ' ' |  |
| 25 | fisapplicableplus | fisapplicableplus | bpchar | 1 |  | √ | ' ' |  |
| 26 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 27 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: acsb :按次申报 aysb :按月申报 ajsb :按季申报 |
| 28 | fregistertype | 登记注册类型 | int8 | 64 |  | √ | 0 | 注册登记类型 tax_info_registertype |
| 29 | fdeductionrate | 加计抵减比例： | varchar | 50 |  | √ | ' ' | 加计抵减比例：,枚举: |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ybhz_policy_conf |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_ybhz_policy_conf |  | fid |
