# 研发公共费用分摊记录-rdem_costalloc_result

## 研发公共费用分摊记录-主表 t_pca_costalloc_result

- **表名称：** 研发公共费用分摊记录-主表
- **表名：** t_pca_costalloc_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbillfrom | 来源模块 | varchar | 50 |  | √ | ' ' | 来源模块,枚举: fi_gl :总账 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | falloctype | 分摊方式 | varchar | 50 |  | √ | ' ' | 分摊方式,枚举: manual_alloc :手工分摊 auto_alloc :自动分摊 reverse_alloc :自动冲销 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcostaccount | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 11 | fallocstandard | 分摊标准 | varchar | 50 |  | √ | ' ' | 分摊标准,枚举: report_hour :汇报工时 custom_alloc :自定义分配 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 14 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 15 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costalloc_result |  | fid |
| 2 | idx_pca_costalloc_result_billno |  | fbillno |

---

## 分摊明细-子表 t_pca_costalloc_result_e

- **表名称：** 分摊明细-子表
- **表名：** t_pca_costalloc_result_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubject | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 3 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 4 | fcostsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 5 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fallocamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | ftaskname | 项目任务名称 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 10 | fsubjectbaltype | 金额类型 | varchar | 50 |  | √ | ' ' | 金额类型,枚举: 1 :实际损益发生额 2 :借方 3 :贷方 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillnumber | 单据号 | varchar | 255 |  | √ | ' ' | 单据号 |
| 13 | fprojectname | fprojectname | int8 | 64 |  | √ | 0 |  |
| 14 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 15 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fprojecttotalcost | 项目总成本 | numeric | 23 | 10 | √ | 0 | 项目总成本 |
| 17 | fcostelement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 18 | ffromentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fallocstandardvalue | 分摊标准值 | numeric | 23 | 10 | √ | 0 | 分摊标准值 |
| 21 | fcostobject | 核算对象 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costalloc_result_e |  | fentryid |
| 2 | idx_pca_costalloc_result_e_pk |  | fid |
