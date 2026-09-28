# 2D受影响文档-plm_plmdc_affected_doc

## 2D受影响文档-主表 t_plmdc_affected_document

- **表名称：** 2D受影响文档-主表
- **表名：** t_plmdc_affected_document

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | foperateid | 操作对象ID | int8 | 64 |  | √ | 0 | [图文档版本 plm_pdm_caddoc_revision](../plmsm_files/plm_pdm_caddoc_revision.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fversionid | 版次信息 | int8 | 64 |  | √ | 0 | [图文档版次模型 plm_pdm_caddoc_version](../plmsm_files/plm_pdm_caddoc_version.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 操作对象编码 | varchar | 30 |  | √ | ' ' | 操作对象编码 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_foperateid |  | foperateid |
| 2 | pk_t_plmdc_affected_document |  | fid |

---

## 单据体-子表 plm_plmdc_affected_detail

- **表名称：** 单据体-子表
- **表名：** plm_plmdc_affected_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faffectsparentid | 受影响父项ID | int8 | 64 |  | √ | 0 | [图文档版本 plm_pdm_caddoc_revision](../plmsm_files/plm_pdm_caddoc_revision.md) |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :待处理 B :已处理 |
| 4 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | faffectsparentversionid | 受影响父项版次ID | int8 | 64 |  | √ | 0 | [图文档版次模型 plm_pdm_caddoc_version](../plmsm_files/plm_pdm_caddoc_version.md) |
| 6 | fsubitemid | 子项ID | int8 | 64 |  | √ | 0 | [图文档版本 plm_pdm_caddoc_revision](../plmsm_files/plm_pdm_caddoc_revision.md) |
| 7 | fsubitemversionid | 子项版次ID | int8 | 64 |  | √ | 0 | [图文档版次模型 plm_pdm_caddoc_version](../plmsm_files/plm_pdm_caddoc_version.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftips | 备注 | varchar | 500 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_plmdc_affected_detail |  | fentryid |
| 2 | idx_plmdc_fid |  | fid |
