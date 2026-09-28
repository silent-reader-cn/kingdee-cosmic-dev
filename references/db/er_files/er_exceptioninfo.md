# 业务异常信息-er_exceptioninfo

## 业务异常信息-主表 t_er_exceptioninfo

- **表名称：** 业务异常信息-主表
- **表名：** t_er_exceptioninfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperate | 业务操作 | varchar | 15 |  | √ | ' ' | 业务操作,枚举: save :保存 submit :提交 unsubmit :撤回 delete :删除 fileUpload :附件上传 push :推送商旅 budgetCheck :项目预算检查 checked :审核通过 audit :审核通过 |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 1 :待分析 2 :已处理 3 :不处理 |
| 4 | fbusinessid | 业务ID | int8 | 64 |  | √ | 0 | 业务ID |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fotherinfo | 其它信息 | varchar | 100 |  | √ | ' ' | 其它信息 |
| 7 | fmessageinfo | 异常信息 | varchar | 2000 |  | √ | ' ' | 异常信息 |
| 8 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: tripreqbill :出差申请单 tripreqbill(loan) :出差借款单 tripreimbursebill :差旅报销单 dailyloanbill :日常借款单 dailyreimbursebill :费用报销单 |
| 9 | fformid | 表单标识 | varchar | 30 |  | √ | ' ' | 表单标识 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_exceptioninfo_pkey |  | fid |
| 2 | idx_er_excep_fcrtetime |  | fcreatetime |
| 3 | idx_er_excep_fbunisgp |  | fbusinessid,fbusinesstype |
