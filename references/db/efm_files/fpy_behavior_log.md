# 行为日志-fpy_behavior_log

## 行为日志-主表 tk_fpy_behavior_log

- **表名称：** 行为日志-主表
- **表名：** tk_fpy_behavior_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_userid | 执行人id | varchar | 50 |  | √ | ' ' | 执行人id |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 5 | fk_eafc_file_sign | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 6 | fk_eafc_executor_arcorg | 执行人归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fk_eafc_file_code | 文件编码 | varchar | 100 |  | √ | ' ' | 文件编码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fk_eafc_bill_relationid | 文件id | int8 | 64 |  | √ | 0 | 文件id |
| 11 | fk_eafc_uniqueid | 文件唯一编号 | varchar | 100 |  | √ | ' ' | 文件唯一编号 |
| 12 | fk_eafc_data_stauts | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :已采集 2 :待组卷 3 :已组卷 4 :归档中 5 :已归档 9 :被移除 11 :异常 12 :检测中 |
| 13 | fbsidentifier | 业务识别符 | varchar | 50 |  | √ | ' ' | 业务识别符 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 16 | fk_eafc_business | 分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 17 | fk_eafc_behavior_time | 行为时间 | timestamp | 0 |  |  | null | 行为时间 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fk_eafc_behavior | 业务行为 | varchar | 50 |  | √ | ' ' | 业务行为,枚举: 1 :签收/形成 2 :接收检查 3 :归档文件调整 4 :立卷 5 :归档检查 6 :归档 7 :存储 8 :编制 9 :修订 10 :审核 11 :过账 12 :采集 13 :创建 14 :修改 15 :制单 16 :记账 17 :出纳 18 :复核 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fbehaviorbasis | 行为依据 | varchar | 255 |  | √ | ' ' | 行为依据 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fdescription | 行为描述 | varchar | 255 |  | √ | ' ' | 行为描述 |
| 25 | fk_eafc_user_org | 执行人所属组织 | varchar | 225 |  | √ | ' ' | 执行人所属组织 |
| 26 | fk_eafc_behavior_source | 行为来源 | varchar | 50 |  | √ | ' ' | 行为来源 |
| 27 | fk_eafc_executor_user | 执行人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fuserposition | 个人职位 | varchar | 255 |  | √ | ' ' | 个人职位 |
| 29 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fk_eafc_user_name | 执行人 | varchar | 50 |  | √ | ' ' | 执行人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_behavior_lo |  | fid |
| 2 | idx__tk_fpy_behavior_log_r |  | fk_eafc_bill_relationid |
| 3 | idx__tk_fpy_behavior_log_r_b |  | fk_eafc_bill_relationid,fk_eafc_behavior |
| 4 | idx__tk_fpy_behavior_log_o_r_b |  | fk_eafc_arcorg,fk_eafc_bill_relationid,fk_eafc_behavior |
