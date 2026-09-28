# 研发费用计算报告-rdem_costcalreport

## 单据体-子表 t_pca_costcalreportentry

- **表名称：** 单据体-子表
- **表名：** t_pca_costcalreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcnsmtime | 耗时（毫秒） | int4 | 32 |  | √ | 0 | 耗时（毫秒） |
| 3 | fdtstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :成功 2 :失败 3 :警告 4 :未执行 |
| 4 | floginfo | 日志信息 | varchar | 2000 |  | √ | ' ' | 日志信息 |
| 5 | flinkinfo | 联查信息 | varchar | 2000 |  | √ | ' ' | 联查信息 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailstep | 详细步骤 | varchar | 255 |  | √ | ' ' | 详细步骤 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcalreportentry_id |  | fid |
| 2 | pk_pca_costcalreportentry |  | fentryid |

---

## 研发费用计算报告-主表 t_pca_costcalreport

- **表名称：** 研发费用计算报告-主表
- **表名：** t_pca_costcalreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpcacostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fprogressmessage_tag | 过程详情_详情 | text | 0 |  |  | null | 过程详情_详情 |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :成功 2 :失败 3 :警告 0 :进行中 |
| 7 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | fcreatorid | 计算执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | freporttype | 报告类型 | varchar | 30 |  | √ | '0' | 报告类型,枚举: 0 :研发费用计算 1 :研发费用核算对象归集 2 :研发费用核算单归集 3 :研发公共费用归集单归集 4 :项目即时成本计算 6 :项目人员工时明细归集 7 :项目结转单归集 |
| 12 | fenable | fenable | varchar | 30 |  | √ | ' ' |  |
| 13 | ftaskid | 计算任务号 | varchar | 255 |  | √ | ' ' | 计算任务号 |
| 14 | ftotalcnsmtime | 总耗时(秒) | int4 | 32 |  | √ | 0 | 总耗时(秒) |
| 15 | fbillno | 报告编号 | varchar | 255 |  | √ | ' ' | 报告编号 |
| 16 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 17 | fprogressmessage | 过程详情 | varchar | 255 |  | √ | 0 | 过程详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcalreport_billno |  | fbillno |
| 2 | idx_pca_costcalreport_taskid |  | ftaskid |
| 3 | pk_pca_costcalreport |  | fid |
