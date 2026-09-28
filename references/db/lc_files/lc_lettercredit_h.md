# 历史版本信用证-lc_lettercredit_h

## 历史版本信用证-关联追踪表 t_lc_lettercredit_tc

- **表名称：** 历史版本信用证-关联追踪表
- **表名：** t_lc_lettercredit_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lc_lettercredit_tc |  | fid |
| 2 | idx_lc_lettercredit_tc_tbill |  | ftbillid |
| 3 | idx_lc_lettercredit_tc_tid |  | ftid |

---

## 费用信息分录-子表 t_lc_fee_h

- **表名称：** 费用信息分录-子表
- **表名：** t_lc_fee_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctbankid | 费用账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 3 | foppacctbank | 对方银行账号 | varchar | 100 |  | √ | ' ' | 对方银行账号 |
| 4 | fschemeid | 费用方案 | int8 | 64 |  | √ | 0 | [费用方案 fbd_feescheme](../fbd_files/fbd_feescheme.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famt | 费用金额 | numeric | 19 | 6 | √ | 0 | 费用金额 |
| 7 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: hand :手工新增 linkgen :费用关联生成 batchinput :批量录入 |
| 8 | frate | 费率（%） | numeric | 23 | 10 | √ | 0 | 费率（%） |
| 9 | fissettle | 已结算 | bpchar | 1 |  | √ | '0' | 已结算 |
| 10 | fbillnum | 费用单据编号 | varchar | 30 |  | √ | ' ' | 费用单据编号 |
| 11 | foppunittext | 对方单位 | varchar | 100 |  | √ | ' ' | 对方单位 |
| 12 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | ffeenumber | 费用编码 | varchar | 80 |  | √ | ' ' | 费用编码 |
| 14 | foppunittype | 对方单位类型 | varchar | 80 |  | √ | ' ' | 对方单位类型,枚举: bos_org :内部单位 bd_finorginfo :合作金融机构 bd_supplier :供应商 bd_customer :客户 fbd_other :其他 |
| 15 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 01LETTER :开证处理 02ARRIVAL :到单处理 03PRESENT :交单处理 04FORFAIT :福费廷处理 05CHANGE :改证 06UNSUBMIT :撤证 07ACTIVE :激活 08CLOSE :闭卷 09APPLY :开证申请 |
| 16 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 17 | ftypeid | 费用类型 | int8 | 64 |  | √ | 0 | [费用类型 fbd_feetype](../fbd_files/fbd_feetype.md) |
| 18 | fexcrate | fexcrate | numeric | 23 | 10 | √ | 0 |  |
| 19 | foppbebankid | 对方开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 20 | fbillentryid | 费用单据分录id | int8 | 64 |  | √ | 0 | 费用单据分录id |
| 21 | fbillid | 费用单据id | int8 | 64 |  | √ | 0 | 费用单据id |
| 22 | foppunitid | 对方单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fpaydate | 费用日期 | timestamp | 0 |  |  | null | 费用日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_fee_h |  | fentryid |
| 2 | idx_lc_fee_h |  | fid |

---

## 合同信息分录-多语言表 t_lc_lettercredit_h_entry_l

- **表名称：** 合同信息分录-多语言表
- **表名：** t_lc_lettercredit_h_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcontractremark | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_lettercredit_h_entry_l |  | fpkid |
| 2 | idx_lc_lettercredit_h_entry_l |  | fentryid,flocaleid |

---

## 合同信息分录-子表 t_lc_lettercredit_h_entry

- **表名称：** 合同信息分录-子表
- **表名：** t_lc_lettercredit_h_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcountscaleupper | 上限 | numeric | 19 | 6 | √ | 0 | 上限 |
| 3 | ftaxamount | 含税金额 | numeric | 19 | 6 | √ | 0 | 含税金额 |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fsourceentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 7 | fordernum | 订单号 | varchar | 50 |  | √ | ' ' | 订单号 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 10 | fcontractamount | 合同金额 | numeric | 19 | 6 | √ | 0 | 合同金额 |
| 11 | fcountscalelow | 下限 | numeric | 19 | 6 | √ | 0 | 下限 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | fcontractremark | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 14 | frate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 15 | forderqty | 订货数量 | int8 | 64 |  | √ | 0 | 订货数量 |
| 16 | fcontractnum | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fmodelnum | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 19 | fcontractcurrencyid | 合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercredit_h_entry |  | fid |
| 2 | pk_t_lc_lettercredit_h_entry |  | fentryid |

---

## 背对背信息分录-子表 t_lc_backentry

- **表名称：** 背对背信息分录-子表
- **表名：** t_lc_backentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fmothercredit | 母证信息 | int8 | 64 |  | √ | 0 | [收证信用证 lc_receipt_f7](../lc_files/lc_receipt_f7.md) |
| 4 | fchildcredit | 子证信息 | int8 | 64 |  | √ | 0 | [信用证 lc_lettercredit_f7](../lc_files/lc_lettercredit_f7.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_backentry |  | fentryid |
| 2 | idx_lc_backentry |  | fid |

---

## 关联信息-子表 t_lc_lettercredit_bill

- **表名称：** 关联信息-子表
- **表名：** t_lc_lettercredit_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 单据金额 | numeric | 20 | 10 | √ | 0 | 单据金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: cas_paybill :付款单 |
| 10 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_lettercredit_bill |  | fentryid |
| 2 | pk_t_lc_lettebill_fid |  | fid |

---

## 历史版本信用证-反写记录表 t_lc_lettercredit_wb

- **表名称：** 历史版本信用证-反写记录表
- **表名：** t_lc_lettercredit_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercredit_wb_fk |  | fid |
| 2 | pk_lc_lettercredit_wb |  | fentryid |

---

## 历史版本信用证-多语言表 t_lc_lettercredit_h_l

- **表名称：** 历史版本信用证-多语言表
- **表名：** t_lc_lettercredit_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 4 | fvalidaddress | 到期地点 | varchar | 255 |  | √ | ' ' | 到期地点 |
| 5 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | fbenefitaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 8 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 9 | freturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 10 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 11 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 12 | fapplyreason | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 13 | fapplyaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 14 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 15 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_lettercredit_h_l |  | fpkid |
| 2 | idx_lc_lettercredit_h_l |  | fid,flocaleid |

---

## 历史版本信用证-分表 t_lc_lettercredit_h_e

- **表名称：** 历史版本信用证-分表
- **表名：** t_lc_lettercredit_h_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freimbursingbank | 偿付行 | varchar | 255 |  | √ | ' ' | 偿付行 |
| 3 | fnotarramount | 未到单金额 | numeric | 23 | 10 | √ | 0 | 未到单金额 |
| 4 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnoticebank | 通知行 | varchar | 255 |  | √ | ' ' | 通知行 |
| 6 | fnegotiatingbank | 议付行 | varchar | 255 |  | √ | ' ' | 议付行 |
| 7 | ftotalarramount | 累计到单金额 | numeric | 23 | 10 | √ | 0 | 累计到单金额 |
| 8 | fpromisrate | 保证金比例(%) | numeric | 23 | 2 | √ | 0 | 保证金比例(%) |
| 9 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 10 | fisinit | 初始化 | bpchar | 1 |  | √ | '0' | 初始化 |
| 11 | fapplyid | 申请单id | int8 | 64 |  | √ | 0 | 申请单id |
| 12 | fbenefiterother | 受益人 | varchar | 255 |  | √ | ' ' | 受益人 |
| 13 | ftotalsuretymoney | 保证金累计金额 | numeric | 23 | 10 | √ | 0 | 保证金累计金额 |
| 14 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 15 | fnegotiatingdate | 议付日期 | timestamp | 0 |  |  | null | 议付日期 |
| 16 | fisbatch | 分批 | bpchar | 1 |  | √ | '0' | 分批 |
| 17 | farrivalsum | 到单笔数 | int4 | 32 |  | √ | 0 | 到单笔数 |
| 18 | fdealbilltermstart | 交单期限.开始 | timestamp | 0 |  |  | null | 交单期限.开始 |
| 19 | fbankcountryid | 通知行国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 20 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 21 | fsuretycur | 保证金币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fpushcount | 下推次数 | int8 | 64 |  | √ | 0 | 下推次数 |
| 23 | fsuretymoney | 保证金初始金额 | numeric | 23 | 10 | √ | 0 | 保证金初始金额 |
| 24 | fcreditamount | 实际占用授信金额 | numeric | 23 | 10 | √ | 0 | 实际占用授信金额 |
| 25 | fdealbilltermend | 交单期限.结束 | timestamp | 0 |  |  | null | 交单期限.结束 |
| 26 | fistransfer | 转运 | bpchar | 1 |  | √ | '0' | 转运 |
| 27 | fbackcredittype | 背对背证类型 | varchar | 50 |  | √ | ' ' | 背对背证类型,枚举: mother_credit :母证 child_credit :子证 |
| 28 | fnoticebankid | 通知行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 29 | fconfirmingbank | 保兑行 | varchar | 255 |  | √ | ' ' | 保兑行 |
| 30 | fbenefitcountryid | 受益人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 31 | feassrcid | eas数据id | varchar | 50 |  | √ | ' ' | eas数据id |
| 32 | fisnegotiating | 议付 | bpchar | 1 |  | √ | '0' | 议付 |
| 33 | frepealdate | 撤证日期 | timestamp | 0 |  |  | null | 撤证日期 |
| 34 | fcargocountryid | 货物国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 35 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 36 | fapplycountryid | 开证人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 37 | fbenefitertype | 受益人类型 | varchar | 50 |  | √ | ' ' | 受益人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 38 | fclosecarddate | 闭卷日期 | timestamp | 0 |  |  | null | 闭卷日期 |
| 39 | fisbackcredit | 背对背证 | bpchar | 1 |  | √ | '0' | 背对背证 |
| 40 | fbenefiterid | 受益人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercredit_h_e |  | forgid |
| 2 | pk_t_lc_lettercredit_h_e |  | fid |

---

## 历史版本信用证-分表 t_lc_lettercredit_h_b

- **表名称：** 历史版本信用证-分表
- **表名：** t_lc_lettercredit_h_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillterm | 单据条款 | varchar | 255 |  | √ | ' ' | 单据条款 |
| 3 | ffeepayerid | 手续费承担 | int8 | 64 |  | √ | 0 | [手续费承担 lc_feepayer](../lc_files/lc_feepayer.md) |
| 4 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: lc_onlineresult :在线查询结果单 cas_paybill :付款处理 |
| 5 | fresubmitsrcno | 失败重提源单编号 | varchar | 50 |  | √ | ' ' | 失败重提源单编号 |
| 6 | fbillterm_tag | 单据条款_详情 | text | 0 |  |  | null | 单据条款_详情 |
| 7 | ftradeterms | 贸易术语 | varchar | 50 |  | √ | ' ' | 贸易术语,枚举: EXW :EXW FCA :FCA CPT :CPT CIP :CIP DAP :DAP DPU :DPU DDP :DDP FAS :FAS FOB :FOB CFR :CFR CIF :CIF |
| 8 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 9 | fsubmittime | 提交日期 | timestamp | 0 |  |  | null | 提交日期 |
| 10 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
| 11 | faddterm_tag | 附加条款_详情 | text | 0 |  |  | null | 附加条款_详情 |
| 12 | fisresubmit | 失败重提 | bpchar | 1 |  | √ | '0' | 失败重提 |
| 13 | flfeeacctbankid | 费用账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 14 | fdays | 交单天数 | int4 | 32 |  | √ | 0 | 交单天数 |
| 15 | fbebankstatus | 直联提交状态 | varchar | 50 |  | √ | ' ' | 直联提交状态,枚举: OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 |
| 16 | faddterm | 附加条款 | varchar | 255 |  | √ | ' ' | 附加条款 |
| 17 | ftradechannel | 交易渠道 | varchar | 50 |  | √ | 'offline' | 交易渠道,枚举: offline :线下处理 online :银企直联 |
| 18 | fpaymenttype | 付款类型 | varchar | 50 |  | √ | ' ' | 付款类型,枚举: presentpay :交单后付款 presentforward :交单后远期 preinstforward :提单日期后远期 invoiceforward :发票日期后远期 sailingforward :船期后远期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_lettercredit_h_b |  | fid |
| 2 | idx_lettercredithb_fsrcbillid |  | fsrcbillid |

---

## 历史版本信用证-主表 t_lc_lettercredit_h

- **表名称：** 历史版本信用证-主表
- **表名：** t_lc_lettercredit_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 3 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 4 | fvalidaddress | 到期地点 | varchar | 255 |  | √ | ' ' | 到期地点 |
| 5 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 6 | flettercreditid | 信用证 | int8 | 64 |  | √ | 0 | [信用证 lc_lettercredit_f7](../lc_files/lc_lettercredit_f7.md) |
| 7 | fcreditno | 信用证号 | varchar | 50 |  | √ | ' ' | 信用证号 |
| 8 | fiscancel | 可撤销 | bpchar | 1 |  | √ | '0' | 可撤销 |
| 9 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreditapplyno | 开证申请 | varchar | 50 |  | √ | ' ' | 开证申请 |
| 12 | fmodifydate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fapplyreason | fapplyreason | varchar | 255 |  | √ | ' ' |  |
| 14 | flowstr | 金额下限 | varchar | 50 |  | √ | ' ' | 金额下限 |
| 15 | fisnationalcard | 国际证 | bpchar | 1 |  | √ | '0' | 国际证 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | famountscaleupper | 溢短装金额浮动比例上限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例上限（%） |
| 18 | fversion | 信用证版本号 | varchar | 50 |  | √ | ' ' | 信用证版本号 |
| 19 | fismakeover | 可转让 | bpchar | 1 |  | √ | '0' | 可转让 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | freturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 24 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 25 | fapplyaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 26 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 27 | fbankid | 开证行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 28 | famountscalelow | 溢短装金额浮动比例下限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例下限（%） |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 33 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |
| 34 | fisclosed | 闭过卷 | bpchar | 1 |  | √ | '0' | 闭过卷 |
| 35 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 36 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fcreditstatus | 信用证状态 | varchar | 50 |  | √ | ' ' | 信用证状态,枚举: done_register :已登记 done_close :已闭卷 done_repeal :已撤证 change_ing :改证中 repeal_ing :撤证中 close_ing :闭卷中 |
| 38 | fapplydate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 39 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 40 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 41 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :信用/无担保 |
| 42 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fdatasources | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand_increase :手工新增 bank_increase :银企生成 |
| 44 | fbenefitaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 45 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 46 | fbizdate | 开证日期 | timestamp | 0 |  |  | null | 开证日期 |
| 47 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 48 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 49 | fupperstr | 金额上限 | varchar | 50 |  | √ | ' ' | 金额上限 |
| 50 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_lettercredit_h |  | fid |
| 2 | idx_lc_lettercredit_h |  | fbillno |

---

## 关联子实体-子表 t_lc_lettercredit_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lc_lettercredit_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lc_lettercredit_lk |  | fpkid |
| 2 | idx_lc_lettercredit_lk_fk |  | fid |
