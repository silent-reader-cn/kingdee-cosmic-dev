# 模板-tctb_template

## 模板-主表 t_tctb_template

- **表名称：** 模板-主表
- **表名：** t_tctb_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fconditionjson | 配置条件 | text | 0 |  |  | null | 配置条件 |
| 5 | fenddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 6 | fgeneral | 通用 | bpchar | 1 |  | √ | '0' | 通用 |
| 7 | ftype | 模板类型 | varchar | 30 |  | √ | ' ' | [模板类型 tctb_template_type](../tctb_files/tctb_template_type.md) |
| 8 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fcontent_tag | 模板内容_详情 | text | 0 |  |  | null | 模板内容_详情 |
| 10 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fnumber | 模板编码 | varchar | 100 |  | √ | ' ' | 模板编码 |
| 12 | fcontent | 模板内容 | varchar | 510 |  | √ | ' ' | 模板内容 |
| 13 | fhtml_tag | 模板html内容_详情 | text | 0 |  |  | null | 模板html内容_详情 |
| 14 | ffiltercondition | 配置条件 | text | 0 |  |  | null | 配置条件 |
| 15 | fhtml | 模板html内容 | varchar | 510 |  | √ | ' ' | 模板html内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_template |  | fid |
| 2 | idx_t_tctb_template |  | ftype,fstartdate |
