# 预缴申请单-tcvat_prepay_application

## 预缴申请单-主表 t_tcvat_prepay_applicate

- **表名称：** 预缴申请单-主表
- **表名：** t_tcvat_prepay_applicate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzzsprepay | 预缴增值税额 | numeric | 23 | 10 | √ | 0 | 预缴增值税额 |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftaxrate | 税率/征收率 | varchar | 50 |  | √ | ' ' | 税率/征收率,枚举: 0.03 :3% 0.05 :5% 0.09 :9% |
| 5 | fprepayrate | 预征率 | varchar | 50 |  | √ | ' ' | 预征率,枚举: 0.02 :2% 0.03 :3% 0.05 :5% |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsalesamount | 本次应税销售额（含税） | numeric | 23 | 10 | √ | 0 | 本次应税销售额（含税） |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftaxbase | 增值税计税基础 | numeric | 23 | 10 | √ | 0 | 增值税计税基础 |
| 10 | fdeductionamount | 本次分包扣除额（含税） | numeric | 23 | 10 | √ | 0 | 本次分包扣除额（含税） |
| 11 | fenddate | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 12 | fpredeductamount | 预收款扣除额 | numeric | 23 | 10 | √ | 0 | 预收款扣除额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fprepaystatus | 预缴状态 | varchar | 50 |  | √ | ' ' | 预缴状态,枚举: 2 :未预缴 3 :待预缴 4 :已预缴 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcrossnumber | 跨区报验管理编号 | varchar | 50 |  | √ | ' ' | 跨区报验管理编号 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fdecimalfield | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 22 | fstartdate | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 23 | fprepayproject | 预缴项目编码 | int8 | 64 |  | √ | 0 | 预缴项目信息 tcvat_prepay_project_info |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fdeclarenumber | 预缴申报表编号 | varchar | 50 |  | √ | ' ' | 预缴申报表编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_prepay_app_01 |  | forgid,fprepayproject,fstartdate |
| 2 | pk_tcvat_prepay_applicate |  | fid |

---

## 应税销售额明细单据体-子表 t_tcvat_prepay_sales

- **表名称：** 应税销售额明细单据体-子表
- **表名：** t_tcvat_prepay_sales

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsinvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 3 | fsremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fstaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fstotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 6 | fsadvancepaymentstatus | 预缴状态 | varchar | 50 |  | √ | ' ' | 预缴状态,枚举: 10 :不预缴 20 :未预缴 30 :待预缴 40 :已预缴 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsinvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 9 | fstotaltax | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 10 | fsinvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 11 | fsbuyername | 购方企业名称 | varchar | 50 |  | √ | ' ' | 购方企业名称 |
| 12 | fsinvoiceid | 发票id | int8 | 64 |  | √ | 0 | 发票id |
| 13 | fsinvoicetype | 发票种类 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 14 | fsissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_prepay_sales |  | fentryid |
| 2 | idx_tcvat_prepay_sales_fk |  | fid |

---

## 预缴其他税种单据体-子表 t_tcvat_prepay_other

- **表名称：** 预缴其他税种单据体-子表
- **表名：** t_tcvat_prepay_other

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasetax | 计税基础 | numeric | 23 | 10 | √ | 0 | 计税基础 |
| 3 | ftaxamount | 预缴其他税种税额 | numeric | 23 | 10 | √ | 0 | 预缴其他税种税额 |
| 4 | frate | 税率/征收率/预征率 | varchar | 50 |  | √ | ' ' | 税率/征收率/预征率 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: tccit :企业所得税 edufjsf :教育费附加 localedufjsfs :地方教育附加费 personaltax :个人所得税 yhs :印花税 cswhjss :城市维护建设税 ghjf :工会经费 hjbhs :环境保护税 sljsjj :水利建设基金 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_prepay_other_fk |  | fid |
| 2 | pk_tcvat_prepay_other |  | fentryid |

---

## 分包扣除额明细单据体-子表 t_tcvat_prepay_deduction

- **表名称：** 分包扣除额明细单据体-子表
- **表名：** t_tcvat_prepay_deduction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdinvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 3 | fdtotaltaxamount | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 4 | fdtotaldeduct | 累计扣除额 | numeric | 23 | 10 | √ | 0 | 累计扣除额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 7 | fdinvoiceid | 发票id | int8 | 64 |  | √ | 0 | 发票id |
| 8 | fdsalername | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 9 | fsinvoiceno11 | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 10 | fdinvoicetype | 发票种类 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 11 | fdremaindeduct | 剩余扣除额 | numeric | 23 | 10 | √ | 0 | 剩余扣除额 |
| 12 | fdremark | 备注 | varchar | 350 |  | √ | ' ' | 备注 |
| 13 | fdcurrentdeduct | 本次扣除额 | numeric | 23 | 10 | √ | 0 | 本次扣除额 |
| 14 | fdavaildeduct | 可扣除额 | numeric | 23 | 10 | √ | 0 | 可扣除额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fmaingoodsname | 商品名称 | varchar | 120 |  | √ | ' ' | 商品名称 |
| 17 | fdinvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 18 | fdtotalamount | 价税合计金额 | numeric | 23 | 10 | √ | 0 | 价税合计金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_prepay_deduction |  | fentryid |
| 2 | idx_tcvat_prepay_dedu_fk |  | fid |
