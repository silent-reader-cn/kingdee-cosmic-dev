# 公式配置页面(弃用)-rdem_formula_edit

## 公式配置页面(弃用)-主表 t_rdem_formula

- **表名称：** 公式配置页面(弃用)-主表
- **表名：** t_rdem_formula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ftemplateid | 模板id | varchar | 50 |  | √ | ' ' | 模板id |
| 4 | fcelltype | 单元格类型 | varchar | 50 |  | √ | ' ' | 单元格类型,枚举: 1 :输入框 2 :下拉框 3 :复选框 4 :单选框 5 :基础资料 6 :URL : |
| 5 | frow | 行 | varchar | 50 |  | √ | ' ' | 行 |
| 6 | ftemplatenum | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码,枚举: |
| 7 | fdescribe | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 8 | fcolumn | 列 | varchar | 50 |  | √ | ' ' | 列 |
| 9 | fisdelay | 延迟公式 | bpchar | 1 |  | √ | '0' | 延迟公式 |
| 10 | fformulaname | 公式名称 | varchar | 2000 |  | √ | ' ' | 公式名称 |
| 11 | ftitle | 标题 | varchar | 1000 |  | √ | ' ' | 标题 |
| 12 | fformulatype | 公式类型 | varchar | 50 |  | √ | ' ' | 公式类型,枚举: 1 :计算公式 2 :校验公式 3 :单元格类型 4 :字符串类型 |
| 13 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 14 | ftable | 表 | varchar | 50 |  | √ | ' ' | 表 |
| 15 | fformula | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 16 | fcontent | 提示语 | varchar | 1000 |  | √ | ' ' | 提示语 |
| 17 | fformulakey | 标示 | varchar | 50 |  | √ | ' ' | 标示 |
| 18 | ftaxtype | 模板类型 | varchar | 36 |  | √ | ' ' | [模板分组 bdtaxr_template_group](../bdtaxr_files/bdtaxr_template_group.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_formula_m0 |  | fname |
| 2 | pk_rdem_formula |  | fid |
