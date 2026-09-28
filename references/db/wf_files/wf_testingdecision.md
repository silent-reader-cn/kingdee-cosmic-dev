# 测试计划决策项-wf_testingdecision

## 测试计划决策项-主表 t_wf_testingdecision

- **表名称：** 测试计划决策项-主表
- **表名：** t_wf_testingdecision

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanid | 测试计划ID | int8 | 64 |  | √ | 0 | 测试计划ID |
| 3 | fdecisions | 多轮次决策项 | varchar | 2000 |  | √ | ' ' | 多轮次决策项 |
| 4 | fnodeid | 节点ID | varchar | 100 |  | √ | ' ' | 节点ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_testingdecision_pkey |  | fid |
| 2 | idx_wf_testingdecision_planid |  | fplanid |
