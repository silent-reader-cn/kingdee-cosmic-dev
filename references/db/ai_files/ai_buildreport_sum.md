# 凭证生成汇总报告-ai_buildreport_sum

## 凭证生成汇总报告-主表 t_ai_buildreport_sum

- **表名称：** 凭证生成汇总报告-主表
- **表名：** t_ai_buildreport_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuildtasktag | 任务标识 | varchar | 50 |  | √ | ' ' | 任务标识 |
| 3 | fcosttime | 总耗时（秒） | int8 | 64 |  | √ | 0 | 总耗时（秒） |
| 4 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbuildstate | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :进行中 1 :成功 2 :失败 3 :部分成功 |
| 8 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 10 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_buildreport_sum |  | fid |
| 2 | idx_ai_buildreport_sum |  | faccountbookid,fperiodid |

---

## 单据体-子表 t_ai_buildreportsum_entry

- **表名称：** 单据体-子表
- **表名：** t_ai_buildreportsum_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffailcount | 失败数量 | int4 | 32 |  | √ | 0 | 失败数量 |
| 3 | floginfo | 日志 | varchar | 2000 |  | √ | ' ' | 日志 |
| 4 | fbillcount | 单据总数 | int4 | 32 |  | √ | 0 | 单据总数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbillentrycount | 分录总数 | int4 | 32 |  | √ | 0 | 分录总数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbizobj | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fsuccesscount | 成功数量 | int4 | 32 |  | √ | 0 | 成功数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_buildreportsum_entry |  | fid |
| 2 | pk_ai_buildreportsum_entry |  | fentryid |
