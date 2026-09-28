# 任务详情计算-tctb_task_calculate

## 任务详情计算-主表 t_tctb_task_calculate

- **表名称：** 任务详情计算-主表
- **表名：** t_tctb_task_calculate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | ftaxtypecount | 样本条数 | int8 | 64 |  | √ | 0 | 样本条数 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | favgcosttime | 平均执行时间 | int8 | 64 |  | √ | 0 | 平均执行时间 |
| 6 | fnumber | 应用number | varchar | 50 |  | √ | ' ' | 应用number |
| 7 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_task_calculate |  | fid |
| 2 | idx_tctb_task_cal_app |  | fappid,fnumber |
