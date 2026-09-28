# 检测日志-eafc_inspect_list_log

## 检测日志-主表 tk_eafc_inspect_list_log

- **表名称：** 检测日志-主表
- **表名：** tk_eafc_inspect_list_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fk_eafc_inspecttype | 检测类别 | varchar | 200 |  | √ | ' ' | 检测类别 |
| 6 | fk_eafc_inspector | 检测人 | varchar | 50 |  | √ | ' ' | 检测人 |
| 7 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fk_eafc_inspectfail | 未通过 | int8 | 64 |  |  | null | 未通过 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_eafc_inspect_link | 检测环节 | varchar | 50 |  | √ | ' ' | 检测环节,枚举: 1 :采集环节 2 :归档环节 3 :移交与接收环节 4 :长期保存环节 |
| 12 | fk_eafc_inspectnum | 检测数量 | int8 | 64 |  |  | null | 检测数量 |
| 13 | fk_eafc_inspecttime | 检测时间 | timestamp | 0 |  |  | null | 检测时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fk_eafc_inspect_batchno | 检测批次 | varchar | 50 |  | √ | ' ' | 检测批次 |
| 16 | fk_eafc_inspectpass | 通过 | int8 | 64 |  |  | null | 通过 |
| 17 | fk_eafc_inspectstatus | 检测状态 | varchar | 50 |  | √ | ' ' | 检测状态,枚举: 1 :进行中 2 :已完成 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fk_eafc_arcorg | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_list_log |  | fid |
