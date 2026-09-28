# 出差申请单-er_tripreqbill

## 多出差人-多选基础资料表 t_er_tripchangetravel

- **表名称：** 多出差人-多选基础资料表
- **表名：** t_er_tripchangetravel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tripchangetravel_fid |  | fentryid |
| 2 | pk_er_tripchangetravel |  | fpkid |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 3 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 6 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 7 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 10 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 12 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invoiceattachinfo |  | fentryid |
| 2 | idx_er_invoiceattachinfo_fid |  | fid |

---

## 行程信息-子表 t_er_reqtripentry

- **表名称：** 行程信息-子表
- **表名：** t_er_reqtripentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriamount | 借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额 |
| 3 | ftriporiaccappamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 4 | faccusedamount | 已报销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额（本位币） |
| 5 | fconvertmode | fconvertmode | varchar | 5 |  | √ | ' ' |  |
| 6 | ftripcurrencyid | 行程币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | froundtrip | froundtrip | varchar | 5 |  | √ | ' ' |  |
| 9 | ftripamount | 借款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额（本位币） |
| 10 | ftripentrystatus | 行程状态 | varchar | 5 |  | √ | ' ' | 行程状态,枚举: A :暂存 B :提交 C :审核中 D :审核不通过 E :审核通过 G :已付款 I :关闭 |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | ftoplaceid | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 15 | fistripmulcurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 16 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 17 | fvehicle | 交通工具 | varchar | 20 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 |
| 18 | ffromplaceid | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 19 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fexchangerateprec | fexchangerateprec | int8 | 64 |  | √ | 0 |  |
| 22 | foriaccusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 23 | findex | 整数 | int8 | 64 |  | √ | 0 | 整数 |
| 24 | foriaccbalanceamount | 可用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用金额 |
| 25 | fexpeorirepayamount | 还款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额 |
| 26 | ftripmpmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 27 | ftripmpmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 28 | ftripexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 29 | fentrycreatetime | 行程分录创建时间 | timestamp | 0 |  |  | null | 行程分录创建时间 |
| 30 | fexperepayamount | 还款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额（本位币） |
| 31 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 32 | ftripaccappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fquotetype | 换算方式(行程) | bpchar | 1 |  | √ | '0' | 换算方式(行程),枚举: 0 :直接汇率 1 :间接汇率 |
| 36 | ftripday | 行程天数 | int8 | 64 |  | √ | 0 | 行程天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_rte_ftexpitemid |  | ftripexpenseitemid |
| 2 | idx_er_rte_fseq |  | fid,fseq |
| 3 | t_er_reqtripentry_pkey |  | fentryid |

---

## 费用明细-子表 t_er_reqentry

- **表名称：** 费用明细-子表
- **表名：** t_er_reqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fhappendate | fhappendate | timestamp | 0 |  |  | null |  |
| 2 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 3 | foriamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 4 | fconvertmode | fconvertmode | varchar | 5 |  | √ | ' ' |  |
| 5 | forientrybalamount | forientrybalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | famount | 本位币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本位币金额 |
| 8 | fisvactax | 增值税专票 | bpchar | 2 |  | √ | ' ' | 增值税专票 |
| 9 | fdaycount | 天数 | int8 | 64 |  | √ | 0 | 天数 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fpic | fpic | varchar | 255 |  | √ | ' ' |  |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | 差旅项目 er_tripexpenseitem |
| 14 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 15 | fnotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 16 | fexchangerateprec | fexchangerateprec | int8 | 64 |  | √ | 0 |  |
| 17 | fcomment | 备注 | varchar | 255 |  |  | null | 备注 |
| 18 | fcaldaycount | fcaldaycount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | ftriptoplaceid | 出差地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 20 | fnotaxoriamount | fnotaxoriamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 21 | fexpenseitemicon | 费用项目图标 | varchar | 255 |  | √ | ' ' | 费用项目图标 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fquotetype | 换算方式(明细) | bpchar | 1 |  | √ | '0' | 换算方式(明细),枚举: 0 :直接汇率 1 :间接汇率 |
| 25 | fentrybalamount | fentrybalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_re_fseq |  | fentryid,fseq |
| 2 | t_er_reqentry_pkey |  | fdetailid |

---

## 关联子实体-子表 t_er_reqentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reqentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_reqentry_lk |  | fpkid |
| 2 | idx_er_reqentry_lk_fdetailid |  | fdetailid |

---

## 无-多选基础资料表 t_er_tripentrymulwayto

- **表名称：** 无-多选基础资料表
- **表名：** t_er_tripentrymulwayto

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_tripentrymulwayto_pkey |  | fpkid |
| 2 | idx_er_mulwayto_entryid |  | fentryid,fbasedataid |

---

## 项目干系人-多选基础资料表 t_er_tripreqower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_tripreqower

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_triprequserid |  | fbasedataid |
| 2 | idx_er_tripreqbillid |  | fid |
| 3 | pk_t_er_tripreqower |  | fpkid |

---

## 出差人-多选基础资料表 t_er_reqbillpartner

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_reqbillpartner

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reqbillpartner_pkey |  | fpkid |
| 2 | idx_er_reqbillpart_entryid |  | fentryid,fbasedataid |

---

## 出差申请单-主表 t_er_reqbill

- **表名称：** 出差申请单-主表
- **表名：** t_er_reqbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | freimbursetime | 报销次数 | int8 | 64 |  | √ | 0 | 报销次数 |
| 5 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpartnerid | fpartnerid | int8 | 64 |  | √ | 0 |  |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 9 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 10 | frvehicle | 交通工具 | varchar | 10 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 6 :中转 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 13 | forigin | 来源 | varchar | 10 |  | √ | ' ' | 来源,枚举: 1 :WEB 2 :移动端 3 :语音助手 |
| 14 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fimageno | 影像编号 | varchar | 100 |  | √ | ' ' | 影像编号 |
| 16 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 17 | fcurrencysettingid | fcurrencysettingid | int8 | 64 |  | √ | 0 |  |
| 18 | fischange | 是否变更 | bpchar | 1 |  | √ | '0' | 是否变更 |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 20 | frfirstenddate | 第一段结束日期 | timestamp | 0 |  |  | null | 第一段结束日期 |
| 21 | fdescription | 事由 | varchar | 1000 |  |  | null | 事由 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | frfirstto | 第一段目的地 | varchar | 80 |  | √ | ' ' | 第一段目的地 |
| 24 | frstartdate | 出发日期 | timestamp | 0 |  |  | null | 出发日期 |
| 25 | fopenid | fopenid | varchar | 80 |  | √ | ' ' |  |
| 26 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 27 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 28 | fnextauditor | 下一步审核人 | varchar | 80 |  | √ | ' ' | 下一步审核人 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fbalanceamount | 未还余额 | numeric | 23 | 10 | √ | 0.0000000000 | 未还余额 |
| 32 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 33 | ftel | 联系方式 | varchar | 25 |  | √ | ' ' | 联系方式 |
| 34 | fistravelers | 多出差人 | bpchar | 1 |  | √ | '0' | 多出差人 |
| 35 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 36 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 37 | fplandays | 预计天数 | int8 | 64 |  | √ | 0 | 预计天数 |
| 38 | fsourcebillformid | fsourcebillformid | varchar | 30 |  | √ | ' ' |  |
| 39 | freturnedamount | 已还金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已还金额 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fusedamount | 已用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已用金额 |
| 42 | fencashamount | 付现金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付现金额 |
| 43 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_reqbill :费用申请单 er_tripreimbursebill :差旅费报销单 er_reimbursebill :费用报销单 er_loanbill :借款单 er_repaymentbill :还款单 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | ftriptypeid | 出差类型 | int8 | 64 |  | √ | 0 | 出差类型 er_triptype |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 49 | floanamount | 借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额 |
| 50 | fisloan | 是否借款 | bpchar | 1 |  | √ | ' ' | 是否借款 |
| 51 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |
| 52 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | frfrom | 出发地 | varchar | 80 |  | √ | ' ' | 出发地 |
| 54 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 55 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 56 | fsourcebillid | 源单ID | varchar | 200 |  | √ | ' ' | 源单ID |
| 57 | frto | 目的地 | varchar | 80 |  | √ | ' ' | 目的地 |
| 58 | frenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 59 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 60 | frepaymentdate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_rb_forgid |  | forgid |
| 2 | idx_er_rb_fbizdate_fbillno |  | fbizdate,fbillno |
| 3 | idx_er_rb_fcreatorid |  | fcreatorid |
| 4 | t_er_reqbill_pkey |  | fid |
| 5 | idx_er_rb_fapplierid |  | fapplierid |
| 6 | idx_er_rb_fbillno |  | fbillno |
| 7 | idx_er_rb_fcompanyid |  | fcompanyid |
| 8 | idx_er_rb_fbillstatus |  | fbillstatus |

---

## 出差申请单-反写记录表 t_er_reqbill_wb

- **表名称：** 出差申请单-反写记录表
- **表名：** t_er_reqbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reqbill_wb_fid |  | fid |
| 2 | t_er_reqbill_wb_pkey |  | fentryid |

---

## 出差申请单-关联追踪表 t_er_reqbill_tc

- **表名称：** 出差申请单-关联追踪表
- **表名：** t_er_reqbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reqbill_tc_pkey |  | fid |
| 2 | idx_er_reqbill_tc_fsbillid |  | fsbillid |
| 3 | idx_er_reqbill_tc_ftbillid |  | ftbillid |
| 4 | idx_er_reqbill_tc_tbill |  | ftbillid |
| 5 | idx_er_reqbill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_er_reqaccountentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reqaccountentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reqaccentry_lk_fentryid |  | fentryid |
| 2 | t_er_reqaccountentry_lk_pkey |  | fpkid |

---

## 付款信息-子表 t_er_tripreqpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_tripreqpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 13 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 14 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | ftargetexchange | 收款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 收款汇率 |
| 16 | ftargetpaybank | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 17 | ffeecurrency | 手续费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fdplocalamt | 付款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额(本位币) |
| 19 | ftargetpayamt | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 20 | ftargetpayacct | 付款账号（文本） | varchar | 50 |  | √ | ' ' | 付款账号（文本） |
| 21 | ftargetopenorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 23 | ftargetpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 24 | ftargetcurrency | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | ftargetsettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tqpe_targetbillid_no |  | ftargetbillid,ftargetbillno |
| 2 | idx_er_tqpe_feq |  | fid,fseq |
| 3 | t_er_tripreqpayentry_pkey |  | fentryid |

---

## 关联子实体-子表 t_er_reqbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reqbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reqbill_lk_pkey |  | fpkid |
| 2 | idx_er_reqbill_lk_fid |  | fid |

---

## 收款信息-子表 t_er_reqaccountentry

- **表名称：** 收款信息-子表
- **表名：** t_er_reqaccountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccpaidamount | 已还款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已还款金额（本位币） |
| 3 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 4 | foriamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 5 | fpayeraccount01 | 银行账号4位 | varchar | 50 |  | √ | ' ' | 银行账号4位 |
| 6 | fconvertmode | fconvertmode | varchar | 5 |  | √ | ' ' |  |
| 7 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | '0' | 分录状态,枚举: F :等待付款 G :已付款 E :审核通过 I :关闭 |
| 8 | fpayerdeptid | 收款人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fpayercompid | 收款人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 11 | foriaccappamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | famount | 金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 金额（本位币） |
| 14 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 15 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 16 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 17 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 18 | fpayeraccountname | 账户名称 | varchar | 50 |  | √ | ' ' | 账户名称 |
| 19 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 20 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 21 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 22 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 23 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 24 | fexchangerateprec | fexchangerateprec | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 26 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 27 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 28 | fbanklogo | 银行卡logo图标 | varchar | 255 |  | √ | ' ' | 银行卡logo图标 |
| 29 | faccounttype | faccounttype | varchar | 10 |  | √ | ' ' |  |
| 30 | fpayeraccount02 | 银行账号(_old) | varchar | 50 |  | √ | ' ' | 银行账号(_old) |
| 31 | fpaidamount | 已还款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已还款金额 |
| 32 | fpayeraccount | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 33 | faccappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 36 | fquotetype | 换算方式(收款) | bpchar | 1 |  | √ | '0' | 换算方式(收款),枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reqaccountentry_pkey |  | fentryid |
| 2 | idx_er_reqae_fseq |  | fid,fseq |

---

## 出差申请单-分表 t_er_reqbill_a

- **表名称：** 出差申请单-分表
- **表名：** t_er_reqbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 3 | ftripreimbursetype | 可下推的差旅报销单类型 | varchar | 10 |  | √ | 'card' | 可下推的差旅报销单类型,枚举: card :卡片式 grid :表格式 |
| 4 | fismanualrepay | 手否手动还款 | bpchar | 1 |  | √ | '0' | 手否手动还款 |
| 5 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 6 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 7 | froutetype | 单程/往返 | varchar | 10 |  | √ | ' ' | 单程/往返,枚举: 0 :单程 1 :往返 |
| 8 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_reqbill_a |  | fid |

---

## 出差申请单-多语言表 t_er_reqbill_l

- **表名称：** 出差申请单-多语言表
- **表名：** t_er_reqbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reqbill_l_pkey |  | fpkid |
| 2 | idx_er_reqb_l_id |  | fid,flocaleid |

---

## 途径地-多选基础资料表 t_er_historyentrymulwayto

- **表名称：** 途径地-多选基础资料表
- **表名：** t_er_historyentrymulwayto

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_historyentrymulwayto_entryid |  | fentryid,fbasedataid |
| 2 | pk_t_er_historyentrymulwayto |  | fpkid |

---

## 行程变更历史记录-子表 t_er_tripchangehistory

- **表名称：** 行程变更历史记录-子表
- **表名：** t_er_tripchangehistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 原始分录id | int8 | 64 |  | √ | 0 | 原始分录id |
| 3 | foriamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 4 | ftriporiaccappamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 5 | ftripcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ftripamount | 申请金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额（本位币） |
| 8 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | ftoplaceid | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 12 | fistripmulcurrency | 是否多币别 | bpchar | 1 |  | √ | '0' | 是否多币别 |
| 13 | fchangedate | 变更日期（废弃） | timestamp | 0 |  |  | null | 变更日期（废弃） |
| 14 | fvehicle | 交通工具 | varchar | 50 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 |
| 15 | fchanger | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ffromplaceid | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | fhistorytripmpmbizopreg | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 19 | fsrcentrydata | 原始分录json数据 | text | 0 |  |  | null | 原始分录json数据 |
| 20 | ftripexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 21 | fsrcentrydata_tag | 原始分录json数据_详情 | text | 0 |  |  | null | 原始分录json数据_详情 |
| 22 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 23 | ftripaccappamount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额(本位币) |
| 24 | fchangetime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 25 | fhistorytripmpmtask | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_change_srcentryid |  | fsrcentryid |
| 2 | pk_er_tripchangehistory |  | fentryid |

---

## 出差人-多选基础资料表 t_er_tripmultitravelers

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_tripmultitravelers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_travelersuserid |  | fbasedataid |
| 2 | idx_er_travelersbillid |  | fid |
| 3 | pk_t_er_tripmultitravelers |  | fpkid |
