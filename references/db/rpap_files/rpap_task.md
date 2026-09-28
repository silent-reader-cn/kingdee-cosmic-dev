# 任务-rpap_task

## 单据体-子表 t_rpap_taskoutargentry

- **表名称：** 单据体-子表
- **表名：** t_rpap_taskoutargentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutargname | 参数名 | varchar | 255 |  | √ | ' ' | 参数名 |
| 3 | foutargtype | 参数类型 | varchar | 255 |  | √ | ' ' | 参数类型 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | foutargvalue | 参数值 | text | 0 |  |  | null | 参数值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rpap_taskoutargentry_fid |  | fid |
| 2 | pk_t_rpap_taskoutargentry |  | fentryid |

---

## 单据体-子表 t_rpap_taskargentry

- **表名称：** 单据体-子表
- **表名：** t_rpap_taskargentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fargname | 参数名 | varchar | 255 |  | √ | ' ' | 参数名 |
| 3 | fargtype | 参数类型 | varchar | 255 |  | √ | ' ' | 参数类型 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fargvalue | 参数值 | text | 0 |  |  | null | 参数值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rpap_taskargentry |  | fentryid |
| 2 | idx_t_rpap_taskargentry_fid |  | fid |

---

## 任务-主表 t_rpap_task

- **表名称：** 任务-主表
- **表名：** t_rpap_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexternalid | 外部id | varchar | 30 |  | √ | ' ' | 外部id |
| 3 | frunningway | 运行方式 | varchar | 10 |  | √ | ' ' | 运行方式,枚举: 0 :立即运行 1 :计划运行 |
| 4 | fbatchnumber | 生成批次 | varchar | 10 |  | √ | ' ' | 生成批次 |
| 5 | fthirdtypeid | 第三方类型 | int8 | 64 |  | √ | 0 | [第三方类型 rpap_thirdtype](../rpap_files/rpap_thirdtype.md) |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fisdelete | 是否删除 | varchar | 10 |  | √ | '0' | 是否删除,枚举: 1 :已删除 0 :未删除 |
| 8 | fresult | 运行结果 | varchar | 10 |  | √ | ' ' | 运行结果,枚举: 0 :异常 1 :正常 |
| 9 | frobot | 机器人 | int8 | 64 |  | √ | 0 | [机器人 rpap_robot](../rpap_files/rpap_robot.md) |
| 10 | fprocess | 流程 | int8 | 64 |  | √ | 0 | [流程 rpap_process](../rpap_files/rpap_process.md) |
| 11 | fsource | 来源描述 | varchar | 30 |  | √ | ' ' | 来源描述 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frunningduration | 运行时长（秒） | int8 | 64 |  | √ | 0 | 运行时长（秒） |
| 15 | fbplantaskid | 批量调度计划id | varchar | 30 |  | √ | ' ' | 批量调度计划id |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fversion | 版本号 | varchar | 10 |  | √ | ' ' | 版本号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fsendsum | 推送总次数(第三方) | varchar | 10 |  | √ | ' ' | 推送总次数(第三方) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fstarttime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 24 | fexceptiondesc | 异常描述（第三方） | varchar | 100 |  | √ | ' ' | 异常描述（第三方） |
| 25 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 26 | frunningstate | 运行状态 | varchar | 10 |  | √ | ' ' | 运行状态,枚举: 0 :计划任务 1 :排队中 2 :运行中 3 :已完成 |
| 27 | fplanstarttime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rpap_task |  | fid |
| 2 | idx_rpap_task_process |  | fprocess |
| 3 | idx_task_extid_thirdtype |  | fexternalid,fthirdtypeid |
