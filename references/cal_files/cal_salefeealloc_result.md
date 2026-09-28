# 销售费用分摊记录-cal_salefeealloc_result

## 销售费用分摊记录-主表 t_cal_salefeealloc

- **表名称：** 销售费用分摊记录-主表
- **表名：** t_cal_salefeealloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fiswrittenoff | 冲销单 | bpchar | 1 |  | √ | '0' | 冲销单 |
| 6 | fisbusalloc | 暂估费用分摊 | bpchar | 1 |  | √ | '0' | 暂估费用分摊 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | falloctype | 分摊方式 | bpchar | 1 |  | √ | ' ' | 分摊方式,枚举: 1 :销售费用手工分摊 2 :销售费用自动分摊 3 :费用差异分摊 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsourceresultid | 上游结果单id（废弃字段） | int8 | 64 |  | √ | 0 | 上游结果单id（废弃字段） |
| 12 | fcreatorid | 分摊人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fallocstand | 分摊标准 | varchar | 20 |  | √ | ' ' | 分摊标准,枚举: LOCALAM :金额（本位币） NUMBER :数量 VOLUME :体积 WEIGHT :净重 DIY :自定义权重 |
| 14 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fisvoucher | 是否已生成凭证 | bpchar | 1 |  | √ | ' ' | 是否已生成凭证 |
| 16 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
| 2 | fsendamount | 发送方单据金额 | numeric | 23 | 10 | √ | 0 | 发送方单据金额 |
| 3 | fmainbillentryseq | 核心单据分录行号 | varchar | 20 |  | √ | ' ' | 核心单据分录行号 |
| 4 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 5 | fsendbillseq | 发送方单据行号 | varchar | 20 |  | √ | ' ' | 发送方单据行号 |
| 6 | fallocamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbasicqty | 基本单位数量 | int8 | 64 |  | √ | 0 | 基本单位数量 |
| 9 | fsendbookdate | 发送方记账日期 | timestamp | 0 |  |  | null | 发送方记账日期 |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fallocbasetaxamount | 分摊含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 分摊含税金额（本位币） |
| 12 | frecievebillno | 承担方单据编号 | varchar | 80 |  | √ | ' ' | 承担方单据编号 |
| 13 | ftotaldistributevalue | 总权重 | numeric | 23 | 10 | √ | 0 | 总权重 |
| 14 | fsrcbillentryseq | 来源单据分录行号 | varchar | 20 |  | √ | ' ' | 来源单据分录行号 |
| 15 | fconbillrownum | 合同行号 | varchar | 20 |  | √ | ' ' | 合同行号 |
| 16 | fconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 17 | fsourceresultentryid | 上游分配结果单分录id | int8 | 64 |  | √ | 0 | 上游分配结果单分录id |
| 18 | fsendbillid | 发送方单据id | int8 | 64 |  | √ | 0 | 发送方单据id |
| 19 | frecievebillseq | 承担方单据行号 | varchar | 20 |  | √ | ' ' | 承担方单据行号 |
| 20 | fsendpricetaxtotalbase | 发送方单据含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 发送方单据含税金额（本位币） |
| 21 | fsendamountbase | 发送方单据金额（本位币） | numeric | 23 | 10 | √ | 0 | 发送方单据金额（本位币） |
| 22 | fdistributevalue | 分摊权重 | numeric | 23 | 10 | √ | 0 | 分摊权重 |
| 23 | fsettlementsupplier | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 24 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 25 | fbizdept | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 27 | fbizorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | frecievebillid | 承担方单据id | int8 | 64 |  | √ | 0 | 承担方单据id |
| 29 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 30 | fcurrency | 发送方单据结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 31 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 32 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 33 | fallocbaseamount | 分摊金额（本位币） | numeric | 23 | 10 | √ | 0 | 分摊金额（本位币） |
| 34 | fbizoperator | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 35 | falloctaxamount | 分摊含税金额 | numeric | 23 | 10 | √ | 0 | 分摊含税金额 |
| 36 | fbasecurrency | 发送方单据本位币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 37 | frecievebilltype | 承担方单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 38 | fsettlecustomer | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 39 | fsendbilltype | 发送方单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 40 | fsendbillno | 发送方单据编号 | varchar | 80 |  | √ | ' ' | 发送方单据编号 |
| 41 | fsendbillentryid | 发送方单据分录id | int8 | 64 |  | √ | 0 | 发送方单据分录id |
| 42 | fcostdepartment | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | frecievebookdate | 承担方记账日期 | timestamp | 0 |  |  | null | 承担方记账日期 |
| 44 | frecievebillentryid | 承担方单据分录id | int8 | 64 |  | √ | 0 | 承担方单据分录id |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fsendpricetaxtotal | 发送方单据含税金额 | numeric | 23 | 10 | √ | 0 | 发送方单据含税金额 |
| 47 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_salefeeallocentry_rb |  | frecievebillid |
| 2 | idx_cal_salefeeallocentry_f |  | fid |
| 3 | idx_cal_salefeeallocentry_sr |  | fsendbillentryid,frecievebillentryid |
| 4 | pk_cal_salefeeallocentry |  | fentryid |
