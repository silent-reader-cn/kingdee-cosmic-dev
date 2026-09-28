# 指标采集分类统计-bos_cbs_shard_metric_stat

## 子单据体-子表 t_cbs_shard_metric_info

- **表名称：** 子单据体-子表
- **表名：** t_cbs_shard_metric_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsql | 采集SQL | text | 0 |  |  | null | 采集SQL |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fstack | 采集堆栈 | text | 0 |  |  | null | 采集堆栈 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fflag | 采集标志 | varchar | 50 |  | √ | ' ' | 采集标志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_s_cbs_shard_metric_info_fk |  | fentryid |
| 2 | pk_s_cbs_shard_metric_info |  | fdetailid |

---

## 单据体-子表 t_cbs_shard_metric_bill

- **表名称：** 单据体-子表
- **表名：** t_cbs_shard_metric_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillnumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_s_cbs_shard_metric_bill_fk |  | fid |
| 2 | pk_s_cbs_shard_metric_bill |  | fentryid |

---

## 指标采集分类统计-主表 t_cbs_shard_metric_stat

- **表名称：** 指标采集分类统计-主表
- **表名：** t_cbs_shard_metric_stat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 统计时间 | timestamp | 0 |  |  | null | 统计时间 |
| 3 | fnumber | 统计编码 | varchar | 50 |  | √ | ' ' | 统计编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_metric_stat |  | fnumber |
| 2 | pk_cbs_shard_metric_stat |  | fid |
