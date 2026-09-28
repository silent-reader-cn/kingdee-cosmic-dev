# 移交任务监控-eafc_deliver_task

## 单据体-子表 tk_eafc_deliver_task_file

- **表名称：** 单据体-子表
- **表名：** tk_eafc_deliver_task_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_feedback_detail_tag | 反馈接口返回详情_详情 | text | 0 |  |  | null | 反馈接口返回详情_详情 |
| 3 | fk_eafc_file_size | 文件大小 | varchar | 50 |  | √ | ' ' | 文件大小 |
| 4 | fk_eafc_response_tag | 通知接口返回详情_详情 | text | 0 |  |  | null | 通知接口返回详情_详情 |
| 5 | fk_eafc_feedback_detail | 反馈接口返回详情 | varchar | 255 |  | √ | ' ' | 反馈接口返回详情 |
| 6 | fk_eafc_file_name | 文件名称 | varchar | 50 |  | √ | ' ' | 文件名称 |
| 7 | fk_eafc_response | 通知接口返回详情 | varchar | 255 |  | √ | ' ' | 通知接口返回详情 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fk_eafc_req_id | 请求id | varchar | 100 |  | √ | ' ' | 请求id |
| 10 | fk_eafc_file_address | 接收方文件地址 | varchar | 200 |  | √ | ' ' | 接收方文件地址 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_task_file_reqid |  | fk_eafc_req_id |
| 2 | pk_eafc_deliver_task_file |  | fentryid |

---

## 单据体-子表 tk_eafc_deliver_task_item

- **表名称：** 单据体-子表
- **表名：** tk_eafc_deliver_task_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_period | 属期 | timestamp | 0 |  |  | null | 属期 |
| 3 | fk_eafc_book_type | 机构问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fk_eafc_file_sign | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 6 | fk_eafc_relation_id | 文件检索id | varchar | 50 |  | √ | ' ' | 文件检索id |
| 7 | fk_eafc_file_code | 文件编号 | varchar | 100 |  | √ | ' ' | 文件编号 |
| 8 | fk_eafc_entity_status | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 |
| 9 | fk_eafc_archivenum | 档号 | varchar | 100 |  | √ | ' ' | 档号 |
| 10 | fk_eafc_shelf_location | 存储位置 | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fk_eafc_business_type | 分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 13 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_deliver_task_item |  | fentryid |

---

## 移交任务监控-主表 tk_eafc_deliver_task

- **表名称：** 移交任务监控-主表
- **表名：** tk_eafc_deliver_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_execution_time | 执行耗时 | varchar | 50 |  | √ | ' ' | 执行耗时 |
| 3 | fk_eafc_test_desc | 检测状态描述 | varchar | 100 |  | √ | ' ' | 检测状态描述 |
| 4 | fk_eafc_deliver_user | 移交人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fk_eafc_book_type | 机构问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 6 | fk_eafc_modifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fk_eafc_task_no | 任务单号 | varchar | 50 |  | √ | ' ' | 任务单号 |
| 8 | fk_eafc_start_time | 移交开始时间 | timestamp | 0 |  |  | null | 移交开始时间 |
| 9 | fk_eafc_volume_relationid | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 10 | fk_eafc_status | 移交任务状态 | varchar | 50 |  | √ | ' ' | 移交任务状态,枚举: 0 :待移交 1 :移交中 2 :移交成功 3 :移交失败 |
| 11 | fk_eafc_description | 移交内容描述 | varchar | 255 |  | √ | ' ' | 移交内容描述 |
| 12 | fk_eafc_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 13 | fk_eafc_deliver_type | 移交类型 | varchar | 50 |  | √ | ' ' | 移交类型,枚举: 1 :对内移交-综合档案（案卷级） 2 :对内移交-综合档案（文件级） |
| 14 | fk_eafc_reason | 原因描述 | varchar | 1000 |  | √ | ' ' | 原因描述 |
| 15 | fk_eafc_deliver_mode | 移交方式 | varchar | 50 |  | √ | ' ' | 移交方式,枚举: 1 :在线移交 2 :手动下载 |
| 16 | fk_eafc_apply_no | 关联申请单号 | varchar | 50 |  | √ | ' ' | 关联申请单号 |
| 17 | fk_eafc_total_size | 总文件大小 | varchar | 50 |  | √ | ' ' | 总文件大小 |
| 18 | fk_eafc_modifier | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fk_eafc_arcorg | 移交组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 20 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 21 | fk_eafc_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_deliver_task_apply |  | fk_eafc_apply_no |
| 2 | pk_eafc_deliver_task |  | fid |
| 3 | idx_eafc_deliver_task_relationid |  | fk_eafc_volume_relationid |
