# 自动结账报告-gl_autoclose_report

## 执行详情-子表 t_gl_ac_reportdetail

- **表名称：** 执行详情-子表
- **表名：** t_gl_ac_reportdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffailcount | 执行失败数量 | int4 | 32 |  | √ | 0 | 执行失败数量 |
| 3 | foperatebegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 4 | foperatecostseconds | 耗时（秒） | int4 | 32 |  | √ | 0 | 耗时（秒） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fexecutestatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 0 :失败 1 :成功 |
| 7 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | foperation | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作,枚举: |
| 9 | foperateendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsuccesscount | 执行成功数量 | int4 | 32 |  | √ | 0 | 执行成功数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_ac_reportdetail |  | fentryid |
| 2 | idx_gl_ac_reportdetail_fid |  | fid |

---

## 自动结账报告-主表 t_gl_autoclose_report

- **表名称：** 自动结账报告-主表
- **表名：** t_gl_autoclose_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fschemeid | 自动结账方案 | int8 | 64 |  | √ | 0 | 自动结账方案 gl_autoclose_scheme |
| 6 | fcostseconds | 耗时（秒） | int4 | 32 |  | √ | 0 | 耗时（秒） |
| 7 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 8 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fexecutemethod | 执行方式 | bpchar | 1 |  | √ | ' ' | 执行方式,枚举: 0 :自动执行 1 :手动执行 |
| 11 | fbizsystem | 业务系统 | varchar | 50 |  | √ | ' ' | 业务系统,枚举: fa :固定资产 gl :总账 |
| 12 | fnumber | 报告编码 | varchar | 80 |  | √ | ' ' | 报告编码 |
| 13 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_autoclose_report |  | fid |
| 2 | idx_gl_autoclose_report_book |  | faccountbookid |

---

## X-执行失败信息-子表 t_gl_ac_reportmsg

- **表名称：** X-执行失败信息-子表
- **表名：** t_gl_ac_reportmsg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailmsg | 执行失败详细信息 | varchar | 2000 |  | √ | ' ' | 执行失败详细信息 |
| 2 | fqueryparamstr | 查询条件 | varchar | 2000 |  | √ | ' ' | 查询条件 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fformid | 表单标识 | varchar | 50 |  | √ | ' ' | 表单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_ac_reportmsg |  | fdetailid |
| 2 | idx_gl_ac_reportmsg_feid |  | fentryid |
