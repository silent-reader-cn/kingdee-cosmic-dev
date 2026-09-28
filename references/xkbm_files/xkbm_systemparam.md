# 预算管理系统参数-xkbm_systemparam

## 单据体-子表 t_xkbm_adjustctrlentity

- **表名称：** 单据体-子表
- **表名：** t_xkbm_adjustctrlentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjustctrl | 预算控制 | bpchar | 1 |  | √ | ' ' | 预算控制 |
| 3 | fadjustoperation | 操作 | varchar | 30 |  | √ | ' ' | 操作,枚举: save :保存 submit :提交 audit :审核 |
| 4 | fadjustbusiness | 业务单据范围 | varchar | 30 |  | √ | ' ' | 业务单据范围,枚举: 1 :已保存、已提交、已审核业务单据 2 :已提交、已审核业务单据 3 :已审核业务单据 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_adjustctrlentity_fid |  | fid |
| 2 | pk_xkbm_adjustctrlentity |  | fentryid |

---

## 预算管理系统参数-主表 t_xkbm_systemparam

- **表名称：** 预算管理系统参数-主表
- **表名：** t_xkbm_systemparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbudgetdimensiongroup | 调整、调剂单，预算维度组合仅来源于预算报表 | bpchar | 1 |  | √ | ' ' | 调整、调剂单，预算维度组合仅来源于预算报表 |
| 3 | fuploadaspdf | pdf格式 | bpchar | 1 |  | √ | ' ' | pdf格式 |
| 4 | fiseditsubmitreport | 在工作流中，允许审批人修改预算报表 | bpchar | 1 |  | √ | ' ' | 在工作流中，允许审批人修改预算报表 |
| 5 | fovertip | fovertip | bpchar | 1 |  | √ | ' ' |  |
| 6 | fuploadasexcel | excel交叉表格式 | bpchar | 1 |  | √ | ' ' | excel交叉表格式 |
| 7 | fuploadasexcellist | excel列表格式 | bpchar | 1 |  | √ | ' ' | excel列表格式 |
| 8 | fbudgetallownegative | 调整、调剂单，允许调整后负数 | bpchar | 1 |  | √ | ' ' | 调整、调剂单，允许调整后负数 |
| 9 | fbudgetctrl | 启用预算控制 | bpchar | 1 |  | √ | ' ' | 启用预算控制 |
| 10 | fuploadasexceldev | excel 默认格式 | bpchar | 1 |  | √ | ' ' | excel 默认格式 |
| 11 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 12 | fenablesumreportctrl | 非周期性预算汇总表提交后，禁止反审核预算报表 | bpchar | 1 |  | √ | ' ' | 非周期性预算汇总表提交后，禁止反审核预算报表 |
| 13 | fenableperiodsumreportctr | 周期性预算汇总表提交后，禁止反审核预算报表 | bpchar | 1 |  | √ | ' ' | 周期性预算汇总表提交后，禁止反审核预算报表 |
| 14 | fnotcompletedbutcanchange | 预算方案监控：已分发预算表未完编，仍允许预算组织切换到[执行中]状态 | bpchar | 1 |  | √ | ' ' | 预算方案监控：已分发预算表未完编，仍允许预算组织切换到[执行中]状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_systemparam |  | fbudgetctrl |
| 2 | pk_xkbm_systemparam |  | fid |
