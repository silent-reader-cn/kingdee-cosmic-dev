# 业务申请-lc_bizapply

## 担保信息分录-子表 t_gm_guaranteeuse_info

- **表名称：** 担保信息分录-子表
- **表名：** t_gm_guaranteeuse_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgcreditortext | fgcreditortext | varchar | 80 |  | √ | ' ' |  |
| 3 | fgcreditguarantee | 额度担保 | bpchar | 1 |  | √ | '0' | 额度担保 |
| 4 | fgsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fgcontractcurrency | 担保合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fgamount | 担保金额 | numeric | 19 | 6 | √ | 0 | 担保金额 |
| 8 | fgcreditorid | fgcreditorid | int8 | 64 |  | √ | 0 |  |
| 9 | fgcontractid | 担保单据编号 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 10 | fgsrcbilltype | 来源单据 | varchar | 80 |  | √ | ' ' | 来源单据 |
| 11 | fgcurrencyid | fgcurrencyid | int8 | 64 |  | √ | 0 |  |
| 12 | fgstatus | 状态 | varchar | 80 |  | √ | ' ' | 状态,枚举: A :担保中 C :已解除 B :已结清 |
| 13 | fgexchrate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 14 | fgratio | 担保比例(%) | numeric | 19 | 6 | √ | 0 | 担保比例(%) |
| 15 | fgcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fgcreditortype | fgcreditortype | varchar | 50 |  | √ | ' ' |  |
| 18 | fgcontractamount | 担保合同金额 | numeric | 19 | 6 | √ | 0 | 担保合同金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteeuse_info_efid |  | fid |
| 2 | pk_t_gm_guaranteeuse_info |  | fentryid |

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
| 18 | fexcrate | 折债务币种汇率 | numeric | 23 | 10 | √ | 0 | 折债务币种汇率 |
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

## 业务申请-主表 t_lc_bizapply

- **表名称：** 业务申请-主表
- **表名：** t_lc_bizapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 3 | fissurety | 关联保证金 | bpchar | 1 |  | √ | '0' | 关联保证金 |
| 4 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 5 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | flettercreditid | 信用证号 | int8 | 64 |  | √ | 0 | [信用证 lc_lettercredit_f7](../lc_files/lc_lettercredit_f7.md) |
| 8 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 9 | fiscancel | 可撤销 | bpchar | 1 |  | √ | '0' | 可撤销 |
| 10 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: open_card :开证 edit_card :改证 repeal_card :撤证 close_card :闭卷 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fapplyreason | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 15 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 16 | flowstr | 金额下限 | varchar | 50 |  | √ | ' ' | 金额下限 |
| 17 | fisnationalcard | 国际证 | bpchar | 1 |  | √ | '0' | 国际证 |
| 18 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | famountscaleupper | 溢短装金额浮动比例上限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例上限（%） |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fismakeover | 可转让 | bpchar | 1 |  | √ | '0' | 可转让 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fguarantee | 担保方式 | varchar | 30 |  | √ | ' ' | 担保方式,枚举: 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :信用/无担保 |
| 28 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 29 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fdatasources | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand_increase :手工新增 |
| 31 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 32 | fbenefitaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 35 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 36 | fapplyaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 37 | fbizdate | 开证日期 | timestamp | 0 |  |  | null | 开证日期 |
| 38 | fcreditgratio | 授信比例 | numeric | 23 | 10 | √ | 0 | 授信比例 |
| 39 | fbankid | 开证行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 40 | famountscalelow | 溢短装金额浮动比例下限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例下限（%） |
| 41 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fupperstr | 金额上限 | varchar | 50 |  | √ | ' ' | 金额上限 |
| 44 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_bizapply |  | fbillno |
| 2 | pk_t_lc_bizapply |  | fid |

---

## 业务申请-分表 t_lc_bizapply_e

- **表名称：** 业务申请-分表
- **表名：** t_lc_bizapply_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freimbursingbank | 偿付行 | varchar | 255 |  | √ | ' ' | 偿付行 |
| 3 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fnoticebank | 通知行 | varchar | 255 |  | √ | ' ' | 通知行 |
| 5 | fnegotiatingbank | 议付行 | varchar | 255 |  | √ | ' ' | 议付行 |
| 6 | fpromisrate | 保证金比例(%) | numeric | 23 | 2 | √ | 0 | 保证金比例(%) |
| 7 | fbenefiterother | 受益人 | varchar | 255 |  | √ | ' ' | 受益人 |
| 8 | ftotalsuretymoney | 保证金累计金额 | numeric | 23 | 10 | √ | 0 | 保证金累计金额 |
| 9 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 10 | fnegotiatingdate | 议付日期 | timestamp | 0 |  |  | null | 议付日期 |
| 11 | fisbatch | 分批 | bpchar | 1 |  | √ | '0' | 分批 |
| 12 | fislastchange | 最后改证申请 | bpchar | 1 |  | √ | '0' | 最后改证申请 |
| 13 | fdealbilltermstart | 交单期限.开始 | timestamp | 0 |  |  | null | 交单期限.开始 |
| 14 | fbankcountryid | 通知行国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 15 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 16 | fsuretycur | 保证金币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fsuretymoney | 保证金初始金额 | numeric | 23 | 10 | √ | 0 | 保证金初始金额 |
| 18 | fcreditamount | 实际占用授信金额 | numeric | 23 | 10 | √ | 0 | 实际占用授信金额 |
| 19 | fdealbilltermend | 交单期限.结束 | timestamp | 0 |  |  | null | 交单期限.结束 |
| 20 | fistransfer | 转运 | bpchar | 1 |  | √ | '0' | 转运 |
| 21 | fnoticebankid | 通知行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 22 | fconfirmingbank | 保兑行 | varchar | 255 |  | √ | ' ' | 保兑行 |
| 23 | fbenefitcountryid | 受益人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 24 | fisnegotiating | 议付 | bpchar | 1 |  | √ | '0' | 议付 |
| 25 | fcargocountryid | 货物国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 26 | fapplycountryid | 开证人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 27 | fbenefitertype | 受益人类型 | varchar | 50 |  | √ | ' ' | 受益人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 28 | fbenefiterid | 受益人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_bizapply_e |  | forgid |
| 2 | pk_t_lc_bizapply_e |  | fid |

---

## 合同信息分录-多语言表 t_lc_bizapply_entrys_l

- **表名称：** 合同信息分录-多语言表
- **表名：** t_lc_bizapply_entrys_l

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
| 1 | pk_t_lc_bizapply_entrys_l |  | fpkid |
| 2 | idx_lc_bizapply_entrys_l |  | fentryid,flocaleid |

---

## 保证金分录-子表 t_lc_bizapply_s

- **表名称：** 保证金分录-子表
- **表名：** t_lc_bizapply_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsuretybillid | 单据编号 | int8 | 64 |  | √ | 0 | [保证金存入处理F7 fbd_suretybill_f7](../fbd_files/fbd_suretybill_f7.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsuretysource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: hand :债务生成 linkgen :保证金生成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_bizapply_s |  | fentryid |
| 2 | idx_lc_bizapply_s_bn |  | fsuretybillid |

---

## 业务申请-多语言表 t_lc_bizapply_l

- **表名称：** 业务申请-多语言表
- **表名：** t_lc_bizapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 4 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 5 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | fbenefitaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 8 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 9 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 10 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 11 | fapplyreason | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 12 | fapplyaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 13 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 14 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_bizapply_l |  | fid,flocaleid |
| 2 | pk_t_lc_bizapply_l |  | fpkid |

---

## 合同信息分录-子表 t_lc_bizapply_entrys

- **表名称：** 合同信息分录-子表
- **表名：** t_lc_bizapply_entrys

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
| 1 | idx_lc_bizapply_entrys |  | fid |
| 2 | pk_t_lc_bizapply_entrys |  | fentryid |
