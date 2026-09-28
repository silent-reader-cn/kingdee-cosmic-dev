# 差旅报销单(共享审批)-er_tripreimbursebill_ssc

## 发票合并信息-子表 t_er_invoicemerge

- **表名称：** 发票合并信息-子表
- **表名：** t_er_invoicemerge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeyserialno | 发票标识序列号 | varchar | 80 |  | √ | ' ' | 发票标识序列号 |
| 3 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoicemerge_fkeyse |  | fkeyserialno |
| 2 | t_er_invoicemerge_pkey |  | fentryid |

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

## 付款信息-子表 t_er_tripreimpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_tripreimpayentry

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
| 1 | idx_er_trpe_feq |  | fid,fseq |
| 2 | t_er_tripreimpayentry_pkey |  | fentryid |
| 3 | idx_er_trpe_targetbillid_no |  | ftargetbillid,ftargetbillno |

---

## 出差人-多选基础资料表 t_er_trip2reimpartner

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_trip2reimpartner

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_trip2reimpartner |  | fpkid |
| 2 | idx_er_trip2reimpartner |  | fdetailid |

---

## 座位等级-多选基础资料表 t_er_tripitemseatgrade

- **表名称：** 座位等级-多选基础资料表
- **表名：** t_er_tripitemseatgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 座位等级 er_seatgradestd |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_tripseatgrade |  | fbasedataid |
| 2 | ix_er_tripitemseatgrade_det |  | fdetailid |
| 3 | t_er_tripitemseatgrade_pkey |  | fpkid |

---

## 冲申请-子表 t_er_reimbclearapplyentry

- **表名称：** 冲申请-子表
- **表名：** t_er_reimbclearapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplytocity | 目的城市 | varchar | 80 |  | √ | ' ' | 行政区划 bd_admindivision |
| 3 | freimbursedamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 4 | fapplystartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fapplyfromcity | 出发城市 | varchar | 80 |  | √ | ' ' | 行政区划 bd_admindivision |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fapplyrvehicle | 交通工具 | varchar | 10 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 6 :中转 |
| 8 | fapplyperson | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fapplybilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 10 | fapplycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 11 | fsourceapplybillid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 12 | fapplybillno | 申请单号 | varchar | 80 |  | √ | '0' | 申请单号 |
| 13 | fapplydescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 14 | fapplyenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 15 | fapplyexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_reimbclearapplyentry |  | fentryid |
| 2 | idx_er_clearapplyent_fid |  | fid |
| 3 | idx_er_clearapplyent_fapplyno |  | fapplybillno |

---

## 项目干系人-多选基础资料表 t_er_tripreimburseower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_tripreimburseower

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
| 1 | idx_er_tripreimburseower_fid |  | fid |
| 2 | pk_t_er_tripreimburseower |  | fpkid |

---

## 关联子实体-子表 t_er_reimbclearloanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reimbclearloanentry_lk

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
| 1 | t_er_reimbclearloanentry_lk_pkey |  | fpkid |
| 2 | idx_er_reimclloet_lk_fetid |  | fentryid |

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

## 关联子实体-子表 t_er_reimbursebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reimbursebill_lk

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
| 1 | idx_reimbursebill_lk_fid |  | fid |
| 2 | t_er_reimbursebill_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_er_reimbursetripentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reimbursetripentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reimbentry_lk_entryid |  | fentryid |
| 2 | pk_t_er_reimbursetripentry_lk |  | fpkid |
| 3 | idx_er_reimbursetripentry_lk_fk |  | fentryid |

---

## 差旅报销单(共享审批)-主表 t_er_reimbursebill

- **表名称：** 差旅报销单(共享审批)-主表
- **表名：** t_er_reimbursebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 5 | fcheckloanamount | 冲销借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销借款金额 |
| 6 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 7 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fpartnerid | fpartnerid | int8 | 64 |  | √ | 0 |  |
| 9 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | flastaccloanamount | flastaccloanamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 12 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 13 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 14 | fmonthrulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 15 | frvehicle | 交通工具 | varchar | 10 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 6 :中转 |
| 16 | fheadproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | forigin | 来源 | varchar | 10 |  | √ | ' ' | 来源,枚举: 1 :WEB 2 :移动端 3 :语音助手 |
| 20 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 21 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | fimageno | 影像编号 | varchar | 255 |  | √ | ' ' | 影像编号 |
| 23 | fheadloancurrency | 冲借款币别（单一） | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 25 | floanchecktype | 核销类型 | varchar | 1 |  | √ | ' ' | 核销类型 |
| 26 | foffsetinvoiceno | 可抵扣发票号码 | varchar | 255 |  | √ | ' ' | 可抵扣发票号码 |
| 27 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 28 | fcurrencysettingid | fcurrencysettingid | int8 | 64 |  | √ | 0 |  |
| 29 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 30 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 31 | frfirstenddate | 第一段结束日期 | timestamp | 0 |  |  | null | 第一段结束日期 |
| 32 | fmonthsettleamount | 月结金额 | numeric | 23 | 10 | √ | 0.0000000000 | 月结金额 |
| 33 | freceiveimagetime | 接收影像或附件时间 | timestamp | 0 |  |  | null | 接收影像或附件时间 |
| 34 | finvoiceoffsetamount | 抵扣税额（发票信息） | numeric | 23 | 10 | √ | 0 | 抵扣税额（发票信息） |
| 35 | fdescription | 事由 | varchar | 1000 |  |  | null | 事由 |
| 36 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 37 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '1' | 智能发票报销 |
| 38 | foffsetamount | 抵扣税额合计(原币合计) | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额合计(原币合计) |
| 39 | frfirstto | 第一段目的地 | varchar | 80 |  | √ | ' ' | 第一段目的地 |
| 40 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 |
| 41 | frstartdate | 出发日期 | timestamp | 0 |  |  | null | 出发日期 |
| 42 | fopenid | fopenid | varchar | 80 |  | √ | ' ' |  |
| 43 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 44 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 45 | fnextauditor | 下一步审核人 | varchar | 80 |  | √ | ' ' | 下一步审核人 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | ' ' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 48 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | fbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 50 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 51 | fheadexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 52 | ftel | 联系方式 | varchar | 25 |  | √ | ' ' | 联系方式 |
| 53 | fisshared | 是否已分摊 | bpchar | 1 |  | √ | '0' | 是否已分摊 |
| 54 | fistravelers | 多出差人 | bpchar | 1 |  | √ | '0' | 多出差人 |
| 55 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 56 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 57 | fprojectsharecount | 下游项目成本分摊单数 | int8 | 64 |  | √ | 0 | 下游项目成本分摊单数 |
| 58 | fplandays | fplandays | int8 | 64 |  | √ | 0 |  |
| 59 | fsourcebillformid | fsourcebillformid | varchar | 30 |  | √ | ' ' |  |
| 60 | fisentrycurrency | fisentrycurrency | varchar | 1 |  | √ | ' ' |  |
| 61 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 62 | fneedsuppleinvoice | 发票后补 | bpchar | 1 |  | √ | '0' | 发票后补 |
| 63 | fsharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 64 | fbillkind | 单据种类 | bpchar | 1 |  | √ | '0' | 单据种类,枚举: 0 :卡片展示的差旅报销单 1 :表格展示的差旅报销单 |
| 65 | fabovequotadept | 部门额度是否超额 | varchar | 30 |  | √ | ' ' | 部门额度是否超额,枚举: 1 :超额 2 :未超额 0 :- |
| 66 | fusedamount | 已用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已用金额 |
| 67 | fencashamount | 付现金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付现金额 |
| 68 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 69 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_reqbill :费用申请单 er_tripreimbursebill :差旅费报销单 er_reimbursebill :费用报销单 er_loanbill :借款单 er_repaymentbill :还款单 |
| 70 | fismultiexpitem | 多费用项目 | bpchar | 1 |  | √ | '0' | 多费用项目 |
| 71 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 72 | fis_all_einvoice | 发票状态 | bpchar | 1 |  | √ | '0' | 发票状态,枚举: 0 :无发票 1 :全电票 2 :含纸票 3 :其它 |
| 73 | fheadhappendate | 费用归属月份 | timestamp | 0 |  |  | null | 费用归属月份 |
| 74 | ftriptypeid | 出差类型 | int8 | 64 |  | √ | 0 | 出差类型 er_triptype |
| 75 | freimbursecontrolcomany | freimbursecontrolcomany | int8 | 64 |  | √ | 0 |  |
| 76 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 77 | fabovequotaemp | 员工额度是否超额 | varchar | 30 |  | √ | ' ' | 员工额度是否超额,枚举: 1 :超额 2 :未超额 0 :- |
| 78 | fisstdover | 是否超标 | bpchar | 1 |  | √ | '0' | 是否超标 |
| 79 | fiscurrency | 多币别 | varchar | 1 |  | √ | ' ' | 多币别 |
| 80 | fisloan | 是否冲销出差借款单 | varchar | 1 |  | √ | ' ' | 是否冲销出差借款单 |
| 81 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |
| 82 | fmonthruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |
| 83 | fapplierid | 报销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 84 | frfrom | 出发地 | varchar | 80 |  | √ | ' ' | 出发地 |
| 85 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 86 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 87 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 88 | fsourcebillid | 上游出差申请单ID | varchar | 200 |  | √ | ' ' | 上游出差申请单ID |
| 89 | frto | 目的地 | varchar | 80 |  | √ | ' ' | 目的地 |
| 90 | frenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 91 | ftarbillstatus | 目标单据 | varchar | 30 |  | √ | ' ' | 目标单据,枚举: B1 :项目成本分摊单 |
| 92 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 93 | frepaymentdate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reim_fapplierid |  | fapplierid |
| 2 | idx_er_reim_ccom_adate |  | fcostcompanyid,fauditdate |
| 3 | idx_er_reim_fcreatorid |  | fcreatorid |
| 4 | idx_er_reim_fbillstatus |  | fbillstatus |
| 5 | t_er_reimbursebill_pkey |  | fid |
| 6 | idx_er_reim_fbillno |  | fbillno |
| 7 | idx_er_reim_fbizdate_fbillno |  | fbizdate,fbillno |
| 8 | idx_er_reim_fcompanyid |  | fcompanyid |

---

## 冲申请与费用明细-子表 t_er_writeofftriprelate

- **表名称：** 冲申请与费用明细-子表
- **表名：** t_er_writeofftriprelate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fwriteoffentryid | 冲申请行id | int8 | 64 |  | √ | 0 | 冲申请行id |
| 4 | fexpenseid | 行程明细id | int8 | 64 |  | √ | 0 | 行程明细id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_writeofftriprelate |  | fentryid |
| 2 | idx_er_writeofftriprelate_fid |  | fid |

---

## 差旅明细-子表 t_er_reimburseentry

- **表名称：** 差旅明细-子表
- **表名：** t_er_reimburseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fhappendate | fhappendate | timestamp | 0 |  |  | null |  |
| 2 | ftravelexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 5 | fconvertmode | fconvertmode | varchar | 5 |  | √ | ' ' |  |
| 6 | fordernum | 关联订单号 | varchar | 1000 |  | √ | ' ' | 关联订单号 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 9 | foriginhighseasondays | 原始旺季天数 | numeric | 23 | 10 | √ | 0.0000000000 | 原始旺季天数 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 12 | fsettlementtype | 结算方式 | bpchar | 1 |  | √ | '1' | 结算方式,枚举: 1 :现付 2 :月结 |
| 13 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 |
| 14 | forderformid | 订单表单ID | varchar | 1000 |  | √ | ' ' | 订单表单ID |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 17 | ftravelcostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 19 | foverdesc | 超标说明 | varchar | 255 |  |  | null | 超标说明 |
| 20 | fhightripstandardamount | 旺季差旅标准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 旺季差旅标准金额 |
| 21 | fexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | 差旅项目 er_tripexpenseitem |
| 22 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 23 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 24 | fstdexchangerate | 标准汇率 | numeric | 23 | 10 | √ | 1 | 标准汇率 |
| 25 | fnotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 26 | fcheckindatestr | 出发(入住)日期 | varchar | 30 |  | √ | ' ' | 出发(入住)日期 |
| 27 | fcaldaycount | 标准天数 | numeric | 23 | 10 | √ | 0.0000000000 | 标准天数 |
| 28 | ftripstdamount | 差旅标准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 差旅标准金额 |
| 29 | ftriptoplaceid | 出差地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 30 | fcheckoutdatestr | 离店日期 | varchar | 30 |  | √ | ' ' | 离店日期 |
| 31 | fnotaxoriamount | fnotaxoriamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | ffromcitystr | 出发(入住)地 | varchar | 255 |  | √ | ' ' | 出发(入住)地 |
| 33 | fispassentry | 是否下穿明细页面 | bpchar | 2 |  | √ | ' ' | 是否下穿明细页面 |
| 34 | fexpenseitemicon | 费用项目图标 | varchar | 255 |  | √ | ' ' | 费用项目图标 |
| 35 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 36 | ftirpcitystr | 城市 | varchar | 100 |  | √ | ' ' | 城市 |
| 37 | forientryappamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 38 | fcabinisover | 舱位是否超标（废弃） | bpchar | 1 |  | √ | '0' | 舱位是否超标（废弃） |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | fisdefault | 是否默认推出明细 | bpchar | 1 |  | √ | '0' | 是否默认推出明细 |
| 41 | fprovider | 服务商 | varchar | 100 |  | √ | ' ' | 服务商 |
| 42 | fentryappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 43 | ftravelhappendate | 费用归属月份 | timestamp | 0 |  |  | null | 费用归属月份 |
| 44 | fstdexpquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 45 | foriamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 46 | fhighseasondaycount | 旺季天数 | numeric | 23 | 10 | √ | 0.0000000000 | 旺季天数 |
| 47 | forientrybalamount | forientrybalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 48 | fcontrolmethod | 控制方式 | varchar | 30 |  | √ | ' ' | 控制方式,枚举: 0 :无控制 1 :严格控制 2 :提示且填写超标说明 3 :仅提示 |
| 49 | fhighseason | 是否旺季 | bpchar | 1 |  | √ | '0' | 是否旺季 |
| 50 | famount | 报销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额（本位币） |
| 51 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 52 | ftrip2startdate | 行程期间.开始 | timestamp | 0 |  |  | null | 行程期间.开始 |
| 53 | fisvactax | 专票 | bpchar | 1 |  | √ | ' ' | 专票 |
| 54 | fdaycount | 行程天数 | int8 | 64 |  | √ | 0 | 行程天数 |
| 55 | ftriparea | 出差地域 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 56 | freimbursestdid | freimbursestdid | int8 | 64 |  | √ | 0 |  |
| 57 | fpic | fpic | varchar | 255 |  | √ | ' ' |  |
| 58 | ftravelcostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 59 | fpulltravelorder | 是否商旅上拉订单 | bpchar | 1 |  | √ | '0' | 是否商旅上拉订单 |
| 60 | ftocitystr | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 61 | ftravelcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 62 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 |
| 63 | ftravelquotactldept | 额度控制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 64 | fstdentrycurrency | 标准币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 65 | fismulticurrency | 是否非本位币 | bpchar | 2 |  | √ | ' ' | 是否非本位币 |
| 66 | fexchangerateprec | fexchangerateprec | int8 | 64 |  | √ | 0 |  |
| 67 | fcomment | 备注 | varchar | 255 |  |  | null | 备注 |
| 68 | fitemreasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 69 | fstddetail | 标准明细 | varchar | 255 |  | √ | ' ' | 标准明细 |
| 70 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 71 | ftrip2enddate | 行程期间.结束 | timestamp | 0 |  |  | null | 行程期间.结束 |
| 72 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 73 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 74 | fquotetype | 换算方式(明细) | bpchar | 1 |  | √ | '0' | 换算方式(明细),枚举: 0 :直接汇率 1 :间接汇率 |
| 75 | fentrybalamount | fentrybalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reimburseentry_pkey |  | fdetailid |
| 2 | idx_t_er_reimburseentry_fseq |  | fentryid,fseq |

---

## 发票明细-子表 t_er_invoiceitem

- **表名称：** 发票明细-子表
- **表名：** t_er_invoiceitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | finvoiceitemoffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fitementryid | 费用项目分录id | int8 | 64 |  | √ | 0 | 费用项目分录id |
| 8 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 9 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 10 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 11 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 12 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 13 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 14 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | '1' | 发票抵扣 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 17 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoiceitem_fid |  | fid |
| 2 | idx_er_invoiceitem_invhead |  | finvoiceheadentryid |
| 3 | idx_er_invoiceitem_itementry |  | fitementryid |
| 4 | t_er_invoiceitem_pkey |  | fentryid |

---

## 差旅报销单(共享审批)-关联追踪表 t_er_reimbursebill_tc

- **表名称：** 差旅报销单(共享审批)-关联追踪表
- **表名：** t_er_reimbursebill_tc

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
| 1 | idx_er_reimbursebill_tc_tid |  | ftid |
| 2 | idx_er_reimbursebill_tc_tbill |  | ftbillid |
| 3 | idx_er_reim_tc_fsbillid |  | fsbillid |
| 4 | t_er_reimbursebill_tc_pkey |  | fid |
| 5 | idx_er_reim_tc_ftbillid |  | ftbillid |

---

## 发票与费用明细-子表 t_er_invoiceandexpense

- **表名称：** 发票与费用明细-子表
- **表名：** t_er_invoiceandexpense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | finvoiceentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 4 | fexpenseentryid | 费用明细分录id | int8 | 64 |  | √ | 0 | 费用明细分录id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ie_finvoiceentryid |  | finvoiceentryid |
| 2 | idx_ie_fexpenseentryid |  | fexpenseentryid |
| 3 | t_er_invoiceandexpense_pkey |  | fentryid |
| 4 | idx_invoiceandexpense_id |  | fid |

---

## 差旅报销单(共享审批)-反写记录表 t_er_reimbursebill_wb

- **表名称：** 差旅报销单(共享审批)-反写记录表
- **表名：** t_er_reimbursebill_wb

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
| 1 | idx_er_reimbursebill_wb_fid |  | fid |
| 2 | t_er_reimbursebill_wb_pkey |  | fentryid |

---

## 出差人-多选基础资料表 t_er_tripreimbursepartner

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_tripreimbursepartner

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
| 1 | t_er_tripreimbursepartner_pkey |  | fpkid |
| 2 | idx_er_trippartner_fentryid |  | fentryid |

---

## 发票信息-子表 t_er_invoiceinfo

- **表名称：** 发票信息-子表
- **表名：** t_er_invoiceinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmapexpenseinfo | 关联费用 | varchar | 255 |  |  | null | 关联费用 |
| 3 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 5 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 8 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 9 | fbuyeraddressphone | 地址电话 | varchar | 255 |  | √ | ' ' | 地址电话 |
| 10 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 11 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 12 | fissupplement | 后补发票 | bpchar | 1 |  | √ | '0' | 后补发票,枚举: 0 :否 1 :是 |
| 13 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 15 | fordertype | 商旅订单类型 | bpchar | 1 |  | √ | ' ' | 商旅订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 16 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 17 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 18 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 19 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 20 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 21 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 22 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 25 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 26 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 27 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 28 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 29 | finvoicecurrencyid | 发票币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 23 :通用机打电子发票 |
| 32 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 33 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 34 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 35 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 36 | ffairtime | 飞机乘机时间 | varchar | 20 |  | √ | ' ' | 飞机乘机时间 |
| 37 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 38 | fsequencenum | 是否连号 | varchar | 30 |  | √ | ' ' | 是否连号,枚举: 1 :是 2 :否 |
| 39 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 42 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 43 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 44 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 45 | fticketchanges | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 |
| 46 | finvoicesrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 47 | fisxbrl | 是否xbrl | bpchar | 1 |  | √ | '0' | 是否xbrl |
| 48 | finvoiceischange | 是否修改 | varchar | 30 |  | √ | ' ' | 是否修改,枚举: 1 :否 2 :是 |
| 49 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 50 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | '3' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 51 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 52 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 53 | finvoicesrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 54 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 55 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 56 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 57 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 58 | fairconstfee | 机场建设费 | numeric | 23 | 10 | √ | 0 | 机场建设费 |
| 59 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 60 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 61 | fislinkagedetail | 是否费用联动 | bpchar | 1 |  | √ | '0' | 是否费用联动 |
| 62 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 63 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 64 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 65 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 66 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 67 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 68 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 69 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 70 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 71 | finvoiceordernum | 订单号 | varchar | 500 |  | √ | ' ' | 订单号 |
| 72 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 73 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 74 | fismapexpense | 是否关联 | bpchar | 1 |  | √ | '1' | 是否关联,枚举: 1 :是 0 :否 |
| 75 | finvoicesrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_expense_recordbill :费用记录 er_trip_recordbill :差旅记录 |
| 76 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 77 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 78 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoice_query |  | finvoicetype,finvoicedate |
| 2 | idx_er_invoice_serialno |  | fserialno |
| 3 | idx_er_invoiceinfo_fseq |  | fid,fseq |
| 4 | t_er_invoiceinfo_pkey |  | fentryid |

---

## 摊销明细-子表 t_er_tripresharedetail

- **表名称：** 摊销明细-子表
- **表名：** t_er_tripresharedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 5 | fsdentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 10 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 11 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 12 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 13 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 16 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 17 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 18 | fcurprice | 核定不含税金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额本位币 |
| 19 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 22 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 23 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 24 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 30 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 31 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 32 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 33 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 34 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 35 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 36 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 37 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 38 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 40 | fsdentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tripresharedetail_fseq |  | fid,fseq |
| 2 | pk_t_er_tripresharedetail |  | fdetailid |

---

## 差旅明细-分表 t_er_reimburseentry_a

- **表名称：** 差旅明细-分表
- **表名：** t_er_reimburseentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftrip2travelerscount | 出差人数 | int8 | 64 |  | √ | 0 | 出差人数 |
| 2 | fwbsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 3 | fsplitparent | 拆分父分录 | varchar | 32 |  | √ | ' ' | 拆分父分录 |
| 4 | ftrip2sharedamount | 已分摊金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额（本位币） |
| 5 | ftrip2to | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 6 | fwbsrcbillno | 源单编码 | varchar | 100 |  | √ | ' ' | 源单编码 |
| 7 | ftrip2orisharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 8 | fwbsrcbilltype | 源单类型 | varchar | 100 |  | √ | ' ' | 源单类型,枚举: |
| 9 | fisover | 是否超标 | bpchar | 1 |  | √ | '0' | 是否超标,枚举: 1 :是 0 :否 |
| 10 | ftrip2from | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 11 | fuseroutstdctrl | 实报实销 | bpchar | 1 |  | √ | '0' | 实报实销 |
| 12 | fiscancelorder | 是否退订订单 | bpchar | 1 |  | √ | '0' | 是否退订订单 |
| 13 | finvoicefromparent | 发票来源父节点 | bpchar | 1 |  | √ | '0' | 发票来源父节点 |
| 14 | fwbsrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | ftrip2tripday | ftrip2tripday | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_reimburseentry_a |  | fdetailid |
| 2 | idx_t_er_reimburseentry_a_fseq |  | fentryid |

---

## 关联子实体-子表 t_er_reimburseentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reimburseentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_reimburseentry_lk |  | fpkid |
| 2 | idx_er_reimburseentry_lk_fk |  | fdetailid |

---

## 冲借款-子表 t_er_reimbclearloanentry

- **表名称：** 冲借款-子表
- **表名：** t_er_reimbclearloanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | floanbillid | 借款单id | int8 | 64 |  | √ | 0 | 借款单id |
| 5 | fsnapclearoriamount | 快照冲销金额（原币） | numeric | 23 | 10 | √ | 0.0000000000 | 快照冲销金额（原币） |
| 6 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 10 | fsnapclearamount | 快照冲销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 快照冲销金额（本位币） |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | fclearoriamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 13 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 14 | freqaccountentryid | 借款分录ID | int8 | 64 |  | √ | 0 | 借款分录ID |
| 15 | fclearamount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额（本位币） |
| 16 | foribalanceamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 17 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_tripreqbill :出差借款单 |
| 18 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | faccbalanceamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额（本位币） |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fquotetype | 换算方式（冲借款） | bpchar | 1 |  | √ | '0' | 换算方式（冲借款）,枚举: 0 :直接汇率 1 :间接汇率 |
| 22 | fbillno | 借款单编号 | varchar | 30 |  | √ | ' ' | 借款单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reimclelanent_fseq |  | fid,fseq |
| 2 | t_er_reimbclearloanentry_pkey |  | fentryid |

---

## 申请单出差人-多选基础资料表 t_er_tripapplytravelers

- **表名称：** 申请单出差人-多选基础资料表
- **表名：** t_er_tripapplytravelers

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
| 1 | idx_er_travelers_fpkid |  | fentryid |
| 2 | pk_t_er_tripapplytravelers |  | fpkid |

---

## 行程信息-子表 t_er_reimbursetripentry

- **表名称：** 行程信息-子表
- **表名：** t_er_reimbursetripentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftripallowanceover | 补助超标 | numeric | 23 | 10 | √ | 0 | 补助超标 |
| 3 | fiscreateprojectcostshare | 生成项目分摊单 | int8 | 64 |  | √ | 0 | 生成项目分摊单 |
| 4 | fconvertmode | fconvertmode | varchar | 5 |  | √ | ' ' |  |
| 5 | ftripcurrencyid | 行程币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | ftaxamounttotal | 税额汇总（本位币）(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 税额汇总（本位币）(废弃) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | froundtrip | froundtrip | varchar | 5 |  | √ | ' ' |  |
| 9 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 10 | ftripamount | 本位币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本位币金额 |
| 11 | ftripentrystatus | 行程状态 | varchar | 5 |  | √ | ' ' | 行程状态,枚举: A :暂存 B :提交 C :审核中 D :审核不通过 E :审核通过 |
| 12 | fpricetotal | 价款汇总 | numeric | 23 | 10 | √ | 0.0000000000 | 价款汇总 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 15 | ftoplaceid | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 16 | fistripmulcurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 17 | fvehicle | 交通工具 | varchar | 50 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 |
| 18 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | ftripappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | ftripmpmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 22 | ftripapporiamount | 核定金额（原币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（原币） |
| 23 | fnotaxamounttotal | 不含税金额汇总（本位币）(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额汇总（本位币）(废弃) |
| 24 | ftripmpmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 25 | ftripexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | ftripday | 行程天数 | int8 | 64 |  | √ | 0 | 行程天数 |
| 29 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 30 | ftaxamounttotalori | 税额汇总（原币） | numeric | 23 | 10 | √ | 0.0000000000 | 税额汇总（原币） |
| 31 | ftripdeductibletax | 行程抵扣税额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 行程抵扣税额合计 |
| 32 | ftravelerid | 出差人(单选)废弃 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | ftripvehicleamount | 长途交通费 | numeric | 23 | 10 | √ | 0 | 长途交通费 |
| 34 | foriamount | 原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原币金额 |
| 35 | fnotaxamounttotalori | 不含税金额汇总（原币） | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额汇总（原币） |
| 36 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fsharedamount | 已分摊金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额（本位币） |
| 38 | fexpwithholdingamount | 已预提金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额本位币 |
| 39 | ftripallowanceamount | 补助 | numeric | 23 | 10 | √ | 0 | 补助 |
| 40 | ftriphappendate | 费用归属月份 | timestamp | 0 |  |  | null | 费用归属月份 |
| 41 | ffromplaceid | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 42 | ftripentrysourceid | 源单行程分录ID | int8 | 64 |  | √ | 0 | 源单行程分录ID |
| 43 | fisexistmonthly | 是否存在月结订单 | bpchar | 1 |  | √ | '0' | 是否存在月结订单 |
| 44 | fexchangerateprec | fexchangerateprec | int8 | 64 |  | √ | 0 |  |
| 45 | ftripotheramount | 其他费用 | numeric | 23 | 10 | √ | 0 | 其他费用 |
| 46 | ftripappnottaxamount | 核定不含税金额（本位币）合计 | numeric | 23 | 10 | √ | 0 | 核定不含税金额（本位币）合计 |
| 47 | ftripentryarea | 出差地域 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 48 | ftripaccommodationamt | 住宿费 | numeric | 23 | 10 | √ | 0 | 住宿费 |
| 49 | forisharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 50 | ftripaccommodationover | 住宿超标 | numeric | 23 | 10 | √ | 0 | 住宿超标 |
| 51 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fquotetype | 换算方式(行程) | bpchar | 1 |  | √ | '0' | 换算方式(行程),枚举: 0 :直接汇率 1 :间接汇率 |
| 53 | ftripvehicleover | 交通工具超标 | bpchar | 1 |  | √ | '0' | 交通工具超标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reimbursetripentry_pkey |  | fentryid |
| 2 | idx_er_rbte_fseq |  | fid,fseq |

---

## 分摊明细-子表 t_er_tripresharerule

- **表名称：** 分摊明细-子表
- **表名：** t_er_tripresharerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | fsharecurrency | fsharecurrency | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 8 | fsharewaitseq | fsharewaitseq | int4 | 32 |  | √ | 0 |  |
| 9 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 10 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fshareappamount | fshareappamount | numeric | 23 | 10 | √ | 0 |  |
| 13 | fentryexpenseitem | fentryexpenseitem | int8 | 64 |  | √ | 0 |  |
| 14 | fsharewaitid | fsharewaitid | int8 | 64 |  | √ | 0 |  |
| 15 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_tripresharerule |  | fdetailid |
| 2 | idx_er_tripresharerule_fseq |  | fid,fseq |

---

## 关联子实体-子表 t_er_reimbclearapplyentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_reimbclearapplyentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reimbclearapplyentry_lk_fk |  | fentryid |
| 2 | pk_er_reimbclearapplyentry_lk |  | fpkid |

---

## 标准座位等级（存储可用标准）-多选基础资料表 t_er_tripstdseatgrade

- **表名称：** 标准座位等级（存储可用标准）-多选基础资料表
- **表名：** t_er_tripstdseatgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 座位等级 er_seatgradestd |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_tripstdseatgrade |  | fpkid |
| 2 | idx_er_detailid_stdgrade |  | fdetailid,fbasedataid |

---

## 收款信息-子表 t_er_reimaccountentry

- **表名称：** 收款信息-子表
- **表名：** t_er_reimaccountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 3 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 4 | fpayeraccount01 | 银行账号4位 | varchar | 50 |  | √ | ' ' | 银行账号4位 |
| 5 | fsrcoribalamount | 源单分录原币可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 源单分录原币可用余额 |
| 6 | fconvertmode | fconvertmode | varchar | 5 |  | √ | ' ' |  |
| 7 | fsourceentryid | fsourceentryid | varchar | 50 |  | √ | ' ' |  |
| 8 | fsrcbalamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 9 | flastaccloanamount | 上一次冲借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 上一次冲借款金额 |
| 10 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | '0' | 分录状态,枚举: F :等待付款 G :已付款 E :审核通过 |
| 11 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 12 | faccsourceentryid | 源单分录ID | varchar | 100 |  | √ | ' ' | 源单分录ID |
| 13 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 14 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 15 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 16 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 17 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 18 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 19 | fpayeraccountname | 账户名称 | varchar | 50 |  | √ | ' ' | 账户名称 |
| 20 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 21 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 22 | facccostcompany | 付款公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 24 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 25 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 26 | fexchangerateprec | fexchangerateprec | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 27 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 28 | faccloanamount | 冲借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲借款金额 |
| 29 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 30 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 31 | faccloancurrencyid | 冲借款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | faccreimamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 33 | fbanklogo | 银行卡logo图标 | varchar | 255 |  | √ | ' ' | 银行卡logo图标 |
| 34 | faccounttype | faccounttype | varchar | 10 |  | √ | ' ' |  |
| 35 | fpayeraccount02 | 银行账号(显示_old) | varchar | 50 |  | √ | ' ' | 银行账号(显示_old) |
| 36 | fpayeraccount | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fquotetype | 换算方式(收款) | bpchar | 1 |  | √ | '0' | 换算方式(收款),枚举: 0 :直接汇率 1 :间接汇率 |
| 40 | facccurrencyid | 报销币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_rae_fseq |  | fid,fseq |
| 2 | t_er_reimaccountentry_pkey |  | fentryid |

---

## 差旅报销单(共享审批)-分表 t_er_reimbursebill_a

- **表名称：** 差旅报销单(共享审批)-分表
- **表名：** t_er_reimbursebill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fautogenshare | 自动生成分摊单 | bpchar | 1 |  | √ | '0' | 自动生成分摊单 |
| 3 | fisinvoicemodified | 发票修改 | bpchar | 1 |  | √ | '0' | 发票修改 |
| 4 | ftravelerssamestd | 多出差人同行程 | bpchar | 1 |  | √ | '0' | 多出差人同行程 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_reimbursebill_a |  | fid |
| 2 | idx_er_reimbill_a |  | fisinvoicemodified |

---

## 差旅报销单(共享审批)-多语言表 t_er_reimbursebill_l

- **表名称：** 差旅报销单(共享审批)-多语言表
- **表名：** t_er_reimbursebill_l

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
| 1 | t_er_reimbursebill_l_pkey |  | fpkid |
| 2 | idx_er_reimbursebill_l_fid |  | fid,flocaleid |

---

## 途径地-多选基础资料表 t_er_trip2mulwayto

- **表名称：** 途径地-多选基础资料表
- **表名：** t_er_trip2mulwayto

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trip2mulwayto_entryid |  | fdetailid |
| 2 | pk_er_trip2mulwayto |  | fpkid |
