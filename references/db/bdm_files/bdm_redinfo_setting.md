# 审批配置单据(弃用)-bdm_redinfo_setting

## 审批配置单据(弃用)-主表 t_bdm_redinfo_setting

- **表名称：** 审批配置单据(弃用)-主表
- **表名：** t_bdm_redinfo_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_api_interface | api接口 | bpchar | 1 |  | √ | ' ' | api接口 |
| 3 | finvcancelapproval | 发票作废审批 | bpchar | 1 |  | √ | ' ' | 发票作废审批 |
| 4 | finvoiceapproval | 开票审批 | bpchar | 1 |  | √ | ' ' | 开票审批 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | 企业管理 bdm_org |
| 7 | f_bill_split_merge | 单据拆合 | bpchar | 1 |  | √ | ' ' | 单据拆合 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | f_batch_import | 批量导入 | bpchar | 1 |  | √ | ' ' | 批量导入 |
| 10 | fbillapproval | 单据审批 | bpchar | 1 |  | √ | ' ' | 单据审批 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | f_manual_new | 手工新增 | bpchar | 1 |  | √ | ' ' | 手工新增 |
| 14 | f_redinfo_approval | 红字信息表审批 | bpchar | 1 |  | √ | ' ' | 红字信息表审批 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_redinfo_setting |  | fid |
| 2 | idx_bdm_redinfo_setting |  | forg |
