# 新增临时填报任务-tctsa_temp_report_item

## 组织被共享范围-子表 t_tctsa_temp_share_orgs

- **表名称：** 组织被共享范围-子表
- **表名：** t_tctsa_temp_share_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_temp_share_orgs |  | fentryid |
| 2 | idx_tctsa_temp_share_orgs_fk |  | fid |

---

## 填报事项-子表 t_tctsa_temp_items

- **表名称：** 填报事项-子表
- **表名：** t_tctsa_temp_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fnote | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fentryname | 事项名称 | varchar | 50 |  | √ | ' ' | 事项名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_temp_items |  | fentryid |
| 2 | idx_tctsa_temp_items_fk |  | fid |

---

## 新增临时填报任务-主表 t_tctsa_temp_report_item

- **表名称：** 新增临时填报任务-主表
- **表名：** t_tctsa_temp_report_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 4 | fdes | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: 1 :可用 0 :禁用 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fstart | 填报日期起 | timestamp | 0 |  |  | null | 填报日期起 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fend | 填报日期止 | timestamp | 0 |  |  | null | 填报日期止 |
| 12 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 13 | fcount | 填报项数量 | int8 | 64 |  | √ | 0 | 填报项数量 |
| 14 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_temp_report_item |  | fstart,fend |
| 2 | pk_tctsa_temp_report_item |  | fid |

---

## 标签单据体-子表 t_tctsa_temp_report_label

- **表名称：** 标签单据体-子表
- **表名：** t_tctsa_temp_report_label

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | flabelid | 标签 | int8 | 64 |  | √ | 0 | [标签 t_tctb_label_info](../tctb_files/t_tctb_label_info.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_temp_report_label_fk |  | fid |
| 2 | pk_tctsa_temp_report_label |  | fentryid |
