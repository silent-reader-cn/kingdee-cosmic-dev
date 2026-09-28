# 质检检测日志-eafc_standard_inspect_log

## 质检检测日志-主表 tk_eafc_s_inspect_log

- **表名称：** 质检检测日志-主表
- **表名：** tk_eafc_s_inspect_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_eafc_completeness_desc | 完整性检测失败描述 | varchar | 200 |  | √ | ' ' | 完整性检测失败描述 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fk_eafc_file_sign | 题名 | varchar | 50 |  | √ | ' ' | 题名 |
| 8 | fk_eafc_inspect_usability | 可用性检测 | varchar | 50 |  | √ | ' ' | 可用性检测,枚举: 1 :通过 2 :不通过 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_eafc_batchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 12 | fk_eafc_inspect_trust | 真实性检测 | varchar | 50 |  | √ | ' ' | 真实性检测,枚举: 1 :通过 2 :不通过 |
| 13 | fk_eafc_file_code | 文件编码 | varchar | 50 |  | √ | ' ' | 文件编码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fk_eafc_inspect_complete | 完整性检测 | varchar | 50 |  | √ | ' ' | 完整性检测,枚举: 1 :通过 2 :不通过 |
| 16 | fk_eafc_combofield | 质检环节 | varchar | 50 |  | √ | ' ' | 质检环节,枚举: 1 :采集环节 2 :归档环节 3 :移交与接收环节 4 :长期保存环节 |
| 17 | fk_eafc_uniqueid | 会计资料唯一ID | varchar | 50 |  | √ | ' ' | 会计资料唯一ID |
| 18 | fk_eafc_base_data_type | 会计资料类型 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 19 | fk_eafc_inspect_safety | 安全性检测 | varchar | 50 |  | √ | ' ' | 安全性检测,枚举: 1 :通过 2 :不通过 |
| 20 | fk_eafc_textfield1 | 真实性检测失败描述 | varchar | 200 |  | √ | ' ' | 真实性检测失败描述 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fk_eafc_usability_desc | 可用性检测失败描述 | varchar | 200 |  | √ | ' ' | 可用性检测失败描述 |
| 24 | fk_eafc_safety_desc | 安全性检测失败描述 | varchar | 50 |  | √ | ' ' | 安全性检测失败描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_s_inspect_log |  | fid |
