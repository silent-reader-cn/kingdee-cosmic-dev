# 我的周报-occbo_weekly

## 我的周报照片分录-子表 t_occbo_weekly_imgentry

- **表名称：** 我的周报照片分录-子表
- **表名：** t_occbo_weekly_imgentry

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
| 1 | pk_t_occbo_weekly_imgentry |  | fentryid |
| 2 | idx_occbo_weekly_imgentry_fk |  | fid |

---

## 单据体-子表 t_occbo_weekly_entry

- **表名称：** 单据体-子表
- **表名：** t_occbo_weekly_entry

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
| 1 | pk_t_occbo_weekly_entry |  | fentryid |
| 2 | idx_occbo_weekly_entry_fk |  | fid |

---

## 我的周报-主表 t_occbo_weekly

- **表名称：** 我的周报-主表
- **表名：** t_occbo_weekly

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdailydate | 报告日期 | timestamp | 0 |  |  | null | 报告日期 |
| 3 | fplantxt | 下周计划 | varchar | 1000 |  |  | null | 下周计划 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbillno | 周报编号 | varchar | 30 |  | √ | ' ' | 周报编号 |
| 9 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpicture6 | 图片字段 | varchar | 255 |  |  | null | 图片字段 |
| 11 | fdeptid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fpicture5 | 图片字段 | varchar | 255 |  |  | null | 图片字段 |
| 13 | freporttxt | 周报内容 | varchar | 1000 |  | √ | ' ' | 周报内容 |
| 14 | fpicture4 | 图片字段 | varchar | 255 |  |  | null | 图片字段 |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fpicture3 | 图片字段 | varchar | 255 |  |  | null | 图片字段 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fpicture2 | 图片字段 | varchar | 255 |  |  | null | 图片字段 |
| 19 | fpicture1 | 图片字段 | varchar | 255 |  |  | null | 图片字段 |
| 20 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 21 | freporterid | 报告人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fweekordinal | 第几周 | numeric | 23 | 10 | √ | 0 | 第几周 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_occbo_weekly |  | fid |
| 2 | idx_occbo_weekly_billno |  | fbillno |
