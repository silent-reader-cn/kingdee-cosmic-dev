# 发票回收-sim_recycle_log

## 发票回收-主表 t_sim_recycle_log

- **表名称：** 发票回收-主表
- **表名：** t_sim_recycle_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 004 :纸质增值税专用发票 005 :机动车销售统一发票 006 :二手车销售统一发票 007 :增值税普通发票（纸票） 025 :增值税普通发票（卷票） 026 :增值税电子普通发票 028 :增值税电子专用发票 |
| 3 | ftax | 企业信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |
| 4 | fcopies | 回收份数 | int8 | 64 |  | √ | 0 | 回收份数 |
| 5 | fterminalname | 开票终端名称 | varchar | 50 |  | √ | ' ' | 开票终端名称 |
| 6 | fterminal | 开票终端代码 | varchar | 50 |  | √ | ' ' | 开票终端代码 |
| 7 | frecycledate | 回收日期 | timestamp | 0 |  |  | null | 回收日期 |
| 8 | fhandlers | 操作者 | varchar | 50 |  | √ | ' ' | 操作者 |
| 9 | feqinfo | 设备编号 | int8 | 64 |  | √ | 0 | [开票设备 bdm_tax_equipment](../bdm_files/bdm_tax_equipment.md) |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_recycle_log |  | fterminal,fterminalname |
| 2 | pk_sim_recycle_log |  | fid |
