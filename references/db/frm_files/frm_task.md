# 对账任务-frm_task

## 取数规则分录-子表 t_frm_task_detail

- **表名称：** 取数规则分录-子表
- **表名：** t_frm_task_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftraceid | traceid | varchar | 255 |  | √ | ' ' | traceid |
| 2 | fruleentryid | 取数规则分录ID | int8 | 64 |  | √ | 0 | 取数规则分录ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdatafilterdesc | 单据过滤 | varchar | 2000 |  |  | ' ' | 单据过滤 |
| 5 | fdetailbegin | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 6 | fdetailend | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 7 | fdscacheid | 缓存数据ID | varchar | 255 |  | √ | ' ' | 缓存数据ID |
| 8 | fstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 0 :未开始 1 :进行中 2 :已完成 3 :异常中断 |
| 9 | famounttype | 取数类型 | int8 | 64 |  | √ | 0 | [对账类型 frm_amouttype_layout](../frm_files/frm_amouttype_layout.md) |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 12 | fcount | 数据量 | int8 | 64 |  | √ | 0 | 数据量 |
| 13 | fentryid | 方案分录entryid | int8 | 64 |  | √ | 0 | 方案分录entryid |
| 14 | fbizobj | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fdatatype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型,枚举: 0 :初始化 1 :期初余额 2 :借方金额 3 :贷方金额 4 :期末余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_frm_task_detail |  | ftaskid,fruleentryid,fentryid |
| 2 | pk_t_frm_task_detail |  | fdetailid |

---

## 对账任务-主表 t_frm_task

- **表名称：** 对账任务-主表
- **表名：** t_frm_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | fmessage | text | 0 |  |  | null |  |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdataruleid | 取数规则 | int8 | 64 |  | √ | 0 | [业务取数规则 frm_recdatarule](../frm_files/frm_recdatarule.md) |
| 5 | freconresult | 对账结果 | bpchar | 1 |  | √ | ' ' | 对账结果,枚举: 1 :对平 2 :对不平 3 :无匹配的账簿 4 :账簿没有适用的对账方案 5 :账簿不存在已启用且设置业务结账必须对账平衡的对账方案 6 :未购买智能会计平台 0 :账簿启用期间大于对账期间 7 :系统异常 8 :总账未结束初始化 9 :对账方案未配置取数规则，请检查 |
| 6 | fapiparam | 接口参数 | varchar | 255 |  |  | ' ' | 接口参数 |
| 7 | fbizappid | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fsuppinst | 下达实例 | varchar | 255 |  | √ | ' ' | 下达实例 |
| 10 | ferror_tag | 错误信息_详情 | text | 0 |  | √ | ' ' | 错误信息_详情 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | freconplanid | 对账方案 | int8 | 64 |  | √ | 0 | [业财对账方案 frm_reconciliation_scheme](../frm_files/frm_reconciliation_scheme.md) |
| 13 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | '0' | 任务状态,枚举: 0 :未开始 1 :进行中 2 :停止 3 :已完成 4 :出错 |
| 14 | fapiparam_tag | 接口参数_详情 | text | 0 |  |  | ' ' | 接口参数_详情 |
| 15 | fpercent | 进度 | int4 | 32 |  | √ | 0 | 进度 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fperiodid | 对账期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | freconresulttype | 任务类型 | bpchar | 1 |  | √ | ' ' | 任务类型,枚举: 1 :对账结果 2 :对账汇总 3 :对账明细 4 :接口调用 5 :自动对账 |
| 19 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 22 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 23 | ferror | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 24 | finit | 初始化对账 | bpchar | 1 |  | √ | '0' | 初始化对账 |
| 25 | fconsinst | 消费实例 | varchar | 255 |  | √ | ' ' | 消费实例 |
| 26 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_frm_task |  | ftaskstatus,forgid,fbizappid,fperiodid |
| 2 | pk_t_frm_task |  | fid |

---

## 科目-多选基础资料表 t_frm_task_account

- **表名称：** 科目-多选基础资料表
- **表名：** t_frm_task_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_frm_task_account |  | fpkid |
| 2 | idx_frm_task_account |  | fentryid |

---

## 取数类型-多选基础资料表 t_frm_task_amounttype

- **表名称：** 取数类型-多选基础资料表
- **表名：** t_frm_task_amounttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [对账类型 frm_amouttype_layout](../frm_files/frm_amouttype_layout.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_frm_task_amounttype |  | fentryid |
| 2 | pk_t_frm_task_amounttype |  | fpkid |

---

## 对账方案分录-子表 t_frm_task_entry

- **表名称：** 对账方案分录-子表
- **表名：** t_frm_task_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 0 :未开始 1 :进行中 2 :已完成-平 3 :异常中断 4 :已完成-不平 |
| 3 | fplandetailid | 方案分录ID | int8 | 64 |  | √ | 0 | 方案分录ID |
| 4 | ftraceid | traceid | varchar | 255 |  | √ | ' ' | traceid |
| 5 | fentrybegin | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 6 | fassisttype | 分类 | varchar | 50 |  | √ | ' ' | 分类,枚举: 1 :科目对账 2 :核算维度对账 3 :辅助资料对账 |
| 7 | fentryend | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fexeced | 已执行数 | int4 | 32 |  | √ | 0 | 已执行数 |
| 10 | ftotalcount | 总数 | int4 | 32 |  | √ | 0 | 总数 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_frm_task_entry |  | fid,fplandetailid |
| 2 | pk_t_frm_task_entry |  | fentryid |
