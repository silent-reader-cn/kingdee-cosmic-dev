# 送检批次-eafc_inspect_batch

## 送检批次-主表 tk_eafc_inspect_batch

- **表名称：** 送检批次-主表
- **表名：** tk_eafc_inspect_batch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fk_eafc_xml_name | xml文件名 | varchar | 500 |  | √ | ' ' | xml文件名 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_eafc_period | 期属 | timestamp | 0 |  |  | null | 期属 |
| 7 | fk_eafc_xml_path | xml的存储路径 | varchar | 500 |  | √ | ' ' | xml的存储路径 |
| 8 | fk_eafc_datasource | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 9 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fk_eafc_xml_type | xml类型 | varchar | 50 |  | √ | ' ' | xml类型,枚举: 1 :addnew 2 :update 3 :delete |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 15 | fk_eafc_is_delete | 是否删除 | varchar | 50 |  | √ | ' ' | 是否删除,枚举: 1 :可用 2 :已删除 |
| 16 | fk_eafc_inspect_status | 检测状态 | varchar | 50 |  | √ | ' ' | 检测状态,枚举: 0 :未检测 1 :已检测 |
| 17 | fk_eafc_business_type | 业务类型 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_batch |  | fid |
