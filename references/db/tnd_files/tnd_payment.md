# 缴费单-tnd_payment

## 供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierusers |  | fpkid |
| 2 | idx_src_supplierusers_eid |  | fentryid |
| 3 | idx_src_supplierusers_bid |  | fbasedataid |

---

## 缴费凭证-附件表 t_src_paymententry_fj1

- **表名称：** 缴费凭证-附件表
- **表名：** t_src_paymententry_fj1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_paymententry_fj1 |  | fpkid |
| 2 | idx_src_paymententry_fj1_bid |  | fbasedataid |
| 3 | idx_src_paymententry_fj1_eid |  | fentryid |

---

## 缴费单-主表 t_src_paymententry

- **表名称：** 缴费单-主表
- **表名：** t_src_paymententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 招标项目 | int8 | 64 |  | √ | 0 | 寻源项目 pds_projectf7 |
| 2 | fpackfeeitemid | fpackfeeitemid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftransferdate | 结余时间 | timestamp | 0 |  |  | null | 结余时间 |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :候选 3 :落标 5 :培养 6 :不推荐 0 :未定标 |
| 7 | freturnopinion | 退还说明 | varchar | 100 |  | √ | ' ' | 退还说明 |
| 8 | fcfmdate | 供应商提交时间 | timestamp | 0 |  |  | null | 供应商提交时间 |
| 9 | ffeewayid | 收费方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftransferuserid | ftransferuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 13 | fsurplustype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :投标保证金 2 :履约保证金 3 :标书费 |
| 14 | fcarryoveropinion | 转履约说明 | varchar | 100 |  | √ | ' ' | 转履约说明 |
| 15 | fconfirmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 16 | freturndate | 退还时间 | timestamp | 0 |  |  | null | 退还时间 |
| 17 | fbillno | 缴费单号 | varchar | 30 |  | √ | ' ' | 缴费单号 |
| 18 | fisfeeagent | 采购方代理缴费 | bpchar | 1 |  | √ | '0' | 采购方代理缴费 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 21 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 22 | fcarryoverdate | 转履约时间 | timestamp | 0 |  |  | null | 转履约时间 |
| 23 | fusesurplus | 本次使用 | numeric | 23 | 10 | √ | 0 | 本次使用 |
| 24 | frejectopinion | 打回原因 | varchar | 100 |  | √ | ' ' | 打回原因 |
| 25 | ffeeitemid | 收费项 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | ' ' | 分录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | famount | 应缴金额 | numeric | 23 | 10 | √ | 0 | 应缴金额 |
| 30 | fpayamount | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 31 | freturnuserid | 退还人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 33 | fsurplusamount | 本次余额 | numeric | 23 | 10 | √ | 0 | 本次余额 |
| 34 | fpresurplusamount | 上次余额 | numeric | 23 | 10 | √ | 0 | 上次余额 |
| 35 | fpaystatus | 缴费状态 | bpchar | 1 |  | √ | ' ' | 缴费状态,枚举: A :待缴费 B :已缴费|待确认 C :已缴费|已确认 D :已退还 E :已转结余 F :免交 G :已转履约金 I :已废标 J :已终止 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 38 | ffeeamount | 缴费金额 | numeric | 23 | 10 | √ | 0 | 缴费金额 |
| 39 | fcarryoveruserid | fcarryoveruserid | int8 | 64 |  | √ | 0 |  |
| 40 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 41 | ftransferamount | 结余金额 | numeric | 23 | 10 | √ | 0 | 结余金额 |
| 42 | fremark | 缴费说明 | varchar | 100 |  | √ | ' ' | 缴费说明 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fconfirmuserid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fusedate | fusedate | timestamp | 0 |  |  | null |  |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fsurplusid | fsurplusid | int8 | 64 |  | √ | 0 |  |
| 48 | freturnamount | 退还金额 | numeric | 23 | 10 | √ | 0 | 退还金额 |
| 49 | fcarryoveramount | 转履约金额 | numeric | 23 | 10 | √ | 0 | 转履约金额 |
| 50 | ftransferopinion | 结余说明 | varchar | 100 |  | √ | ' ' | 结余说明 |
| 51 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 52 | frejectuserid | 打回人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已拒绝 D :未回复 |
| 54 | fconfirmopinion | 确认意见 | varchar | 255 |  | √ | ' ' | 确认意见 |
| 55 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 56 | fpaydate | 缴费时间 | timestamp | 0 |  |  | null | 缴费时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_paymententry_fct |  | fcreatetime |
| 2 | idx_src_paymententry_fpg |  | fpackageid |
| 3 | idx_src_paymententry_fid |  | fid |
| 4 | idx_src_paymententry_ftype |  | fsurplustype |
| 5 | pk_src_paymententry |  | fentryid |
| 6 | idx_src_paymententry_fbillno |  | fbillno |
| 7 | idx_src_paymententry_fsup |  | fsupplierid |
