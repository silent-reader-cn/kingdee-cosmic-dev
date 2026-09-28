# 失败成本域信息表-cal_failcostdomain

## 失败成本域信息表-主表 t_cal_failcostdomain

- **表名称：** 失败成本域信息表-主表
- **表名：** t_cal_failcostdomain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftimes | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 3 | ffailcostdomainkey | 失败成本域 | varchar | 50 |  | √ | ' ' | 失败成本域 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fcaltime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_failcostdomain |  | fid |
| 2 | idx_cal_failcostdomain_cdkey |  | ffailcostdomainkey |
