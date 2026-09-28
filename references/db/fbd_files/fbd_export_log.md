# 网银导出结果-fbd_export_log

## 网银导出结果-主表 t_fbd_export_log

- **表名称：** 网银导出结果-主表
- **表名：** t_fbd_export_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fbizobject | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | foriginaldata | 导出内容 | varchar | 255 |  | √ | ' ' | 导出内容 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | foriginaldata_tag | 导出内容_详情 | text | 0 |  | √ | ' ' | 导出内容_详情 |
| 10 | fcreatorid | 导出执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftotal | 执行总数 | int4 | 32 |  | √ | 0 | 执行总数 |
| 12 | fbillno | 日志编码 | varchar | 50 |  | √ | ' ' | 日志编码 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftemplate | 导出模板 | int8 | 64 |  | √ | 0 | [网银引出模板 fbd_export_template](../fbd_files/fbd_export_template.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_export_log |  | fid |

---

## 单据体-子表 t_fbd_export_logentry

- **表名称：** 单据体-子表
- **表名：** t_fbd_export_logentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbizno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 4 | fbizid | 单据标识 | int8 | 64 |  | √ | 0 | 单据标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_export_logentry |  | fid |
| 2 | pk_t_fbd_export_logentry |  | fentryid |
