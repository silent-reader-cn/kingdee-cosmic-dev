# 进项账票比对结果单-tcvat_in_accinv_comp

## 进项账票比对结果单-主表 t_tcvat_in_accinv_comp

- **表名称：** 进项账票比对结果单-主表
- **表名：** t_tcvat_in_accinv_comp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbqyspbqyrzamtsum | 本期已收票，本期已入账税额合计 | numeric | 23 | 10 | √ | 0 | 本期已收票，本期已入账税额合计 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fwfstartdate | 核销期间.开始 | timestamp | 0 |  |  | null | 核销期间.开始 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 11 | fwqwspbqyrzamtsum | 本期未收票，本期已入账税额合计 | numeric | 23 | 10 | √ | 0 | 本期未收票，本期已入账税额合计 |
| 12 | fenddate | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 13 | fwfenddate | 核销期间.结束 | timestamp | 0 |  |  | null | 核销期间.结束 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fstartdate | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 16 | fbqyspbqwrzamtsum | 本期已收票，本期未入账税额合计 | numeric | 23 | 10 | √ | 0 | 本期已收票，本期未入账税额合计 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_in_accinv_comp |  | forgid,fwriteofftypeid,fstartdate,fenddate |
| 2 | pk_tcvat_in_accinv_comp |  | fid |

---

## 本期已收票，本期未入账-子表 t_tcvat_in_accinvcom_ent2

- **表名称：** 本期已收票，本期未入账-子表
- **表名：** t_tcvat_in_accinvcom_ent2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 发票税额 | numeric | 23 | 10 | √ | 0 | 发票税额 |
| 3 | finvoiceinfo | 发票信息 | varchar | 50 |  | √ | ' ' | 发票信息,枚举: ty_1 :电子普通发票 ty_2 :电子专用发票 ty_3 :增值税普通发票 ty_4 :增值税专用发票 ty_5 :普通纸质卷票 ty_7 :通用机打发票 ty_8 :出租车票 ty_9 :火车票 ty_10 :飞机行程单 ty_11 :其它票 ty_12 :机动车销售发票 ty_13 :二手车销售发票 ty_14 :定额发票 ty_15 :通行费电子发票 ty_16 :公路汽车票 ty_17 :过路桥费发票 ty_19 :完税证明 ty_20 :轮船票 ty_23 :通用机打电子发票 ty_30 :海外发票 st_3 :红冲 st_2 :作废 ex_1 :未用 ex_30 :在用 ex_60 :已用 ex_65 :已入账 ch_1 :已验 ch_2 :未验 ch_3 :未验 ch_4 :不查验 or_0 :未签收 or_1 :已签收 au_0 :未勾选 au_1 :已勾选 au_2 :已认证 au_3 :已认证 au_4 :预勾选 au_5 :勾选中 td_1 :旅客运输抵扣 mo_1 :已改 ty_21 :海关缴款书 ty_24 :火车票退票凭证 ty_25 :财政电子票据 ty_26 :数电普票 ty_27 :数电专票 st_7 :部分红冲 st_8 :全额红冲 st_4 :异常 st_6 :红字发票待确认 |
| 4 | foriginaltime | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 5 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 6 | fsalername | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 9 | fauthenticateflag | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 5 :勾选中 |
| 10 | fnowriteoff | 未核销税额 | numeric | 23 | 10 | √ | 0 | 未核销税额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_in_accinvcom_ent2_fk |  | fid |
| 2 | pk_tcvat_in_accinvcom_ent2 |  | fentryid |

---

## 本期未收票，本期已入账-子表 t_tcvat_in_accinvcom_ent1

- **表名称：** 本期未收票，本期已入账-子表
- **表名：** t_tcvat_in_accinvcom_ent1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |
| 3 | fje | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 5 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 6 | fbalance | 科目 | varchar | 36 |  | √ | ' ' | 科目 tdm_account |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fvouchercode | 记账凭证编号 | varchar | 50 |  | √ | ' ' | 记账凭证编号 |
| 9 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 10 | fnowriteoff | 未核销税额 | numeric | 23 | 10 | √ | 0 | 未核销税额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_in_accinvcom_ent1_fk |  | fid |
| 2 | pk_tcvat_in_accinvcom_ent1 |  | fentryid |

---

## 本期已收票，本期已入账-子表 t_tcvat_in_accinvcom_ent

- **表名称：** 本期已收票，本期已入账-子表
- **表名：** t_tcvat_in_accinvcom_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fje | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | ftaxamount | 发票税额 | numeric | 23 | 10 | √ | 0 | 发票税额 |
| 4 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 5 | finvoiceinfo | 发票信息 | varchar | 50 |  | √ | ' ' | 发票信息,枚举: ty_1 :电子普通发票 ty_2 :电子专用发票 ty_3 :增值税普通发票 ty_4 :增值税专用发票 ty_5 :普通纸质卷票 ty_7 :通用机打发票 ty_8 :出租车票 ty_9 :火车票 ty_10 :飞机行程单 ty_11 :其它票 ty_12 :机动车销售发票 ty_13 :二手车销售发票 ty_14 :定额发票 ty_15 :通行费电子发票 ty_16 :公路汽车票 ty_17 :过路桥费发票 ty_19 :完税证明 ty_20 :轮船票 ty_23 :通用机打电子发票 ty_30 :海外发票 st_3 :红冲 st_2 :作废 ex_1 :未用 ex_30 :在用 ex_60 :已用 ex_65 :已入账 ch_1 :已验 ch_2 :未验 ch_3 :未验 ch_4 :不查验 or_0 :未签收 or_1 :已签收 au_0 :未勾选 au_1 :已勾选 au_2 :已认证 au_3 :已认证 au_4 :预勾选 au_5 :勾选中 td_1 :旅客运输抵扣 mo_1 :已改 ty_21 :海关缴款书 ty_24 :火车票退票凭证 ty_25 :财政电子票据 ty_26 :数电普票 ty_27 :数电专票 st_7 :部分红冲 st_8 :全额红冲 st_4 :异常 st_6 :红字发票待确认 |
| 6 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fvouchercode | 记账凭证编号 | varchar | 50 |  | √ | ' ' | 记账凭证编号 |
| 9 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 10 | fauthenticateflag | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 5 :勾选中 |
| 11 | faccperiod | 会计期间号 | varchar | 50 |  | √ | ' ' | 会计期间号,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 12 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 13 | fcurwfdata | 本期核销税额 | numeric | 23 | 10 | √ | 0 | 本期核销税额 |
| 14 | foriginaltime | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 15 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 16 | fsalername | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 17 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 18 | fbalanceid | 科目 | varchar | 36 |  | √ | ' ' | 科目 tdm_account |
| 19 | fwfdate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 22 | fbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_in_accinvcom_ent |  | fentryid |
| 2 | idx_tcvat_in_accinvcom_ent_fk |  | fid |
