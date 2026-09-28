# 自动生成方案执行记录-xkrpt_autocreatereportlog

## 自动生成方案执行记录-主表 t_xkrpt_autocreaterptlog

- **表名称：** 自动生成方案执行记录-主表
- **表名：** t_xkrpt_autocreaterptlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | frptcount | 报表总数 | int4 | 32 |  | √ | 0 | 报表总数 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fenddatetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbegindatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fautocreaterptscheme | 方案名称 | int8 | 64 |  | √ | 0 | 报表自动生成方案 xkrpt_rptautocrt |
| 12 | fcreatetype | 执行方式 | bpchar | 1 |  | √ | '0' | 执行方式,枚举: 0 :自动 1 :手动 |
| 13 | fsucesscount | 成功个数 | int4 | 32 |  | √ | 0 | 成功个数 |
| 14 | ferrorcount | 失败个数 | int4 | 32 |  | √ | 0 | 失败个数 |
| 15 | fskipcount | 未执行个数 | int4 | 32 |  | √ | 0 | 未执行个数 |
| 16 | fbillno | 方案编号 | varchar | 30 |  | √ | ' ' | 方案编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_autocreaterptlog_sch |  | fautocreaterptscheme,fbillno |
| 2 | pk_xkrpt_autocreaterptlog |  | fid |

---

## 报表生成信息-子表 t_xkrpt_autorptlogentry

- **表名称：** 报表生成信息-子表
- **表名：** t_xkrpt_autorptlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauditcheck | 审核检查 | bpchar | 1 |  | √ | '0' | 审核检查,枚举: 0 :未检查 1 :通过 2 :未通过 |
| 3 | fexceptionmsg | 失败原因 | varchar | 2000 |  | √ | ' ' | 失败原因 |
| 4 | fcosttime | 耗时 | varchar | 50 |  | √ | ' ' | 耗时 |
| 5 | frptid | 报表ID | varchar | 50 |  | √ | ' ' | 报表ID |
| 6 | ftipmsg | 警告信息 | varchar | 2000 |  | √ | ' ' | 警告信息 |
| 7 | fcreatestatus | 生成状态 | bpchar | 1 |  | √ | '0' | 生成状态,枚举: 0 :失败 1 :成功 2 :警告 3 :未执行 |
| 8 | frptname | 报表名称 | varchar | 255 |  | √ | ' ' | 报表名称 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fauditcheckmsg | 审核检查信息 | varchar | 2000 |  | √ | ' ' | 审核检查信息 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_autorptelog_fid |  | fid |
| 2 | pk_xkrpt_autorptlogentry |  | fentryid |
