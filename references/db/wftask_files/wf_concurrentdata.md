# 并发数据池-wf_concurrentdata

## 并发数据池-主表 t_wf_concurrentdata

- **表名称：** 并发数据池-主表
- **表名：** t_wf_concurrentdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 参数 | varchar | 2000 |  | √ | ' ' | 参数 |
| 3 | fstate | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftype | 业务类型 | varchar | 200 |  | √ | ' ' | 业务类型 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreater | 创建人ID | int8 | 64 |  | √ | 0 | 创建人ID |
| 8 | fdata | 业务数据 | text | 0 |  |  | null | 业务数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_concurrentdata |  | fid |
| 2 | idx_wf_concurdata_typestate |  | ftype,fstate |
