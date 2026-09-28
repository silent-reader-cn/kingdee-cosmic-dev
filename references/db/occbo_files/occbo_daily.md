# 我的日报-occbo_daily

## 单据体-子表 t_occbo_daily_entry

- **表名称：** 单据体-子表
- **表名：** t_occbo_daily_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillnum | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 3 | fbillcreatedate | 单据创建日期 | timestamp | 0 |  |  | null | 单据创建日期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillentity | 单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_daily_entry_fk |  | fid |
| 2 | pk_t_occbo_daily_entry |  | fentryid |

---

## 我的日报照片分录-子表 t_occbo_daily_imgentry

- **表名称：** 我的日报照片分录-子表
- **表名：** t_occbo_daily_imgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fthumbnailurl | 缩略图路径 | varchar | 255 |  | √ | ' ' | 缩略图路径 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fpicurl | 图片路径 | varchar | 255 |  | √ | ' ' | 图片路径 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_occbo_daily_imgentry |  | fentryid |
| 2 | idx_occbo_daily_imgentry_fk |  | fid |

---

## 我的日报-主表 t_occbo_daily

- **表名称：** 我的日报-主表
- **表名：** t_occbo_daily

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpicture6 | 图片字段6 | varchar | 255 |  |  | null | 图片字段6 |
| 4 | fdeptid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpicture5 | 图片字段5 | varchar | 255 |  |  | null | 图片字段5 |
| 6 | freporttxt | 今日报告 | varchar | 1000 |  | √ | ' ' | 今日报告 |
| 7 | fdailydate | 报告日期 | timestamp | 0 |  |  | null | 报告日期 |
| 8 | fpicture4 | 图片字段4 | varchar | 255 |  |  | null | 图片字段4 |
| 9 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fpicture3 | 图片字段3 | varchar | 255 |  |  | null | 图片字段3 |
| 11 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fpicture2 | 图片字段2 | varchar | 255 |  |  | null | 图片字段2 |
| 13 | fpicture1 | 图片字段1 | varchar | 255 |  |  | null | 图片字段1 |
| 14 | fplantxt | 明日计划 | varchar | 1000 |  |  | null | 明日计划 |
| 15 | freporterid | 报告人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbillno | 日报编号 | varchar | 30 |  | √ | ' ' | 日报编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_daily_billno |  | fbillno |
| 2 | pk_t_occbo_daily |  | fid |
