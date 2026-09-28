# 待填报任务列表-tctsa_report_dtask_bill

## 卡片分录-子表 t_tctsa_temp_dtask_label

- **表名称：** 卡片分录-子表
- **表名：** t_tctsa_temp_dtask_label

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | flabelid | 标签 | int8 | 64 |  | √ | 0 | 标签 t_tctb_label_info |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_temp_dtask_label |  | fentryid |
| 2 | idx_tctsa_temp_dtask_label_fk |  | fid |

---

## 待填报任务列表-主表 t_tctsa_report_dtask_bill

- **表名称：** 待填报任务列表-主表
- **表名：** t_tctsa_report_dtask_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 3 | forgfield | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdes | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :可用 0 :禁用 |
| 6 | fstart | 填报时间起 | timestamp | 0 |  |  | null | 填报时间起 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fsubmitstatus | 提交状态 | varchar | 50 |  | √ | ' ' | 提交状态,枚举: 0 :未提交 1 :已提交 2 :重新填报 |
| 10 | fsbbid | 长整数(用于关联临时填报主见) | int8 | 64 |  | √ | 0 | 长整数(用于关联临时填报主见) |
| 11 | fend | 填报时间止 | timestamp | 0 |  |  | null | 填报时间止 |
| 12 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 13 | fbillno | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 14 | fcombofield | 填报状态 | varchar | 50 |  | √ | ' ' | 填报状态,枚举: 0 :● 未填报 1 :● 填报中 2 :● 已完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_report_dtask_bill |  | forgfield,fstart,fend |
| 2 | pk_tctsa_report_dtask_bill |  | fid |

---

## 单据体-子表 t_tctsa_temp_dtask_djt

- **表名称：** 单据体-子表
- **表名：** t_tctsa_temp_dtask_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 5 | fentryname | 事项名称 | varchar | 50 |  | √ | ' ' | 事项名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftaxtype | 基础资料 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_temp_dtask_djt_fk |  | fid |
| 2 | pk_tctsa_temp_dtask_djt |  | fentryid |
