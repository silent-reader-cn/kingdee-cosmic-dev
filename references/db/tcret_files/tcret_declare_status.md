# 申报状态-tcret_declare_status

## 申报状态-主表 t_tcret_declare_status

- **表名称：** 申报状态-主表
- **表名：** t_tcret_declare_status

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 3 :第三步 4 :第四步 5 :第五步 |
| 4 | fiscreated | 是否生成申报表 | int8 | 64 |  | √ | 0 | 是否生成申报表 |
| 5 | fdeclaremonth | 申报月份 | varchar | 50 |  | √ | ' ' | 申报月份 |
| 6 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcount | 生成申报表总数 | int8 | 64 |  | √ | 0 | 生成申报表总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_declare_status |  | fstartdate,fenddate,forgid |
| 2 | t_tcret_declare_status_pkey |  | fid |
