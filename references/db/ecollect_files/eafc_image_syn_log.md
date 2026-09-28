# 影像调用日志-eafc_image_syn_log

## 影像调用日志-主表 tk_eafc_image_syn_log

- **表名称：** 影像调用日志-主表
- **表名：** tk_eafc_image_syn_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_image_no | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :失败 1 :成功 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 调用组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fk_eafc_system_name | 系统名称 | varchar | 100 |  | √ | ' ' | 系统名称 |
| 8 | fk_eafc_invoice_num | 获取发票数 | int8 | 64 |  |  | null | 获取发票数 |
| 9 | fk_eafc_attach_num | 获取附件数 | int8 | 64 |  |  | null | 获取附件数 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fk_eafc_general_org | 调用全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_eafc_call_type | 调用方式 | varchar | 50 |  | √ | ' ' | 调用方式,枚举: 1 :手工同步 2 :自动获取 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fk_eafc_call_result | 调用结果 | varchar | 200 |  | √ | ' ' | 调用结果 |
| 18 | fk_eafc_arcorg | 调用归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_image_syn_log |  | fid |
