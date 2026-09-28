# 软件、集成电路优惠基本信息底稿-tccit_soft_ic_jb_summary

## 软件、集成电路优惠基本信息底稿-主表 t_tccit_soft_ic_jb_sum

- **表名称：** 软件、集成电路优惠基本信息底稿-主表
- **表名：** t_tccit_soft_ic_jb_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | int8 | 64 |  | √ | 0 | 行次 |
| 3 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 5 | fjmfsnumber | 减免方式编码 | varchar | 50 |  | √ | ' ' | 减免方式编码 |
| 6 | fjmfs | 减免方式 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fhlnd | 获利年度\开始计算优惠期年度 | timestamp | 0 |  |  | null | 获利年度\开始计算优惠期年度 |
| 9 | fjmfsname | 减免方式名称 | varchar | 200 |  | √ | ' ' | 减免方式名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_soft_ic_jb_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_soft_ic_jb_sum |  | fid |
