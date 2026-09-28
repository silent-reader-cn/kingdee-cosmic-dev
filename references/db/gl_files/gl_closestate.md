# 结账状态-gl_closestate

## 结账状态-主表 t_gl_closestate

- **表名称：** 结账状态-主表
- **表名：** t_gl_closestate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcloseuserid | 结账用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fthisclosetime | 本次结账耗时 | int8 | 64 |  | √ | 0 | 本次结账耗时 |
| 4 | fclosedetailsid | 结账详情 | int8 | 64 |  | √ | 0 | 结账详情 |
| 5 | fisautoclose | 自动结账区分 | bpchar | 1 |  | √ | '0' | 自动结账区分,枚举: 0 :手工结账 1 :自动结账 |
| 6 | fclosestate | 结账状态 | bpchar | 1 |  | √ | '0' | 结账状态,枚举: 0 :默认 1 :成功 2 :失败 |
| 7 | fcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 9 | fclosedate | 结账日期 | timestamp | 0 |  |  | null | 结账日期 |
| 10 | flinestate | 排队状态 | bpchar | 1 |  | √ | '0' | 排队状态,枚举: 0 :默认 1 :结账中 2 :队列中 3 :重排队 |
| 11 | faccountbooks | 子系统账簿 | varchar | 50 |  | √ | ' ' | 子系统账簿 |
| 12 | fsubsysformnum | 子系统表单标识 | varchar | 50 |  | √ | ' ' | 子系统表单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_closestate_pkey |  | fid |
| 2 | idx_gl_closestate |  | fcompany,fperiod,fsubsysformnum |
