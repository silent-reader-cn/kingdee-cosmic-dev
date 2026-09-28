# 联动付款日志-mpm_calcamount_log

## 付款单据体-子表 t_mpm_calamtlogpayentry

- **表名称：** 付款单据体-子表
- **表名：** t_mpm_calamtlogpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrency_pay | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fpaybillno | 付款单据编号 | varchar | 255 |  | √ | ' ' | 付款单据编号 |
| 4 | fpurorderid_pay | 采购订单id | int8 | 64 |  | √ | 0 | 采购订单id |
| 5 | fpaybillid | 付款单据id | int8 | 64 |  | √ | 0 | 付款单据id |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpaybillstatus | 付款单据状态 | varchar | 50 |  | √ | ' ' | 付款单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已付款 E :付款处理中 F :银行退票 G :已退单 H :已作废 I :退款 J :票据处理中 |
| 8 | fpayentryid | 付款单分录id | int8 | 64 |  | √ | 0 | 付款单分录id |
| 9 | fprojectid_pay | 项目id | int8 | 64 |  | √ | 0 | 项目id |
| 10 | frefundamt | 退款金额 | numeric | 23 | 10 | √ | 0 | 退款金额 |
| 11 | fpayentryseq | 付款单分录序号 | int4 | 32 |  | √ | 0 | 付款单分录序号 |
| 12 | fpayableamt | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_calamtlogpayentry |  | fentryid |
| 2 | idx_mpm_calamtlogpay_fk |  | fid |

---

## 应收单据体-子表 t_mpm_calamtlogadventry

- **表名称：** 应收单据体-子表
- **表名：** t_mpm_calamtlogadventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrency_recadvan | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 4 | frecadbillobject | 应收单据实体 | varchar | 80 |  | √ | ' ' | 应收单据实体,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frecadbillid | 应收单据id | int8 | 64 |  | √ | 0 | 应收单据id |
| 7 | frelrecamount | 关联收款金额 | numeric | 23 | 10 | √ | 0 | 关联收款金额 |
| 8 | frecadbillno | 应收单据编号 | varchar | 255 |  | √ | ' ' | 应收单据编号 |
| 9 | frecadvancerate | 应收比例(%) | numeric | 15 | 2 | √ | 0 | 应收比例(%) |
| 10 | frecamount | 已收金额 | numeric | 23 | 10 | √ | 0 | 已收金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fprojectid_recad | 项目id | int8 | 64 |  | √ | 0 | 项目id |
| 13 | frecadvanceamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 14 | frecplanprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_calamtlogadv_fk |  | fid |
| 2 | pk_mpm_calamtlogadventry |  | fentryid |

---

## 联动付款日志-主表 t_mpm_calamtlog

- **表名称：** 联动付款日志-主表
- **表名：** t_mpm_calamtlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fopbillobject | 操作单据实体 | varchar | 80 |  | √ | ' ' | 操作单据实体,枚举: ap_payapply :付款申请单 cas_paybill :付款单 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: submit :提交 audit :审核 pay :提交银企 |
| 9 | fbillno | 日志编号 | varchar | 80 |  | √ | ' ' | 日志编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_calamtlog_fb |  | fbillno |
| 2 | pk_mpm_calamtlog |  | fid |

---

## 收款单据体-子表 t_mpm_calamtlogrecentry

- **表名称：** 收款单据体-子表
- **表名：** t_mpm_calamtlogrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecentryseq | 收款单分录序号 | int4 | 32 |  | √ | 0 | 收款单分录序号 |
| 3 | frecbillno | 收款单编号 | varchar | 255 |  | √ | ' ' | 收款单编号 |
| 4 | fe_refundamt | 退款金额 | numeric | 23 | 10 | √ | 0 | 退款金额 |
| 5 | fe_receivableamt | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frecentryid | 收款单分录id | int8 | 64 |  | √ | 0 | 收款单分录id |
| 8 | fcurrency_rec | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | frecbillid | 收款单id | int8 | 64 |  | √ | 0 | 收款单id |
| 11 | fprojectid_rec | 项目id | int8 | 64 |  | √ | 0 | 项目id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_calamtlogrecentry |  | fentryid |
| 2 | idx_mpm_calamtlogrec_fk |  | fid |

---

## 操作单据单据体-子表 t_mpm_calamtlogopentry

- **表名称：** 操作单据单据体-子表
- **表名：** t_mpm_calamtlogopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanprojrecamount | 项目采购服务确认金额 | numeric | 23 | 10 | √ | 0 | 项目采购服务确认金额 |
| 3 | ffinalallowamount | 总允付金额（最终） | numeric | 23 | 10 | √ | 0 | 总允付金额（最终） |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fopamount | 本单据付款金额 | numeric | 23 | 10 | √ | 0 | 本单据付款金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frecrate | 收款比例(%) | numeric | 23 | 2 | √ | 0 | 收款比例(%) |
| 8 | fremainamount | 剩余允付金额 | numeric | 23 | 10 | √ | 0 | 剩余允付金额 |
| 9 | frectotalamount | 收款总金额 | numeric | 23 | 10 | √ | 0 | 收款总金额 |
| 10 | fpurorderbillno | 采购订单编号 | varchar | 255 |  | √ | ' ' | 采购订单编号 |
| 11 | fpayrate | 允付比例(%) | numeric | 23 | 2 | √ | 0 | 允付比例(%) |
| 12 | fcheckresult | 校验结果 | bpchar | 1 |  | √ | ' ' | 校验结果,枚举: Y :通过 N :不通过 |
| 13 | fusedamount | 已占用付款金额 | numeric | 23 | 10 | √ | 0 | 已占用付款金额 |
| 14 | fcurrency_op | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fallowamount | 总允付金额（根据允付比例） | numeric | 23 | 10 | √ | 0 | 总允付金额（根据允付比例） |
| 16 | fpurorderid | 采购订单id | int8 | 64 |  | √ | 0 | 采购订单id |
| 17 | foppayamount | 本次操作付款金额 | numeric | 23 | 10 | √ | 0 | 本次操作付款金额 |
| 18 | fopbillno | 操作单据编号 | varchar | 255 |  | √ | ' ' | 操作单据编号 |
| 19 | frecadvantotalamt | 应收总金额 | numeric | 23 | 10 | √ | 0 | 应收总金额 |
| 20 | fopbillid | 操作单据id | int8 | 64 |  | √ | 0 | 操作单据id |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_calamtlogop_fk |  | fid |
| 2 | pk_mpm_calamtlogopentry |  | fentryid |

---

## 付款申请单据体-子表 t_mpm_calamtlogapplyentry

- **表名称：** 付款申请单据体-子表
- **表名：** t_mpm_calamtlogapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurorderid_apply | 采购订单id | int8 | 64 |  | √ | 0 | 采购订单id |
| 3 | fapplyentryseq | 付款申请单分录序号 | int4 | 32 |  | √ | 0 | 付款申请单分录序号 |
| 4 | fapplybillstatus | 付款申请单据状态 | varchar | 50 |  | √ | ' ' | 付款申请单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 5 | fapplyentryid | 付款申请单分录id | int8 | 64 |  | √ | 0 | 付款申请单分录id |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fprojectid_apply | 项目id | int8 | 64 |  | √ | 0 | 项目id |
| 8 | fapplybillid | 付款单据id | int8 | 64 |  | √ | 0 | 付款单据id |
| 9 | fcurrency_apply | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fapplybillno | 付款单据编号 | varchar | 255 |  | √ | ' ' | 付款单据编号 |
| 11 | fapprovedseleamt | 核准金额 | numeric | 23 | 10 | √ | 0 | 核准金额 |
| 12 | fpaidamt | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_calamtlogapplyentry |  | fentryid |
| 2 | idx_mpm_calamtlogapply_fk |  | fid |

---

## 里程碑单据体-子表 t_mpm_calamtlogtaskentry

- **表名称：** 里程碑单据体-子表
- **表名：** t_mpm_calamtlogtaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 3 | fprojectid_task | 项目id | int8 | 64 |  | √ | 0 | 项目id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpurorderid_task | 采购订单id | int8 | 64 |  | √ | 0 | 采购订单id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmilestonetaskid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 8 | fprojectphaseid | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_calamtlogtask_fk |  | fid |
| 2 | pk_mpm_calamtlogtaskentry |  | fentryid |
