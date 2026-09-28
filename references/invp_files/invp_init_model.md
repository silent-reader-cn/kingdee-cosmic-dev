# 快速搭建模型-invp_init_model

## 快速搭建模型-主表 t_invp_initmodel

- **表名称：** 快速搭建模型-主表
- **表名：** t_invp_initmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | finittext | 详细内容 | varchar | 512 |  | √ | ' ' | 详细内容 |
| 4 | fmodelitem | 模型项 | varchar | 10 |  | √ | ' ' | 模型项,枚举: A :资源模型 B :算法模型 C :水位因子模型 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | finitstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: A :已完成 B :未开始 C :进行中 |
| 9 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_initmodel |  | fid |
