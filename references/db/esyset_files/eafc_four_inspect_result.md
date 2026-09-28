# 四性检测方案结果-eafc_four_inspect_result

## 四性检测方案结果-主表 tk_eafc_inspect_result

- **表名称：** 四性检测方案结果-主表
- **表名：** tk_eafc_inspect_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_check_type | 检测类型 | varchar | 50 |  | √ | ' ' | 检测类型,枚举: 1 :自动检测 2 :手动检测 |
| 3 | fk_eafc_inspector | fk_eafc_inspector | int8 | 64 |  |  | null |  |
| 4 | forgid | 检测组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fk_eafc_inspect_time | fk_eafc_inspect_time | timestamp | 0 |  |  | null |  |
| 6 | fk_eafc_result_warn_level | 检测结果警示级别 | varchar | 50 |  | √ | ' ' | 检测结果警示级别,枚举: 1 :严格管控(红) 2 :严重提示(橙色) 3 :轻度提示(绿) 0 :全部检测通过(绿) |
| 7 | fk_eafc_inspect_range | fk_eafc_inspect_range | varchar | 50 |  | √ | ' ' |  |
| 8 | fk_eafc_inspect_proc | fk_eafc_inspect_proc | varchar | 50 |  | √ | ' ' |  |
| 9 | fk_fpy_status | 检测状态 | varchar | 50 |  | √ | ' ' | 检测状态,枚举: 1 :检测中 2 :检测成功 3 :检测失败 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_fpy_report | 检测报告 | varchar | 500 |  |  | ' ' | 检测报告 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 批次号 | varchar | 100 |  | √ | ' ' | 批次号 |
| 14 | fk_eafc_qualified | fk_eafc_qualified | varchar | 50 |  | √ | ' ' |  |
| 15 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 检测时间 | timestamp | 0 |  |  | null | 检测时间 |
| 18 | fk_eafc_inspect_config | fk_eafc_inspect_config | int8 | 64 |  |  | null |  |
| 19 | fk_eafc_inspect_schema | 检测方案 | int8 | 64 |  |  | null | [四性检测配置 eafc_inspect_schema](../esyset_files/eafc_inspect_schema.md) |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fk_eafc_manual_items | 人工检测项 | varchar | 50 |  | √ | ' ' | 人工检测项 |
| 22 | fk_eafc_inspect_explain | fk_eafc_inspect_explain | varchar | 50 |  | √ | ' ' |  |
| 23 | fk_fpy_progress | 检测进度 | varchar | 50 |  | √ | ' ' | 检测进度 |
| 24 | fk_eafc_check_user | 检测人员 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fk_eafc_inspect_type | fk_eafc_inspect_type | varchar | 50 |  | √ | ' ' |  |
| 26 | fk_fpy_general_org | 全宗 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 27 | fk_eafc_batch_num | fk_eafc_batch_num | varchar | 50 |  | √ | ' ' |  |
| 28 | fk_eafc_file_count | 检测文件数量 | int8 | 64 |  |  | null | 检测文件数量 |
| 29 | fk_eafc_result | 检测结果 | varchar | 2000 |  | √ | ' ' | 检测结果 |
| 30 | fk_eafc_check_process | 检测环节 | varchar | 50 |  | √ | ' ' | 检测环节,枚举: 1 :接收环节 2 :归档环节 3 :移交环节 4 :保存环节 |
| 31 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_result |  | fid |
| 2 | idx_eafc_inspect_result_no |  | fbillno |

---

## 单据体-子表 tk_fpy_inspect_itemdetail

- **表名称：** 单据体-子表
- **表名：** tk_fpy_inspect_itemdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_item_desc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fk_fpy_item_base | 四性检测 | int8 | 64 |  | √ | 0 | [四性检测基础资料 eafc_inspect_base](../esyset_files/eafc_inspect_base.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fk_fpy_item_result | 检测结果 | varchar | 50 |  | √ | ' ' | 检测结果,枚举: 1 :通过 2 :不通过 |
| 7 | fk_fpy_item_desc_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__fpy_inspect_itemdetail_fk |  | fid |
| 2 | pk__fpy_inspect_itemdetail |  | fentryid |

---

## 单据体-子表 tk_eafc_inspect_detail

- **表名称：** 单据体-子表
- **表名：** tk_eafc_inspect_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_base_billid | 长整数 | int8 | 64 |  |  | null | 长整数 |
| 3 | fk_eafc_safe_check_detail | 安全性详情 | varchar | 255 |  | √ | ' ' | 安全性详情 |
| 4 | fk_eafc_complete_check | 完整性 | varchar | 2000 |  | √ | ' ' | 完整性 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_file_sign | 题名 | varchar | 200 |  | √ | ' ' | 题名 |
| 7 | fk_eafc_usable_detail | 可用性详情 | varchar | 255 |  | √ | ' ' | 可用性详情 |
| 8 | fk_eafc_usable_detail_tag | 可用性详情_详情 | text | 0 |  |  | null | 可用性详情_详情 |
| 9 | fk_eafc_file_code | 文号 | varchar | 200 |  | √ | ' ' | 文号 |
| 10 | fk_eafc_safe_check_detail_tag | 安全性详情_详情 | text | 0 |  |  | null | 安全性详情_详情 |
| 11 | fk_eafc_mild_item_num | 轻度提示不通过项数量 | int8 | 64 |  |  | null | 轻度提示不通过项数量 |
| 12 | fk_eafc_safe_check | 安全性 | varchar | 2000 |  | √ | ' ' | 安全性 |
| 13 | fk_eafc_usable_check | 可用性 | varchar | 2000 |  | √ | ' ' | 可用性 |
| 14 | fk_eafc_real_check | 真实性 | varchar | 2000 |  | √ | ' ' | 真实性 |
| 15 | fbusinesscategory | 业务类型 | varchar | 200 |  | √ | ' ' | 业务类型 |
| 16 | fk_eafc_complete_detail | 完整性详情 | varchar | 255 |  | √ | ' ' | 完整性详情 |
| 17 | fk_eafc_complete_detail_tag | 完整性详情_详情 | text | 0 |  |  | null | 完整性详情_详情 |
| 18 | fbusinessnumber | 业务编号 | varchar | 200 |  | √ | ' ' | 业务编号 |
| 19 | fk_eafc_period | 所属期间 | varchar | 50 |  | √ | ' ' | 所属期间 |
| 20 | fk_eafc_real_check_detail_tag | 真实性详情_详情 | text | 0 |  |  | null | 真实性详情_详情 |
| 21 | fk_eafc_real_check_detail | 真实性详情 | varchar | 255 |  | √ | ' ' | 真实性详情 |
| 22 | fk_eafc_serious_item_num | 重度提示不通过项数量 | int8 | 64 |  |  | null | 重度提示不通过项数量 |
| 23 | fk_eafc_strict_item_num | 严格检测不通过项数量 | int8 | 64 |  |  | null | 严格检测不通过项数量 |
| 24 | fbusinesstypeid | 类别 | int8 | 64 |  | √ | 0 | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_detail |  | fentryid |
