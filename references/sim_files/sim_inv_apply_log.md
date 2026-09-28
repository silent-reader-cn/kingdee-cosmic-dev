# 发票申领-sim_inv_apply_log

## 发票申领-主表 t_sim_inv_apply_log

- **表名称：** 发票申领-主表
- **表名：** t_sim_inv_apply_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftextfield1 | 预申领编号 | varchar | 50 |  | √ | ' ' | 预申领编号 |
| 3 | fdealtime | fdealtime | timestamp | 0 |  |  | null |  |
| 4 | fapplydate | 申领时间 | timestamp | 0 |  |  | null | 申领时间 |
| 5 | fdispose | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: 0 :申领中 1 :成功 2 :失败 3 :撤销 |
| 6 | fno | 申领序号 | varchar | 40 |  | √ | ' ' | 申领序号 |
| 7 | fagent | 经办人姓名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fdisposedate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | fmsg | 申领说明 | varchar | 255 |  | √ | ' ' | 申领说明 |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fconductor | fconductor | int8 | 64 |  | √ | 0 |  |
| 12 | fnum | 申领数量 | int8 | 64 |  | √ | 0 | 申领数量 |
| 13 | finvoicekindcode | 发票种类代码 | varchar | 20 |  | √ | ' ' | 发票种类代码 |
| 14 | ftype | 申领方式 | varchar | 30 |  | √ | ' ' | 申领方式,枚举: 1 :自行领取 2 :快递配送 |
| 15 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 004 :纸质增值税专用发票 005 :机动车销售统一发票 006 :二手车销售统一发票 007 :增值税普通发票（纸票） 025 :增值税普通发票（卷票） 026 :增值税电子普通发票 028 :增值税电子专用发票 |
| 16 | ftax | 纳税人名称 | int8 | 64 |  | √ | 0 | 企业基础信息 bdm_enterprise_baseinfo |
| 17 | fapplypurchasequantity | fapplypurchasequantity | int8 | 64 |  | √ | 0 |  |
| 18 | fdisposemsg | 处理信息 | varchar | 100 |  | √ | ' ' | 处理信息 |
| 19 | finvoicekindname | 发票种类名称 | varchar | 20 |  | √ | ' ' | 发票种类名称 |
| 20 | fterminal | 自动分发终端 | varchar | 50 |  | √ | ' ' | 自动分发终端 |
| 21 | fapplytype | 结果确认标志 | varchar | 30 |  | √ | ' ' | 结果确认标志,枚举: 0 :未确认 1 :已确认 |
| 22 | feqinfo | 设备编号 | int8 | 64 |  | √ | 0 | 开票设备 bdm_tax_equipment |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_inv_apply_log |  | fid |
| 2 | idx_sim_inv_apply_log |  | ftax |

---

## 申领结果-子表 t_sim_apply_result

- **表名称：** 申领结果-子表
- **表名：** t_sim_apply_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fendnum | 终止号码 | int8 | 64 |  | √ | 0 | 终止号码 |
| 3 | fcopies | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 6 | fstartnum | 起始号码 | int8 | 64 |  | √ | 0 | 起始号码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_apply_result |  | fid |
| 2 | pk_sim_apply_result |  | fentryid |

---

## 配送信息盒子-子表 t_sim_delivery_msg

- **表名称：** 配送信息盒子-子表
- **表名：** t_sim_delivery_msg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelnumber | 固定电话 | varchar | 50 |  | √ | ' ' | 固定电话 |
| 3 | fdelremork | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fdelname | 收件人姓名 | varchar | 50 |  | √ | ' ' | 收件人姓名 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdeladdress | 收件地址 | varchar | 50 |  | √ | ' ' | 收件地址 |
| 7 | fdelphone | 移动电话 | varchar | 50 |  | √ | ' ' | 移动电话 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdelpostcode | 邮编 | varchar | 50 |  | √ | ' ' | 邮编 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_delivery_msg_fk |  | fid |
| 2 | pk_sim_delivery_msg |  | fentryid |
