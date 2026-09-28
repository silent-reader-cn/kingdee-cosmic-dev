# 财务报告生成记录-fgptas_fireportgenlog

## 财务报告生成记录-多语言表 t_fgptas_fireportgenlog_l

- **表名称：** 财务报告生成记录-多语言表
- **表名：** t_fgptas_fireportgenlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexecreason | fexecreason | varchar | 1024 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | ffireportname | 报告名称 | varchar | 255 |  | √ | ' ' | 报告名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_fireportgenlog_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_fireportgenlog_l |  | fpkid |

---

## 财务报告生成记录-主表 t_fgptas_fireportgenlog

- **表名称：** 财务报告生成记录-主表
- **表名：** t_fgptas_fireportgenlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | fcreatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 4 | ftasktype | 任务发起方式 | varchar | 50 |  | √ | ' ' | 任务发起方式,枚举: 1 :手工发起 2 :定时发起 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ffireportid | 财务报告 | int8 | 64 |  | √ | 0 | 财务报告 |
| 7 | fparagraphids | 报告章节 | varchar | 1024 |  | √ | ' ' | 报告章节 |
| 8 | fexecreason | 异常原因 | varchar | 255 |  | √ | ' ' | 异常原因 |
| 9 | freporttemplateid | 报告模板 | int8 | 64 |  | √ | 0 | [财务报告模板 fgptas_fireporttemplate](../fgptas_files/fgptas_fireporttemplate.md) |
| 10 | fgendocumenttype | 生成文档类型 | varchar | 50 |  | √ | ' ' | 生成文档类型,枚举: 1 :Word 2 :PPT |
| 11 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 12 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 13 | fstatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: 1 :成功 2 :失败 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fperiod | fperiod | varchar | 1024 |  | √ | ' ' |  |
| 16 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 17 | fcycleid | 周期类型 | varchar | 1024 |  | √ | ' ' | 周期类型,枚举: 2 :日报 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 18 | ffireportname | 报告名称 | varchar | 255 |  | √ | ' ' | 报告名称 |
| 19 | ffireportnumber | 报告编号 | varchar | 30 |  | √ | ' ' | 报告编号 |
| 20 | ftaskscheduleid | 定时方案 | int8 | 64 |  | √ | 0 | [财务报告生成定时方案 fgptas_taskschedule](../fgptas_files/fgptas_taskschedule.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_fireportgenlog |  | fid |
| 2 | idx_fgptas_firptgenlog_rptid |  | ffireportid |
