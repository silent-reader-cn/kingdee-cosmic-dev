# 销售费用分摊记录-cal_salefeealloc_result

## 销售费用分摊记录-主表 t_cal_salefeealloc

- **表名称：** 销售费用分摊记录-主表
- **表名：** t_cal_salefeealloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fiswrittenoff | 冲销单 | bpchar | 1 |  | √ | '0' | 冲销单 |
| 6 | fisbusalloc | 暂估费用分摊 | bpchar | 1 |  | √ | '0' | 暂估费用分摊 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fismigrate | 是否（企业版）迁移 | bpchar | 1 |  | √ | '0' | 是否（企业版）迁移 |
| 9 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | falloctype | 分摊方式 | bpchar | 1 |  | √ | ' ' | 分摊方式,枚举: 1 :销售费用手工分摊 2 :销售费用自动分摊 3 :费用差异分摊 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fsourceresultid | 上游结果单id（废弃字段） | int8 | 64 |  | √ | 0 | 上游结果单id（废弃字段） |
| 13 | fcreatorid | 分摊人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fallocstand | 分摊标准 | varchar | 20 |  | √ | ' ' | 分摊标准,枚举: LOCALAM :金额（本位币） NUMBER :数量 VOLUME :体积 WEIGHT :净重 DIY :自定义权重 |
| 15 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fisvoucher | 是否已生成凭证 | bpchar | 1 |  | √ | ' ' | 是否已生成凭证 |
| 17 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_salefeealloc |  | fid |
| 2 | idx_cal_salefeealloc_r |  | fsourceresultid |
| 3 | idx_cal_salefeealloc |  | fbillno |

---

## 单据体-子表 t_cal_salefeeallocentry

- **表名称：** 单据体-子表
- **表名：** t_cal_salefeeallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsendbillseq | 发送方单据行号 | varchar | 20 |  | √ | ' ' | 发送方单据行号 |
| 3 | ftotalallocamount | 总分配金额 | numeric | 23 | 10 | √ | 0 | 总分配金额 |
| 4 | fallocamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsendbookdate | 发送方记账日期 | timestamp | 0 |  |  | null | 发送方记账日期 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fallocbasetaxamount | 分摊含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 分摊含税金额（本位币） |
| 9 | fsrcbillentryseq | 来源单据分录行号 | varchar | 20 |  | √ | ' ' | 来源单据分录行号 |
| 10 | fconbillrownum | 合同行号 | varchar | 20 |  | √ | ' ' | 合同行号 |
| 11 | fconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 12 | fsourceresultentryid | 上游分配结果单分录id | int8 | 64 |  | √ | 0 | 上游分配结果单分录id |
| 13 | frecievebillseq | 承担方单据行号 | varchar | 20 |  | √ | ' ' | 承担方单据行号 |
| 14 | fsendpricetaxtotalbase | 发送方单据含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 发送方单据含税金额（本位币） |
| 15 | fsendamountbase | 发送方单据金额（本位币） | numeric | 23 | 10 | √ | 0 | 发送方单据金额（本位币） |
| 16 | fsendsourceentryid | 发送方源单分录id | int8 | 64 |  | √ | 0 | 发送方源单分录id |
| 17 | fallocpricetaxtotalbase | 总分配含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 总分配含税金额（本位币） |
| 18 | fdistributevalue | 分摊权重 | numeric | 23 | 10 | √ | 0 | 分摊权重 |
| 19 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | fallocpricetaxtotal | 总分配含税金额 | numeric | 23 | 10 | √ | 0 | 总分配含税金额 |
| 21 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 22 | fbizorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fbizoperator | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 26 | falloctaxamount | 分摊含税金额 | numeric | 23 | 10 | √ | 0 | 分摊含税金额 |
| 27 | fsendbilltype | 发送方单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 28 | fcostdepartment | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | frecievebookdate | 承担方记账日期 | timestamp | 0 |  |  | null | 承担方记账日期 |
| 30 | frecievebillentryid | 承担方单据分录id | int8 | 64 |  | √ | 0 | 承担方单据分录id |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fsendpricetaxtotal | 发送方单据含税金额 | numeric | 23 | 10 | √ | 0 | 发送方单据含税金额 |
| 33 | fsendamount | 发送方单据金额 | numeric | 23 | 10 | √ | 0 | 发送方单据金额 |
| 34 | fmainbillentryseq | 核心单据分录行号 | varchar | 20 |  | √ | ' ' | 核心单据分录行号 |
| 35 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 36 | fbasicqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 37 | frecievebillno | 承担方单据编号 | varchar | 80 |  | √ | ' ' | 承担方单据编号 |
| 38 | ftotaldistributevalue | 总权重 | numeric | 23 | 10 | √ | 0 | 总权重 |
| 39 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 40 | fsendbillid | 发送方单据id | int8 | 64 |  | √ | 0 | 发送方单据id |
| 41 | fsettlementsupplier | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 42 | fbizdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | frecievebillid | 承担方单据id | int8 | 64 |  | √ | 0 | 承担方单据id |
| 44 | fcurrency | 发送方单据结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 46 | fallocbaseamount | 分摊金额（本位币） | numeric | 23 | 10 | √ | 0 | 分摊金额（本位币） |
| 47 | fbasecurrency | 发送方单据本位币币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 48 | fallocsendamountbase | 总分配单据金额（本位币） | numeric | 23 | 10 | √ | 0 | 总分配单据金额（本位币） |
| 49 | frecievebilltype | 承担方单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 50 | fsettlecustomer | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 51 | fsendbillno | 发送方单据编号 | varchar | 80 |  | √ | ' ' | 发送方单据编号 |
| 52 | fsendbillentryid | 发送方单据分录id | int8 | 64 |  | √ | 0 | 发送方单据分录id |
| 53 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_salefeeallocentry_rb |  | frecievebillid |
| 2 | idx_cal_salefeeallocentry_f |  | fid |
| 3 | pk_cal_salefeeallocentry |  | fentryid |
