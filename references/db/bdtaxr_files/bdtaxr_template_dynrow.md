# 动态行设置-bdtaxr_template_dynrow

## 动态行设置-主表 t_bdtaxr_template_dynrow

- **表名称：** 动态行设置-主表
- **表名：** t_bdtaxr_template_dynrow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 3 | fdisablefrontop | 禁用前端操作 | bpchar | 1 |  | √ | '0' | 禁用前端操作 |
| 4 | fpluginpath | 插件路径 | varchar | 400 |  | √ | ' ' | 插件路径 |
| 5 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: 2 :2.0 3 :3.0 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | frule_name | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 9 | fstart_row | 起始行 | varchar | 30 |  | √ | ' ' | 起始行,枚举: 1 :第一行 2 :第二行 |
| 10 | fdynheader | 动态行标题行序号 | int8 | 64 |  | √ | '-1' | 动态行标题行序号 |
| 11 | fdynrow_no | 动态行标识 | varchar | 200 |  | √ | ' ' | 动态行标识 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: rule_fetch :规则取数 plugin_fetch :插件取数 |
| 14 | fgroup_no | 动态行组编号 | varchar | 50 |  | √ | ' ' | 动态行组编号 |
| 15 | ftemplate_id | 模版id | int8 | 64 |  | √ | 0 | 模版id |
| 16 | fenable | 是否启用 | varchar | 10 |  | √ | ' ' | 是否启用 |
| 17 | fseq_no | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 18 | ffilter | 启用动态行筛选功能 | bpchar | 1 |  | √ | '0' | 启用动态行筛选功能 |
| 19 | frule_id | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_template_dynrow |  | ftemplate_id |
| 2 | pk_bdtaxr_template_dynrow |  | fid |
