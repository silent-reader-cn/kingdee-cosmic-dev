# 标准成本卷算批次计算参数-cad_stdcalbatchsizeparam

## 标准成本卷算批次计算参数-主表 t_cad_stdcalbatchsizepara

- **表名称：** 标准成本卷算批次计算参数-主表
- **表名：** t_cad_stdcalbatchsizepara

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchsize | 批次卷算数据量 | int8 | 64 |  | √ | 0 | 批次卷算数据量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_stdcalbatchsizepara |  | fid |
| 2 | idx_cad_stdcalbatchsizepara |  | fbatchsize |
