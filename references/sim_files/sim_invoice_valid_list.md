# 发票作废-sim_invoice_valid_list

## 发票作废-分表 t_sim_vatinvoice_e

- **表名称：** 发票作废-分表
- **表名：** t_sim_vatinvoice_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fssyf | fssyf | varchar | 10 |  | √ | ' ' |  |
| 3 | finvaliddate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 4 | ftaxorg | ftaxorg | int8 | 64 |  | √ | 0 |  |
| 5 | fmsgresendnum | fmsgresendnum | int4 | 32 |  | √ | 0 |  |
| 6 | fqmz | fqmz | varchar | 450 |  | √ | ' ' |  |
| 7 | fgovorderno | fgovorderno | varchar | 50 |  | √ | ' ' |  |
| 8 | fykfsje | fykfsje | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fresult | fresult | varchar | 300 |  | √ | ' ' |  |
| 10 | ffileurl | ffileurl | varchar | 330 |  | √ | ' ' |  |
| 11 | fdownloadflag | fdownloadflag | varchar | 4 |  | √ | ' ' |  |
| 12 | fissuebillstatus | fissuebillstatus | varchar | 50 |  | √ | ' ' |  |
| 13 | fspecialredflag | fspecialredflag | varchar | 50 |  | √ | ' ' |  |
| 14 | fbatchbelong | fbatchbelong | varchar | 50 |  | √ | ' ' |  |
| 15 | fcardbagstatus | fcardbagstatus | varchar | 30 |  | √ | ' ' |  |
| 16 | fpushtype | fpushtype | varchar | 50 |  | √ | ' ' |  |
| 17 | fbaseinvoicetype | fbaseinvoicetype | int8 | 64 |  | √ | 0 |  |
| 18 | fuploadmark | fuploadmark | varchar | 8 |  | √ | ' ' |  |
| 19 | fpdffileurl | fpdffileurl | varchar | 200 |  | √ | ' ' |  |
| 20 | foccupystatus | 占用状态 | varchar | 10 |  | √ | ' ' | 占用状态,枚举: 0 :未占用 1 :已占用 |
| 21 | fofdstatus | fofdstatus | varchar | 8 |  | √ | ' ' |  |
| 22 | fbillstatus | 作废审批状态 | varchar | 50 |  | √ | ' ' | 作废审批状态,枚举: A :暂存 B :已提交 C :已审核 D :无需审批 |
| 23 | fredreason | fredreason | varchar | 200 |  | √ | ' ' |  |
| 24 | fuploadismcstatus | fuploadismcstatus | varchar | 2 |  | √ | ' ' |  |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | fissuesource | 开票来源 | varchar | 60 |  | √ | ' ' | 开票来源,枚举: 0 :税务ukey 1 :税控盘 2 :金税盘 3 :税控虚拟ukey 4 :金税盘-托管 5 :区块链 6 :税控盘-托管 7 :税务ukey-托管 8 :百望服务器 9 :联云托管 |
| 27 | fabolishreason | 作废原因 | varchar | 50 |  | √ | ' ' | 作废原因 |
| 28 | fmergelable | fmergelable | varchar | 50 |  | √ | ' ' |  |
| 29 | freissuestatus | freissuestatus | varchar | 4 |  | √ | ' ' |  |
| 30 | abolishtype | abolishtype | varchar | 5 |  | √ | ' ' |  |
| 31 | fcanredtaxamount | fcanredtaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fissuestatus | fissuestatus | varchar | 30 |  | √ | ' ' |  |
| 33 | fcontraststatus | fcontraststatus | varchar | 8 |  | √ | ' ' |  |
| 34 | fproject | fproject | int8 | 64 |  | √ | 0 |  |
| 35 | fsnapshoturl | fsnapshoturl | varchar | 330 |  | √ | ' ' |  |
| 36 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 37 | fterminalno | fterminalno | varchar | 50 |  | √ | ' ' |  |
| 38 | fbuyertype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :单张开票 1 :批量导入 3 :接口同步 4 :单据拆合 5 :作废重开 7 :扫码开票 9 :进项下载 10 :公有云同步 11 :手工新增红字信息表编号 |
| 39 | fabolishtype | 作废类型 | varchar | 5 |  | √ | ' ' | 作废类型,枚举: 0 :发票作废 1 :空白作废 |
| 40 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 41 | fremainredamount | fremainredamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fauditsuggestion | fauditsuggestion | varchar | 200 |  | √ | ' ' |  |
| 43 | fxmlfileurl | fxmlfileurl | varchar | 200 |  | √ | ' ' |  |
| 44 | fprintflag | fprintflag | varchar | 4 |  | √ | ' ' |  |
| 45 | fskm | 多行文本1 | varchar | 500 |  | √ | ' ' | 多行文本1 |
| 46 | finvalider | 作废人 | varchar | 50 |  | √ | ' ' | 作废人 |
| 47 | fxxbbh | fxxbbh | varchar | 20 |  | √ | ' ' |  |
| 48 | foperator | foperator | int8 | 64 |  | √ | 0 |  |
| 49 | finfocode | finfocode | varchar | 50 |  | √ | ' ' |  |
| 50 | fthirdserialno | fthirdserialno | varchar | 50 |  | √ | ' ' |  |
| 51 | fdatahash | fdatahash | varchar | 50 |  | √ | ' ' |  |
| 52 | fbuyerproperty | fbuyerproperty | varchar | 30 |  | √ | ' ' |  |
| 53 | fpushstatus | fpushstatus | varchar | 50 |  | √ | ' ' |  |
| 54 | freorderno | freorderno | varchar | 50 |  | √ | ' ' |  |
| 55 | fwxid | fwxid | varchar | 50 |  | √ | ' ' |  |
| 56 | fjqbh | 设备编号 | varchar | 20 |  | √ | ' ' | 设备编号 |
| 57 | finventorymark | finventorymark | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_vatinvoice_e |  | fid |
| 2 | idx_sim_vatinvoice_e_fk |  | fcontraststatus |

---

## 单据体-子表 t_sim_vatinvoice_item

- **表名称：** 单据体-子表
- **表名：** t_sim_vatinvoice_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsimplegoodsname | fsimplegoodsname | varchar | 50 |  | √ | ' ' |  |
| 3 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 4 | fdiscountrate | fdiscountrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | frowtype | frowtype | varchar | 30 |  | √ | ' ' |  |
| 6 | fdiscountamount | fdiscountamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fspmc | fspmc | int8 | 64 |  | √ | 0 |  |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 10 | fitemremainredtax | fitemremainredtax | numeric | 23 | 10 | √ | 0 |  |
| 11 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 12 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 13 | fwriteoffqty | fwriteoffqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 15 | fspecification | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 16 | fgoodsname | 商品名称 | varchar | 128 |  | √ | ' ' | 商品名称 |
| 17 | fbillsourceid | fbillsourceid | varchar | 50 |  | √ | ' ' |  |
| 18 | fitemremainredamount | fitemremainredamount | numeric | 23 | 10 | √ | 0 |  |
| 19 | foriginalinvoiceitemid | foriginalinvoiceitemid | int8 | 64 |  | √ | 0 |  |
| 20 | fzzstsgl | fzzstsgl | varchar | 2000 |  | √ | ' ' |  |
| 21 | fuserinputgoodsname | fuserinputgoodsname | varchar | 128 |  | √ | ' ' |  |
| 22 | fspbm | fspbm | varchar | 50 |  | √ | ' ' |  |
| 23 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | ftaxflag | ftaxflag | varchar | 8 |  | √ | ' ' |  |
| 25 | fzerotaxmark | fzerotaxmark | varchar | 8 |  | √ | ' ' |  |
| 26 | ftaxpremark | ftaxpremark | varchar | 16 |  | √ | ' ' |  |
| 27 | ftaxunitprice | ftaxunitprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | fgoodscode | fgoodscode | varchar | 50 |  | √ | ' ' |  |
| 29 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 30 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 31 | fzxbm | fzxbm | varchar | 128 |  | √ | ' ' |  |
| 32 | fvehplate | fvehplate | varchar | 50 |  | √ | ' ' |  |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_vatinvoice_item |  | fentryid |
| 2 | idx_vatinvo_item_fgoodscode |  | fgoodscode |
| 3 | idx_sim_vatinvoice_item_fk |  | fid |

---

## 发票作废-主表 t_sim_vatinvoice

- **表名称：** 发票作废-主表
- **表名：** t_sim_vatinvoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyeraddr | 购方地址电话 | varchar | 150 |  | √ | ' ' | 购方地址电话 |
| 3 | fdrawer | 开票人： | varchar | 50 |  | √ | ' ' | 开票人： |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftaxedtype | 征税方式 | varchar | 8 |  | √ | ' ' | 征税方式,枚举: 0 :普通征税 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | finvoicecopy | 联次发票 | varchar | 30 |  | √ | ' ' | 联次发票,枚举: -1 :无 二联 :二联 三联 :三联 五联 :五联 |
| 9 | fsalerbankacc | fsalerbankacc | varchar | 50 |  | √ | ' ' |  |
| 10 | fbaseinvoicetype | fbaseinvoicetype | int8 | 64 |  | √ | 0 |  |
| 11 | fsaleraddr | 销方地址电话 | varchar | 150 |  | √ | ' ' | 销方地址电话 |
| 12 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 13 | fissuewritebackreason | fissuewritebackreason | varchar | 100 |  | √ | ' ' |  |
| 14 | fspecialtype | fspecialtype | varchar | 30 |  | √ | ' ' |  |
| 15 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 16 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 17 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 18 | fsalertaxno | 销方纳税人识别号 | varchar | 50 |  | √ | ' ' | 销方纳税人识别号 |
| 19 | fmaintaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | foriginalinvoiceno | foriginalinvoiceno | varchar | 50 |  | √ | ' ' |  |
| 21 | fdeduction | 扣除额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除额 |
| 22 | fbuyerphone | fbuyerphone | varchar | 50 |  | √ | ' ' |  |
| 23 | forderno | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 24 | fsalertelno | fsalertelno | varchar | 50 |  | √ | ' ' |  |
| 25 | finvoicetype | 发票种类 | varchar | 8 |  | √ | ' ' | 发票种类,枚举: 007 :纸质普通发票 004 :纸质专用发票 025 :增值税普通发票（卷票） |
| 26 | foriginalinvoicecode | foriginalinvoicecode | varchar | 50 |  | √ | ' ' |  |
| 27 | fbuyerbank | 购方开户行及账号 | varchar | 150 |  | √ | ' ' | 购方开户行及账号 |
| 28 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 29 | fbuyerbankacc | fbuyerbankacc | varchar | 50 |  | √ | ' ' |  |
| 30 | fissuetype | 开票类型 | varchar | 8 |  | √ | ' ' | 开票类型,枚举: 0 :蓝票 1 :红票 |
| 31 | fbuyeremail | fbuyeremail | varchar | 100 |  | √ | ' ' |  |
| 32 | fbuyertype | fbuyertype | varchar | 8 |  | √ | ' ' |  |
| 33 | fcheckcode | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 34 | fpayee | 收款人： | varchar | 50 |  | √ | ' ' | 收款人： |
| 35 | finvoicestatus | 发票状态 | varchar | 8 |  | √ | ' ' | 发票状态,枚举: 0 :正常 6 :作废 7 :作废中 |
| 36 | fhsbz | 是否含税 | varchar | 8 |  | √ | ' ' | 是否含税,枚举: 0 :不含税 1 :含税 |
| 37 | fabolishwritebackstatus | fabolishwritebackstatus | varchar | 30 |  | √ | ' ' |  |
| 38 | fbuyertelno | fbuyertelno | varchar | 50 |  | √ | ' ' |  |
| 39 | fissuewritebackstatus | fissuewritebackstatus | varchar | 30 |  | √ | ' ' |  |
| 40 | ftotaltax | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 41 | fissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 42 | fsourcetype | fsourcetype | varchar | 30 |  | √ | ' ' |  |
| 43 | freviewer | 复核人： | varchar | 50 |  | √ | ' ' | 复核人： |
| 44 | fbuyertaxno | 购方纳税人识别号 | varchar | 50 |  | √ | ' ' | 购方纳税人识别号 |
| 45 | fsalerbank | 销方开户行及账号 | varchar | 150 |  | √ | ' ' | 销方开户行及账号 |
| 46 | fremark | 多行文本 | varchar | 512 |  | √ | ' ' | 多行文本 |
| 47 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 48 | fsplitorder | fsplitorder | int4 | 32 |  | √ | 1 |  |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fapplicant | fapplicant | varchar | 50 |  | √ | ' ' |  |
| 51 | foriginalinvoicetype | foriginalinvoicetype | varchar | 30 |  | √ | ' ' |  |
| 52 | foriginaldeduction | foriginaldeduction | numeric | 23 | 10 | √ | 0 |  |
| 53 | foriginalissuetime | foriginalissuetime | timestamp | 0 |  |  | null |  |
| 54 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 55 | fapplytaxno | fapplytaxno | varchar | 50 |  | √ | ' ' |  |
| 56 | fsystemsource | 数据来源系统 | varchar | 50 |  | √ | ' ' | 数据来源系统 |
| 57 | finventorymark | finventorymark | varchar | 8 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_createtime_status |  | fcreatetime,finvoicestatus |
| 2 | idx_sim_vatinvoice2 |  | fmaintaxorg,fissuetime,fbaseinvoicetype,finvoicestatus |
| 3 | idx_org |  | forgid |
| 4 | idx_billno_org |  | fbillno,forgid |
| 5 | idx_sim_vatinvoice |  | finvoicecode,finvoiceno |
| 6 | idx_vatinvoice_fissuetime |  | fissuetime |
| 7 | pk_sim_vatinvoice |  | fid |
| 8 | idx_vatinvoice_orderno |  | forderno |
