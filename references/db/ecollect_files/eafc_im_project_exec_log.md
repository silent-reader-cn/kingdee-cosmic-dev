# 资料捕获-eafc_im_project_exec_log

## 资料捕获-主表 tk_eafc_im_proj_exec_log

- **表名称：** 资料捕获-主表
- **表名：** tk_eafc_im_proj_exec_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  | √ | 0 | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fk_eafc_fail_count | 失败数 | int8 | 64 |  |  | null | 失败数 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 7 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fk_eafc_total_count | 应归数 | int8 | 64 |  |  | null | 应归数 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 11 | fk_eafc_sucess_count | 采集数 | int8 | 64 |  |  | null | 采集数 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fk_eafc_period | 归档期间 | varchar | 50 |  | √ | ' ' | 归档期间 |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fk_eafc_project_name | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 18 | fk_eafc_content | 归档内容 | int8 | 64 |  |  | null | [集成内容 eafc_im_content](../ecollect_files/eafc_im_content.md) |
| 19 | fk_eafc_exec_status | 归档状态 | varchar | 50 |  | √ | ' ' | 归档状态,枚举: 0 :待解析 1 :采集失败 2 :已解析 3 :采集中 4 :待采集 5 :已完成 6 :待退回 7 :退回中 8 :已退回 9 :部分退回 10 :退回失败 11 :退回成功 12 :待入库 13 :入库中 14 :检测中 15 :入库失败 16 :已终止 |
| 20 | fk_eafc_category_name | 方案分类名称 | varchar | 50 |  | √ | ' ' | 方案分类名称 |
| 21 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 22 | fk_eafc_exec_progress | 进度 | varchar | 50 |  | √ | ' ' | 进度 |
| 23 | fk_eafc_project | 方案 | int8 | 64 |  |  | null | [集成方案 eafc_im_project](../ecollect_files/eafc_im_project.md) |
| 24 | fk_eafc_content_name | 归档内容名称 | varchar | 50 |  | √ | ' ' | 归档内容名称 |
| 25 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_im_proj_exec_log |  | fid |
