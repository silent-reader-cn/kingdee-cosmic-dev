# 人工复核记录-eafc_reviewrecord

## 人工复核记录-主表 t_eafc_reviewrecord

- **表名称：** 人工复核记录-主表
- **表名：** t_eafc_reviewrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | ffilesign | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 6 | fcreatetime | 复核时间 | timestamp | 0 |  |  | null | 复核时间 |
| 7 | freviewerorgid | 复核人所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | ffileno | 文件编号 | varchar | 200 |  | √ | ' ' | 文件编号 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | farcorgid | 归档组织 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbooktypeid | 机构问题 | int8 | 64 |  | √ | 0 | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 14 | fcreatorid | 复核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbusinesstypeid | 类别 | int8 | 64 |  | √ | 0 | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 16 | fbillno | 复核单号 | varchar | 30 |  | √ | ' ' | 复核单号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | freviewerstep | 复核环节 | varchar | 2 |  | √ | ' ' | 复核环节,枚举: 1 :收集环节 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_reviewrecord_1 |  | fbatchno |
| 2 | pk_eafc_reviewrecord |  | fid |

---

## 单据体-子表 t_eafc_reviewrecord_ent

- **表名称：** 单据体-子表
- **表名：** t_eafc_reviewrecord_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectresult | 检测结果 | varchar | 200 |  | √ | ' ' | 检测结果 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | finspecttype | 检测类别 | varchar | 100 |  | √ | ' ' | 检测类别 |
| 5 | freviewresult | 复核结果 | varchar | 2 |  | √ | ' ' | 复核结果,枚举: 1 :复核通过 |
| 6 | fdescription | 备注说明 | varchar | 200 |  | √ | ' ' | 备注说明 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | finspectitem | 检测项 | varchar | 100 |  | √ | ' ' | 检测项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_reviewrecord_ent |  | fentryid |
| 2 | idx_eafc_revrecord_ent_1 |  | fid |
