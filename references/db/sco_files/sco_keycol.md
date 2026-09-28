# 卷算维度数据表-sco_keycol

## 卷算维度数据表-主表 t_sco_keycol

- **表名称：** 卷算维度数据表-主表
- **表名：** t_sco_keycol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fmatvers | 版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 7 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 9 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | fkeycol | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_keycol |  | fid |
| 2 | idx_sco_keycol |  | fkeycol |
