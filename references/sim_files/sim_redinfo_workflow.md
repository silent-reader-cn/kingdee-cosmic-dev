# 发票审批-sim_redinfo_workflow

## 单据体-子表 t_sim_vatinvoice_wf_item

- **表名称：** 单据体-子表
- **表名：** t_sim_vatinvoice_wf_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoicestatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 |
| 3 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftotaltax | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 6 | fissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 7 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 8 | fissuetype | 开票类型 | varchar | 50 |  | √ | ' ' | 开票类型,枚举: 0 :蓝票 1 :红票 |
| 9 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 10 | fbuyername | 购方企业名称 | varchar | 50 |  | √ | ' ' | 购方企业名称 |
| 11 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_vatinvoice_wf_item |  | fentryid |
| 2 | idx_sim_vatinvoice_wf_item |  | finvoicecode,finvoiceno |

---

## 发票审批-主表 t_sim_redinfo_wf

- **表名称：** 发票审批-主表
- **表名：** t_sim_redinfo_wf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fapplyer | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | falltotalpriceandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 6 | fapplynum | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | frebackreason | 理由 | varchar | 50 |  | √ | ' ' | 理由 |
| 9 | fapplyreason | 事由 | varchar | 50 |  | √ | ' ' | 事由 |
| 10 | falltotaltaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 11 | fallftotalamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 12 | fapplytype | 申请类型 | varchar | 50 |  | √ | ' ' | 申请类型,枚举: 1 :发票作废 2 :红字信息表 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_redinfo_wf |  | fbillno |
| 2 | pk_sim_redinfo_wf |  | fid |

---

## 单据体-子表 t_sim_redinfo_wf_item

- **表名称：** 单据体-子表
- **表名：** t_sim_redinfo_wf_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuyertaxno | 购方税号 | varchar | 50 |  | √ | ' ' | 购方税号 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 5 | fhsbz | 是否含税 | varchar | 50 |  | √ | ' ' | 是否含税,枚举: 0 :不含税 1 :含税 |
| 6 | foriginalinvoiceno | 对应蓝票号码 | varchar | 20 |  | √ | ' ' | 对应蓝票号码 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fapplicant | 申请方 | varchar | 50 |  | √ | ' ' | 申请方 |
| 9 | fdecimalfield | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 10 | finfosource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :税局下载 3 :批量导入 4 :API接口 5 :单据开票 |
| 11 | foriginalissuetime | 对应蓝票日期 | timestamp | 0 |  |  | null | 对应蓝票日期 |
| 12 | finvoicetype | 发票种类 | varchar | 50 |  | √ | ' ' | 发票种类,枚举: 028 :电子专用发票 004 :纸质专用发票 |
| 13 | fremainredamount | 剩余可红冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可红冲金额 |
| 14 | foriginalinvoicecode | 对应蓝票代码 | varchar | 20 |  | √ | ' ' | 对应蓝票代码 |
| 15 | finfoserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 16 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 17 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 18 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fsalertaxno | 销方税号 | varchar | 50 |  | √ | ' ' | 销方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_redinfo_wf_item_fk |  | fid |
| 2 | pk_sim_redinfo_wf_item |  | fentryid |
