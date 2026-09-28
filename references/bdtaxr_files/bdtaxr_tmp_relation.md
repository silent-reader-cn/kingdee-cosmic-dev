# 模版关系设置-bdtaxr_tmp_relation

## 模版关系设置-主表 t_bdtaxr_tmp_relation

- **表名称：** 模版关系设置-主表
- **表名：** t_bdtaxr_tmp_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemplateid | 主模版编号 | int8 | 64 |  | √ | 0 | 主模版编号,枚举: |
| 3 | ftemplatenum | 主模版编号 | varchar | 50 |  | √ | ' ' | 主模版编号 |
| 4 | fre_templateid | 依赖模版编号 | int8 | 64 |  | √ | 0 | 依赖模版编号,枚举: |
| 5 | fre_templatenum | 依赖模版编号 | varchar | 50 |  | √ | ' ' | 依赖模版编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_tmp_relation |  | ftemplateid,fre_templateid |
| 2 | pk_bdtaxr_tmp_relation |  | fid |
