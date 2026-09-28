# 签署任务-ccas_signtask

## 签署任务-主表 t_ccas_signtask

- **表名称：** 签署任务-主表
- **表名：** t_ccas_signtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' | id |
| 2 | fdeadlinetime | 截止时间 | timestamp | 0 |  |  | null | 截止时间 |
| 3 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsigntasksubject | 签署任务名称 | varchar | 255 |  | √ | ' ' | 签署任务名称 |
| 5 | finitiatorname | 发起主体 | varchar | 255 |  | √ | ' ' | 发起主体 |
| 6 | fbilltypename | 单据分类 | varchar | 50 |  | √ | ' ' | 单据分类 |
| 7 | fstarttime | 发起时间 | timestamp | 0 |  |  | null | 发起时间 |
| 8 | fsignrule_tag | 签章配置规则_详情 | text | 0 |  |  | null | 签章配置规则_详情 |
| 9 | fsrc_cloudname | 云 | varchar | 50 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 10 | fsrc_appname | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fsigntaskstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: task_created :任务创建中 finish_creation :已创建 fill_progress :填写进行中 fill_completed :填写已完成 sign_progress :签署进行中 task_finished :已完成 task_terminated :已终止 expired :已逾期 abolishing :作废中 revoked :已作废 |
| 12 | fjudgebilltype | 关联业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | ffinishtime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 14 | fcancelreason | 撤销原因 | varchar | 255 |  | √ | ' ' | 撤销原因 |
| 15 | fsigntaskid | 签署任务ID | varchar | 50 |  | √ | ' ' | 签署任务ID |
| 16 | frelatebilltype | 关联单据类型（废弃） | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 17 | fsrc_billno | 关联单据号 | varchar | 100 |  | √ | ' ' | 关联单据号 |
| 18 | fintegratedservice | 集成服务商（废弃） | varchar | 1 |  | √ | ' ' | 集成服务商（废弃）,枚举: 1 :法大大 2 :e签宝 |
| 19 | fesserviceprovider | 集成服务 | int8 | 64 |  | √ | 0 | [集成服务配置 ccas_cisconfig](../ccas_files/ccas_cisconfig.md) |
| 20 | fsignrule | 签章配置规则 | varchar | 255 |  | √ | ' ' | 签章配置规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | udx_ccas_signtask_list_taskid |  | fsigntaskid |
| 2 | pk_ccas_signtask |  | fid |

---

## 参与方-子表 t_ccas_signtask_actors

- **表名称：** 参与方-子表
- **表名：** t_ccas_signtask_actors

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' |  |
| 2 | factorid | 参与方标识 | varchar | 50 |  | √ | ' ' | 参与方标识 |
| 3 | factorname | 参与方名称 | varchar | 100 |  | √ | ' ' | 参与方名称 |
| 4 | factorphone | 参与方电话 | varchar | 50 |  | √ | ' ' | 参与方电话 |
| 5 | factortype | 参与方主体类型 | varchar | 1 |  | √ | ' ' | 参与方主体类型,枚举: 1 :企业 2 :个人 |
| 6 | factorcontactperson | 参与方联系人 | varchar | 100 |  | √ | ' ' | 参与方联系人 |
| 7 | fsigningsequence | 签署顺序 | int4 | 32 |  | √ | 0 | 签署顺序 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | factorsignstatus | 参与方签署状态 | varchar | 50 |  | √ | 'wait_sign' | 参与方签署状态,枚举: wait_sign :待签署 signed :已签署 sign_rejected :已拒签 |
| 10 | fentryid | fentryid | varchar | 50 |  | √ | ' ' | id |
| 11 | factoremail | 参与方邮箱 | varchar | 50 |  | √ | ' ' | 参与方邮箱 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_signtask_actors |  | fentryid |
| 2 | udx_ccas_signtask_actorid |  | fid,factorid |
