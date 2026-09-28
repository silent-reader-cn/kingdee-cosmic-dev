# 收费明细(工具)-src_payment_tool

## 收费明细(工具)-主表 t_src_paymententry

- **表名称：** 收费明细(工具)-主表
- **表名：** t_src_paymententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 2 | fpackfeeitemid | fpackfeeitemid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftransferdate | 结余时间 | timestamp | 0 |  |  | null | 结余时间 |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :候选 3 :落标 5 :培养 6 :不推荐 0 :未定标 |
| 7 | freturnopinion | 退还说明 | varchar | 100 |  | √ | ' ' | 退还说明 |
| 8 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 9 | ffeewayid | 收费方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | ftransferuserid | 结余人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 13 | fsurplustype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :投标保证金 2 :履约保证金 3 :标书费 |
| 14 | fcarryoveropinion | 转履约说明 | varchar | 100 |  | √ | ' ' | 转履约说明 |
| 15 | fconfirmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 16 | freturndate | 退还时间 | timestamp | 0 |  |  | null | 退还时间 |
| 17 | fbillno | 收费单号 | varchar | 30 |  | √ | ' ' | 收费单号 |
| 18 | fisfeeagent | fisfeeagent | bpchar | 1 |  | √ | '0' |  |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 22 | fcarryoverdate | 转履约时间 | timestamp | 0 |  |  | null | 转履约时间 |
| 23 | fusesurplus | 本次使用 | numeric | 23 | 10 | √ | 0 | 本次使用 |
| 24 | frejectopinion | 打回原因 | varchar | 100 |  | √ | ' ' | 打回原因 |
| 25 | ffeeitemid | 收费项 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | ' ' | 分录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | famount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 30 | fpayamount | 实收金额 | numeric | 23 | 10 | √ | 0 | 实收金额 |
| 31 | freturnuserid | 退还人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 33 | fsurplusamount | 本次余额 | numeric | 23 | 10 | √ | 0 | 本次余额 |
| 34 | fpresurplusamount | 上次余额 | numeric | 23 | 10 | √ | 0 | 上次余额 |
| 35 | fpaystatus | 收费状态 | bpchar | 1 |  | √ | ' ' | 收费状态,枚举: A :待收款 B :已收款\|待确认 C :已收款\|已确认 D :已退还 E :已转结余 F :免交 G :已转履约金 I :已废标 J :已终止 |
| 36 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 37 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 38 | ffeeamount | 收费金额 | numeric | 23 | 10 | √ | 0 | 收费金额 |
| 39 | fcarryoveruserid | 转履约人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 41 | ftransferamount | 结余金额 | numeric | 23 | 10 | √ | 0 | 结余金额 |
| 42 | fremark | 收费说明 | varchar | 100 |  | √ | ' ' | 收费说明 |
| 43 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 44 | fconfirmuserid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fusedate | 使用余额时间 | timestamp | 0 |  |  | null | 使用余额时间 |
| 46 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 47 | fsurplusid | 费用余额ID | int8 | 64 |  | √ | 0 | 费用余额ID |
| 48 | freturnamount | 退还金额 | numeric | 23 | 10 | √ | 0 | 退还金额 |
| 49 | fcarryoveramount | 转履约金额 | numeric | 23 | 10 | √ | 0 | 转履约金额 |
| 50 | ftransferopinion | 结余说明 | varchar | 100 |  | √ | ' ' | 结余说明 |
| 51 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 52 | frejectuserid | 打回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 54 | fconfirmopinion | 确认意见 | varchar | 255 |  | √ | ' ' | 确认意见 |
| 55 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 56 | fpaydate | 收费时间 | timestamp | 0 |  |  | null | 收费时间 |

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
