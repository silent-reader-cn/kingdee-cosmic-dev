# 进项账票核销记录查询-tcvat_in_wfrecord

## 进项账票核销记录查询-主表 t_tcvat_in_wfrecord

- **表名称：** 进项账票核销记录查询-主表
- **表名：** t_tcvat_in_wfrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 核销序号 | varchar | 50 |  | √ | ' ' | 核销序号 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 8 | fheadwfinfo | 核销详情 | varchar | 255 |  | √ | ' ' | 核销详情 |
| 9 | fwfnumber | 核销编码 | varchar | 30 |  | √ | ' ' | 核销编码 |
| 10 | fheadwfinfo_tag | 核销详情_详情 | text | 0 |  |  | null | 核销详情_详情 |
| 11 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_in_wfrecord |  | ftaxorg,fwriteofftypeid |
| 2 | pk_tcvat_in_wfrecord |  | fid |

---

## 单据体-子表 t_tcvat_in_wfrecord_entry

- **表名称：** 单据体-子表
- **表名：** t_tcvat_in_wfrecord_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbackwfop | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 3 | fbillqty | 数量-主 | numeric | 23 | 10 | √ | 0 | 数量-主 |
| 4 | finvoiceinfo | 发票信息 | varchar | 50 |  | √ | ' ' | 发票信息,枚举: ty_1 :电子普通发票 ty_2 :电子专用发票 ty_3 :增值税普通发票 ty_4 :增值税专用发票 ty_5 :普通纸质卷票 ty_7 :通用机打发票 ty_8 :出租车票 ty_9 :火车票 ty_10 :飞机行程单 ty_11 :其它票 ty_12 :机动车销售发票 ty_13 :二手车销售发票 ty_14 :定额发票 ty_15 :通行费电子发票 ty_16 :公路汽车票 ty_17 :过路桥费发票 ty_19 :完税证明 ty_20 :轮船票 ty_23 :通用机打电子发票 ty_30 :海外发票 st_3 :红冲 st_2 :作废 ex_1 :未用 ex_30 :在用 ex_60 :已用 ex_65 :已入账 ch_1 :已验 ch_2 :未验 ch_3 :未验 ch_4 :不查验 or_0 :未签收 or_1 :已签收 au_0 :未勾选 au_1 :已勾选 au_2 :已认证 au_3 :已认证 au_4 :预勾选 au_5 :勾选中 td_1 :旅客运输抵扣 mo_1 :已改 ty_21 :海关缴款书 ty_24 :火车票退票凭证 ty_25 :财政电子票据 ty_26 :数电普票 ty_27 :数电专票 st_7 :部分红冲 st_8 :全额红冲 st_4 :异常 st_6 :红字发票待确认 |
| 5 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 6 | fassbillid | 单据ID-辅 | int8 | 64 |  | √ | 0 | 单据ID-辅 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fvouchercode | 记账凭证编号 | varchar | 50 |  | √ | ' ' | 记账凭证编号 |
| 9 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 10 | fauthenticateflag | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 5 :勾选中 |
| 11 | fbchxse | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 12 | fassbillqty | 数量-辅 | numeric | 23 | 10 | √ | 0 | 数量-辅 |
| 13 | fassbillno | 单据编号-辅 | varchar | 50 |  | √ | ' ' | 单据编号-辅 |
| 14 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 15 | fassbchxse | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 16 | fassbilltype | 单据类型-辅 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 17 | fmainwfinfo_tag | 核销详情-主_详情 | text | 0 |  |  | null | 核销详情-主_详情 |
| 18 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 19 | fbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |
| 20 | fqty | 核销数量-主 | numeric | 23 | 10 | √ | 0 | 核销数量-主 |
| 21 | fassbillentryid | 单据分录ID-辅 | int8 | 64 |  | √ | 0 | 单据分录ID-辅 |
| 22 | fje | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 23 | ftaxamount | 发票税额 | numeric | 23 | 10 | √ | 0 | 发票税额 |
| 24 | fassunit | 计量单位-辅 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 26 | fmainwfinfo | 核销详情-主 | varchar | 255 |  | √ | ' ' | 核销详情-主 |
| 27 | fasswfinfo_tag | 核销详情-辅_详情 | text | 0 |  |  | null | 核销详情-辅_详情 |
| 28 | faccperiod | 会计期间号 | varchar | 50 |  | √ | ' ' | 会计期间号,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 29 | fbillno1 | fbillno1 | varchar | 50 |  | √ | ' ' |  |
| 30 | fbillentryid | 单据分录ID-主 | int8 | 64 |  | √ | 0 | 单据分录ID-主 |
| 31 | foriginaltime | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 32 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 33 | fassqty | 核销数量-辅 | numeric | 23 | 10 | √ | 0 | 核销数量-辅 |
| 34 | fsalername | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 35 | fbillid | 单据ID-主 | int8 | 64 |  | √ | 0 | 单据ID-主 |
| 36 | fbalanceid | 科目 | varchar | 36 |  | √ | ' ' | 科目 tdm_account |
| 37 | fasswfinfo | 核销详情-辅 | varchar | 255 |  | √ | ' ' | 核销详情-辅 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fbilltype | 单据类型-主 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 40 | funit | 计量单位-主 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 41 | fsummary | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_in_wfrecord_entry |  | fentryid |
| 2 | idx_tcvat_in_wfrecord_entry_fk |  | fid |
