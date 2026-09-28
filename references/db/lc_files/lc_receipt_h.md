# 历史版本信用证-lc_receipt_h

## 合同信息分录-多语言表 t_lc_receipt_entry_h_l

- **表名称：** 合同信息分录-多语言表
- **表名：** t_lc_receipt_entry_h_l

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
| 1 | idx_lc_receipt_entry_h_l |  | fentryid,flocaleid |
| 2 | pk_t_lc_receipt_entry_h_l |  | fpkid |

---

## 历史版本信用证-主表 t_lc_receipt_h

- **表名称：** 历史版本信用证-主表
- **表名：** t_lc_receipt_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 3 | freceiptdate | 收证日期 | timestamp | 0 |  |  | null | 收证日期 |
| 4 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 5 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | flettercreditid | 信用证 | int8 | 64 |  | √ | 0 | [信用证 lc_lettercredit_f7](../lc_files/lc_lettercredit_f7.md) |
| 8 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 9 | fcreditno | 信用证号 | varchar | 80 |  | √ | ' ' | 信用证号 |
| 10 | fiscancel | 可撤销 | bpchar | 1 |  | √ | '0' | 可撤销 |
| 11 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmodifydate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 15 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 16 | flowstr | 金额下限 | varchar | 50 |  | √ | ' ' | 金额下限 |
| 17 | fisnationalcard | 国际证 | bpchar | 1 |  | √ | '0' | 国际证 |
| 18 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | famountscaleupper | 溢短装金额浮动比例上限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例上限（%） |
| 21 | fversion | 信用证版本号 | varchar | 80 |  | √ | ' ' | 信用证版本号 |
| 22 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fismakeover | 可转让 | bpchar | 1 |  | √ | '0' | 可转让 |
| 25 | fcreditstatus | 信用证状态 | varchar | 50 |  | √ | ' ' | 信用证状态,枚举: done_register :已登记 done_close :已闭卷 |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fapplydate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 30 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fdatasources | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand_increase :手工新增 |
| 32 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 33 | fbenefitaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 34 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 35 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 36 | fbizcontactinfo | 业务联系方式 | varchar | 80 |  | √ | ' ' | 业务联系方式 |
| 37 | fapplyaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 38 | fbizdate | 开证日期 | timestamp | 0 |  |  | null | 开证日期 |
| 39 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 40 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 41 | fbankid | 通知行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 42 | famountscalelow | 溢短装金额浮动比例下限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例下限（%） |
| 43 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fupperstr | 金额上限 | varchar | 50 |  | √ | ' ' | 金额上限 |
| 46 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_receipt_h |  | fbillno |
| 2 | pk_t_lc_receipt_h |  | fid |

---

## 合同信息分录-子表 t_lc_receipt_entry_h

- **表名称：** 合同信息分录-子表
- **表名：** t_lc_receipt_entry_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftransportway | ftransportway | varchar | 255 |  | √ | ' ' |  |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fvalidaddress | fvalidaddress | varchar | 255 |  | √ | ' ' |  |
| 5 | fsourceentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 6 | fcargodesc | fcargodesc | varchar | 255 |  | √ | ' ' |  |
| 7 | fordernum | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 10 | fcountscalelow | 下限 | numeric | 19 | 6 | √ | 0 | 下限 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fstartplace | fstartplace | varchar | 255 |  | √ | ' ' |  |
| 13 | frate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 14 | fbankaddress | fbankaddress | varchar | 255 |  | √ | ' ' |  |
| 15 | forderqty | 订货数量 | int8 | 64 |  | √ | 0 | 订货数量 |
| 16 | funloadplace | funloadplace | varchar | 255 |  | √ | ' ' |  |
| 17 | fcountscaleupper | 上限 | numeric | 19 | 6 | √ | 0 | 上限 |
| 18 | ftaxamount | 含税金额 | numeric | 19 | 6 | √ | 0 | 含税金额 |
| 19 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fdestination | fdestination | varchar | 255 |  | √ | ' ' |  |
| 22 | fbenefitaddress | fbenefitaddress | varchar | 255 |  | √ | ' ' |  |
| 23 | fcontractamount | 合同金额 | numeric | 19 | 6 | √ | 0 | 合同金额 |
| 24 | fcontractremark | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 25 | fapplyaddress | fapplyaddress | varchar | 255 |  | √ | ' ' |  |
| 26 | fcontractnum | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fmodelnum | 规格型号 | varchar | 80 |  | √ | ' ' | 规格型号 |
| 29 | fcontractcurrencyid | 合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_receipt_entry_h |  | fentryid |
| 2 | idx_lc_receipt_entry_h |  | fid |

---

## 关联子实体-子表 t_lc_receipt_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lc_receipt_lk

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
| 1 | pk_lc_receipt_lk |  | fpkid |
| 2 | idx_lc_receipt_lk_fk |  | fid |

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

## 历史版本信用证-关联追踪表 t_lc_receipt_tc

- **表名称：** 历史版本信用证-关联追踪表
- **表名：** t_lc_receipt_tc

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
| 1 | pk_lc_receipt_tc |  | fid |
| 2 | idx_lc_receipt_tc_tbill |  | ftbillid |
| 3 | idx_lc_receipt_tc_tid |  | ftid |

---

## 历史版本信用证-分表 t_lc_receipt_h_e

- **表名称：** 历史版本信用证-分表
- **表名：** t_lc_receipt_h_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freimbursingbank | 偿付行 | varchar | 255 |  | √ | ' ' | 偿付行 |
| 3 | fnotarramount | 未交单金额 | numeric | 23 | 10 | √ | 0 | 未交单金额 |
| 4 | forgid | 受益人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnoticebank | 开证行 | varchar | 255 |  | √ | ' ' | 开证行 |
| 6 | fnegotiatingbank | 议付行 | varchar | 255 |  | √ | ' ' | 议付行 |
| 7 | ftotalarramount | 累计交单金额 | numeric | 23 | 10 | √ | 0 | 累计交单金额 |
| 8 | fpayamount | 已收金额 | numeric | 23 | 10 | √ | 0 | 已收金额 |
| 9 | fbenefiterother | 开证人 | varchar | 255 |  | √ | ' ' | 开证人 |
| 10 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 11 | fnegotiatingdate | 议付日期 | timestamp | 0 |  |  | null | 议付日期 |
| 12 | fisbatch | 分批 | bpchar | 1 |  | √ | '0' | 分批 |
| 13 | farrivalsum | 交单笔数 | int4 | 32 |  | √ | 0 | 交单笔数 |
| 14 | fdealbilltermstart | 交单期限.开始 | timestamp | 0 |  |  | null | 交单期限.开始 |
| 15 | fbankcountryid | 通知行国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 16 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 17 | fdealbilltermend | 交单期限.结束 | timestamp | 0 |  |  | null | 交单期限.结束 |
| 18 | fistransfer | 转运 | bpchar | 1 |  | √ | '0' | 转运 |
| 19 | fconfirmingbank | 保兑行 | varchar | 255 |  | √ | ' ' | 保兑行 |
| 20 | fbenefitcountryid | 开证人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 21 | fisnegotiating | 议付 | bpchar | 1 |  | √ | '0' | 议付 |
| 22 | fcargocountryid | 货物国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 23 | fnotpayamount | 未收金额 | numeric | 23 | 10 | √ | 0 | 未收金额 |
| 24 | fapplycountryid | 受益人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 25 | fbenefitertype | 开证人类型 | varchar | 50 |  | √ | ' ' | 开证人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 26 | fbenefiterid | 开证人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_receipt_h_e |  | fid |
| 2 | idx_lc_receipt_h_e |  | forgid |

---

## 历史版本信用证-反写记录表 t_lc_receipt_wb

- **表名称：** 历史版本信用证-反写记录表
- **表名：** t_lc_receipt_wb

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
| 1 | pk_lc_receipt_wb |  | fentryid |
| 2 | idx_lc_receipt_wb_fk |  | fid |

---

## 历史版本信用证-多语言表 t_lc_receipt_h_l

- **表名称：** 历史版本信用证-多语言表
- **表名：** t_lc_receipt_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 4 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 5 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | fbenefitaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 8 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 9 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 10 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 11 | fapplyaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 12 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 13 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_receipt_h_l |  | fid,flocaleid |
| 2 | pk_t_lc_receipt_h_l |  | fpkid |
