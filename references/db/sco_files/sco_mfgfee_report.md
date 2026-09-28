# 制造费用归集报告-sco_mfgfee_report

## 单据体-子表 t_sco_mfgfee_configentry

- **表名称：** 单据体-子表
- **表名：** t_sco_mfgfee_configentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | faccountorgid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 5 | fsrcbill | 来源单据 | varchar | 30 |  | √ | ' ' | 来源单据,枚举: gl_voucher :凭证 ap_process :暂估应付单/财务应付单（取加工费） ap_freight :暂估应付单/财务应付单（取运费） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | faccountbook | 来源会计账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfee_configentry |  | fentryid |
| 2 | idx_sco_mfgfee_configentry_fid |  | fid |

---

## 制造费用归集报告-主表 t_sco_mfgfee_report

- **表名称：** 制造费用归集报告-主表
- **表名：** t_sco_mfgfee_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferror | 存在差异或异常 | bpchar | 1 |  | √ | '0' | 存在差异或异常 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fappnum | 业务标识 | varchar | 10 |  | √ | ' ' | 业务标识,枚举: sca :标准成本 aca :实际成本 |
| 10 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_mfgfee_report |  | fid |
| 2 | idx_sco_mfgfee_report_forgid |  | forgid |

---

## 单据体-子表 t_sco_mfgfee_stepentry

- **表名称：** 单据体-子表
- **表名：** t_sco_mfgfee_stepentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 详细步骤 | varchar | 50 |  | √ | ' ' | 详细步骤 |
| 3 | ftip | 提示 | varchar | 255 |  | √ | ' ' | 提示 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresult | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :通过 6 :不通过 7 :提醒 |
| 6 | fcostime | 耗时（毫秒） | varchar | 50 |  | √ | ' ' | 耗时（毫秒） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftip_tag | 提示_详情 | text | 0 |  |  | null | 提示_详情 |
| 9 | fcheckdesc | 归集结果 | varchar | 255 |  | √ | ' ' | 归集结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgfee_stepentry_fid |  | fid |
| 2 | pk_sco_mfgfee_stepentry |  | fentryid |
