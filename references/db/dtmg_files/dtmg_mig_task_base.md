# 迁移任务基础资料-dtmg_mig_task_base

## 迁移任务基础资料-主表 t_dtmg_migrationtask

- **表名称：** 迁移任务基础资料-主表
- **表名：** t_dtmg_migrationtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdepaccount | fdepaccount | varchar | 100 |  | √ | ' ' |  |
| 3 | ftasktype | ftasktype | varchar | 20 |  | √ | '0' |  |
| 4 | fexecutebegindate | fexecutebegindate | timestamp | 0 |  |  | null |  |
| 5 | ftaskresult | ftaskresult | varchar | 2 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsourceaccount | fsourceaccount | varchar | 100 |  | √ | ' ' |  |
| 8 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fdataconfig | fdataconfig | varchar | 255 |  | √ | ' ' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftaskmode | ftaskmode | varchar | 1 |  | √ | '0' |  |
| 13 | fbreakid | fbreakid | varchar | 100 |  | √ | ' ' |  |
| 14 | fsourcetype | fsourcetype | varchar | 3 |  | √ | ' ' |  |
| 15 | fplandate | fplandate | timestamp | 0 |  |  | null |  |
| 16 | ftaskstatus | ftaskstatus | varchar | 1 |  | √ | '1' |  |
| 17 | fexecuteenddate | fexecuteenddate | timestamp | 0 |  |  | null |  |
| 18 | fdataconfig_tag | fdataconfig_tag | text | 0 |  |  | null |  |
| 19 | fusetime | fusetime | int4 | 32 |  | √ | 0 |  |
| 20 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillstatus | fbillstatus | varchar | 1 |  | √ | 'A' |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | ftasknum | ftasknum | int4 | 32 |  | √ | 0 |  |
| 26 | fbillname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 27 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_migrationtask |  | fid |
| 2 | idx_dtmg_mg_breakid |  | fbreakid |
| 3 | idx_dtmg_migrationtask_create |  | fcreatetime |
| 4 | udx_dtmg_migrationtask_billno |  | fbillno |

---

## 迁移任务基础资料-多语言表 t_dtmg_migrationtask_l

- **表名称：** 迁移任务基础资料-多语言表
- **表名：** t_dtmg_migrationtask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fbillname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dtmg_migtask_l |  | fid,flocaleid |
| 2 | pk_t_dtmg_migrationtask_l |  | fpkid |
