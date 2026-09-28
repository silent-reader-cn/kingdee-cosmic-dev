# 预缴项目销项发票-sim_vatinvoice_output_sig

## 明细单据体-子表 t_sim_vatinvoice_item

- **表名称：** 明细单据体-子表
- **表名：** t_sim_vatinvoice_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsimplegoodsname | 分类编码简称 | varchar | 50 |  | √ | ' ' | 分类编码简称 |
| 3 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 4 | fdiscountrate | 折扣率 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣率 |
| 5 | frowtype | 发票行性质 | varchar | 30 |  | √ | ' ' | 发票行性质,枚举: 0 :明细行 1 :折扣行 2 :被折扣行 |
| 6 | fdiscountamount | 折扣金额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fspmc | fspmc | int8 | 64 |  | √ | 0 |  |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 10 | fitemremainredtax | 蓝票剩余可红冲税额 | numeric | 23 | 10 | √ | 0 | 蓝票剩余可红冲税额 |
| 11 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 12 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fwriteoffqty | 已核销数量 | numeric | 23 | 10 | √ | 0 | 已核销数量 |
| 14 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 15 | fspecification | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 16 | fgoodsname | 商品名称 | varchar | 128 |  | √ | ' ' | 商品名称 |
| 17 | fbillsourceid | 单据来源id | varchar | 50 |  | √ | ' ' | 单据来源id |
| 18 | fitemremainredamount | 蓝票剩余可红冲金额 | numeric | 23 | 10 | √ | 0 | 蓝票剩余可红冲金额 |
| 19 | foriginalinvoiceitemid | 对应蓝票明细id | int8 | 64 |  | √ | 0 | 对应蓝票明细id |
| 20 | fzzstsgl | 增值税特殊管理 | varchar | 2000 |  | √ | ' ' | 增值税特殊管理 |
| 21 | fuserinputgoodsname | fuserinputgoodsname | varchar | 128 |  | √ | ' ' |  |
| 22 | fspbm | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 23 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 含税金额 |
| 24 | ftaxflag | 含税标识 | varchar | 8 |  | √ | ' ' | 含税标识 |
| 25 | fzerotaxmark | 零税率标识 | varchar | 8 |  | √ | ' ' | 零税率标识 |
| 26 | ftaxpremark | 税收优惠政策标识 | varchar | 16 |  | √ | ' ' | 税收优惠政策标识 |
| 27 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 28 | fgoodscode | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 29 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 30 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 31 | fzxbm | 纳税人自行编码 | varchar | 128 |  | √ | ' ' | 纳税人自行编码 |
| 32 | fvehplate | 车牌号 | varchar | 50 |  | √ | ' ' | 车牌号 |
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

## 预缴项目销项发票-主表 t_sim_vatinvoice

- **表名称：** 预缴项目销项发票-主表
- **表名：** t_sim_vatinvoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyeraddr | 购方地址电话 | varchar | 150 |  | √ | ' ' | 购方地址电话 |
| 3 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftaxedtype | 征税方式 | varchar | 8 |  | √ | ' ' | 征税方式,枚举: 0 :普通征税 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | finvoicecopy | 联次发票 | varchar | 30 |  | √ | ' ' | 联次发票,枚举: -1 :无 二联 :二联 三联 :三联 五联 :五联 |
| 9 | fsalerbankacc | 销方银行账号(废弃) | varchar | 50 |  | √ | ' ' | 销方银行账号(废弃) |
| 10 | fbaseinvoicetype | 基础发票种类 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 11 | fsaleraddr | 销方地址电话 | varchar | 150 |  | √ | ' ' | 销方地址电话 |
| 12 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 13 | fissuewritebackreason | 开票回写失败原因 | varchar | 100 |  | √ | ' ' | 开票回写失败原因 |
| 14 | fspecialtype | 特殊票种 | varchar | 30 |  | √ | ' ' | 特殊票种,枚举: 00 :非特殊票种 02 :收购 06 :抵扣通行费 07 :不抵扣通行费 08 :成品油 11 :卷烟 18 :机动车 |
| 15 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 16 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 17 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 18 | fsalertaxno | 销方纳税人识别号 | varchar | 50 |  | √ | ' ' | 销方纳税人识别号 |
| 19 | fmaintaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | foriginalinvoiceno | 原发票号码 | varchar | 50 |  | √ | ' ' | 原发票号码 |
| 21 | fdeduction | 扣除额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除额 |
| 22 | fbuyerphone | 购方手机号 | varchar | 50 |  | √ | ' ' | 购方手机号 |
| 23 | forderno | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 24 | fsalertelno | 销方电话(废弃) | varchar | 50 |  | √ | ' ' | 销方电话(废弃) |
| 25 | finvoicetype | 发票类型 | varchar | 8 |  | √ | ' ' | 发票类型,枚举: 026 :电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :纸质专用发票 025 :增值税普通发票（卷票） 10xdp :全电发票（普通发票） 08xdp :全电发票（增值税专用发票） |
| 26 | foriginalinvoicecode | 原发票代码 | varchar | 50 |  | √ | ' ' | 原发票代码 |
| 27 | fbuyerbank | 购方开户行及账号 | varchar | 150 |  | √ | ' ' | 购方开户行及账号 |
| 28 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 29 | fbuyerbankacc | 购方银行账号(废弃) | varchar | 50 |  | √ | ' ' | 购方银行账号(废弃) |
| 30 | fissuetype | 开票类型 | varchar | 8 |  | √ | ' ' | 开票类型,枚举: 0 :蓝票 1 :红票 |
| 31 | fbuyeremail | 购方邮箱 | varchar | 100 |  | √ | ' ' | 购方邮箱 |
| 32 | fbuyertype | fbuyertype | varchar | 8 |  | √ | ' ' |  |
| 33 | fcheckcode | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 34 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 35 | finvoicestatus | 发票状态 | varchar | 8 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 7 :作废中 |
| 36 | fhsbz | 是否含税 | varchar | 8 |  | √ | ' ' | 是否含税,枚举: 0 :不含税 1 :含税 |
| 37 | fabolishwritebackstatus | 作废回写状态 | varchar | 30 |  | √ | ' ' | 作废回写状态,枚举: 0 :未回写 1 :回写成功 2 :不回写 -1 :回写失败 |
| 38 | fbuyertelno | 购方电话(用做显示设备名称) | varchar | 50 |  | √ | ' ' | 购方电话(用做显示设备名称) |
| 39 | fissuewritebackstatus | 开票回写状态 | varchar | 30 |  | √ | ' ' | 开票回写状态,枚举: 0 :未回写 1 :回写成功 -1 :回写失败 |
| 40 | ftotaltax | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 41 | fissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 42 | fsourcetype | fsourcetype | varchar | 30 |  | √ | ' ' |  |
| 43 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 44 | fbuyertaxno | 购方税号 | varchar | 50 |  | √ | ' ' | 购方税号 |
| 45 | fsalerbank | 销方开户行及账号 | varchar | 150 |  | √ | ' ' | 销方开户行及账号 |
| 46 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fsplitorder | 拆分顺序 | int4 | 32 |  | √ | 1 | 拆分顺序 |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fapplicant | 红字信息表申请方 | varchar | 50 |  | √ | ' ' | 红字信息表申请方,枚举: 2 :销方申请 1 :购方申请-未抵扣 0 :购方申请-已抵扣 |
| 51 | foriginalinvoicetype | 原发票类型 | varchar | 30 |  | √ | ' ' | 原发票类型,枚举: 026 :增值税电子普通发票 004 :增值税专用发票 |
| 52 | foriginaldeduction | 原发票扣除额 | numeric | 23 | 10 | √ | 0 | 原发票扣除额 |
| 53 | foriginalissuetime | 原开票日期 | timestamp | 0 |  |  | null | 原开票日期 |
| 54 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 55 | fapplytaxno | 红字信息表申请方税号 | varchar | 50 |  | √ | ' ' | 红字信息表申请方税号 |
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

---

## 预缴项目销项发票-分表 t_sim_vatinvoice_f

- **表名称：** 预缴项目销项发票-分表
- **表名：** t_sim_vatinvoice_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadvancepaymentstatus | 预缴状态 | varchar | 50 |  | √ | ' ' | 预缴状态,枚举: 10 :不预缴 20 :未预缴 30 :待预缴 40 :已预缴 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_vatinvoice_f |  | fid |

---

## 预缴项目销项发票-分表 t_sim_vatinvoice_e

- **表名称：** 预缴项目销项发票-分表
- **表名：** t_sim_vatinvoice_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fssyf | fssyf | varchar | 10 |  | √ | ' ' |  |
| 3 | finvaliddate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 4 | ftaxorg | ftaxorg | int8 | 64 |  | √ | 0 |  |
| 5 | fmsgresendnum | 短信重发计数 | int4 | 32 |  | √ | 0 | 短信重发计数 |
| 6 | fqmz | fqmz | varchar | 450 |  | √ | ' ' |  |
| 7 | fgovorderno | 全电发票开具税局返回流水号 | varchar | 50 |  | √ | ' ' | 全电发票开具税局返回流水号 |
| 8 | fykfsje | fykfsje | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fresult | 开票结果 | varchar | 300 |  | √ | ' ' | 开票结果 |
| 10 | ffileurl | 板式文件url | varchar | 330 |  | √ | ' ' | 板式文件url |
| 11 | fdownloadflag | 下载标识 | varchar | 4 |  | √ | ' ' | 下载标识,枚举: 0 :未下载 1 :板式文件生成中 2 :已下载 |
| 12 | fissuebillstatus | 开票审批状态 | varchar | 50 |  | √ | ' ' | 开票审批状态,枚举: A :暂存 B :已提交 C :已审核 D :无需审批 |
| 13 | fspecialredflag | 特殊红冲标志 | varchar | 50 |  | √ | ' ' | 特殊红冲标志,枚举: 0 :否 1 :是 |
| 14 | fbatchbelong | 所属批次 | varchar | 50 |  | √ | ' ' | 所属批次 |
| 15 | fcardbagstatus | 卡包状态 | varchar | 30 |  | √ | ' ' | 卡包状态,枚举: -1 :未同步 1 :已同步 |
| 16 | fpushtype | 推送方式 | varchar | 50 |  | √ | ' ' | 推送方式,枚举: 0 :手机 1 :邮箱 2 :邮箱&手机 |
| 17 | fbaseinvoicetype | fbaseinvoicetype | int8 | 64 |  | √ | 0 |  |
| 18 | fuploadmark | 上传标识 | varchar | 8 |  | √ | ' ' | 上传标识,枚举: 0 :失败 1 :成功 |
| 19 | fpdffileurl | 全电发票pdf下载地址 | varchar | 200 |  | √ | ' ' | 全电发票pdf下载地址 |
| 20 | foccupystatus | 占用状态 | varchar | 10 |  | √ | ' ' | 占用状态,枚举: 0 :未占用 1 :已占用 |
| 21 | fofdstatus | OFD状态 | varchar | 8 |  | √ | ' ' | OFD状态,枚举: 0 :失败 1 :成功 3 :无需生成 |
| 22 | fbillstatus | 作废审批状态 | varchar | 50 |  | √ | ' ' | 作废审批状态,枚举: A :暂存 B :已提交 C :已审核 D :无需审批 |
| 23 | fredreason | 冲红原因 | varchar | 200 |  | √ | ' ' | 冲红原因 |
| 24 | fuploadismcstatus | 上传税控系统云状态 | varchar | 2 |  | √ | ' ' | 上传税控系统云状态,枚举: 0 :未同步 1 :已同步 2 :无需同步 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fissuesource | 设备类型 | varchar | 60 |  | √ | ' ' | 设备类型,枚举: 0 :税务ukey 1 :税控盘 2 :金税盘 3 :虚拟ukey 4 :金税盘-托管 5 :区块链 6 :税控盘-托管 7 :税务ukey-托管 8 :百望服务器 9 :联云托管-金税盘 10 :联云托管-Ukey 11 :联云托管-税控盘 12 :全电平台 |
| 27 | fabolishreason | 作废原因 | varchar | 50 |  | √ | ' ' | 作废原因 |
| 28 | fmergelable | 合并标志 | varchar | 50 |  | √ | ' ' | 合并标志 |
| 29 | freissuestatus | 重开状态 | varchar | 4 |  | √ | ' ' | 重开状态,枚举: 0 :未重开 1 :已重开 2 :重开中 |
| 30 | abolishtype | abolishtype | varchar | 5 |  | √ | ' ' |  |
| 31 | fcanredtaxamount | 可红冲税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可红冲税额 |
| 32 | fissuestatus | 开票状态 | varchar | 30 |  | √ | ' ' | 开票状态,枚举: 2 :未开票 4 :已提交 1 :开票中 0 :已开票 3 :开票失败 |
| 33 | fcontraststatus | 对账状态 | varchar | 8 |  | √ | ' ' | 对账状态,枚举: 0 :失败 1 :成功 |
| 34 | fproject | 项目 | int8 | 64 |  | √ | 0 | [预缴项目信息 tcvat_prepay_project_info](../tcvat_files/tcvat_prepay_project_info.md) |
| 35 | fsnapshoturl | 快照url | varchar | 330 |  | √ | ' ' | 快照url |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fterminalno | 终端编号 | varchar | 50 |  | √ | ' ' | 终端编号 |
| 38 | fbuyertype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :单张 1 :批量导入 2 :数据同步 3 :接口同步 4 :单据拆合 5 :作废重开 6 :空白作废 7 :扫码开票 8 :excel导入 9 :进项下载 10 :公有云同步 11 :手工新增红字信息表编号 |
| 39 | fabolishtype | 作废类型 | varchar | 5 |  | √ | ' ' | 作废类型,枚举: 0 :发票作废 1 :空白作废 |
| 40 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 41 | fremainredamount | 剩余可红冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可红冲金额 |
| 42 | fauditsuggestion | 审核意见 | varchar | 200 |  | √ | ' ' | 审核意见 |
| 43 | fxmlfileurl | xml下载地址 | varchar | 200 |  | √ | ' ' | xml下载地址 |
| 44 | fprintflag | 打印标识 | varchar | 4 |  | √ | ' ' | 打印标识,枚举: 0 :未打印 1 :已打印 2 :打印失败 |
| 45 | fskm | 税控码 | varchar | 500 |  | √ | ' ' | 税控码 |
| 46 | finvalider | 作废人 | varchar | 50 |  | √ | ' ' | 作废人 |
| 47 | fxxbbh | fxxbbh | varchar | 20 |  | √ | ' ' |  |
| 48 | foperator | 经办人 | int8 | 64 |  | √ | 0 | [经办人信息 bdm_operator_info](../bdm_files/bdm_operator_info.md) |
| 49 | finfocode | 红字信息表编号/红字确认单编号 | varchar | 50 |  | √ | ' ' | 红字信息表编号/红字确认单编号 |
| 50 | fthirdserialno | 第三方流水号 | varchar | 50 |  | √ | ' ' | 第三方流水号 |
| 51 | fdatahash | 数据hash校验 | varchar | 50 |  | √ | ' ' | 数据hash校验 |
| 52 | fbuyerproperty | 购方企业类型 | varchar | 30 |  | √ | ' ' | 购方企业类型,枚举: 0 :企业 1 :个人 |
| 53 | fpushstatus | 推送状态 | varchar | 50 |  | √ | ' ' | 推送状态,枚举: 0 :成功 1 :短信推送失败 2 :邮件推送失败 3 :失败 4 :不推送 5 :推送中 |
| 54 | freorderno | 重开流水号 | varchar | 50 |  | √ | ' ' | 重开流水号 |
| 55 | fwxid | 微信ID | varchar | 50 |  | √ | ' ' | 微信ID |
| 56 | fjqbh | 机器编号 | varchar | 20 |  | √ | ' ' | 机器编号 |
| 57 | finventorymark | 清单标志 | varchar | 50 |  | √ | ' ' | 清单标志,枚举: 0 :无清单 1 :有清单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_vatinvoice_e |  | fid |
| 2 | idx_sim_vatinvoice_e_fk |  | fcontraststatus |
