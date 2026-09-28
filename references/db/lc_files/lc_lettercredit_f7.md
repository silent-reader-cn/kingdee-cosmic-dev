# 信用证-lc_lettercredit_f7

## 信用证-分表 t_lc_lettercredit_b

- **表名称：** 信用证-分表
- **表名：** t_lc_lettercredit_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillterm | fbillterm | varchar | 255 |  | √ | ' ' |  |
| 3 | ffeepayerid | ffeepayerid | int8 | 64 |  | √ | 0 |  |
| 4 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: lc_onlineresult :在线查询结果单 cas_paybill :付款处理 |
| 5 | fresubmitsrcno | fresubmitsrcno | varchar | 50 |  | √ | ' ' |  |
| 6 | fbillterm_tag | fbillterm_tag | text | 0 |  |  | null |  |
| 7 | ftradeterms | ftradeterms | varchar | 50 |  | √ | ' ' |  |
| 8 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 9 | fsubmittime | fsubmittime | timestamp | 0 |  |  | null |  |
| 10 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
| 11 | faddterm_tag | faddterm_tag | text | 0 |  |  | null |  |
| 12 | fisresubmit | fisresubmit | bpchar | 1 |  | √ | '0' |  |
| 13 | flfeeacctbankid | flfeeacctbankid | int8 | 64 |  | √ | 0 |  |
| 14 | fdays | fdays | int4 | 32 |  | √ | 0 |  |
| 15 | fbebankstatus | 直联提交状态 | varchar | 50 |  | √ | ' ' | 直联提交状态,枚举: OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 |
| 16 | faddterm | faddterm | varchar | 255 |  | √ | ' ' |  |
| 17 | ftradechannel | 交易渠道 | varchar | 50 |  | √ | 'offline' | 交易渠道,枚举: offline :线下处理 online :银企直联 |
| 18 | fpaymenttype | fpaymenttype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_lettercredit_b |  | fid |
| 2 | idx_lettercreditb_fsrcid |  | fsrcbillid |

---

## 信用证-分表 t_lc_lettercredit_e

- **表名称：** 信用证-分表
- **表名：** t_lc_lettercredit_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freimbursingbank | 偿付行 | varchar | 255 |  | √ | ' ' | 偿付行 |
| 3 | fnotarramount | fnotarramount | numeric | 23 | 10 | √ | 0 |  |
| 4 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnoticebank | 通知行 | varchar | 255 |  | √ | ' ' | 通知行 |
| 6 | fnegotiatingbank | 议付行 | varchar | 255 |  | √ | ' ' | 议付行 |
| 7 | ftotalarramount | 累计到单金额 | numeric | 23 | 10 | √ | 0 | 累计到单金额 |
| 8 | fpromisrate | fpromisrate | numeric | 23 | 2 | √ | 0 |  |
| 9 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 10 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 11 | fbenefiterother | 受益人 | varchar | 255 |  | √ | ' ' | 受益人 |
| 12 | ftotalsuretymoney | ftotalsuretymoney | numeric | 23 | 10 | √ | 0 |  |
| 13 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 14 | fnegotiatingdate | 议付日期 | timestamp | 0 |  |  | null | 议付日期 |
| 15 | fisbatch | 分批 | bpchar | 1 |  | √ | '0' | 分批 |
| 16 | farrivalsum | farrivalsum | int4 | 32 |  | √ | 0 |  |
| 17 | fdealbilltermstart | 交单期限.开始 | timestamp | 0 |  |  | null | 交单期限.开始 |
| 18 | fbankcountryid | 通知行国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 19 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 20 | fsuretycur | fsuretycur | int8 | 64 |  | √ | 0 |  |
| 21 | fpushcount | fpushcount | int8 | 64 |  | √ | 0 |  |
| 22 | fsuretymoney | fsuretymoney | numeric | 23 | 10 | √ | 0 |  |
| 23 | fcreditamount | fcreditamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | fdealbilltermend | 交单期限.结束 | timestamp | 0 |  |  | null | 交单期限.结束 |
| 25 | fbuyerint | fbuyerint | varchar | 50 |  | √ | '0' |  |
| 26 | fistransfer | 转运 | bpchar | 1 |  | √ | '0' | 转运 |
| 27 | fnoticebankid | fnoticebankid | int8 | 64 |  | √ | 0 |  |
| 28 | fbackcredittype | 背对背证类型 | varchar | 50 |  | √ | ' ' | 背对背证类型,枚举: mother_credit :母证 child_credit :子证 |
| 29 | fconfirmingbank | 保兑行 | varchar | 255 |  | √ | ' ' | 保兑行 |
| 30 | fbenefitcountryid | 受益人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 31 | feassrcid | feassrcid | varchar | 50 |  | √ | ' ' |  |
| 32 | fisnegotiating | 议付 | bpchar | 1 |  | √ | '0' | 议付 |
| 33 | frepealdate | frepealdate | timestamp | 0 |  |  | null |  |
| 34 | fcargocountryid | 货物国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 35 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 36 | fapplycountryid | 开证人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 37 | fbenefitertype | 受益人类型 | varchar | 50 |  | √ | ' ' | 受益人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 38 | fclosecarddate | fclosecarddate | timestamp | 0 |  |  | null |  |
| 39 | fisbackcredit | 背对背证 | bpchar | 1 |  | √ | '0' | 背对背证 |
| 40 | fbenefiterid | 受益人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercredit_eassrcid |  | feassrcid |
| 2 | idx_lc_lettercredit_e |  | forgid |
| 3 | pk_t_lc_lettercredit_e |  | fid |

---

## 信用证-多语言表 t_lc_lettercredit_l

- **表名称：** 信用证-多语言表
- **表名：** t_lc_lettercredit_l

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
| 9 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
| 10 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 11 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 12 | fapplyreason | fapplyreason | varchar | 255 |  | √ | ' ' |  |
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
| 1 | idx_lc_lettercredit_l |  | fid,flocaleid |
| 2 | pk_t_lc_lettercredit_l |  | fpkid |

---

## 信用证-主表 t_lc_lettercredit

- **表名称：** 信用证-主表
- **表名：** t_lc_lettercredit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 3 | fissurety | fissurety | bpchar | 1 |  | √ | '0' |  |
| 4 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 5 | fvalidaddress | fvalidaddress | varchar | 255 |  | √ | ' ' |  |
| 6 | fcargodesc | fcargodesc | varchar | 255 |  | √ | ' ' |  |
| 7 | fcreditno | 信用证号 | varchar | 50 |  | √ | ' ' | 信用证号 |
| 8 | fiscancel | 可撤销 | bpchar | 1 |  | √ | '0' | 可撤销 |
| 9 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreditapplyno | 开证申请 | varchar | 50 |  | √ | ' ' | 开证申请 |
| 12 | fapplyreason | fapplyreason | varchar | 255 |  | √ | ' ' |  |
| 13 | flowstr | 金额下限 | varchar | 50 |  | √ | ' ' | 金额下限 |
| 14 | fisnationalcard | 国际证 | bpchar | 1 |  | √ | '0' | 国际证 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | famountscaleupper | 溢短装金额浮动比例上限 | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例上限 |
| 17 | fismakeover | 可转让 | bpchar | 1 |  | √ | '0' | 可转让 |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
| 22 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 23 | fcontractremark | fcontractremark | varchar | 255 |  | √ | ' ' |  |
| 24 | fapplyaddress | fapplyaddress | varchar | 255 |  | √ | ' ' |  |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 27 | fbankid | 开证行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 28 | famountscalelow | 溢短装金额浮动比例下限 | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例下限 |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 33 | fbankaddress | fbankaddress | varchar | 255 |  | √ | ' ' |  |
| 34 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |
| 35 | fisclosed | fisclosed | bpchar | 1 |  | √ | '0' |  |
| 36 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fcreditstatus | 信用证状态 | varchar | 50 |  | √ | ' ' | 信用证状态,枚举: done_register :已登记 done_close :已闭卷 done_repeal :已撤证 change_ing :改证中 |
| 39 | fapplydate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 |
| 42 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 43 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fdatasources | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand_increase :手工新增 |
| 45 | fbenefitaddress | fbenefitaddress | varchar | 255 |  | √ | ' ' |  |
| 46 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 47 | fbizdate | 开证日期 | timestamp | 0 |  |  | null | 开证日期 |
| 48 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 49 | fupperstr | 金额上限 | varchar | 50 |  | √ | ' ' | 金额上限 |
| 50 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercredit |  | fbillno |
| 2 | pk_t_lc_lettercredit |  | fid |
