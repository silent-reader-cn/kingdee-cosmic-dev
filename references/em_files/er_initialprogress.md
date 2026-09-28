# 初始化进度-er_initialprogress

## 初始化进度-主表 t_er_initialprogress

- **表名称：** 初始化进度-主表
- **表名：** t_er_initialprogress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbaseaccorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftotalprogress | 初始化进度 | numeric | 23 | 10 | √ | 0 | 初始化进度 |
| 4 | fcompletedtime | 完成初始化时间 | timestamp | 0 |  |  | null | 完成初始化时间 |
| 5 | finitialschemeid | 初始化方案 | int8 | 64 |  | √ | 0 | 初始化方案 er_initialscheme |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_initialprogress |  | fbaseaccorgid,ftotalprogress |
| 2 | pk_t_er_initialprogress |  | fid |
