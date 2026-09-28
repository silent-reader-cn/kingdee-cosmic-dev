# 数据迁移任务-dtmg_datamigration_task

## 数据迁移任务-主表 t_dtmg_migrationtask

- **表名称：** 数据迁移任务-主表
- **表名：** t_dtmg_migrationtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdepaccount | 依赖账套 | varchar | 100 |  | √ | ' ' | 依赖账套 |
| 3 | ftasktype | 任务类型 | varchar | 20 |  | √ | '0' | 任务类型,枚举: 0 :历史数据沿用 1 :历史数据备查 2 :初始化数据迁移 |
| 4 | fexecutebegindate | 开始执行时间 | timestamp | 0 |  |  | null | 开始执行时间 |
| 5 | ftaskresult | 迁移结果 | varchar | 2 |  | √ | ' ' | 迁移结果,枚举: A :成功 B :失败 C :部分成功 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsourceaccount | 来源账套 | varchar | 100 |  | √ | ' ' | 来源账套 |
| 8 | fstatus | fstatus | varchar | 2 |  | √ | ' ' |  |
| 9 | fdataconfig | 数据包配置 | varchar | 255 |  | √ | ' ' | 数据包配置 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | ftaskmode | 任务模式 | varchar | 1 |  | √ | '0' | 任务模式,枚举: 0 :全量迁移 1 :增量迁移 |
| 13 | fbreakid | 断点任务ID | varchar | 100 |  | √ | ' ' | 断点任务ID |
| 14 | fsourcetype | 来源类型 | varchar | 3 |  | √ | ' ' | 来源类型 |
| 15 | fplandate | 计划执行时间 | timestamp | 0 |  |  | null | 计划执行时间 |
| 16 | ftaskstatus | 迁移状态 | varchar | 1 |  | √ | '1' | 迁移状态,枚举: A :待执行 B :执行中 C :已执行 F :手动终止 |
| 17 | fexecuteenddate | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 18 | fdataconfig_tag | 数据包配置_详情 | text | 0 |  |  | null | 数据包配置_详情 |
| 19 | fusetime | 用时（秒） | int4 | 32 |  | √ | 0 | 用时（秒） |
| 20 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillstatus | 单据状态 | varchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | ftasknum | 迁移对象数量 | int4 | 32 |  | √ | 0 | 迁移对象数量 |
| 26 | fbillname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 27 | fenable | fenable | varchar | 2 |  | √ | ' ' |  |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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

## 附件-附件表 t_dtmg_migrationtask_atta

- **表名称：** 附件-附件表
- **表名：** t_dtmg_migrationtask_atta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_migrationtask_atta |  | fpkid |
| 2 | udx_dtmg_migrationtask_atta |  | fentryid,fbasedataid |

---

## 单据体-子表 t_dtmg_migrationtask_list

- **表名称：** 单据体-子表
- **表名：** t_dtmg_migrationtask_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 转换关系名称 | varchar | 255 |  | √ | ' ' | 转换关系名称 |
| 3 | ffilesign | 文件MD5 | varchar | 50 |  | √ | ' ' | 文件MD5 |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | ferrmsg_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fobjectid | 业务对象（旗舰版） | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 8 | fsubtaskconfig_tag | config.json_详情 | text | 0 |  |  | null | config.json_详情 |
| 9 | fsubtaskendtime | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 10 | fprogress | 进度 | numeric | 23 | 4 | √ | 0 | 进度 |
| 11 | fsuccessnum | 成功数 | int4 | 32 |  | √ | 0 | 成功数 |
| 12 | fallnum | 迁移数据量 | int4 | 32 |  | √ | 0 | 迁移数据量 |
| 13 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 14 | fsubtaskconfig | config.json | varchar | 255 |  | √ | ' ' | config.json |
| 15 | ferrmsg | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 16 | ffilename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 17 | fsubstatus | 任务状态 | varchar | 1 |  | √ | ' ' | 任务状态,枚举: A :待执行 B :执行中 C :已执行 D :手动终止 G :异常终止 |
| 18 | fnumber | 转换关系编码 | varchar | 100 |  | √ | ' ' | 转换关系编码 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fsubstarttime | 任务执行时间 | timestamp | 0 |  |  | null | 任务执行时间 |
| 21 | ferrornum | 失败数 | int4 | 32 |  | √ | 0 | 失败数 |
| 22 | fimporttype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_migrationtask_list |  | fentryid |
| 2 | udx_dtmg_migrationtask_list |  | fid,fnumber |
