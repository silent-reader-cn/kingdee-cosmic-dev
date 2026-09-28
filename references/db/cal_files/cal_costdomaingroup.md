# 成本域维度成组关系-cal_costdomaingroup

## 成本域维度成组关系-主表 t_cal_costdomaingroup

- **表名称：** 成本域维度成组关系-主表
- **表名：** t_cal_costdomaingroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsdimensionid | 来源维度 | int8 | 64 |  | √ | 0 | 成本域维度 cal_costdomain |
| 3 | ftmaterialid | 目标物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | ftperiodid | 目标期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fdimensionkey | 维度key | varchar | 50 |  | √ | ' ' | 维度key |
| 6 | fisdiffdomain | 是否跨成本域 | bpchar | 1 |  | √ | '1' | 是否跨成本域 |
| 7 | fissamematerial | 是否相同物料 | bpchar | 1 |  | √ | '1' | 是否相同物料 |
| 8 | fsortid | 排序链ID | int8 | 64 |  | √ | 0 | 排序链ID |
| 9 | fsperiodid | 来源期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 10 | ftdimensionkey | 目标维度key | varchar | 50 |  | √ | ' ' | 目标维度key |
| 11 | ftdimensionid | 目标维度 | int8 | 64 |  | √ | 0 | 成本域维度 cal_costdomain |
| 12 | fcount | 计数器 | int8 | 64 |  | √ | 0 | 计数器 |
| 13 | fsdimensionkey | 来源维度key | varchar | 50 |  | √ | ' ' | 来源维度key |
| 14 | fsmaterialid | 来源物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costdomaingroup_stk |  | fsdimensionkey,ftdimensionkey |
| 2 | idx_cal_sortresultentry_sortid |  | fsortid |
| 3 | idx_cal_costdomaingroup_dk |  | fdimensionkey |
| 4 | idx_cal_costdomaingroup_tk |  | ftdimensionkey |
| 5 | pk_t_cal_costdomaingroup |  | fid |
| 6 | idx_cal_costdomaingroup_fsi |  | fsdimensionid |
