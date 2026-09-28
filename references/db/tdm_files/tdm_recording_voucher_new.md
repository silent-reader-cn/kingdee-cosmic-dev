# 凭证数据-tdm_recording_voucher_new

## 凭证数据-主表 t_tdm_recordingvoucher

- **表名称：** 凭证数据-主表
- **表名：** t_tdm_recordingvoucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 记账凭证类型 | varchar | 100 |  | √ | ' ' | 记账凭证类型 |
| 3 | fadjust | 调整期 | varchar | 50 |  | √ | '0' | 调整期,枚举: 1 :是 0 :否 |
| 4 | fmeasureunit | 计量单位 | varchar | 100 |  | √ | ' ' | 计量单位 |
| 5 | fdebitlocalcurrency | 借方本币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借方本币金额 |
| 6 | fdebitoriginalcurrency | 借方原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借方原币金额 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fvoucherrow | 记账凭证行号 | varchar | 100 |  | √ | ' ' | 记账凭证行号 |
| 9 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 10 | fbillcode | 票据号 | varchar | 100 |  | √ | ' ' | 票据号 |
| 11 | frecordlineextend | 分录行可扩展字段结构值 | varchar | 100 |  | √ | ' ' | 分录行可扩展字段结构值 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 16 | fauditor | 审核人 | varchar | 100 |  | √ | ' ' | 审核人 |
| 17 | fcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 18 | fsettlementtype | 结算方式编码 | varchar | 100 |  | √ | ' ' | 结算方式编码 |
| 19 | fbookkeeper | 记账人 | varchar | 100 |  | √ | ' ' | 记账人 |
| 20 | faccountcode | 科目编码 | varchar | 100 |  | √ | ' ' | 科目编码 |
| 21 | fnowriteoff | 账票未核销金额 | numeric | 23 | 10 | √ | 0 | 账票未核销金额 |
| 22 | fcurrencytype | 币种编码 | varchar | 100 |  | √ | ' ' | 币种编码 |
| 23 | fbzmc | 币种名称 | varchar | 50 |  | √ | ' ' | 币种名称 |
| 24 | fvoucherid | 凭证ID | varchar | 50 |  | √ | ' ' | 凭证ID |
| 25 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 26 | fverifymatch | 核销匹配 | varchar | 50 |  | √ | ' ' | 核销匹配 |
| 27 | fvoucherremark | 记账凭证摘要 | varchar | 2000 |  | √ | ' ' | 记账凭证摘要 |
| 28 | fwriteoff | 账票已核销金额 | numeric | 23 | 10 | √ | 0 | 账票已核销金额 |
| 29 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fsubaccount4 | 辅助项4编号 | varchar | 100 |  | √ | ' ' | 辅助项4编号 |
| 31 | fsubaccount3 | 辅助项3编号 | varchar | 100 |  | √ | ' ' | 辅助项3编号 |
| 32 | fsubaccount6 | 科目名称 | varchar | 500 |  | √ | ' ' | 科目名称 |
| 33 | fsubaccount5 | 辅助项5编号 | varchar | 100 |  | √ | ' ' | 辅助项5编号 |
| 34 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 35 | fcreditamount | 贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方数量 |
| 36 | fsourcesys | 来源系统 | varchar | 50 |  |  | ' ' | 来源系统 |
| 37 | fdebitamount | 借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 借方数量 |
| 38 | frecordingflag | 记账标志 | varchar | 100 |  | √ | ' ' | 记账标志 |
| 39 | foriginator | 制单人 | varchar | 100 |  | √ | ' ' | 制单人 |
| 40 | faccountperiod | 会计期间号 | varchar | 100 |  | √ | ' ' | 会计期间号,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 41 | fdatasource | 数据来源 | varchar | 100 |  | √ | ' ' | 数据来源 |
| 42 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 43 | faccountyear | 会计年度 | varchar | 100 |  | √ | ' ' | 会计年度 |
| 44 | finvalidflag | 作废标志 | varchar | 100 |  | √ | ' ' | 作废标志 |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | faccountcycle | 会计账期 | varchar | 100 |  | √ | ' ' | 会计账期 |
| 47 | fvouchercode | 记账凭证编号 | varchar | 100 |  | √ | ' ' | 记账凭证编号 |
| 48 | fbilldate | 票据日期 | varchar | 100 |  | √ | ' ' | 票据日期 |
| 49 | fexchangeratetype | 汇率类型编号 | varchar | 100 |  | √ | ' ' | 汇率类型编号 |
| 50 | fadjperi | 调整期间 | varchar | 50 |  | √ | ' ' | 调整期间 |
| 51 | fcreditoriginalcurrency | 贷方原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方原币金额 |
| 52 | fvouchersource | 记账凭证来源 | varchar | 100 |  | √ | ' ' | 记账凭证来源 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fext4 | 拓展字段4 | varchar | 1000 |  |  | ' ' | 拓展字段4 |
| 55 | faccountbookstype | 账簿类型 | varchar | 50 |  |  | ' ' | 账簿类型 |
| 56 | fext3 | 拓展字段3 | varchar | 1000 |  |  | ' ' | 拓展字段3 |
| 57 | fext5 | 拓展字段5 | varchar | 1000 |  |  | ' ' | 拓展字段5 |
| 58 | fsubaccount2 | 辅助项2编号 | varchar | 100 |  | √ | ' ' | 辅助项2编号 |
| 59 | fext2 | 拓展字段2 | varchar | 1000 |  |  | ' ' | 拓展字段2 |
| 60 | fisadjust | 调整期 | bpchar | 1 |  | √ | '0' | 调整期 |
| 61 | fsubaccount1 | 辅助项1编号 | varchar | 500 |  | √ | ' ' | 辅助项1编号 |
| 62 | fext1 | 拓展字段1 | varchar | 1000 |  |  | ' ' | 拓展字段1 |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 64 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 65 | faccountdimension | 核算维度 | varchar | 2000 |  | √ | ' ' | 核算维度 |
| 66 | fcreditlocalcurrency | 贷方本币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 贷方本币金额 |
| 67 | fattachcount | 附件数量 | int8 | 64 |  | √ | 0 | 附件数量 |
| 68 | fbalanceid | 科目 | varchar | 36 |  | √ | ' ' | [科目 tdm_account](../tdm_files/tdm_account.md) |
| 69 | fbilltype | 票据类型 | varchar | 100 |  | √ | ' ' | 票据类型 |
| 70 | fbkpfextend | 凭证头可扩展字段结构值 | varchar | 100 |  | √ | ' ' | 凭证头可扩展字段结构值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_recordingvoucher |  | faccountcode |
| 2 | pk_t_tdm_recordingvoucher |  | fid |
| 3 | idx_tdm_org_year_period |  | forgid,faccountyear,faccountperiod |
| 4 | idx_t_tdm_recordingvoucher_2 |  | fbalanceid |
| 5 | idx_tdm_rv_voucherid |  | fvoucherid |
| 6 | idx_voucher_creditlocalcurency |  | fcreditlocalcurrency |
