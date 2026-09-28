# 申报模版-rdem_template_main

## 申报模版-主表 t_rdem_template_main

- **表名称：** 申报模版-主表
- **表名：** t_rdem_template_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fconditionjson | 配置条件 | varchar | 2000 |  | √ | ' ' | 配置条件 |
| 5 | fenddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 6 | fgeneral | 通用 | bpchar | 1 |  | √ | '0' | 通用 |
| 7 | ftype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 8 | fcontent_tag | 模板内容_详情 | text | 0 |  |  | null | 模板内容_详情 |
| 9 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fnumber | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |
| 12 | fhtml_tag | 模板html内容_详情 | text | 0 |  |  | null | 模板html内容_详情 |
| 13 | fcontent | 模板内容 | varchar | 255 |  | √ | ' ' | 模板内容 |
| 14 | ffiltercondition | 配置条件 | varchar | 2000 |  | √ | ' ' | 配置条件 |
| 15 | fhtml | 模板html内容 | varchar | 255 |  | √ | ' ' | 模板html内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_template_main_m0 |  | fnumber |
| 2 | pk_rdem_template_main |  | fid |
