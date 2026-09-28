# 模型初始化训练记录-task_modelinitrecord

## 模型初始化训练记录-主表 t_tk_modelinitrecord

- **表名称：** 模型初始化训练记录-主表
- **表名：** t_tk_modelinitrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 生成时间 | varchar | 50 |  | √ | ' ' | 生成时间 |
| 3 | ffeaturecode | 特征代码 | varchar | 250 |  | √ | ' ' | 特征代码 |
| 4 | faccuracy | 准确率 | varchar | 50 |  | √ | ' ' | 准确率 |
| 5 | fstatus | 状态 | varchar | 8 |  | √ | ' ' | 状态,枚举: 0 :有效 1 :无效 |
| 6 | frecall | 召回率 | varchar | 50 |  | √ | ' ' | 召回率 |
| 7 | flasttraintime | 最后一次迭代时间 | varchar | 50 |  | √ | ' ' | 最后一次迭代时间 |
| 8 | fservicename | 服务名称 | varchar | 50 |  | √ | ' ' | 服务名称 |
| 9 | fmodelname | 模型名称 | varchar | 50 |  | √ | ' ' | 模型名称 |
| 10 | fusedtimes | 调用次数 | varchar | 50 |  | √ | ' ' | 调用次数 |
| 11 | ftraindata | 训练使用数据量 | varchar | 50 |  | √ | ' ' | 训练使用数据量 |
| 12 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |
| 13 | ffscore | F1值 | varchar | 50 |  | √ | ' ' | F1值 |
| 14 | fdatatype | 数据类型 | varchar | 8 |  | √ | ' ' | 数据类型,枚举: 0 :特征向量 1 :训练结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_modelinitrecord |  | fid |
| 2 | idx_ssc_modelinitrecord_fver |  | fversion |
