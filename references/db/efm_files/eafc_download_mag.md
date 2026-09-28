# 下载管理-eafc_download_mag

## 下载管理-主表 tk_eafc_download_mag

- **表名称：** 下载管理-主表
- **表名：** tk_eafc_download_mag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_downloadurl | 下载路径 | varchar | 400 |  | √ | ' ' | 下载路径 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_eafc_taskstatus | 作业状态 | varchar | 50 |  | √ | ' ' | 作业状态,枚举: 1 :执行中 2 :成功 3 :失败 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fk_eafc_opt_user | 操作人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_eafc_work_type | 存储类型 | varchar | 50 |  | √ | ' ' | 存储类型,枚举: 1 :长期存储 2 :临时存储 |
| 10 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 11 | fk_eafc_operation_time | 作业次数 | int8 | 64 |  |  | null | 作业次数 |
| 12 | fk_eafc_affiorg | 所属组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fk_eafc_errmsg | 错误信息 | varchar | 50 |  | √ | ' ' | 错误信息 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fk_eafc_booktype | 机构/问题 | varchar | 50 |  | √ | ' ' | 机构/问题 |
| 16 | fk_eafc_taskprocess | 作业进度 | varchar | 50 |  | √ | ' ' | 作业进度 |
| 17 | fk_eafc_des_status | 状态描述 | varchar | 50 |  | √ | ' ' | 状态描述 |
| 18 | fk_eafc_name | 作业名称 | varchar | 50 |  | √ | ' ' | 作业名称 |
| 19 | fbillno | 作业批次号 | varchar | 30 |  | √ | ' ' | 作业批次号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_download_mag |  | fid |
